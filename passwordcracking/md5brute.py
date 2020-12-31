#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/hashlib.html
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
# ministry: 3e98ecfa6a4c765c5522f897a4a8de23
# amigos: c2b592488a765722513420108c466524
# password-list-top-10000.txt

import hashlib
import sys
import time

# Colors
RESET, GREEN, RED = '\033[0m', '\033[92m', '\033[91m'

def found(password,count):
  end = time.time() - start
  print('\n{}[+]{} The Password is: {}{}{} found in {:.2f} segs. Processed {}{}{} hashes'.format(GREEN,RESET,GREEN,str(password), RESET, end,GREEN,count,RESET))

def tryOpen(wordlist):
  try:
    global pass_file
    pass_file = open(wordlist, "r")
  except:
    print("[!!] No Such file at That Path!")
    quit()

pass_hash = input("[*] Enter MD5 Hash Value: ")
wordlist = input("[*] Enter Path to the Password File: ")
tryOpen(wordlist)

# Start the crack
start = time.time()

# count the amount of passwords processed
count = 0

for word in pass_file:
  # print("[-] Trying: {} ".format(word.strip('\n')))
  enc_wrd = word.encode('utf-8')
  md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

  if md5digest == pass_hash:
    found(word.strip(),count)
    # print('[+] Password Found: {} '.format(word.strip()))
    # sys.exit(0)
    quit()
  else:
    print('{}[-]{} Password guess {}{}{} doe not match, trying next...'.format(RED,RESET,RED,str(word.strip()),RESET))
    count = count + 1

print("[!!] Password Not In List")