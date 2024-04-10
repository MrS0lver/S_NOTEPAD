import tkinter as tk
from tkinter import filedialog,font
import speech_recognition as sr
import pyttsx3 as pt
import webbrowser as wb

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("SM Notepad")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.text_area.bind("<MouseWheel>", self.change_font_size)
        
        # self.text_area = tk.Text(self.root)
        # self.text_area.pack(fill=tk.BOTH, expand=True)

        #Files
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        #Edit
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        #Font :)
        self.Font_menu = tk.Menu(self.edit_menu, tearoff=0)
        self.Font_menu.add_command(label="Consolas", command=self.consolas)
        self.Font_menu.add_command(label="Candara", command=self.candara)
        self.Font_menu.add_command(label="Castellar", command=self.castellar)
        self.Font_menu.add_command(label="Chiller", command=self.chiller)
        self.Font_menu.add_command(label="Harrington", command=self.harrington)
        
        
        self.menu_bar.add_cascade(label="Fonts", menu=self.Font_menu)
        #Task (Speak & Read)
        self.voice_menu = tk.Menu(self.edit_menu, tearoff=0)
        self.voice_menu.add_command(label="Speak & Write", command=self.voice_writting)
        self.voice_menu.add_separator()
        self.voice_menu.add_command(label="Read", command=self.read)
        self.menu_bar.add_cascade(label="Task", menu=self.voice_menu)
        #Contact us 
        self.contact_menu = tk.Menu(self.edit_menu, tearoff=0)
        self.contact_menu.add_command(label="Twitter", command=self.Instagram)
        self.contact_menu.add_command(label="GitHub", command=self.github)
        self.menu_bar.add_cascade(label="Contact", menu=self.contact_menu)

        self.root.config(menu=self.menu_bar)
    def harrington(self):
        self.text_area.config(font=("Harrington"))
    def chiller(self):
        self.text_area.config(font=("Chiller"))
    def castellar(self):
        self.text_area.config(font=("castellar"))
    def candara(self):
        self.text_area.config(font=("Candara"))
    def consolas(self):
        self.text_area.config(font=("consolas"))
    def change_font_size(self, event):
        current_font = font.Font(font=self.text_area["font"])
        size = current_font.actual()["size"]
        if event.delta > 0:
            size += 2
        else:
            size -= 2
        if size < 8:
            size = 8
        self.text_area.configure(font=("Arial", size))
    def Instagram(self):
        wb.open_new("https://twitter.com/Mrs0lver")
    def github(self):
        wb.open_new("https://github.com/MrS0lver")
    def read(self):
        eng = pt.init()
        eng.getProperty('rate')
        eng.setProperty('rate',145)
        eng.say(self.text_area.get('1.0','end-1c'))
        eng.runAndWait()

    def voice_writting(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(text)
            self.text_area.insert(tk.END, text + " ")
        except sr.UnknownValueError:
            self.text_area.insert(tk.END, "Could not understand audio")
        except sr.RequestError:
            self.text_area.insert(tk.END, "Could not request results from Google Speech Recognition")

    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def cut_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_area.get("sel.first", "sel.last"))
        self.text_area.delete("sel.first", "sel.last")

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_area.get("sel.first", "sel.last"))

    def paste_text(self):
        self.text_area.insert(tk.INSERT, self.root.clipboard_get())

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()