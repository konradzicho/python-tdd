

def invert_list(input_list):
    N = len(input_list)
    if N >1:
        buffer = input_list[0]
        input_list[0] = input_list[N - 1]
        input_list[N - 1] = buffer

    return input_list

