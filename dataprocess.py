from PIL import Image
import os

dir = os.listdir('images/')
i = 0
for s in dir:
    if s[-4:] == '.png':
        name = s[0:-4]
        img = Image.open('images/'+s)
        im = img.convert('RGB')
        im.save('images/name'+'.jpg')
        i+=1
        print(i)

#
