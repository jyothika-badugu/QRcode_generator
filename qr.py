import qrcode

data="https://jyothika-badugu.github.io/My_portfolio/"

qr=qrcode.make(data)

qr.save("qrcode.png")

print("qrcode is ready")
