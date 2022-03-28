import pyqrcode
from pyqrcode import QRCode
import turtle

# string which represent the QR code
s = "https://remote-coders-2022.netlify.app/"

# here i will generate qrcode for my website
# generate QR code

url = pyqrcode.create(s)

# create and save the svg file naming "myqr.svg"

url.svg("mywebsite.svg", scale=8)

# Open this in Browser(Chrome, Microsoft Edge, FireFox, DuckDuckGo)
# Scan the Qr Code with Phone Camera
# You will be redirect on that website which you fill in code

# made with ❤️ by Silent programmer