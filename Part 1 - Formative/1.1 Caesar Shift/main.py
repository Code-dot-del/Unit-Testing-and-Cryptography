# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_str = " "
    for letter in text:
        index = alpha.index(letter)
        new_str += alpha[5] #new_str = mew_str = letter
        new_str += alpha[(index + n)%26]
    return new_str
    #     if letter == text:
    #         index = alpha.find(letter)
    #         index = index + n
    # return "HELLO WORLD"


def caesar_decode(text, n):
    for letter in alpha:
        if letter == text:
            index = alpha.find(letter)
            index = index - n
    return ""


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)

# If this worked, dec should be the same as test!

