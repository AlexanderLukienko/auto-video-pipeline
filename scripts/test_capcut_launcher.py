from app.services.capcut.launcher import ensure_capcut_started


def main():
    ensure_capcut_started()
    print("✅ CapCut запущен и активирован")


if __name__ == "__main__":
    main()