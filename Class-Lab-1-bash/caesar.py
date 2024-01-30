def shift_up_character(character, shift):
    char_number = ord(character) # the numerical representation
    new_number = char_number + shift
    new_character = chr(new_number)
    return new_character


def shift_down_character(character, shift):
    char_number = ord(character)  # the numerical representation
    new_number = char_number - shift
    new_character = chr(new_number)
    return new_character


def shift_message_up_and_down(message, shift):
    shifted_up = []
    shifted_down = []
    for c in message:
        shifted_up.append(shift_up_character(c, shift))
        shifted_down.append(shift_down_character(c, shift))
    string_shifted_up = "".join(shifted_up)
    string_shifted_down = "".join(shifted_down)
    print(f"shifted up: {string_shifted_up}")
    print(f"shifted down: {string_shifted_down}")


if __name__ == '__main__':
    input_string = input("Input a string\n")
    shift = int(input("input a shift amount\n"))
    shift_message_up_and_down(input_string, shift)
