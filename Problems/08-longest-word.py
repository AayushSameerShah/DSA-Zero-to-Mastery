# Given the sentence, return the longest word.

def get_longest_word(sentence):
    count_till_now = 0
    best_count = 0
    for idx, character in enumerate(sentence):
        if character != " ":
            count_till_now += 1
        else:
            best_count = max(best_count, count_till_now)
            count_till_now = 0
    
    best_count = max(best_count, count_till_now)
    return best_count

print(get_longest_word("aayush sameer shah is the man of the centuries"))