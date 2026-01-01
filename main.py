import telebot
import os
import time
import subprocess

# ================= KONFIGURASI =================
# Ganti dengan Token dari BotFather
API_TOKEN = 'GANTI_DENGAN_TOKEN_BOT_KAMU_DISINI'

# Ganti dengan ID Telegram kamu (agar orang lain tidak bisa akses)
# Cara cek ID: Chat ke bot @userinfobot
ALLOWED_ID = 123456789 

# Nomor GPIO STB (Sesuaikan dengan map pin STB kamu)
# Contoh: HG680P biasanya GPIO 496 (Pin Header tertentu)
# Silakan riset "GPIO Mapping [Tipe STB Kamu]"
LAMP_PIN = '496' 

bot = telebot.TeleBot(API_TOKEN)

# ================= FUNGSI GPIO (SYSTEM) =================
def setup_gpio(pin):
    """Menyiapkan GPIO untuk output"""
    export_path = f"/sys/class/gpio/export"
    pin_path = f"/sys/class/gpio/gpio{pin}"
    
    if not os.path.exists(pin_path):
        try:
            with open(export_path, 'w') as f:
                f.write(pin)
        except Exception as e:
            print(f"Error Export GPIO: {e}")
            return False
            
    # Tunggu sebentar agar system siap
    time.sleep(0.5)
    
    # Set Direction ke OUT
    try:
        with open(f"{pin_path}/direction", 'w') as f:
            f.write("out")
    except Exception as e:
        print(f"Error Direction GPIO: {e}")
        return False
    return True

def set_gpio(pin, value):
    """Mengubah nilai GPIO (1=Nyala, 0=Mati)"""
    # Catatan: Relay module biasanya Active LOW (0=Nyala, 1=Mati)
    # Sesuaikan logika value di sini
    try:
        path = f"/sys/class/gpio/gpio{pin}/value"
        with open(path, 'w') as f:
            f.write(str(value))
        return True
    except Exception as e:
        print(f"Error Set GPIO: {e}")
        return False

# ================= LOGIKA BOT =================

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.chat.id != ALLOWED_ID:
        bot.reply_to(message, "Maaf, Anda bukan pemilik rumah ini!")
        return
        
    intro = (
        "🏠 **STB Smart Home Controller** 🏠\n\n"
        "Perintah yang tersedia:\n"
        "/on - Nyalakan Lampu\n"
        "/off - Matikan Lampu\n"
        "/status - Cek Status & Suhu STB"
    )
    bot.reply_to(message, intro, parse_mode="Markdown")

@bot.message_handler(commands=['on'])
def turn_on(message):
    if message.chat.id != ALLOWED_ID: return
    
    # Ubah '0' atau '1' sesuai jenis Relay kamu (Active High/Low)
    if set_gpio(LAMP_PIN, 1): 
        bot.reply_to(message, "💡 Lampu BERHASIL Dinyalakan!")
    else:
        bot.reply_to(message, "⚠️ Gagal mengakses GPIO.")

@bot.message_handler(commands=['off'])
def turn_off(message):
    if message.chat.id != ALLOWED_ID: return
    
    # Ubah '0' atau '1' sesuai jenis Relay kamu
    if set_gpio(LAMP_PIN, 0):
        bot.reply_to(message, "🌑 Lampu BERHASIL Dimatikan.")
    else:
        bot.reply_to(message, "⚠️ Gagal mengakses GPIO.")

@bot.message_handler(commands=['status'])
def check_status(message):
    if message.chat.id != ALLOWED_ID: return
    
    # Cek suhu CPU STB
    try:
        temp = subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True).decode()
        temp_c = int(temp) / 1000
    except:
        temp_c = "N/A"
        
    info = (
        f"🖥 **Status STB**\n"
        f"Suhu CPU: {temp_c}°C\n"
        f"Bot: Online ✅"
    )
    bot.reply_to(message, info, parse_mode="Markdown")

# ================= RUN =================
if __name__ == "__main__":
    print("Mencoba menyiapkan GPIO...")
    setup_gpio(LAMP_PIN)
    print("Bot Berjalan...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Error: {e}")
