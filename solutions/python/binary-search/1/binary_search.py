def find(search_list, value):
    
    low = 0
    high = len(search_list) - 1

    while low <= high:
        middle = (low + high) // 2

        if search_list[middle] == value:
            return middle
        elif value > search_list[middle]:
            low = middle + 1
        elif value < search_list[middle]:
            high = middle - 1

    raise ValueError("value not in array")

