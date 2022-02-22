import time
from vlc import MediaPlayer

# Morse code list
morse_code = {
"0": "-----",
"1": ".----",
"2": "..---",
"3": "...--",
"4": "....-",
"5": ".....",
"6": "-....",
"7": "--...",
"8": "---..",
"9": "----.",
"a": ".-",
"b": "-...",
"c": "-.-.",
"d": "-..",
"e": ".",
"f": "..-.",
"g": "--.",
"h": "....",
"i": "..",
"j": ".---",
"k": "-.-",
"l": ".-..",
"m": "--",
"n": "-.",
"o": "---",
"p": ".--.",
"q": "--.-",
"r": ".-.",
"s": "...",
"t": "-",
"u": "..-",
"v": "...-",
"w": ".--",
"x": "-..-",
"y": "-.--",
"z": "--..",
".": ".-.-.-",
",": "--..--",
"?": "..--..",
"!": "-.-.--",
"-": "-....-",
"/": "-..-.",
"@": ".--.-.",
"(": "-.--.",
")": "-.--.-"
}

# Variables that we want to use later
# Output that will be shown on console
morse_output = ""
# Count valid input
valid_letters = 0
# Count invalid inputs
invalid_letters = 0

# Get input from user
text_input = input("Enter text to convert: \n").lower()

# Convert test to morse code
for letter in text_input:
    # Is the 'letter' valid to convert to morse?
    if letter not in morse_code:
        morse_output += " "
        invalid_letters += 1
    else:
        morse_output += morse_code[letter]
        valid_letters += 1
    # After every letter add a space for better readability
    morse_output += " "

# Print morse code result to the console
print(f"Your text has {valid_letters+invalid_letters} letters which has {valid_letters} translatable letter(s) and "
      f"{invalid_letters} invalid letters\n"
      f"Translation: {morse_output}\n"
      f"Let's hear your text")

# Why not play some sound
for letter in morse_output:
    # To allow user to follow the sound, print each code for each sound
    print(letter, end=" ")
    # Need to set sound for every loop. Otherwise, sound will end and not start again
    sound = MediaPlayer("beep.mp3")
    # Play sound
    if letter == ".":
        sound.play()
        sound.set_time(500)
        time.sleep(0.5)
    elif letter == "-":
        sound.play()
        sound.set_time(200)
        time.sleep(0.5)
    else:
        time.sleep(1)

