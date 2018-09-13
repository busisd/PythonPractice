from PIL import Image

##pic = Image.new("RGB", (60,60), color="red")
##pic_pixels = pic.load()

img1 = Image.open("MeldImages/img1.png")
img2 = Image.open("MeldImages/img2.png")

#Image.alpha_composite(img2, img1).show()
Image.blend(img1, img2, .5).show()
#Image.blend(img1, img2, .2).show()
#Image.blend(img1, img2, .8).show()

