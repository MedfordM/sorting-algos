from .utils.random_data import generate_random_array
from .algorithms import bubble

def main():
    num_elements = 100000
    data = generate_random_array(num_elements)
    print('Generated ' + str(num_elements) + ' elements')
    data, execution_time = bubble.sort(data)
    print('Bubble sort: ' + str(execution_time) + 'ms')

if __name__ == "__main__":
    main()
