import tkinter 
import customtkinter 

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("System")

class TextEditorGui(customtkinter.CTk):
    def __init__(self):

        super().__init__()

        # self.root = customtkinter.CTk()
        self.title("Text Editor")
        self.minsize(400, 300)
        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.pack()



if __name__ == "__main__":
    textEditor = TextEditorGui()
    textEditor.mainloop()
