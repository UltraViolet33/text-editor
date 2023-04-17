import tkinter as tk
import customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("System")


class TextEditorGui(customtkinter.CTk):
    def __init__(self):

        super().__init__()

        self.text = ""
        self.title("Text Editor")
        self.minsize(800, 600)
        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.pack(expand=1, fill="both")
        self.textbox.bind("<KeyRelease>", self.update_text)

        self.load_button = customtkinter.CTkButton(
            master=self, text="Load", command=self.load)
        self.load_button.pack(side=tk.LEFT)

        self.save_button = customtkinter.CTkButton(
            master=self, text="Save", command=self.save)
        self.save_button.pack(side=tk.RIGHT)

    def save(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt")
        with open(filename, "w") as f:
            f.write(self.text)

    def load(self):
        filename = tk.filedialog.askopenfilename(defaultextension=".txt")
        with open(filename, "r") as f:
            self.text = f.read()
        self.update_textbox()


    def update_textbox(self):
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, self.text)

    def update_text(self, event):
        self.text = self.textbox.get(1.0, 'end-1c')
        print(self.text)


if __name__ == "__main__":
    textEditor = TextEditorGui()
    textEditor.mainloop()
