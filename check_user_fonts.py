import os

def check_user_fonts():
    # User local fonts directory on Windows
    user_profile = os.environ.get("USERPROFILE", "")
    local_fonts_dir = os.path.join(user_profile, "AppData", "Local", "Microsoft", "Windows", "Fonts")
    
    if not os.path.exists(local_fonts_dir):
        print(f"Local fonts directory not found: {local_fonts_dir}")
        return
        
    print(f"Searching for Tobias font files in {local_fonts_dir}...")
    found_files = []
    for file in os.listdir(local_fonts_dir):
        if "tobias" in file.lower():
            found_files.append(file)
            
    if found_files:
        print("Found Tobias font files:")
        for f in found_files:
            print(f"- {f}")
    else:
        print("No Tobias font files found in user-level directory.")

if __name__ == "__main__":
    check_user_fonts()
