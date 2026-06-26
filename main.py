from collections.abc import Generator
import logging
import time
from functools import wraps
from managed_file import ManagedFile

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timing
@logger
def read_file(file_path: str) -> Generator[str, None, None]:
    try:
        with ManagedFile(path=file_path, mode="r") as file:
            for line in file:
                yield line.rstrip("\n")
            # raise OSError
    except FileNotFoundError as f:
        logging.error(f"File not found: {f}")
        raise
    except OSError as os:
        logging.error(f"OS error while reading file: {os}")
        raise



def main():
    FILE = "file.txt"
    gen = read_file(FILE)
    
    for line in gen:
        print(line)
    

if __name__ == "__main__":
    main()
