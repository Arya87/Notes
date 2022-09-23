from PIL import Image

filename = r'cat.jpg'
img = Image.open(filename)
size = img.size
print(size)

# 准备将图片切割成100张小图片
weight = int(size[0] // 3)
height = int(size[1] // 3)
# 切割后的小图的宽度和高度
print(weight, height)

for j in range(5):
    for i in range(5):
        box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
        region = img.crop(box)
        region.save('./image/139_{}{}.png'.format(j, i))