# coding: utf-8
import binascii

idats1 = []
idats2 = []
idat_last1 = 0
idat_last2 = 0

f = open('image1.png', 'rb')
data1 = f.read()
f.close()
pos1 = []
target = 'IDAT' #IDHR、PLTE、tRNS、IDAT複数、IEND

for i in range(len(data1) - 4):
    ds = data1[i:i+4]
    flag = True
    for d in ds:
        if d > 127:
            flag = False
    if flag:
        s = ''.join(map(chr, ds))
        if s == target:
            pos1.append(i - 4)

print(len(pos1))

for p in pos1:
    length = int.from_bytes(data1[p:p+4],'big')
    print(length)
    chank_type = data1[p + 4 : p + 8]
    idat_data = data1[p + 8 : p + 8 + length]
    crc = int.from_bytes(data1[p + 8 + length :p + 8 + length + 4], 'big')
    check_crc = binascii.crc32(chank_type + idat_data)
    idats1.append(data1[p:p + 8 + length + 4])
    idat_last1 = p + 8 + length + 4
    print('crc:%s, check:%s' % (crc, check_crc))
    if crc != check_crc:
        print('wrong crc')


'''
2
'''
f = open('image2.png', 'rb')
data2 = f.read()
f.close()
pos2 = []
target = 'IDAT' #IDHR、PLTE、tRNS、IDAT複数、IEND

for i in range(len(data2) - 4):
    ds = data2[i:i+4]
    flag = True
    for d in ds:
        if d > 127:
            flag = False
    if flag:
        s = ''.join(map(chr, ds))
        if s == target:
            pos2.append(i - 4)

print(len(pos2))

for p in pos2:
    length = int.from_bytes(data2[p:p+4],'big')
    print(length)
    chank_type = data2[p + 4 : p + 8]
    idat_data = data2[p + 8 : p + 8 + length]
    crc = int.from_bytes(data2[p + 8 + length :p + 8 + length + 4], 'big')
    check_crc = binascii.crc32(chank_type + idat_data)
    idats2.append(data2[p:p + 8 + length + 4])
    idat_last2 = p + 8 + length + 4
    print('crc:%s, check:%s' % (crc, check_crc))
    if crc != check_crc:
        print('wrong crc')


'''
Write data
'''
f = open('exchanged_img1.png', 'wb')
f.write(data1[:pos1[0]])

for idat in idats2:
    f.write(idat)

f.write(data1[idat_last1:])
f.close()

f = open('exchanged_img2.png', 'wb')
f.write(data2[:pos2[0]])

for idat in idats1:
    f.write(idat)

f.write(data2[idat_last2:])
f.close()


f = open('sync_img.png', 'wb')
f.write(data2[:pos2[0]])

for idat in idats1:
    f.write(idat)
for idat in idats2:
    f.write(idat)



f.write(data2[idat_last2:])
f.close()
