import random, string

def random_string(n):
    return random.choices(string.ascii_letters + string.digits, k=n)
