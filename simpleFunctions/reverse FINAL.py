# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.
def reverse(text):
    text_list = list(text)
    reverse_list = []
    while len(text_list) > 0:
        reverse_list.append(text_list[-1])
        del text_list[-1]
    return "".join(reverse_list)

print reverse("abc")
