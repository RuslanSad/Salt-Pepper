def coincidence(list=[], range=0):
    arr = []
    if list == 0 or range == 0:
        print(arr)
    else:
        for i in list:
            if isinstance(i, (int, float)) and i >= range[0] and i <= range[-1]:
                arr.append(i)
        return arr
