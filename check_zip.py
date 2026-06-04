import zipfile
import os

def check_zip_contents():
    zip_path = r"c:\Users\james\OneDrive - 逢甲大學\文件\Projects\Unseen-Needs-Website-CS\assets\png-20260603T012555Z-3-001.zip"
    if not os.path.exists(zip_path):
        print(f"Zip file not found at {zip_path}")
        return
        
    print(f"Inspecting contents of {zip_path}...")
    font_extensions = ('.ttf', '.otf', '.woff', '.woff2')
    found_fonts = []
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            filename = file_info.filename
            if any(filename.lower().endswith(ext) for ext in font_extensions) or "font" in filename.lower() or "tobias" in filename.lower():
                found_fonts.append(filename)
                
    if found_fonts:
        print("Found potential font files in zip:")
        for f in found_fonts:
            print(f"- {f}")
    else:
        print("No font files found in the zip archive.")

if __name__ == "__main__":
    check_zip_contents()
