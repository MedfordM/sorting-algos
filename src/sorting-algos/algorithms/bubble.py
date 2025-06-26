def sort(input):
    length = len(input)
    for i in range(length):
        did_swap = False
        for j in range(0, length - i - 1):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]
                did_swap = True

            if not did_swap:
                break

