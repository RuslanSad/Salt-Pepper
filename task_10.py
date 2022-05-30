def count_words(string):
    BOOK = 'qwertyuiopasdfghjklzxcvbnm '
    st_arr = ''
    dict1 = {}
    for i in string.lower():
        if i in BOOK:
            st_arr += i
    st_arr = st_arr.split(' ')
    for i in st_arr:
        if len(i) >= 1 and i != ' ':
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] += 1
    return dict1


