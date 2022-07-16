import pyqrcode

address = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11652530580705530&slink=oljp2r'
url = pyqrcode.create(address)
url.png('Ferrari.png', scale=8)
