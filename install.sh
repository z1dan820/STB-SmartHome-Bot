#!/bin/bash

echo "=========================================="
echo "   INSTALLER STB SMART HOME @z1dan820"
echo "=========================================="

# 1. Update System
echo "[1/4] Update Repository..."
sudo apt-get update

# 2. Install Python & Tools
echo "[2/4] Install Python3 & PIP..."
sudo apt-get install python3 python3-pip git -y

# 3. Install Library
echo "[3/4] Install Library Bot..."
pip3 install -r requirements.txt

# 4. Ijin Akses GPIO (Opsional tapi penting)
echo "[4/4] Setting Permission..."
chmod +x main.py

echo "=========================================="
echo " INSTALASI SUKSES!"
echo " Silakan edit file main.py untuk memasukkan TOKEN."
echo " Ketik: nano main.py"
echo " Lalu jalankan dengan: python3 main.py"
echo "=========================================="
