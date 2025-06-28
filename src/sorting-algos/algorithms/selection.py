from ..utils.timer import time_execution

@time_execution
def sort(input):
    length = len(input)
    for i in range(length - 1):
        lowest_index = i
        for j in range(i + 1, length):
            if input[j] < input[lowest_index]:
                lowest_index = j
                input.insert(i, input.pop(lowest_index))

    return input
