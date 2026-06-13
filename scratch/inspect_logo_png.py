import os
from PIL import Image

path = r"c:\Users\james\OneDrive - 逢甲大學\文件\Projects\Unseen-Needs-Website-CS\assets\png\01-Logo\logo.png"
if os.path.exists(path):
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    
    # Analyze transparency of columns (x)
    col_has_pixels = []
    for x in range(w):
        has_pixel = False
        for y in range(h):
            r, g, b, a = im.getpixel((x, y))
            if a > 20: # non-transparent
                has_pixel = True
                break
        col_has_pixels.append(has_pixel)
        
    # Group continuous segments
    segments = []
    in_segment = False
    start_x = 0
    for x in range(w):
        if col_has_pixels[x] and not in_segment:
            in_segment = True
            start_x = x
        elif not col_has_pixels[x] and in_segment:
            in_segment = False
            segments.append((start_x, x - 1))
    if in_segment:
        segments.append((start_x, w - 1))
        
    print(f"Found {len(segments)} segments:")
    for idx, seg in enumerate(segments):
        print(f"Segment {idx}: {seg}, width: {seg[1]-seg[0]+1}")
        
    # Let's also calculate the gaps between segments
    for idx in range(len(segments) - 1):
        gap = segments[idx+1][0] - segments[idx][1] - 1
        print(f"  Gap between {idx} and {idx+1}: {gap} pixels")
else:
    print("logo.png not found!")
