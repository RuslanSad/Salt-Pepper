def multiply_numbers(inputs=None):
    BOOK='1234567890'
    var=None
    for i in str(inputs):
        if i in BOOK and var==None:
            var=int(i)
        elif i in BOOK:
            var*=int(i)
    return var
