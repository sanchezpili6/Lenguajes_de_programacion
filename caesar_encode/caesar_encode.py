alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'x', 'y', 'z']
encoded_message_list = []
encoded_message = ""


def caesar_encode(message, shift_num):
    for i in message:
        index = alphabet.index(i)
        new_index = index + shift_num
        encoded_message_list.append(alphabet[new_index])
    return encoded_message.join(encoded_message_list)


print(caesar_encode('abc', 3))
