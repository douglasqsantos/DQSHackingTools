#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/hashlib.html
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
# http://patorjk.com/software/taag/#p=testall&f=Graffiti&t=BREAK%20THE%20HASH
# md5: amigos: c2b592488a765722513420108c466524
# sha1: jakarta: 632a86021c4b0c02a6bb86b2194417c586054b3e
# sha224: usmarine: 1d678efc94cb6c25234d419222912420ca9790c2d38b82c6b0266b5a
# sha256: contract: cc8321d6375c494d043fdd0260f21bc0ec51dacc9f6abb7f909cdcd3041b78bf
# sha384: atticus: 6304a5096e2914126c5dd41bf7112f718d091e4f22027e89adfff0072c2efc85f4458863a4f17dd7ae4aecd15af0a48f
# sha512: shodan: 99c05883fd2a67737a7b3515f8dfd73518d6f4474b4bcdfa0a4147e3f710ba797c6914156bae88972a5c3302e69a5fd8d9c17aa2c578f6e4831add82f20442c9
# password-list-top-10000.txt

# TODO: Support to get the wordlist from an URL

"""
./dqsbrutehash.py --hash c2b592488a765722513420108c466524 --wordlist ./password-list-top-10000.txt --hashtype md5 --silence

[+] The String for c2b592488a765722513420108c466524 is: amigos found in 0.03 segs. Processed 7569 hashes

./dqsbrutehash.py --hash 632a86021c4b0c02a6bb86b2194417c586054b3e --wordlist ./password-list-top-10000.txt --hashtype sha1 --silence

[+] The String for 632a86021c4b0c02a6bb86b2194417c586054b3e is: jakarta found in 0.03 segs. Processed 9668 hashes

./dqsbrutehash.py --hash 1d678efc94cb6c25234d419222912420ca9790c2d38b82c6b0266b5a --wordlist ./password-list-top-10000.txt --hashtype sha224 --silence

[+] The String for 1d678efc94cb6c25234d419222912420ca9790c2d38b82c6b0266b5a is: usmarine found in 0.03 segs. Processed 9882 hashes

./dqsbrutehash.py --hash cc8321d6375c494d043fdd0260f21bc0ec51dacc9f6abb7f909cdcd3041b78bf --wordlist ./password-list-top-10000.txt --hashtype sha256 --silence

[+] The String for cc8321d6375c494d043fdd0260f21bc0ec51dacc9f6abb7f909cdcd3041b78bf is: contract found in 0.04 segs. Processed 9418 hashes

./dqsbrutehash.py --hash 6304a5096e2914126c5dd41bf7112f718d091e4f22027e89adfff0072c2efc85f4458863a4f17dd7ae4aecd15af0a48f --wordlist ./password-list-top-10000.txt --hashtype sha384 --silence

[+] The String for 6304a5096e2914126c5dd41bf7112f718d091e4f22027e89adfff0072c2efc85f4458863a4f17dd7ae4aecd15af0a48f is: atticus found in 0.03 segs. Processed 8894 hashes

./dqsbrutehash.py --hash 99c05883fd2a67737a7b3515f8dfd73518d6f4474b4bcdfa0a4147e3f710ba797c6914156bae88972a5c3302e69a5fd8d9c17aa2c578f6e4831add82f20442c9 --wordlist ./password-list-top-10000.txt --hashtype sha512 --silence

[+] The String for 99c05883fd2a67737a7b3515f8dfd73518d6f4474b4bcdfa0a4147e3f710ba797c6914156bae88972a5c3302e69a5fd8d9c17aa2c578f6e4831add82f20442c9 is: shodan found in 0.03 segs. Processed 8580 hashes


"""

import hashlib
import sys
import time
import argparse
import os

# Colors
RESET = '\033[0m'
GRAY = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'

# Hashes supported
HASHES = ['md5','sha1','sha224','sha256', 'sha384', 'sha512']

# Author
AUTHOR = 'Douglas Quintiliano dos Santos'

# Version
VERSION = '1.0'

BREAK_THE_HASH_COOL_LOOKING = '''
 /$$$$$$$  /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$   /$$       /$$$$$$$$ /$$   /$$ /$$$$$$$$       /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$
| $$__  $$| $$__  $$| $$_____/ /$$__  $$| $$  /$$/      |__  $$__/| $$  | $$| $$_____/      | $$  | $$ /$$__  $$ /$$__  $$| $$  | $$
| $$  \ $$| $$  \ $$| $$      | $$  \ $$| $$ /$$/          | $$   | $$  | $$| $$            | $$  | $$| $$  \ $$| $$  \__/| $$  | $$
| $$$$$$$ | $$$$$$$/| $$$$$   | $$$$$$$$| $$$$$/           | $$   | $$$$$$$$| $$$$$         | $$$$$$$$| $$$$$$$$|  $$$$$$ | $$$$$$$$
| $$__  $$| $$__  $$| $$__/   | $$__  $$| $$  $$           | $$   | $$__  $$| $$__/         | $$__  $$| $$__  $$ \____  $$| $$__  $$
| $$  \ $$| $$  \ $$| $$      | $$  | $$| $$\  $$          | $$   | $$  | $$| $$            | $$  | $$| $$  | $$ /$$  \ $$| $$  | $$
| $$$$$$$/| $$  | $$| $$$$$$$$| $$  | $$| $$ \  $$         | $$   | $$  | $$| $$$$$$$$      | $$  | $$| $$  | $$|  $$$$$$/| $$  | $$
|_______/ |__/  |__/|________/|__/  |__/|__/  \__/         |__/   |__/  |__/|________/      |__/  |__/|__/  |__/ \______/ |__/  |__/

By: {} Version: {}
'''.format(AUTHOR,VERSION)

