def is_palindrome(st1):
    st1 = str(st1).lower()
    st2 = ''
    BOOK = 'qwertyuiopasdfghjklzxcvbnm'
    for i in st1:
        if i in BOOK:
            st2 += i
    print(st2 == st2[::-1])
