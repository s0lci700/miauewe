from escpos.printer import Usb
Epson = Usb(0x04b8,0x0e15)
print(Epson)
Epson.text('''
           
           ESKERE
           
           ''')
Epson.cut()
Epson.close()