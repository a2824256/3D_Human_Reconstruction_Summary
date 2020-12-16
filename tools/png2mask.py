import cv2
import numba
from PIL import Image

# 带numba加速计算，请安装numba
# pip install numba
@numba.jit
def png2mask(img):
    shape = img.shape
    width = shape[0]
    height = shape[1]
    for y in range(height):
        for x in range(width):
            color = img[x, y]
            if color[3] == 0:
                img[x, y] = [0, 0, 0, 255]
            else:
                img[x, y] = [255, 255, 255, 255]
    return img

if __name__ == '__main__':
    img = cv2.imread('ce.png', -1)
    img_copy = img.copy()
    result = png2mask(img_copy)
    image = Image.fromarray(result)
    image = image.convert('L')
    image.save('ce_mask.png')
    image.show()