import random
import math

def generate_random_array(num_elements):
    numbers = []
    for x in range(num_elements):
        number = random.random()
        number = math.floor(number * 100)
        numbers.append(number)
    return numbers
