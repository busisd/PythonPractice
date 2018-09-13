from PIL import Image

MAX_X = 400
MAX_Y = 400

pic = Image.new("RGB", (MAX_X, MAX_Y))
pic_pix = pic.load()

for i in range(0, MAX_X):
    for j in range(0, MAX_Y):
        color_R = 255 - int(255*(i/(MAX_X-1)))
        color_G = int(255*(j/(MAX_Y-1)))
        color_B = int(255*(i/(MAX_X-1))/2) + int(255*(j/(MAX_Y-1))/2)
        pic_pix[i,j] = (color_R, color_G, color_B)
    #print(color_R, color_G, color_B)

pic.show()
