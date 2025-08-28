from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BankaDurum(models.Model):
    _name = 'banka.durum'
    _description = 'Banka Durum Yönetimi'
    _order = 'sequence, name'

    name = fields.Char(string='Durum Adı', required=True, translate=True)
    code = fields.Char(string='Kod', required=True, size=20)
    description = fields.Text(string='Açıklama', translate=True)
    color = fields.Integer(string='Renk')
    sequence = fields.Integer(string='Sıra', default=10)
    active = fields.Boolean(string='Aktif', default=True)
    
    # İlişkiler
    terminal_ids = fields.One2many('terminal.management', 'banka_durum', string='Terminaller')
    terminal_count = fields.Integer(string='Terminal Sayısı', compute='_compute_terminal_count')
    
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Banka durum kodu benzersiz olmalıdır!'),
        ('name_uniq', 'unique(name)', 'Banka durum adı benzersiz olmalıdır!')
    ]
    
    @api.constrains('code')
    def _check_code_format(self):
        for record in self:
            if record.code and not record.code.replace('_', '').isalnum():
                raise ValidationError(_('Kod sadece harf, rakam ve alt çizgi içerebilir!'))
    
    @api.depends('terminal_ids')
    def _compute_terminal_count(self):
        for record in self:
            record.terminal_count = len(record.terminal_ids)
    
    def action_view_terminals(self):
        """Terminal listesini görüntüle"""
        self.ensure_one()
        return {
            'name': _('Terminaller - %s') % self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'terminal.management',
            'view_mode': 'list,form',
            'domain': [('banka_durum', '=', self.id)],
            'context': {'default_banka_durum': self.id},
        }
    
    def name_get(self):
        """Display name for the record"""
        result = []
        for record in self:
            name = f"{record.name} ({record.code})"
            result.append((record.id, name))
        return result
