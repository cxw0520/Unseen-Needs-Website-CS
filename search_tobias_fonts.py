import os

def search_for_tobias_fonts():
    user_profile = os.environ.get("USERPROFILE", "")
    if not user_profile:
        print("User profile directory not found.")
        return
        
    print(f"Searching for Tobias font files in {user_profile}...")
    font_extensions = ('.ttf', '.otf', '.woff', '.woff2')
    found_paths = []
    
    # We will search standard directories to avoid scanning the entire hard drive (which would take too long)
    # Search Downloads, OneDrive, Documents, Desktop
    target_dirs = [
        os.path.join(user_profile, "Downloads"),
        os.path.join(user_profile, "OneDrive - 逢甲大學"),
        os.path.join(user_profile, "Documents"),
        os.path.join(user_profile, "Desktop")
    ]
    
    for base_dir in target_dirs:
        if not os.path.exists(base_dir):
            continue
        print(f"Scanning: {base_dir}")
        for root, dirs, files in os.walk(base_dir):
            # Skip hidden directories and build/git dirs
            dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() not in ('node_modules', 'dist', 'build', 'git')]
            for file in files:
                if any(file.lower().endswith(ext) for ext in font_extensions):
                    if "tobias" in file.lower():
                        full_path = os.path.join(root, file)
                        found_paths.append(full_path)
                        
    if found_paths:
        print("\nFound Tobias font files:")
        for p in found_paths:
            print(f"- {p}")
    else:
        print("\nNo Tobias font files found in standard user directories.")

if __name__ == "__main__":
    search_for_tobias_fonts()
