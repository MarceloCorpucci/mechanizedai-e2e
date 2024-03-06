import random
import string

class GenerateRandomString:
    def __init__(self):
        self.generated_string = ""
        
    @classmethod
    def generateLettersAndDigits(self, length):
        letters_and_digits = string.ascii_letters + string.digits
        self.generated_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
        return self.generated_string

    @classmethod
    def generateLetters(self, length):
        letters_and_digits = string.ascii_letters
        self.generated_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
        return self.generated_string
    
    @classmethod    
    def generateDigits(self, length):
        letters_and_digits = string.digits
        self.generated_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
        return self.generated_string