import tkinter
import consts

class WindowSetting():
    def __init__(self, right):
        self.right = right

    def show(self):
        titleblock = tkinter.Label(self.right, text="Shortcut 1", justify='left', height=2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, font='Helvetica 11 bold')
        titleblock.grid(row=0, column=1, sticky='W')
        titleblock.grid_columnconfigure(0)
        labelframe = tkinter.LabelFrame(self.right, bg='black', bd=1, relief='flat')
        labelframe.grid(row=1, column=1, sticky='WE')
        labelframe.grid_columnconfigure(0, weight=1)
        labelframe2 = tkinter.LabelFrame(labelframe, bg=consts.MENU_COLOR, fg='red', bd=5, relief='flat')
        labelframe2.grid(row=1, column=0, sticky='NEWS')
        labelframe2.grid_columnconfigure(0, minsize=125)
        labelframe2.grid_columnconfigure(1, weight=1)
        shortcutLabel = tkinter.Label(labelframe2, text="Label", height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        shortcutLabel.grid(row=1, column=0, sticky='WE')
        shortcutEntry = tkinter.Entry(labelframe2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, bd=5, highlightbackground=consts.BACKGROUND_COLOR, relief='flat')
        shortcutEntry.grid(row=1, column=1, sticky='WE')
        commandLabel = tkinter.Label(labelframe2, text="Commands", height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        commandLabel.grid(row=2, column=0, sticky='WE')
        commandEntry = tkinter.Entry(labelframe2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, bd=5, highlightbackground=consts.BACKGROUND_COLOR, relief='flat')
        commandEntry.grid(row=2, column=1, sticky='WE')

        def clean_panel(self):
            for widget in self.right.winfo_children():
                widget.destroy()
            self.right.pack_forget()
