def find_fewest_coins(coins, target):
    """
    Docstring for find_fewest_coins
    
    :param coins: [int] - different coin values
    :param target: int - Number made up using the least amount of values in int

    Returns the least amount of coins required to make up the target.

    This solution makes use of dynamic programming. 
    Essentially, we calculate the coins required for every single value from 1 to target.
    
    Starting from 1, if we find a coin less than the current value,
    AND we can make up this value using this coin and coins from array(value - coin),
    candidate = coins from array(value - coin) and coin

    Then, we check if there were no coins for the value
    OR len(candidate) < len(current coins present) for that value,
    we replace the coins for that value with candidate.

    (This ensures that we use the least number of coins required for each value,
    as we already know the least number of coins required for array(remainder of value - coin), 
    and then we add that coin to those coins to make up this value.)

    We repeat this for every value until target.
    Then we return the coins required for target.
    """
    if target < 0:
        raise ValueError("target can't be negative")
    
    if target == 0:
        return []
    
    dp = [None] * (target+1)
    dp[0] = []

    for amount in range(1, target+1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] is not None:
                candidate = dp[amount-coin] + [coin]

                if dp[amount] is None or len(candidate) < len(dp[amount]):
                    dp[amount] = candidate

    if dp[target] == None:
        raise ValueError("can't make target with given coins")
    
    return sorted(dp[target])
    