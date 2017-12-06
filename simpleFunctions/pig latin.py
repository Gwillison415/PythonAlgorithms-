# # Move the first letter of each word to the end of it, then add 'ay' to the end of the word.
# def pig_it(text):
#     new_text = ""
#     text = text.split(" ")
#     for i in text:
#         new_letter = i[0]
#         new_text += str(i[1::]) + str(new_letter) +"ay "
#     return (new_text[:len(new_text) -1:])
# print(pig_it("pig latin is cool"))
# print(pig_it('This is my string'))


# # Move the first letter of each word to the end of it, then add 'ay' to the end of the word.
# def pig_it(text):
#     new_text = ""
#     text = text.split(" ")
#     for i in text:
#         if len(i) > 1:
#             new_letter = i[0]
#             new_text += str(i[1::]) + str(new_letter) +"ay "
#         else: new_text += i
#     return (new_text[:len(new_text):])
# print(pig_it("pig latin is cool"))
# print(pig_it('This is my string !'))

def pig_it(text):
    new_text = ""
    text_segment = text.split(" ")
    for i in text_segment:
        if len(i) > 1:
            new_letter = i[0]
            new_text += str(i[1::]) + str(new_letter) +"ay "
        else: new_text += text[len(text)-1] + " "
    return (new_text[:(len(new_text) -1):] )

print(pig_it("! emporatay ! oresmay !"))
print(pig_it('This is my string !'))
