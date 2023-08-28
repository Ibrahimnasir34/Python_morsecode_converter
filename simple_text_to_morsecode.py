def to_morse_code(text):
    code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    morse_code = ""
    for x in text:
        if x.upper() in code:  # Convert the character to uppercase
            morse_code += code[x.upper()] + ' '
        elif x == ' ':
            morse_code += ' '
    return morse_code


while True:  # Infinite loop
    text = input("Enter text to convert to Morse Code: ")
    morse_result = to_morse_code(text)
    print("Morse Code:", morse_result)

    repeat = input("Enter '1' to convert more text or any other key to exit: ")
    if repeat != '1':
        break  # Exit the loop if user doesn't want to continue