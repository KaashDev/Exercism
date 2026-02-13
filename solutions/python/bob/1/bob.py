def response(hey_bob):

    """
    Docstring for response
    
    :param hey_bob: what bob is saying
    Returns "Calm down, I know what I'm doing!" if it is a question and uppercase
    Returns "Sure." if question only
    Returns returns "Whoa, chill out!" if uppercase only
    Otherwise returns "Whatever."
    """
    
    hey_bob = hey_bob.strip(" ")

    if hey_bob == "" or "\t" in hey_bob:
        return "Fine. Be that way!"
    
    if hey_bob[-1] == '?' and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == '?':
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    
    return "Whatever."