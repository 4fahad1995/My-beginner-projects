import qrcode as qr 

def getqr():
    data=input('Enter url:')
    img=qr.make(data)
    img.save('qr.png') 
