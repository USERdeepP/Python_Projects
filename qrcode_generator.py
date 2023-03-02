import qrcode
def generate(a) :
    img = qrcode.make(a)
    type(img)
    img.save(f'{b[1]}.png')
    

b = input("paste or enter link/number/text to generate qr code ")
generate(b)
