from .utils.random_data import generate_random_array
from .algorithms.bubble import sort

def main():
    data = generate_random_array(10)
    print(data)
    data = sort(data)
    print(data)

if __name__ == "__main__":
    main()
