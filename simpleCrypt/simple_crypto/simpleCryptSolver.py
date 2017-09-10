#!/usr/bin/python
#coding: utf-8

KEY = 'musZTXmxV58UdwiKt8Tp'

def xor_str(x, y):
    if len(x) > len(y):
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x[:len(y)], y)])
    else:
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x, y[:len(x)])])

key = KEY.encode('hex')
f = open('flag.enc', 'r')
enc = f.read().encode('hex').decode('hex')
f.close()

flag = xor_str(key * (len(enc) // len(key) + 1), enc).encode('hex')

f = open('flag', 'w')
f.write(flag.decode('hex'))
f.close()
