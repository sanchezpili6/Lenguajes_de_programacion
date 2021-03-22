alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']


def shift_char(letter, num):
    letter_index = alphabet.index(letter)
    new_letter = letter_index + num
    return alphabet[new_letter]


print(shift_char('f', 3))
