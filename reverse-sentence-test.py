
def reverse_string(s):
    return s[::-1]


def reverse_words(originalString):
    temp_string = ""
    words = originalString.split(" ")
    for word in words:
        temp_string += reverse_string(word)+" "
    return temp_string




print(reverse_words("Hello my name is stephen."))