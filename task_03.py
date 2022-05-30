def max_odd(array):
    max_val = None
    for i in array:
        if isinstance(i,(int,float)):
            i=int(i)
            if max_val == None and i % 2 != 0:
                max_val = i
            elif i % 2 != 0 and i > max_val:
                max_val = i
    return max_val
