# 🚀 Terminal Yönetim Sistemi - Kurulum Talimatları

Bu dosya, Terminal Yönetim Sistemi modülünü farklı ortamlarda nasıl kuracağınızı açıklar.

## 📋 Gereksinimler

- Odoo 16.0 Community Edition
- Python 3.8+
- PostgreSQL 12+

## 🎯 Kurulum Seçenekleri

### Seçenek 1: Docker ile Hızlı Kurulum (Önerilen)

#### 1. Docker Desktop Kurulumu
```bash
# macOS
brew install --cask docker

# Windows
# https://docs.docker.com/desktop/install/windows-install/

# Linux
sudo apt-get install docker.io docker-compose
```

#### 2. Modülü İndirme
```bash
git clone https://github.com/erhan-hash/odoo.git
cd odoo
```

#### 3. Docker Compose ile Başlatma
```bash
# Docker Desktop'ı başlatın
# Applications > Docker.app

# Odoo'yu başlatın
docker compose up -d

# Logları kontrol edin
docker compose logs -f odoo
```

#### 4. Erişim
- **Odoo Web**: http://localhost:8069
- **Veritabanı**: odoo16
- **Kullanıcı**: admin
- **Şifre**: admin

### Seçenek 2: Manuel Kurulum

#### 1. Odoo 16 Community İndirme
```bash
# Odoo kaynak kodunu indirin
git clone https://github.com/odoo/odoo.git --depth 1 --branch 16.0
cd odoo

# Python virtual environment oluşturun
python3 -m venv odoo_env
source odoo_env/bin/activate  # Linux/macOS
# odoo_env\Scripts\activate  # Windows

# Gereksinimleri yükleyin
pip install -r requirements.txt
```

#### 2. Modülü Kopyalama
```bash
# Modülü Odoo addons dizinine kopyalayın
cp -r terminal_management /path/to/odoo/addons/

# veya symbolic link oluşturun
ln -s /path/to/your/module /path/to/odoo/addons/terminal_management
```

#### 3. Odoo'yu Başlatma
```bash
# Odoo'yu başlatın
./odoo-bin --addons-path=addons,../terminal_management --db_host=localhost --db_user=odoo --db_password=odoo
```

### Seçenek 3: Mevcut Odoo Kurulumuna Ekleme

#### 1. Modülü Kopyalama
```bash
# Modülü mevcut Odoo addons dizinine kopyalayın
sudo cp -r terminal_management /opt/odoo/addons/
sudo chown -R odoo:odoo /opt/odoo/addons/terminal_management
```

#### 2. Odoo'yu Yeniden Başlatma
```bash
# Systemd ile
sudo systemctl restart odoo

# veya service ile
sudo service odoo restart
```

## 🔧 Modül Yükleme

### 1. Odoo Web Arayüzü
1. **Apps** menüsüne gidin
2. **Update Apps List** butonuna tıklayın
3. "Terminal Yönetim Sistemi" modülünü arayın
4. **Install** butonuna tıklayın

### 2. Komut Satırı
```bash
# Modülü yükleyin
./odoo-bin -d your_database -i terminal_management --stop-after-init
```

## ✅ Kurulum Sonrası Kontrol

### 1. Modül Kontrolü
- Ana menüde **"Terminal Yönetimi"** seçeneği görünmeli
- **Terminal Yönetimi > Terminaller** menüsü çalışmalı

### 2. Demo Veri Kontrolü
- Modül yüklendikten sonra 3 demo terminal kaydı görünmeli
- TERM001, TERM002, TERM003 kayıtları mevcut olmalı

### 3. Güvenlik Kontrolü
- Normal kullanıcılar terminal ekleyebilmeli/düzenleyebilmeli
- Sadece sistem yöneticileri silebilmeli

## 🐛 Sorun Giderme

### Modül Görünmüyor
```bash
# Odoo loglarını kontrol edin
tail -f /var/log/odoo/odoo.log

# Modül dizinini kontrol edin
ls -la /opt/odoo/addons/terminal_management/

# İzinleri kontrol edin
sudo chown -R odoo:odoo /opt/odoo/addons/terminal_management
```

### Veritabanı Hatası
```bash
# PostgreSQL bağlantısını kontrol edin
sudo -u postgres psql -d odoo16 -c "\dt"

# Odoo veritabanı kullanıcısını kontrol edin
sudo -u postgres psql -c "\du"
```

### Python Hatası
```bash
# Python versiyonunu kontrol edin
python3 --version

# Virtual environment'ı kontrol edin
which python3
```

## 📱 Test Senaryoları

### 1. Temel CRUD İşlemleri
- ✅ Yeni terminal ekleme
- ✅ Terminal düzenleme
- ✅ Terminal silme (sadece admin)
- ✅ Terminal listeleme

### 2. Durum Yönetimi
- ✅ Aktif etme
- ✅ Pasif etme
- ✅ Arıza bildirimi

### 3. Arama ve Filtreleme
- ✅ Mali No ile arama
- ✅ Durum filtreleme
- ✅ Tarih filtreleme

## 🔗 Faydalı Linkler

- **Odoo Resmi**: https://www.odoo.com/
- **Odoo Dokümantasyon**: https://www.odoo.com/documentation/16.0/
- **GitHub Repository**: https://github.com/erhan-hash/odoo

## 📞 Destek

Herhangi bir sorun yaşadığınızda:
1. Bu README dosyasını tekrar gözden geçirin
2. Odoo log dosyalarını kontrol edin
3. GitHub Issues'da sorun bildirin

---

**Not**: Bu modül Odoo 16.0 Community Edition ile test edilmiştir.
