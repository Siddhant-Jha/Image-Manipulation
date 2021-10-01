from PIL import Image
from PIL import ImageFilter

img = Image.open("image.jpg")
print(img.size)

#Original Size of the image is 2853x3803
#The size of image is way to large let's resize it a bit

l,b = img.size
l //= 5
b //= 5

imgR = img.resize((l,b))
print(imgR.size)

#New size of the image is 285x380 As we reduced the size of the image by factor of 10
#New size of the image is 570x760 As we reduced the size of the image by factor of 5

#Let's find edge from the image using edge detection algorithm

edges = imgR.filter(ImageFilter.FIND_EDGES)

edges.save("edge3.jpg")
bands = edges.split()

outline = bands[0].point(lambda x: 255 if x<100 else 0)
# outline.save("outline1.jpg")
#edges = imgR.filter(ImageFilter.FIND_EDGES)
edges = imgR.filter(ImageFilter.FIND_EDGES)

edges.save("edge3.jpg")
bands = edges.split()

outline = bands[0].point(lambda x: 255 if x<100 else 0)
# outline.save("outline1.jpg")
