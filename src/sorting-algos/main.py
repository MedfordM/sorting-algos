from .utils.random_data import generate_random_array
from .algorithms import bubble

def main():
    data = generate_random_array(10)
    print(data)
    bubble.sort(data)
    print(data)

if __name__ == "__main__":
    main()
