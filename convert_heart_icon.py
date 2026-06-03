import os
from PIL import Image

path = r"c:\Users\james\OneDrive - 逢甲大學\文件\Projects\Unseen-Needs-Website-CS\assets\png\06-Unseen\unseen-heart.png"
im = Image.open(path).convert("RGBA")
pixels = im.load()

# Replace red pixels (205, 71, 55) with white (255, 255, 255)
# We can check if r > 180 and g < 100 and b < 100 to be robust to anti-aliasing
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            # check if it's red (body)
            if r > 180 and g < 100 and b < 100:
                pixels[x, y] = (255, 255, 255, a)

im.save(path)
print("Successfully converted unseen-heart.png red pixels to white")
