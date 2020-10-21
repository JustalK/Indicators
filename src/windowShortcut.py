import tkinter
import consts

class WindowShortcut():
    def __init__(self, right):
        self.right = right

    def show(self):
        self.clean_panel()
        titleblock = tkinter.Label(self.right, text="Shortcut 1", justify='left', height=2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, font='Helvetica 11 bold')
        titleblock.grid(row=0, column=1, sticky='W')
        titleblock.grid_columnconfigure(0)

    def clean_panel(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.right.pack_forget()
