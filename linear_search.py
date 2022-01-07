# An example function demonstrating linear search

def linear_search(input_list, target):
    for i in range(0, len(input_list)):
        if input_list[i] == target:
            return i
    return None


def verify(results):
    if results is not None:
        print(f"Target found at index: {results}")
    else:
        print(f"Target not found.")


num_list = [n for n in range(1, 11)]
result = linear_search(num_list, 6)
verify(result)
