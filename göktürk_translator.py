import tkinter as tk
from tkinter import ttk, Canvas, NW
from PIL import Image, ImageTk
import pygame


# Initialize pygame mixer
pygame.mixer.init()

# the music file
def play_music():
    pygame.mixer.music.load(r"Paste here Altai.mp3 full file path as BG music")
    pygame.mixer.music.play(loops=-1)  # -1 makes the music loop indefinitely


# the Göktürk alphabet mapping
gokturk_alphabet = {
    'A': '𐰀', 'B': '𐰉', 'C': '𐰲', 'D': '𐰑', 'E': '𐰃', 'F': '𐱂', 'G': '𐰍', 'H': '𐰴',
    'I': '𐰃', 'J': '𐰶', 'K': '𐰴', 'L': '𐰢', 'M': '𐰢', 'N': '𐰤', 'O': '𐰆', 'P': '𐰯',
    'Q': '𐰴', 'R': '𐰼', 'S': '𐰽', 'T': '𐱅', 'U': '𐰆', 'ü': '𐰇','V': '𐰉', 'W': '𐰉', 'X': '𐰲',
    'Y': '𐰖', 'Z': '𐰔',
    'a': '𐰀', 'b': '𐰉', 'c': '𐰲', 'd': '𐰑', 'e': '𐰃', 'f': '𐱂', 'g': '𐰍', 'h': '𐰴',
    'i': '𐰃', 'j': '𐰶', 'k': '𐰚', 'l': '𐰢', 'm': '𐰢', 'n': '𐰤', 'o': '𐰆', 'p': '𐰯',
    'q': '𐰴', 'r': '𐰼', 's': '𐰽', 't': '𐱅', 'u': '𐰆', 'v': '𐰉', 'w': '𐰉', 'x': '𐰲',
    'y': '𐰖', 'z': '𐰔',
    ' ': ' '  # Preserve spaces
}

def translate_to_gokturk(text):
    translated = ''.join([gokturk_alphabet.get(char, char) for char in text])
    return translated[::-1]  # Reverse the string to match right-to-left order

def on_translate(event=None):
    user_input = input_entry.get()
    translated_text = translate_to_gokturk(user_input)
    output_label.config(text=translated_text)

def validate_input(new_value):
    # Check if the new value contains any digits
    if any(char.isdigit() for char in new_value) or len(new_value) >50:
        return False
    return True

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_label.cget("text"))

def open_telegram():
    import webbrowser
    webbrowser.open('https://www.linkedin.com/in/nursaid-kamilli/')

# the main window
root = tk.Tk()
root.title("Göktürk Alphabet Translator")
root.geometry('1200x600')
root.resizable(False, False)
root.configure(bg='#ADD8E6')  # bg = light blue

# the widgets
input_label = ttk.Label(root, text="Hərfi Tərcümə etmək istədiyiniz ifadəni yazın:", font=("Helvetica", 15), background='#ADD8E6')
input_label.pack(pady=5)

validate_cmd = root.register(validate_input)
input_entry = ttk.Entry(root, width=50, validate="key", validatecommand=(validate_cmd, '%P'))
input_entry.pack(pady=5)


translate_button = ttk.Button(root, text="Tərcümə et", command=on_translate, cursor='hand2')
translate_button.pack(pady=5)

output_label = ttk.Label(root, text="", font=("Helvetica", 25), background='#ADD8E6', cursor='hand2')
output_label.pack(pady=20)

copy_button = ttk.Button(root, text="Mətni kopyala", command=copy_output, cursor='hand2')
copy_button.pack(pady=5)

# Label in the bottom-left corner
info_label = ttk.Label(root, text="SaidSecurity.com\nLinkedIn: @nursaid-kamilli", anchor='w', cursor='hand2', foreground='#0000ff', background='#ffffff' )
info_label.pack(side='top', anchor='nw', padx=10, pady=10)

info_label.bind("<Button-1>", lambda e: open_telegram())

class AutoResizingImage:
    def __init__(self, master, path):
        self.master = master
        self.path = path
        self.img = None
        self.tk_img = None
        self.image_id = None
        self.update_image()

    def update_image(self):
        width, height = self.master.winfo_width(), self.master.winfo_height()
        self.img = Image.open(self.path)
        self.img = self.img.resize((width, height), Image.LANCZOS)
        if self.tk_img is not None:
            # Delete the previous image from the canvas
            self.master.delete(self.image_id)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.image_id = self.master.create_image(0, 0, image=self.tk_img, anchor=NW)


canv = Canvas(root, width=1200, height=600, bg='white')
canv.pack(fill='both', expand=True)

img = AutoResizingImage(canv, r"Paste GokTurkBGjpg.jpg full file path as BG image")

def resize(event):
    img.update_image()

root.bind('<Configure>', resize)
root.bind('<Return>', on_translate)

# Plays music when app starts
play_music()
# Run the loop
root.mainloop()
