class ManagedFile:
    def __init__(self, path : str, mode : str = "r"):
        self.path = path
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file
    
    def __exit__(self, exc_type, exc, tb):
        print(f"__exit__ called - exc_type: {exc_type} exc: {exc} tb: {tb}")
        self.file.close()
        return False