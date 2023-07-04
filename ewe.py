from escpos.printer import Usb
from escpos import codepages
from escpos import capabilities
from escpos import image
from escpos import config
from escpos import *
import time
from PIL import Image
import glob
from random import randint

prints = glob.glob("G:\\Mi unidad\\Sol\\blender\\fotogrametria\\sol\\aa\\printtest\\new\\*.png")
path = "E:\\Documentos\\solpy\\Nueva carpeta\\config.yml"
c = config.Config()
c.load(path)
Epson = Usb(0x04b8,0x0e15,in_ep = 0x82,out_ep = 0x1,profile="TM-T20II")

print(Epson.profile.profile_data.items())
ratio = 2.5

# RESIZE TO FULL WIDTH AND PRINT ALL IMAGES
def printall():
    for img in prints:
        Epson.text(img)
        Epson.cut(mode="PART")
        
        Epson.ln(30)

        imgIn = Image.open(img)
        ImgOut = imgIn.resize((int(576),int(imgIn.height*(ratio*1.1))))
        Epson.image(ImgOut,center=True,impl="bitImageRaster")

        Epson.ln(40)

        Epson.cut()