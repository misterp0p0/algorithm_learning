# Binary Search

def binary_search(user_list, target):
    first = 0
    last = len(user_list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if user_list[midpoint] == target:
            return midpoint

        elif user_list[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None


values = [n for n in range(0, 11)]
print(binary_search(values, 9))

