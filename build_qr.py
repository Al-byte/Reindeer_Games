import sys, math
sys.path.insert(0, '.qr-tools')
import qrcode
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
url = 'https://al-byte.github.io/Reindeer_Games/'
green, gold, cream, red = '#0a211e', '#e9c783', '#fff5dc', '#aa302c'
im = Image.new('RGB', (1400, 1750), green)
d = ImageDraw.Draw(im)
d.rounded_rectangle((35,35,1365,1715),radius=38,outline=gold,width=4)
d.rounded_rectangle((52,52,1348,1698),radius=28,outline='#426253',width=2)
def font(size,bold=False): return ImageFont.truetype('C:/Windows/Fonts/'+('georgiab.ttf' if bold else 'georgia.ttf'),size)
def text(y,s,size,color=cream,bold=False):
    d.text((700,y),s,font=font(size,bold),fill=color,anchor='mt')
def snow(x,y,r):
    for a in range(0,360,60):
        t=math.radians(a); dx,dy=math.cos(t),math.sin(t)
        d.line((x,y,x+r*dx,y+r*dy),fill=gold,width=4)
        for side in [-1,1]:
            b=t+side*.8
            d.line((x+r*.62*dx,y+r*.62*dy,x+r*.62*dx-r*.23*math.cos(b),y+r*.62*dy-r*.23*math.sin(b)),fill=gold,width=3)
def holly(x,y,flip=1):
    for dx,dy in [(65,-32),(35,-70)]:
        d.ellipse((x+flip*dx-32,y+dy-14,x+flip*dx+32,y+dy+14),fill='#315b49',outline=gold,width=2)
    for dx,dy in [(0,0),(24,0),(12,-22)]:
        d.ellipse((x+flip*dx-12,y+dy-12,x+flip*dx+12,y+dy+12),fill=red)
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
qr.add_data(url); qr.make(fit=True)
code=qr.make_image(fill_color=green,back_color=cream).convert('RGB')
x=(1400-code.width)//2; y=440
# Match the visible text-to-frame spacing above and below the QR code.
text_gap = 73
title_height = d.textbbox((0,0),'Reindeer Games',font=font(88,True),anchor='mt')[3]
title_y = y - 17 - text_gap - title_height
text(title_y - 86,'N O R T H   P O L E   D I S P A T C H',36,gold)
text(title_y,'Reindeer Games',88,cream,True)
snow(135,title_y+34,35); snow(1265,title_y+34,35)
# Keep the full four-module quiet zone untouched.
d.rounded_rectangle((x-17,y-17,x+code.width+17,y+code.height+17),radius=22,fill=cream,outline=gold,width=5)
im.paste(code,(x,y))
text(y+code.height+17+text_gap,'Found the keys?',70,cream,True)
text(1540,'Reward given for any useful information.',42,gold)
holly(130,1610); holly(1270,1610,-1)
out=Path('images/reindeer-games-qr.png'); im.save(out,dpi=(300,300))
import cv2
value,points,_=cv2.QRCodeDetector().detectAndDecode(cv2.imread(str(out)))
assert value==url, repr(value)
print('Verified QR destination:',value)
print('Saved:',out.resolve())
