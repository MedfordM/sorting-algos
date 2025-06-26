from ..utils.timer import time_execution

@time_execution
def sort(input):
    length = len(input)
    for i in range(length):
        did_swap = False
        for j in range(0, length - i - 1):
            left = input[j]
            right = input[j + 1]
            if left > right:
                input[j], input[j + 1] = right, left
                did_swap = True

        if not did_swap:
            break
    
    return input
