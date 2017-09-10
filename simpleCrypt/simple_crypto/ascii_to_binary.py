#coding: utf-8

f = open('flag', 'r')
str_data = f.read()
f.close()

png = open('flag.png', 'wb')
length = len(str_data)

for i in range(length // 2):
    a = int(str_data[i * 2],16)
    b = int(str_data[i * 2 + 1],16)

    c = a * 16 + b
    png.write(c.to_bytes(1, 'big'))

png.close()
