import tkinter 
import customtkinter 


class TextEditorGui:
    def __init__(self):

        self.root = customtkinter.CTk()

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    textEditor = TextEditorGui()
    textEditor.run()
