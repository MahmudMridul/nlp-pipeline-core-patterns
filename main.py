def read_file(file_path) -> list[str]:
    try:
        with open(file=file_path, mode="r", encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    FILE = "file.txt"
    print(read_file(FILE))


if __name__ == "__main__":
    main()
