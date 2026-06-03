import os
from PIL import Image

dir_path = r"c:\Users\james\OneDrive - 逢甲大學\文件\Projects\Unseen-Needs-Website-CS\assets\png\06-Unseen"
for filename in os.listdir(dir_path):
    if filename.endswith(".png"):
        path = os.path.join(dir_path, filename)
        try:
            im = Image.open(path)
            # convert to RGBA
            im = im.convert("RGBA")
            colors = im.getdata()
            
            # Find unique non-transparent colors
            unique_colors = {}
            for r, g, b, a in colors:
                if a > 50: # non-transparent
                    rgb = (r, g, b)
                    unique_colors[rgb] = unique_colors.get(rgb, 0) + 1
            
            # Sort by frequency
            sorted_colors = sorted(unique_colors.items(), key=lambda x: x[1], reverse=True)
            print(f"File: {filename}")
            for color, count in sorted_colors[:5]:
                # approximate color name
                r, g, b = color
                cname = "unknown"
                if r > 200 and g < 150 and b > 150:
                    cname = "pink"
                elif r > 200 and g < 100 and b < 100:
                    cname = "red"
                elif r < 100 and g > 150 and b > 150:
                    cname = "teal"
                elif r > 200 and g > 180 and b < 100:
                    cname = "yellow"
                elif r < 100 and g < 150 and b > 180:
                    cname = "blue"
                elif r > 180 and g > 180 and b > 180:
                    cname = "white/light"
                elif r < 100 and g < 100 and b < 100:
                    cname = "dark/black"
                print(f"  Color: {color} ({cname}) - Count: {count}")
        except Exception as e:
            print(f"Error {filename}: {e}")
