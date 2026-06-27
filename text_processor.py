class TextProcessor:
    def count_words(self, line : str) -> int:
        words = line.split(" ")
        return len(words)
    
    def count_chars(self, line : str) -> int: 
        return len(line)