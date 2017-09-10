# coding: utf-8
import binascii

f = open('image1.png', 'rb')
data = f.read()
f.close()
pos = []
target = 'IDAT' #IDHR、PLTE、tRNS、IDAT複数、IEND

for i in range(len(data) - 4):
    ds = data[i:i+4]
    flag = True
    for d in ds:
        if d > 127:
            flag = False
    if flag:
        s = ''.join(map(chr, ds))
        if s == target:
            pos.append(i - 4)

print(len(pos))

for p in pos:
    length = int.from_bytes(data[p:p+4],'big')
    print(length)
    chank_type = data[p + 4 : p + 8]
    idat_data = data[p + 8 : p + 8 + length]
    crc = int.from_bytes(data[p + 8 + length :p + 8 + length + 4], 'big')
    check_crc = binascii.crc32(chank_type + idat_data)
    print('crc:%s, check:%s' % (crc, check_crc))
    if crc != check_crc:
        print('wrong crc')
