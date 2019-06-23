def reverseWords(str):    
    split_str = str.split(' ')[:-1]
    #attention renvoie un array
    join = ' '.join(split_str)
    # convertis un array en string
    return join


assert reverseWords("hello world") == "world hello"

