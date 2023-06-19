def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    max=0
    if a>max:
        max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max
print(find_max(2,-9,5))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    max=0
    if a>max:
        max=a
    if b>max:
        max=b
    if c>max:
        max=c
    if max==a:
        result=1
    if max==b:
        result=2
    if max==c:
        result=3
    return result
print(find_max_idx(9,5,-8))
    

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2