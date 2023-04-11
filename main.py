import tkinter as tk
import customtkinter
from TextEditor import TextEditor

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("System")


class TextEditorGui(customtkinter.CTk):
    def __init__(self):

        super().__init__()

        self.editor = TextEditor()
        self.title("Text Editor")
        self.minsize(400, 300)
        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.pack()

        self.textbox.bind("<Key>", self.update_text)

        self.undo_button = customtkinter.CTkButton(master=self, text="Undo")
        self.undo_button.pack(side=tk.LEFT)

    def undo(self):
        self.editor.undo()
        self.update_textbox()

    def update_textbox(self):
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, self.editor.text)

    def update_text(self, event):
        self.editor.text = self.textbox.get("1.0", tk.END)
        print(self.editor.text)


if __name__ == "__main__":
    textEditor = TextEditorGui()
    textEditor.mainloop()
