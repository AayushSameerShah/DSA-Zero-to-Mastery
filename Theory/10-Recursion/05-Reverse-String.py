def reverseString(string):
    if len(string) < 1:
        return
    
    last_char = string[-1]
    print(last_char, end="")
    reverseString(string[:-1])



reverseString("AAYUSH")