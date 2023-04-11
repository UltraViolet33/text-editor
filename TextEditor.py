class TextEditor:

    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def undo(self):
        if len(self.undo_stack) > 0:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
