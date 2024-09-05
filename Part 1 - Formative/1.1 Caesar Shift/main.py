# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_word = " "
    for let in text:
        index = alpha.index(let) + n % 27
        new_let = alpha[index]
        new_word += new_let
    return new_word


def caesar_decode(text, n):
    new_word = " "
    for let in text:
        index = alpha.index(let) - n % 27
        new_let = alpha[index]
        new_word += new_let
    return new_word


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)

# If this worked, dec should be the same as test!

