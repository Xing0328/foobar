# Returns n or n-1
def answer(x):
    count = len(x)
    if sum(x) % count == 0:
        return count 
    else:
        return count - 1
