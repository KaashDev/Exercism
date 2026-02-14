def value(colors):

    color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    result = str(color_list.index(colors[0])) + str(color_list.index(colors[1]))

    return int(result)
