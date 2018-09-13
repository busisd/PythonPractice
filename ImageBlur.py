from PIL import Image

BLUR_RANGE = 3

pic = Image.open("images/pic_0.jpg")
pic_pixels = pic.load()

pic_size = pic.size

new_pic_pixels = []
a=0
for i in range(0,pic_size[0]):
    curList = []
    for j in range(0,pic_size[1]):
        new_r = 0
        new_g = 0
        new_b = 0
        count = 0 #count the pixels in the summed region
        for f in range(max((0, i-BLUR_RANGE)), min((i+BLUR_RANGE+1, pic_size[0]))):
            for g in range(max((0, j-BLUR_RANGE)), min((j+BLUR_RANGE+1, pic_size[1]))):
                new_r += pic_pixels[f,g][0]
                new_g += pic_pixels[f,g][1]
                new_b += pic_pixels[f,g][2]
                count += 1
        newPixel = (new_r//count, new_g//count, new_b//count)

        curList.append(newPixel)
    new_pic_pixels.append(curList)

for i in range(0,pic_size[0]):
    for j in range(0,pic_size[1]):
        pic_pixels[i,j] = new_pic_pixels[i][j]

pic.save("images/pic_"+str(BLUR_RANGE)+".png")
