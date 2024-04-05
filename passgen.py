import string
import random


class PassGen():
    
    def __init__(self, password_length = 8) -> None:
        self.wordlist = self.load_wordlist('wordlist.txt')
        self.charset = string.ascii_letters + string.digits
        self.password_length = password_length
    
    def load_wordlist(self, file_path):
        try:
            with open(file_path, 'r') as file:
                wordlist = file.read().splitlines()
            return wordlist
        except FileNotFoundError:
            return None

    def generate_password(self):
        return ''.join(random.choice(self.charset) for _ in range(self.password_length))

    