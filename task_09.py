def vip_dicts(dicts1, dicts2):
    val1 = sum(dicts1.values())
    val2 = sum(dicts2.values())
    if val2 >= val1:
        return True
    else:
        return False


def connect_dicts(dict1, dict2):
    vip_dict = {}
    dict_nonvip = {}
    dict3 = {}
    if vip_dicts(dict1, dict2):
        vip_dict = dict2
        dict_nonvip = dict1
    else:
        vip_dict = dict1
        dict_nonvip = dict2
    for k, v in vip_dict.items():
        if not v < 10:
            dict3[k] = v
    for k, v in dict_nonvip.items():
        if v >= 10 and k not in dict3.keys():
            dict3[k] = v

    return dict(sorted(dict3.items(), key=lambda x: x[1]))
