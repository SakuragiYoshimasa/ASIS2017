#!/usr/bin/python
# coding:utf-8
import random
#from secret import FLAG

KEY = 'musZTXmxV58UdwiKt8Tp'

def xor_str(x, y):
    if len(x) > len(y):
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x[:len(y)], y)])
    else:
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x, y[:len(x)])])

flag, key = FLAG.encode('hex'), KEY.encode('hex') #FLAGとKEYを16進数でエンコード
enc = xor_str(key * (len(flag) // len(key) + 1), flag).encode('hex')

ef = open('flag.enc', 'w')
ef.write(enc.decode('hex'))
ef.close()
