#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/hashlib.html

import hashlib

hashvalue = input("[*] Enter a string to hash: ")

# hashobj = hashlib.md5()
# hashobj.update(hashvalue.encode())
# print(hashobj.hexdigest())

strhash = hashvalue.encode()

### Hashes
print("MD5: {}".format(hashlib.md5(strhash).hexdigest()))
print("SHA1: {}".format(hashlib.sha1(strhash).hexdigest()))
print("SHA224: {}".format(hashlib.sha224(strhash).hexdigest()))
print("SHA256: {}".format(hashlib.sha256(strhash).hexdigest()))
print("SHA384: {}".format(hashlib.sha384(strhash).hexdigest()))
print("SHA512: {}".format(hashlib.sha512(strhash).hexdigest()))