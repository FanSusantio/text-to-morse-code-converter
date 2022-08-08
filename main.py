from art import logo

print(logo)

char_code_dict = {
    # letters
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    # numbers
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '0': '_____',
    # punctuation
    '.': '._._._',
    ',': '__..__',
    '?': '..__..',
    "'": '.____.',
    '!': '_._.__',
    ' ': '/'
}


# function to convert message into morse code

def encode_to_morse(input_code):
    morse_code = ""
    error_list = []
    for char in input_code:
        try:
            morse_code += char_code_dict[char] + " "
        except KeyError:
            error_list.append(char)

    if len(error_list) == 0:
        print(f"Your message in morse code is:\n {morse_code}")
    else:
        print(f"Error in input. Cannot translate the following characters: {' '.join(error_list)}\n")


def decode_morse(input_code):
    output_message = ""
    error_list = []

    keys_list = list(char_code_dict.keys())
    values_list = list(char_code_dict.values())

    morse_to_decode = input_code.split(" ")

    for signal in morse_to_decode:
        try:
            position = values_list.index(signal)
            letter = keys_list[position]
            output_message += letter
        except ValueError:
            error_list.append(signal)

    if len(error_list) == 0:
        print(f"Your message is:\n {output_message}")
    else:
        print(f"Error in input. Cannot translate the following signal: {' '.join(error_list)}\n")



converter_end = False

while not converter_end:
    convert_direction = int(input("Type '1' to encode    Message ----> Morse Code\n"
                              "Type '2' to decode    Morse Code ----> Message\n"))

    if convert_direction == 1:
        message_input = input("Enter the message to encode into morse code:\n").lower()
        encode_to_morse(message_input)
    elif convert_direction == 2:
        message_input = input("Enter the message to decode:\n").lower()
        decode_morse(message_input)

    else:
        print("Please type in one of the options")

    restart = input("Type 'yes' if you want to convert another message. Otherwise type 'no'.\n")
    if restart == "no":
        converter_end = True
        print("Goodbye! Time to dash, we have to draw the line at some point!")


# https://morsecode.world/international/translator.html

