def transform(legacy_data):
    
    data = {}

    for key, value in legacy_data.items():
        for item in value:
            data[item.lower()] = key

    return data