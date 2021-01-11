from morse_code_table import CODE
from playsound import playsound
import time


def sentence_to_morse_code(word_list: list):
    morse_code_list = []
    for word in word_list:
        morse_code_list.append(word_to_morse_code(word))

    return morse_code_list


def word_to_morse_code(word: str) -> str:
    morse_code = ""
    for char in word:
        if char == '\n' or char == '\t' or char == " ":
            continue
        morse_code = morse_code + CODE[char] + "   "
    return morse_code + "|  "


def play_sound(morse_code: list):
    print(morse_code)
    for code in morse_code:
        print(code)
        for char in code:
            if char == '-':
                playsound('sound/morse_line.mp3')
            elif char == '.':
                playsound('sound/morse_dot.mp3')
            elif char == '|':
                continue
            time.sleep(0.05)
        time.sleep(1)


def character_morse_code(char):
    if char == '\n' or char != ' ':
        return
    morse_code = CODE[char] + "   "
    return morse_code
