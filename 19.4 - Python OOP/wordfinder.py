"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file):
        """Defines file, prints the file lenth"""
        self.file = file
        file_len = self.count_file_length()
        print(f"{file_len} words read")
    
    def read_file(self):
        """Opens the file given, reads the lines, closes the file, then returns the file content to be used"""
        file = open(self.file, 'r')
        content = file.readlines()
        file.close()
        return content
    
    def random(self):
        """Returns a random choice from file"""
        content = self.read_file()
        return(random.choice(content).strip())
    
    def count_file_length(self):
        """Finds the file length"""
        conent = self.read_file()
        return len(conent)
    
class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)

    def random(self):
        content = self.read_file()
        rand_val = (random.choice(content).strip())
        if rand_val and not rand_val.startswith("#"):
            return rand_val
        else:
            return self.random()