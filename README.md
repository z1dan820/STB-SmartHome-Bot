# 🏠 STB Smart Home (Telegram Bot)

Ubah STB bekas (B860H/HG680P) menjadi server Smart Home murah meriah! Kontrol lampu rumah dari jarak jauh menggunakan Telegram.

Project ini dibuat untuk tujuan edukasi dan konten YouTube.

## 🌟 Fitur
- **Kontrol Jarak Jauh:** Nyalakan/Matikan alat elektronik via Chat.
- **Secure Access:** Hanya ID pemilik yang bisa mengontrol.
- **Suhu Monitor:** Cek suhu STB real-time.
- **Lightweight:** Script sangat ringan, tidak membebani RAM STB 1GB.

## 🛠 Persiapan Hardware
1. STB Android (Sudah terinstall Armbian/OpenWrt).
2. Modul Relay 5V (1 Channel atau lebih).
3. Kabel Jumper (Female to Female).
4. Koneksi Internet.

## 🚀 Cara Install (1 Klik)

Buka terminal STB kamu (via PuTTY/Termius), lalu jalankan perintah ini:

```bash
git clone [https://github.com/z1dan820/STB-SmartHome-Bot.git](https://github.com/z1dan820/STB-SmartHome-Bot.git)
cd STB-SmartHome-Bot
chmod +x install.sh
./install.sh
```
