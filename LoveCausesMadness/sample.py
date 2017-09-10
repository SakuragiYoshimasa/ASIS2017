#!/usr/bin/python
# coding: utf-8

from bitcoin import *
from hashlib import sha256


def search():
    i = 10000
    while(i < 10000):

        hash = sha256(str(i).encode('hex')).digest()
        hash.encode('hex')

        privkeyToWIF(hash)
        pubkeyToAddress(privkeyToPubkey(hash))

        privkeyToWIF(hash, False)
        p =  pubkeyToAddress(privkeyToPubkey(hash, False))
        print(p[0:5])
        if p[0:5] == '116Es': break
        i +=1

if __name__ == '__main__':
    search()
