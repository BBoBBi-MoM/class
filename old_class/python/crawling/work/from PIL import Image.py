from PIL import Image
from time import time
start_time = time()
# %%
def rotate(path):
    
    original_img = Image.open(path)
    original_img_size = original_img.size
    original_width = original_img_size[0]
    original_height = original_img_size[1]
    rotated_img = Image.new('RGB',(original_height,original_width))
    width = original_height
    height = original_width
    for y in range(height):
        for x in range(width):
            rotated_img.putpixel((x,y),original_img.getpixel((height-1-y,x)))
    #rotated_img.show()
    #rotated_img.save('rotated_img.jpg')
    #original_img.close()
    #rotated_img.close()

#ny_path = './data/newyork.jpg'
#lenna_path = './data/lenna.png'
path = './data/KakaoTalk_20230127_105724457.jpg'
rotate(path)
end_time = time()
print(end_time-start_time)
#mirror(ny_path)