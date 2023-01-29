def pingpong_loop(n):
    i = 1
    res = 1
    positive = 1
    while i < n:
        if i % 8 == 0 or num_eights(i) > 0:
            positive = 1 - positive
        if positive:
            res += 1
        else:
            res -= 1
        i+=1
    return res

def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos < 10:
        if pos == 8:
            return 1
        else:
            return 0
    else:
        if pos % 10 == 8:
            return 1 + num_eights(pos//10)
        else:
            return num_eights(pos//10)

def ping(n):
    if n == 1:
        return 1
    else:
        return ping(n-1) + pong(n-1)

def pong(n):
    if n < 8:
        return 1
    else:
        if n % 8 == 0 or num_eights(n) > 0:
            return -pong(n-1)
        else:
            return pong(n-1)
    

print(ping(30))
#print(pingpong_loop(28))

