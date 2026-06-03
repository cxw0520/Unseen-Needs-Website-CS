import os
from PIL import Image

path_in = r"c:\Users\james\OneDrive - 逢甲大學\文件\Projects\Unseen-Needs-Website-CS\assets\png\06-Unseen\unseen (10).png"
path_out = r"c:\Users\james\OneDrive - 逢甲大學\文件\Projects\Unseen-Needs-Website-CS\assets\png\06-Unseen\unseen-hero.png"

im = Image.open(path_in).convert("RGBA")
pixels = im.load()

# Swap colors: 
# - Blue body (69, 128, 179) -> Yellow (222, 192, 71)
# - Yellow heart (222, 192, 71) -> Red (205, 71, 55)
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            # check if it's blue body
            if r < 100 and g < 150 and b > 150:
                pixels[x, y] = (222, 192, 71, a)
            # check if it's yellow heart
            elif r > 200 and g > 180 and b < 100:
                pixels[x, y] = (205, 71, 55, a)

im.save(path_out)
print("Successfully created unseen-hero.png with yellow body and red heart")
