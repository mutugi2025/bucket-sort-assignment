import random

def generate_dataset(size):
    return [random.randint(1,1000000) for _ in range(size)]