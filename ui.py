import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from morse_code import sentence_to_morse_code, play_sound
import pyperclip


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse Code App")
        self.window.config(padx=30, pady=30)
        self.app_logo = PhotoImage(file="img/morse-code.png")
        self.app_logo = self.app_logo.subsample(3, 3)
        self.canvas = Canvas(width=600, height=200)
        self.canvas.create_image(120, 120, image=self.app_logo)
        self.entry_text_label = Label(text="           Enter Text :")

        self.entry_text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD,
                                                         width=30, height=10,
                                                         font=('Times New Roman', 15))
        self.output_label = Label(text="Morse Code Output:")
        self.output_text_area = scrolledtext.ScrolledText(self.window,
                                                          wrap=tk.WORD,
                                                          width=30,
                                                          height=10,
                                                          font=('Times New Roman', 15, 'bold'))
        self.output_text_area.config(state='disable')

        self.button_area = Frame(self.window, bd=2, relief=RIDGE)
        self.copy_btn = Button(self.button_area, text="Copy", command=self.copy_morse_code)
        self.play_btn = Button(self.button_area, text="Play", command=self.play_btn_func)

        self.canvas.grid(column=1, row=1)
        self.entry_text_label.grid(column=1, row=0)
        self.entry_text_area.grid(column=1, row=1, sticky="E")
        self.output_label.grid(column=2, row=0, sticky="W")
        self.output_text_area.grid(column=2, row=1, sticky="E")
        self.morse_code = []
        self.button_area.grid(column=2, row=3, sticky="E")
        self.copy_btn.pack(side="right")
        self.play_btn.pack(side="left")
        self.morse_code = []

        self.window.mainloop()

    def play_btn_func(self):
        self.output_text_area.config(state="normal")
        self.output_text_area.delete(1.0, END)
        self.output_text_area.config(state="disable")
        self.morse_code = []

        message = self.entry_text_area.get("1.0", "end-1c").replace('\n', '')
        message = message.upper().split(' ')
        self.morse_code = sentence_to_morse_code(message)

        for item in self.morse_code:
            self.output_text_area.config(state="normal")
            self.output_text_area.insert(END, item)
            self.output_text_area.config(state="disable")
            cp = ''.join([str(elem) for elem in self.morse_code])
            pyperclip.copy(cp)
        play_sound(self.morse_code)

    def sound(self):
        play_sound(self.morse_code)

    def copy_morse_code(self):
        cp= ''.join([str(elem) for elem in self.morse_code])
        pyperclip.copy(cp)

