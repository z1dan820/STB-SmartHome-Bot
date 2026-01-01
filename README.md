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
**⚙️ Konfigurasi**

Sebelum dijalankan, kamu wajib memasukkan Token Bot:

Ketik ```bash nano main.py```
Cari baris API_TOKEN dan masukkan token dari BotFather.
Cari baris ALLOWED_ID dan masukkan ID Telegram kamu (Cek di @userinfobot).
Sesuaikan LAMP_PIN dengan GPIO STB kamu.
Save (Ctrl+X, Y, Enter).

**▶️ Cara Menjalankan**

```bash python3 main.py```

Agar jalan otomatis saat STB nyala (Auto-start), tambahkan ke /etc/rc.local.

***🤝 Support***
Jika bermanfaat, jangan lupa Subscribe channel YouTube saya: Fahrul Hamzidan Pulungan 



***#panduan wiring menggunakan STB dan Modul Relay 5V:***

1. Persiapan Alat
   
Modul Relay 5V (1 Channel): Pastikan ada 3 pin input (VCC, GND, IN).
Kabel Jumper Female-to-Female: Untuk menghubungkan pin STB ke Relay.
Adaptor STB: Pastikan adaptornya ori/stabil karena relay butuh daya saat "klik".

2. Diagram Penyambungan (Pinout)
   
Secara umum, koneksinya adalah sebagai berikut:
```bash
 **Pin Modul Relay | Pin di STB**
       VCC         |     Pin 5V 
       GND         | Pin Ground (GND) 
   IN (Signal)     | Pin GPIO (Misal: GPIO 496)
```
Penting: Tiap tipe STB punya letak pin yang berbeda. Untuk B860H atau HG680P, biasanya kamu harus membongkar casing dan mencari deretan pin header (biasanya dekat port USB atau dekat lubang Jack Audio). Cari tulisan 5V, GND, dan TX/RX (TX/RX ini bisa dijadikan GPIO).

3. Skema ke Lampu (Tegangan Tinggi 220V)
   
⚠️ PERINGATAN: Bagian ini berhubungan dengan listrik PLN. Pastikan kabel power lampu dicabut saat memasang!
Relay memiliki 3 terminal output (biasanya berbentuk baut): 

COM, NO (Normally Open), dan NC (Normally Closed).

Ambil satu kabel dari lampu (kabel fasa/setrum).

Potong kabel tersebut menjadi dua ujung.

Masukkan ujung satu ke lubang COM.

Masukkan ujung satunya lagi ke lubang NO.

Kencangkan bautnya.

***Logikanya: Relay berfungsi seperti saklar. Saat Bot mengirim perintah "ON", terminal COM dan NO akan menyambung, sehingga lampu menyala.***
