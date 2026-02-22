import art
print(art.logo)

def caesar(original_text, shift_amount, action):
    if action == "decode":
        shift_amount *= -1
    result_text = ""
    for letter in original_text:
        ascii_value = ord(letter)
        if letter.isalpha():
            if letter.isupper(): #65 - 90
                ascii_value = (ascii_value - 65 + shift_amount) % 26 + 65
            elif letter.islower(): #97 - 122
                ascii_value = (ascii_value - 97 + shift_amount) % 26 + 97
            result_text += chr(ascii_value)
        else:
            result_text += letter
    return result_text


keep_going = True
while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        direction = input("Please type either 'encode' or 'decode'.\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    print(f"Here is the {direction}d result: {caesar(text, shift, direction)}")
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    while restart not in ["yes", "no"]:
        restart = input("Please type either 'yes' or 'no'.\n").lower()
    if restart == "no":
        keep_going = False