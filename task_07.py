def combine_anagrams(words_array):
    arr_anagrams = []
    for i in range(len(words_array)):
        arr = []
        if len(words_array) == 0:
            break
        for j in range(len(words_array)):
            if arr == []:
                arr.append(words_array[j])
            elif len(words_array[j]) == len(arr[0]):
                v = 0
                for k in words_array[j]:
                    if k.lower() in arr[0].lower():
                        v += 1
                if v == len(words_array[j]):
                    arr.append(words_array[j])
        arr_anagrams.append(arr)
        for i in arr:
            if i in words_array:
                words_array.remove(i)
    print(arr_anagrams)


combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"])