#>>> import pyqrcode
#>>> qr = pyqrcode.create("HORN O.K. PLEASE.")
#>>> qr.png("horn.png", scale=6)

import pyqrcode
import base64
import glob
import random

for i in range(0,100):
    qr = pyqrcode.create(str(random.random()))
    qr.png("{0}.png".format(i), scale=8)

for img in glob.glob('*.png'):
    with open(img, 'rb') as fimg:
        print(base64.b64encode(fimg.read())[:100])
