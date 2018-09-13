from PIL import Image
import random

for num in range(0,64):
    binary_num = bin(num)
    bin_str = str(binary_num)
    
    num_len = len(bin_str)
    bin_str = "0"*(8-num_len)+bin_str[2:]
    print(bin_str)
    
    MAX_X = 400
    MAX_Y = 400

    pic = Image.new("RGB", (MAX_X, MAX_Y))
    pic_pix = pic.load()

    def zero_up(axis, max_axis):
        return int(255*(axis/(max_axis-1)))

    def max_down(axis, max_axis):
        return 255 - zero_up(axis, max_axis-1)

    #def both_axes(axis1, max_axis1, axis2, max_axis2):

    choose_dict = {0 : zero_up, 1 : max_down}
    choose_max_axis = {0 : MAX_X, 1 : MAX_Y}

##    R_mode = random.randint(0,1)
##    R_axis = random.randint(0,1)
##    G_mode = random.randint(0,1)
##    G_axis = random.randint(0,1)
##    B_mode = random.randint(0,1)
##    B_axis = random.randint(0,1)

    R_mode = int(bin_str[0])
    R_axis = int(bin_str[1])
    G_mode = int(bin_str[2])
    G_axis = int(bin_str[3])
    B_mode = int(bin_str[4])
    B_axis = int(bin_str[5])

    for i in range(0, MAX_X):
        for j in range(0, MAX_Y):
            choose_axis = {0 : i, 1 : j}
            color_R = choose_dict[R_mode](choose_axis[R_axis], choose_max_axis[R_axis])
            color_G = choose_dict[G_mode](choose_axis[G_axis], choose_max_axis[G_axis])
            color_B = choose_dict[B_mode](choose_axis[B_axis], choose_max_axis[B_axis])
            pic_pix[i,j] = (color_R, color_G, color_B)
        #print(color_R, color_G, color_B)

    #pic.show()
    pic_name = "GradientImages1/Image_"+str(R_mode)+str(R_axis)+str(B_mode)+str(B_axis)+str(G_mode)+str(G_axis)+".jpg"
    pic.save(pic_name)


