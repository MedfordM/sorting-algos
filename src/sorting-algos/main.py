from .utils.random_data import generate_random_array
from .algorithms import bubble
from .algorithms import insertion
from .algorithms import selection
from .algorithms import merge

def main():
    num_elements = 10000
    data = generate_random_array(num_elements)
    data, execution_time = bubble.sort(data)
    print('Bubble sort: ' + str(execution_time) + 'ms')

    data = generate_random_array(num_elements)
    data, execution_time = selection.sort(data)
    print('Selection sort: ' + str(execution_time) + 'ms')

    data = generate_random_array(num_elements)
    data, execution_time = insertion.sort(data)
    print('Insertion sort: ' + str(execution_time) + 'ms')

    data = generate_random_array(num_elements)
    data, execution_time = merge.sort(data)
    print('Merge sort: ' + str(execution_time) + 'ms')

if __name__ == "__main__":
    main()
