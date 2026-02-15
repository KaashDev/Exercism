def label(colors):
    
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
    
    result =  int(str(color_list.index(colors[0])) + str(color_list.index(colors[1])))
    result = result * (10 ** color_list.index(colors[2]))

    ending = ""

    if result >= 1000000000:
        ending = 'giga'
        result = result//1000000000
        
    elif result >= 1000000:
        ending = 'mega'
        result = result//1000000

    elif result >= 1000:
        ending = 'kilo'
        result = result//1000

    result = str(result) + " " + ending + "ohms"
    return result