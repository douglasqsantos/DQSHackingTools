#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import ftplib

def anonLogin(host):
  try:
    ftp = ftplib.FTP(host)
    ftp.login('ftp','ftp')
    print('[+] {} FTP Anonymous Logon Succeeded.'.format(host))
    ftp.quit()
    return True
  except Exception as e:
    print('[-] {} FTP Anonymous Logon Failed: {}'.format(host, e))

host = input("[*] Enter the IP Address: ")

anonLogin(host)

