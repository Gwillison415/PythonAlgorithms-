def caesar_cipher(offset, string):
    word = string.split(" ")
    idx_of_words = 0
    while idx_of_words < len(word):
        each_word = word[idx_of_words]

        each_letter_idx = 0
        while each_letter_idx < len(each_word):
            old_letter = ord(each_word[each_letter_idx]) - ord("a")
            new_letter = chr((old_letter + offset) % 26)
            print(new_letter)
            each_word[each_letter_idx] = chr(ord("a") - ord(new_letter))
            each_letter_idx +=1
    idx_of_words +=1
    return " ".join(each_word)


print (caesar_cipher(3, 'abc'))
print (caesar_cipher(3, 'abc xyz'))
