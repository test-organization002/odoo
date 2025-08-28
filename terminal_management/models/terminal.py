from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime


class Terminal(models.Model):
    _name = 'terminal.management'
    _description = 'Terminal Yönetim Sistemi'
    _rec_name = 'mali_no'
    _order = 'id desc'

    # Ana alanlar
    mali_no = fields.Char(string='Mali No', required=True, index=True)
    org_id = fields.Char(string='Organizasyon ID')
    banka_adi = fields.Char(string='Banka Adı')
    
    # Durum alanları - Many2one ilişkiler
    banka_durum = fields.Many2one('banka.durum', string='Banka Durumu', required=True, ondelete='restrict')
    pos_durum = fields.Many2one('pos.durum', string='POS Durumu', required=True, ondelete='restrict')
    terminal_durum = fields.Many2one('pos.durum', string='Terminal Durumu', required=True, ondelete='restrict')
    siparis_durum = fields.Many2one('siparis.durum', string='Sipariş Durumu', required=True, ondelete='restrict')
    
    # Tarih alanları
    satis_aktivasyon_tarihi = fields.Datetime(string='Satış Aktivasyon Tarihi')
    banka_gonderim_tarihi = fields.Datetime(string='Banka Gönderim Tarihi')
    banka_yanit_tarihi = fields.Datetime(string='Banka Yanıt Tarihi')
    satis_iptal_tarihi = fields.Datetime(string='Satış İptal Tarihi')
    iptal_gonderim_tarihi = fields.Datetime(string='İptal Gönderim Tarihi')
    iptal_yanit_tarihi = fields.Datetime(string='İptal Yanıt Tarihi')
    
    # Teknik alanlar
    marka = fields.Char(string='Marka')
    model = fields.Char(string='Model')
    sim_id = fields.Char(string='SIM ID')
    imei = fields.Char(string='IMEI')
    operator = fields.Char(string='Operatör')
    son_haberlesme = fields.Datetime(string='Son Haberleşme')
    
    # Banka bilgileri
    banka_mid = fields.Char(string='Banka MID')
    banka_tid = fields.Char(string='Banka TID')
    pos_mid = fields.Char(string='POS MID')
    pos_tid = fields.Char(string='POS TID')
    
    # Diğer alanlar
    terminal_kanali = fields.Selection([
        ('internet', 'İnternet'),
        ('gprs', 'GPRS'),
        ('ethernet', 'Ethernet'),
        ('wifi', 'WiFi')
    ], string='Terminal Kanali')
    
    aciklama = fields.Text(string='Açıklama')
    request_type = fields.Char(string='İstek Tipi')
    terminal_type = fields.Char(string='Terminal Tipi')
    
    satis_durum = fields.Selection([
        ('aktif', 'Aktif'),
        ('pasif', 'Pasif'),
        ('beklemede', 'Beklemede')
    ], string='Satış Durumu', default='beklemede')
    
    # Sistem alanları
    active = fields.Boolean(default=True, string='Aktif')
    create_date = fields.Datetime(string='Oluşturulma Tarihi', readonly=True)
    write_date = fields.Datetime(string='Güncellenme Tarihi', readonly=True)
    create_uid = fields.Many2one('res.users', string='Oluşturan', readonly=True)
    write_uid = fields.Many2one('res.users', string='Güncelleyen', readonly=True)

    # Constraints
    _sql_constraints = [
        ('mali_no_unique', 'UNIQUE(mali_no)', 'Mali No benzersiz olmalıdır!'),
    ]

    @api.constrains('mali_no')
    def _check_mali_no(self):
        for record in self:
            if record.mali_no and len(record.mali_no) < 3:
                raise ValidationError(_('Mali No en az 3 karakter olmalıdır.'))

    @api.constrains('imei')
    def _check_imei(self):
        for record in self:
            if record.imei and len(record.imei) != 15:
                raise ValidationError(_('IMEI 15 karakter olmalıdır.'))

    def action_aktif_et(self):
        """Terminali aktif et"""
        # Aktif durumları bul
        aktif_durum = self.env['pos.durum'].search([('code', '=', 'aktif')], limit=1)
        tamamlandi_durum = self.env['banka.durum'].search([('code', '=', 'tamamlandi')], limit=1)
        
        if aktif_durum and tamamlandi_durum:
            self.write({
                'terminal_durum': aktif_durum.id,
                'pos_durum': aktif_durum.id,
                'banka_durum': tamamlandi_durum.id
            })

    def action_pasif_et(self):
        """Terminali pasif et"""
        # Pasif durumları bul
        pasif_durum = self.env['pos.durum'].search([('code', '=', 'pasif')], limit=1)
        reddedildi_durum = self.env['banka.durum'].search([('code', '=', 'reddedildi')], limit=1)
        
        if pasif_durum and reddedildi_durum:
            self.write({
                'terminal_durum': pasif_durum.id,
                'pos_durum': pasif_durum.id,
                'banka_durum': reddedildi_durum.id
            })

    def action_ariza_bildir(self):
        """Terminal arıza bildirimi"""
        # Arıza durumları bul
        ariza_durum = self.env['pos.durum'].search([('code', '=', 'ariza')], limit=1)
        hata_durum = self.env['banka.durum'].search([('code', '=', 'hata')], limit=1)
        
        if ariza_durum and hata_durum:
            self.write({
                'terminal_durum': ariza_durum.id,
                'pos_durum': ariza_durum.id,
                'banka_durum': hata_durum.id
            })

    def action_banka_gonder(self):
        """Banka gönderim işlemi"""
        yanit_bekleniyor_durum = self.env['banka.durum'].search([('code', '=', 'yanit_bekleniyor')], limit=1)
        if yanit_bekleniyor_durum:
            self.write({
                'banka_durum': yanit_bekleniyor_durum.id,
                'banka_gonderim_tarihi': fields.Datetime.now()
            })

    def action_banka_yanit_al(self):
        """Banka yanıtı alındı"""
        tamamlandi_durum = self.env['banka.durum'].search([('code', '=', 'tamamlandi')], limit=1)
        if tamamlandi_durum:
            self.write({
                'banka_durum': tamamlandi_durum.id,
                'banka_yanit_tarihi': fields.Datetime.now()
            })

    def action_banka_reddet(self):
        """Banka reddetti"""
        reddedildi_durum = self.env['banka.durum'].search([('code', '=', 'reddedildi')], limit=1)
        if reddedildi_durum:
            self.write({
                'banka_durum': reddedildi_durum.id,
                'banka_yanit_tarihi': fields.Datetime.now()
            })

    def action_banka_hata(self):
        """Banka hatası"""
        hata_durum = self.env['banka.durum'].search([('code', '=', 'hata')], limit=1)
        if hata_durum:
            self.write({
                'banka_durum': hata_durum.id,
                'banka_yanit_tarihi': fields.Datetime.now()
            })

    def name_get(self):
        """Terminal adını mali_no ile göster"""
        result = []
        for record in self:
            name = f"{record.mali_no}"
            if record.banka_adi:
                name += f" - {record.banka_adi}"
            result.append((record.id, name))
        return result
