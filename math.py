def fact(n, accumulator=1):
    """
    TAIL RECURSION
    n - object to be factored
    accumulator - the accumulator of the previous state
    """
    if n == 0:
        return accumulator
    else:
        return fact(n - 1, accumulator * n)

def permutate(p, n):
    """
    p - object to be permutated
    n - the length of fields (by elimination)
    """
    return int(fact(p) / fact(p - n))

def combinate(l, p):
    """
    l - length of object
    p - number of possibilities
    """
    return p ** l
