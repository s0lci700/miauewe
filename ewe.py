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
c = config.Config()
c.load(path)
Epson = Usb(0x04b8,0x0e15,in_ep = 0x82,out_ep = 0x1,profile="TM-T20II")

Epson.text("aa")

print(Epson.profile.profile_data.items())
ratio = 2.54

## RESIZE TO FULL WIDTH AND PRINT ALL IMAGES
# for img in prints:
#     Epson.text(img) #path
#     Epson.cut()
    
#     imgIn = Image.open(img)
#     ImgOut = imgIn.resize((int(imgIn.width*ratio),int(imgIn.height*ratio)))
#     Epson.image(ImgOut,center=True)
#     Epson.cut()
    

Epson.cut("PART")
Epson.close()