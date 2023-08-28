import pygame

# Initialize Pygame
pygame.init()

# Initialize the sound mixer
pygame.mixer.init()

# Load and play a sound
sound_path = r"C:\Users\Ibrahim\Desktop\pycharm projects\beep-01a.mp3"
sound = pygame.mixer.Sound(sound_path)
sound_path2 = r"C:\Users\Ibrahim\Desktop\pycharm projects\beep-02.mp3"
sound2 = pygame.mixer.Sound(sound_path2)

# Define the Morse code dictionary
translate_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', " ": "/"
}

# Convert a message to Morse code
message = "this is just a message"
message = " ".join(translate_dict[c] for c in message.upper())

def play_morse_code(message):
    for c in message:
        if c == ".":
            sound.play()
            while pygame.mixer.get_busy():
                pygame.time.delay(100)
        elif c == "-":
            sound2.play()
            while pygame.mixer.get_busy():
                pygame.time.delay(100)
        elif c == "/" or c == " ":
            pygame.time.delay(100)
        else:
            print("INVALID CHARACTER DETECTED")

print(message)
play_morse_code(message)

# Quit Pygame
pygame.quit()
