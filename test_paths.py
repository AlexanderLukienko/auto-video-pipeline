from config import ALL_DIRS

def check_dirs():
    for folder in ALL_DIRS:
        if folder.exists():
            print(f"✅ {folder} существует")
        else:
            print(f"❌ {folder} НЕ найден")

if __name__ == "__main__":
    check_dirs()