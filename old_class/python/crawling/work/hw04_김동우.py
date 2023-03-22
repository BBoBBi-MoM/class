#%%
from PIL import Image

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
    rotated_img.show()
    rotated_img.save('rotated_img.jpg')
    original_img.close()
    rotated_img.close()

def mirror(path):
    original_img = Image.open(path)
    original_img_size = original_img.size
    width = original_img_size[0]
    height = original_img_size[1]
    mirror_img = Image.new('RGB',(width,height))
    for y in range(height):
        for x in range(width):
            mirror_img.putpixel((x,y),original_img.getpixel((width-1-x,y)))
    mirror_img.show()
    mirror_img.save('mirror_img.jpg')
    original_img.close()
    mirror_img.close()
# %%
ny_path = './data/newyork.jpg'
lenna_path = './data/lenna.png'
rotate(ny_path)
mirror(ny_path)
rotate(lenna_path)
mirror(lenna_path)


# %%
