def resistor_label(colors):
    
    color_list = ['black', 
                  'brown', 
                  'red', 
                  'orange', 
                  'yellow', 
                  'green', 
                  'blue', 
                  'violet', 
                  'grey', 
                  'white']
    
    tolerance_list = {
    "silver": "10%",
    "gold": "5%",
    "red": "2%",
    "brown": "1%",
    "green": "0.5%",
    "blue": "0.25%",
    "violet": "0.1%",
    "grey": "0.05%",
}
    
    if len(colors) == 1:
        return str(color_list.index(colors[0])) + ' ohms'
    
    #Build the number
    if len(colors) == 4:
        result = str(color_list.index(colors[0])) + str(color_list.index(colors[1]))
    
    if len(colors) == 5:
        result = str(color_list.index(colors[0])) + str(color_list.index(colors[1])) + str(color_list.index(colors[2]))

    #Convert number to integer
    result = int(result)

    #Add zeroes
    result = result * (10 ** color_list.index(colors[-2]))

    #Find ending
    ending = ' '
    if result >= 1000000:
        result = result / 1000000
        ending += 'mega'

    elif result >= 1000:
        result = result / 1000
        ending += 'kilo'

    #Round number
    round(result, 2)

    if (str(result)).endswith(".0"):
        result = int(result)

    result = str(result) + ending + 'ohms'
    
    result += tolerance_list[colors[-1]]

    return result