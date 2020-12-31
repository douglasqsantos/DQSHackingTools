#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/hashlib.html
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
# platinum: eefc1767fec313f654053139e7d7aa4d786e6387
# newlife: 83b996ac02b20aed2705130b008222a456d6d04f
# moonligh: e0a5b617fb6476dc12dbefd701968de5a3c7468d

from urllib.request import urlopen
import hashlib
import time

# Colors
RESET, GREEN, RED = '\033[0m', '\033[92m', '\033[91m'


def found(password,count):
  end = time.time() - start
  print('\n{}[+]{} The Password is: {}{}{} found in {:.2f} segs. Processed {}{}{} hashes'.format(GREEN,RESET,GREEN,str(password), RESET, end,GREEN,count,RESET))


sha1hash = input("[+] Enter Sha1 Hash: ")

# Start the crack
start = time.time()

# count the amount of passwords processed
count = 0

# Get the list
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(),'utf-8')

# Hash all the list if needed
for password in passlist.split('\n'):
  hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
  if hashguess == sha1hash:
    found(password,count)
    quit()
  else:
    print('{}[-]{} Password guess {}{}{} doe not match, trying next...'.format(RED,RESET,RED,str(password),RESET))
    count = count + 1


print("Password not in passwordlist")
