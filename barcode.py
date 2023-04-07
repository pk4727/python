import qrcode
import image

p='https://www.hackerrank.com/certificates/iframe/5de487ed423d'                    # information
features = qrcode.QRCode(version = 2,box_size = 10,border = 3)            # design
features.add_data(p)                   # for add design in information
features.make(fit = True)
image = features.make_image(fill_color = 'black',back_color = 'white')       # feature colour
image.save('Python basic.png')               # save qrcode in img
print("QRCode is created succesfully")  # done sign


# import pyzbar
# from pyzbar import cv2 ,decode
# def barcodeReader(image):
#     gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     barcodes = decode(gray_img)

# barcode = barcodeReader("My_image")
# print (barcode)