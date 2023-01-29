
def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True    
    """
    "*** YOUR CODE HERE ***"
    if change >= 25:
        return count_coins(change-25)+foo(change,10)
    elif change >= 10:
        return count_coins(change-10)+foo(change,5)
    elif change >=5:
        return count_coins(change-5)+foo(change,1)
    else:
        return 1

def foo(change,coin):
    if coin == 1:
        return 1
    elif coin == None:
        return 0
    elif change == 0:
        return 1
    elif change < coin:
        return count_coins(change)
    else:
        return foo(change - coin, coin)+foo(change, next_smaller_coin(coin))


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

print(count_coins(200))