import string
import random


class RandomUtils:
    min_string_length = 5
    max_string_length = 50

    def get_random_string(self):
        result = ''.join((random.choice(string.ascii_lowercase) for x in
                          range(random.randint(self.min_string_length, self.max_string_length))))
        return result
