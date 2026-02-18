def convert(input_grid):

    """
    Docstring for convert
    
    :param input_grid: [str] - lines representing numbers
    Returns what numbers the lines represent
    """
    
    if any(len(line) % 3 != 0 for line in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    num_digits = len(input_grid[0]) // 3
    
    final_result = ""
    for row_start in range(0, len(input_grid), 4):

        row_group = input_grid[row_start:row_start+4]

        numbers = [""] * num_digits

        for i in range(len(row_group)):
            for j in range(0, num_digits * 3, 3):
                numbers[j // 3] += (row_group[i][j:j+3])


        digit_map = {
            "     |  |   ": "1",
            " _  _||_    ": "2",
            " _  _| _|   ": "3",
            "   |_|  |   ": "4",
            " _ |_  _|   ": "5",
            " _ |_ |_|   ": "6",
            " _   |  |   ": "7",
            " _ |_||_|   ": "8",
            " _ |_| _|   ": "9",
            " _ | ||_|   ": "0",
        }

        result = ""
        for num in numbers:
            if num in digit_map:
                result += digit_map[num]
            else:
                result += "?"

        if final_result == "":
            final_result += result
        else:
            final_result += "," + result

    return final_result

