def value(colors):

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

    result = color_list.index(colors[0]) * 10 + color_list.index(colors[1])

    return result
