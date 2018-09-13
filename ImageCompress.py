from PIL import Image

orig_img = Image.open("CompressImages/img_compressed_4.png")
orig_img_pixels = orig_img.load()
orig_img_size = orig_img.size

new_img_size = (orig_img_size[0]//2, orig_img_size[1]//2)
new_img = Image.new("RGB", new_img_size)
new_img_pixels = new_img.load()

for i in range(1, orig_img_size[0], 2):
    for j in range(1, orig_img_size[1], 2):
        new_img_pixels[i//2, j//2] = orig_img_pixels[i,j]

new_img.save("CompressImages/img_compressed_5.png")
