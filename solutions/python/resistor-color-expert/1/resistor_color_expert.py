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
    
    tolerance_list = ['silver', 
                  'gold', 
                  'red', 
                  'brown', 
                  'green', 
                  'blue', 
                  'violet', 
                  'grey']
    
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
    
    if colors[-1] == 'grey':
        result += " ±0.05%"
    if colors[-1] == 'violet':
        result += " ±0.1%"
    if colors[-1] == 'blue':
        result += " ±0.25%"
    if colors[-1] == 'green':
        result += " ±0.5%"
    if colors[-1] == 'brown':
        result += " ±1%"
    if colors[-1] == 'red':
        result += " ±2%"
    if colors[-1] == 'gold':
        result += " ±5%"
    if colors[-1] == 'silver':
        result += " ±10%"
        

    return result