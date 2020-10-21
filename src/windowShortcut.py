import tkinter
import consts

class WindowShortcut():
    def __init__(self, panel):
        self.frame = panel

    def show(self):
        titleblock = tkinter.Label(self.frame, text="Shortcut 1", justify='left', height=2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, font='Helvetica 11 bold')
        titleblock.grid(row=0, column=1, sticky='W')
        titleblock.grid_columnconfigure(0)
