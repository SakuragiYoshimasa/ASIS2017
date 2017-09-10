# coding: utf-8
import binascii

f = open('sync_plte_img.png', 'rb')
data = f.read()
f.close()
p = 8
target = 'IDHR' #IDHR、PLTE、tRNS、IDAT複数、IEND
length = int.from_bytes(data[p:p+4],'big')
chank_type = data[p + 4 : p + 8]
color_bit = b'\x01'
w = (2752).to_bytes(4, 'big')
h = (54).to_bytes(4, 'big')

new_idhr = b''
new_idhr += data[:p+4]
new_idhr += chank_type
#new_idhr += data[p + 8: p + 16] #w and h
new_idhr += w
new_idhr += h
new_idhr += color_bit#color_bit
new_idhr += data[p + 17: p + 8 + length] #other info
#new_idhr += binascii.crc32(chank_type + data[p + 8: p + 16] + b'\x01' + data[p + 17: p + 8 + length]).to_bytes(4, 'big')
new_idhr += binascii.crc32(chank_type + w + h + color_bit + data[p + 17: p + 8 + length]).to_bytes(4, 'big')


f = open('sync_plte_img_01.png', 'wb')
f.write(new_idhr + data[33:])
print(new_idhr + data[33:])
f.close()
