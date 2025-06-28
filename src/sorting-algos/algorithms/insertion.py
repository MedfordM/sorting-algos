from ..utils.timer import time_execution

@time_execution
def sort(input):
    for i in range(1, len(input)):
        target_index = 1
        current_value = input[i]
        for j in range(i - 1, -1, -1):
            if input[j] > current_value:
               target_index = j
        input.insert(target_index, current_value)

    return input
