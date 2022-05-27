def sort_list(list):
    if len(list) > 1:
        max_val = max(list)
        min_val = min(list)
        for i in range(len(list)):
            if list[i] == min_val:
                list[i] = max_val
            elif list[i] == max_val:
                list[i] = min_val
        list += [min_val]
    elif len(list) == 1:
        list = list * 2
    print(list)
