import os
import sys

def check_fonts():
    fonts_dir = r"C:\Windows\Fonts"
    if not os.path.exists(fonts_dir):
        print("Windows Fonts directory not found.")
        return
    
    print("Searching for Tobias font files in C:\\Windows\\Fonts...")
    found_files = []
    for file in os.listdir(fonts_dir):
        if "tobias" in file.lower():
            found_files.append(file)
            
    if found_files:
        print("Found Tobias font files:")
        for f in found_files:
            print(f"- {f}")
    else:
        print("No Tobias font files found in C:\\Windows\\Fonts.")

if __name__ == "__main__":
    check_fonts()
