from escpos.printer import Usb
from escpos import codepages
from escpos import capabilities
from escpos import image
from escpos import config
from escpos import *
import time
from PIL import Image
import glob

prints = glob.glob("G:\\Mi unidad\\Sol\\blender\\fotogrametria\\sol\\aa\\printtest\\*.png")
path = "E:\\Documentos\\solpy\\Nueva carpeta\\config.yml"
# Usb(0x04b8,0x0e15,in_ep = 0x82,out_ep = 0x1,profile="TM-T20II").open
c = config.Config()
c.load(path)
Epson = Usb(0x04b8,0x0e15,in_ep = 0x82,out_ep = 0x1,profile="TM-T20II")
# Epson.control("LF")
# Epson.control("FF")
# Epson.control("CR")
# Epson.control("HT")
# Epson.control("VT")
# print(Epson.profile.profile_data.items())
# print(prints)
# print(Epson.is_online())

Epson.text("aa")

print(Epson.profile.profile_data.items())
Epson.text("aa")
Epson.text(Epson.paper_status())

# print(Epson)
# preratio = 227 / 2835
# postratio = 639 : 7980
ratio = 2.54

# print(ratio)
# 72mm = 576 px
# 80mm = 639 px
# _8m = 639

# for img in prints:
#     Epson.text(img) #path
#     Epson.cut()
    
#     imgIn = Image.open(img)
#     ImgOut = imgIn.resize((int(imgIn.width*ratio),int(imgIn.height*ratio)))
#     Epson.image(ImgOut,center=True)
#     Epson.cut()
    
# print(int(ima.width*ratio))
# c.load(path)
# Epson.textln("AA")
Epson.cut("PART")
Epson.close()