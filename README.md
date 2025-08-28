# Terminal Yönetim Sistemi - Odoo 16 Modülü

Bu modül, Odoo 16 Community sürümünde terminal kayıtlarını yönetmek için geliştirilmiştir.

## Özellikler

- **Terminal Kayıtları**: Terminal bilgilerini görüntüleme, düzenleme ve silme
- **Durum Takibi**: Terminal, POS ve banka durumlarını takip etme
- **Filtreleme ve Arama**: Gelişmiş arama ve filtreleme özellikleri
- **Demo Veri**: Kurulum sonrası test için hazır demo veriler
- **Güvenlik**: Kullanıcı bazlı erişim kontrolü

## Kurulum

### 1. Modül Dosyalarını Kopyalama
Modül dosyalarını Odoo addons dizinine kopyalayın:
```bash
cp -r terminal_management /path/to/odoo/addons/
```

### 2. Odoo'yu Yeniden Başlatma
Odoo servisini yeniden başlatın:
```bash
sudo systemctl restart odoo
# veya
sudo service odoo restart
```

### 3. Modülü Yükleme
- Odoo web arayüzünde **Apps** menüsüne gidin
- **Update Apps List** butonuna tıklayın
- "Terminal Yönetim Sistemi" modülünü arayın
- **Install** butonuna tıklayın

## Kullanım

### Ana Menü
Modül yüklendikten sonra ana menüde **"Terminal Yönetimi"** seçeneği görünecektir.

### Terminal Ekleme
1. **Terminal Yönetimi > Terminaller** menüsüne gidin
2. **Create** butonuna tıklayın
3. Gerekli alanları doldurun (Mali No zorunludur)
4. **Save** butonuna tıklayın

### Terminal Düzenleme
1. Terminal listesinde düzenlemek istediğiniz kaydı seçin
2. **Edit** butonuna tıklayın
3. Değişiklikleri yapın
4. **Save** butonuna tıklayın

### Durum Yönetimi
- **Aktif Et**: Terminali aktif duruma getirir
- **Pasif Et**: Terminali pasif duruma getirir
- **Arıza Bildir**: Terminal arıza durumunu bildirir

## Veritabanı Şeması

Modül, aşağıdaki alanları içerir:

### Temel Bilgiler
- `mali_no`: Terminal mali numarası (benzersiz)
- `org_id`: Organizasyon ID
- `banka_adi`: Banka adı
- `marka`: Terminal markası
- `model`: Terminal modeli

### Durum Bilgileri
- `banka_durum`: Banka durumu (aktif/pasif/beklemede)
- `pos_durum`: POS durumu (aktif/pasif/arıza/beklemede)
- `terminal_durum`: Terminal durumu (aktif/pasif/arıza/beklemede)
- `satis_durum`: Satış durumu

### Teknik Bilgiler
- `sim_id`: SIM kart ID
- `imei`: Terminal IMEI numarası
- `operator`: Mobil operatör
- `terminal_kanali`: Haberleşme kanalı

### Tarih Bilgileri
- `satis_aktivasyon_tarihi`: Satış aktivasyon tarihi
- `banka_gonderim_tarihi`: Banka gönderim tarihi
- `banka_yanit_tarihi`: Banka yanıt tarihi

## Güvenlik

Modül, aşağıdaki güvenlik seviyelerini sağlar:

- **Kullanıcı**: Okuma, yazma ve oluşturma izni
- **Sistem Yöneticisi**: Tüm izinler (silme dahil)

## Gereksinimler

- Odoo 16.0 Community Edition
- Python 3.8+
- PostgreSQL 12+

## Destek

Herhangi bir sorun yaşadığınızda:
1. Odoo log dosyalarını kontrol edin
2. Modül kurulum adımlarını tekrar gözden geçirin
3. Odoo sürüm uyumluluğunu kontrol edin

## Lisans

Bu modül LGPL-3 lisansı altında dağıtılmaktadır.

## Sürüm Geçmişi

- **16.0.1.0.0**: İlk sürüm
  - Temel terminal yönetimi
  - CRUD işlemleri
  - Durum takibi
  - Demo veriler
