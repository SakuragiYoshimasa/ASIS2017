#coding: utf-8

import numpy as np
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

img1 = Image.open('image1.png').convert('RGBA')
img2 = Image.open('image2.png').convert('RGBA')


data1 = np.asarray(img1)
data2 = np.asarray(img2)

#print(data1.shape) #(56, 2752, 4)
#print(data2.shape) #(74, 2738, 4)
#img1.show()
#img2.show()

converted_data1 = []
n = 0
'''
for i in range(data2.shape[0]):
    for j in range(data2.shape[1]):
        if not (data2[i][j][0] == 71 and data2[i][j][1] == 112 and data2[i][j][2] == 76):
            print('%d, %d, %s' % (i, j, data2[i][j]))
        #    n += 1
'''

valid_data1 = data1[1:6]
print(valid_data1.shape)

#13760 = 20 * 688
for j in range(4):

    for i in range(5):
        row = []
        for k in range(688):

            row.append(valid_data1[i][k + 688 * j])

        converted_data1.append(row)

converted_data1 = np.array(converted_data1)
print(converted_data1.shape)


img1 = Image.fromarray(converted_data1)
img1.show()
img2 = Image.fromarray(data2)

print(n)

#print('data1')
#print(data1)
#print('data2')
#print(data2)
