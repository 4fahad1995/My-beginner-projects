import qrcode 
from tkinter import*
from tkinter import messagebox
from PIL import Image

def getqr():
    qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=4,)
    qr.add_data(urlentry.get())
    qr.make(fit=True)
    img=qr.make_image(fill_color='red',back_color='white')
    img.save(('Google_qr_ver2.png'))
    messagebox.showinfo('My QRCode Generator','QRCode Generated Successfully')
    

wn=Tk()
wn.title('My QRCode Generator')
wn.geometry('400x100')


url=Label(wn,text='Enter URL with http://')
url.grid(row=1,column=1)

urlval=StringVar()
urlentry=Entry(wn,textvariable=urlval)
urlentry.grid(row=1,column=3)

Button(text='Get QRcode',command=getqr).grid(row=2,column=3)
wn.mainloop()