# Start the crack
start = time.time()

"""
Function to define the parameters that we can handle
"""
def get_parser():
  parser = argparse.ArgumentParser(description="Script to check a given hash against a wordlist by hashing it in the following supported formats: {}".format(HASHES))
  parser.add_argument('--hashtype',type=str,help='Supported Hashes: {}'.format(HASHES))
  parser.add_argument('--wordlist',type=str,help='Path to the wordlist')
  parser.add_argument('--hash',type=str,help='Hash to Crack')
  parser.add_argument('--silence',help='Do not show the tried password',action="store_true")
  parser.add_argument('-v', '--version',action='version',version='%(prog)s {}'.format(VERSION))
  return parser

"""
Function to handle the parameters given
"""
def get_parsed_args(parser, args):
  args_parsed = parser.parse_args(args)
  problem = False

  if not args_parsed.hashtype:
    print('{}[!!]{} Need a hashtype to work with ({}--hashtype{} : {})'.format(RED,RESET,GREEN,RESET,HASHES))
    problem = True
  if not args_parsed.hash:
    print('{}[!!]{} Need a hash to work with ({}--hash{})'.format(RED,RESET,GREEN,RESET))
    problem = True
  if not args_parsed.wordlist:
    print('{}[!!]{} Need a wordlist to work with ({}--wordlist{})'.format(RED,RESET,GREEN,RESET))
    problem = True

  if problem:
    print('{}[!!]{} Use {}{}{} --hashtype {} --wordlist rockyou.txt --hash YOURHASH'.format(RED,RESET,RED,sys.argv[0],RESET,HASHES))

  return args_parsed


"""
Function to handle the wordlist given
"""
def check_file(file):
  if not os.path.isfile(file):
    return { "msg" : "File {} Does not Exist!".format(file), "eval": False }
  elif not os.access(file,os.R_OK):
    return { "msg": "Access Denied for File: {}!".format(file), "eval": False } 
  else:
    return { "msg": "Access Ok", "eval": True }

"""
Function to handle the password found msg
"""
def found(str_hash, password,hashtype,count):
  end = time.time() - start
  print('{}[+]{} The Hash Given is: {}{}{}'.format(GREEN,RESET,GREEN,str(str_hash),RESET))
  print("{}[+]{} The Hash Type Given is: {}{}{}".format(GREEN,RESET,GREEN,str(hashtype),RESET))
  print("{}[+]{} The String for the Given Hash is: {}{}{}".format(GREEN,RESET,GREEN,str(password),RESET))
  print("{}[+]{} Found in {}{:.2f}{} segs.".format(GREEN,RESET,GREEN,end,RESET))
  print("{}[+]{} Hashes Processed: {}{}{} ".format(GREEN,RESET,GREEN,count,RESET))


def hasher(hashtype, word):
  # Supported Hashes so Far
  # ['md5','sha1','sha224','sha256', 'sha384', 'sha512']
  if hashtype == 'md5':
    return hashlib.md5(word.strip()).hexdigest()
  elif hashtype == 'sha1':
    return hashlib.sha1(word.strip()).hexdigest()
  elif hashtype == 'sha224':
    return hashlib.sha224(word.strip()).hexdigest()
  elif hashtype == 'sha256':
    return hashlib.sha256(word.strip()).hexdigest()
  elif hashtype == 'sha384':
    return hashlib.sha384(word.strip()).hexdigest()
  elif hashtype == 'sha384':
    return hashlib.sha384(word.strip()).hexdigest()
  elif hashtype == 'sha512':
    return hashlib.sha512(word.strip()).hexdigest()
  else:
    print("{}[!!]{} The Hash {}{}{} does not have support yet.".format(RED,RESET,RED,hashtype,RESET))
    quit()

def crack_hash(hashtype, str_hash, wordlist, silence):

  if not hashtype or not str_hash or not wordlist:
    print("[+] Something is Wrong. Aborting...")
    quit()

  # count the amount of passwords processed
  count = 0

  file = open(wordlist, "r")
  for word in file.readlines():
    enc_wrd = word.encode('utf-8')
    digest = hasher(hashtype, enc_wrd)
    if digest == str_hash:
      found(str_hash, word.strip(),hashtype, count)
      quit()
    else:
      if not silence:
        print('{}[-]{} Password guess {}{}{} doe not match, trying next...'.format(RED,RESET,RED,str(word.strip()),RESET))
      count = count + 1

  print("[!!] Password Not In List")


def main():
  print(BREAK_THE_HASH_COOL_LOOKING)
  parser = get_parser()
  args = get_parsed_args(parser, sys.argv[1:])
  problem = False

  if args.wordlist:
    ck_wordlist = check_file(args.wordlist)
    if ck_wordlist["eval"] == False:
      print("{}[!!]{} {}".format(RED,RESET,ck_wordlist["msg"]))
      problem = True
  
  if not problem:
    crack_hash(args.hashtype, args.hash, args.wordlist, args.silence)


if __name__ == "__main__":
  main()