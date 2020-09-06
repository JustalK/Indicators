import tkinter
import consts

class Settings():

    right = None

    def __init__(self):
        self.parent = self
        window = tkinter.Tk()
        window.title(consts.NAME_SETTING)
        width  = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        x = int(width/2 - width/3)
        y = int(height/2 - height/4)
        window.geometry("{}x{}+{}+{}".format(int(width*2/3), int(height/2), x, y))
        window.grid_columnconfigure(0, minsize=consts.MENU_SIZE)
        window.grid_columnconfigure(1, minsize=1)
        window.grid_columnconfigure(2, weight=1)
        window.grid_rowconfigure(0, weight=1)
        left = tkinter.Frame(master=window, width=consts.MENU_SIZE, bg=consts.MENU_COLOR)
        left.grid(row=0, column=0, sticky='NSEW')
        left.grid_columnconfigure(0, weight=1)
        border = tkinter.Frame(master=window, bg=consts.BORDER_COLOR)
        border.grid(row=0, column=1, sticky='NSEW')
        self.right = tkinter.Frame(master=window, bg=consts.BACKGROUND_COLOR)
        self.right.grid(row=0, column=2,sticky='NSEW')
        self.right.grid_columnconfigure(0, minsize=10)
        self.right.grid_columnconfigure(1, minsize=20)
        self.right.grid_columnconfigure(2, minsize=10)
        self.right.grid_columnconfigure(3, weight=1)
        self.menubar(left)
        window.mainloop()

    def globalSettings(self):
        shortcutLabel = tkinter.Label(self.right, text="Label")
        shortcutLabel.grid(row=0, column=0, sticky='WE')
        shortcutEntry = tkinter.Entry(self.right)
        shortcutEntry.grid(row=0, column=1, sticky='WE')
        commandLabel = tkinter.Label(self.right, text="Commands")
        commandLabel.grid(row=0, column=2, sticky='WE')
        commandEntry = tkinter.Entry(self.right)
        commandEntry.grid(row=0, column=3, sticky='WE')
        print('GLOBAL')

    def shortcutSettings(self):
        print('SHORTCUT')

    def menubar(self, frame):
        button1 = self.buttonMenubar(frame, 'Global', self.parent.globalSettings)
        button1.grid(row=0, column=0, sticky='WE')
        button2 = self.buttonMenubar(frame, 'Shortcut', self.parent.shortcutSettings)
        button2.grid(row=1, column=0, sticky='WE')

    def buttonMenubar(self, frame, text, command):
        return tkinter.Button(frame, text=text, bd=0, height=2, highlightthickness=0, fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR,bg=consts.MENU_COLOR, justify='left', anchor='w', relief='flat', command = command)
