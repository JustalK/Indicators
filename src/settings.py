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
        self.right.grid_columnconfigure(0, minsize=100)
        self.right.grid_columnconfigure(1, weight=1)
        self.right.grid_columnconfigure(2, minsize=100)
        self.menubar(left)
        window.mainloop()

    def globalSettings(self):
        labelframe = tkinter.LabelFrame(self.right, bg='black', bd=1, relief='flat')
        labelframe.grid(row=0, column=1, sticky='WE')
        labelframe.grid_columnconfigure(0, weight=1)
        labelframe2 = tkinter.LabelFrame(labelframe, bg=consts.MENU_COLOR, fg='red', bd=5, relief='flat')
        labelframe2.grid(row=0, column=0, sticky='NEWS')
        labelframe2.grid_columnconfigure(0, minsize=125)
        labelframe2.grid_columnconfigure(1, weight=1)
        shortcutLabel = tkinter.Label(labelframe2, text="Label", height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        shortcutLabel.grid(row=0, column=0, sticky='WE')
        shortcutEntry = tkinter.Entry(labelframe2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, bd=5, highlightbackground=consts.BACKGROUND_COLOR, relief='flat')
        shortcutEntry.grid(row=0, column=1, sticky='WE')
        commandLabel = tkinter.Label(labelframe2, text="Commands", height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        commandLabel.grid(row=1, column=0, sticky='WE')
        commandEntry = tkinter.Entry(labelframe2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, bd=5, highlightbackground=consts.BACKGROUND_COLOR, relief='flat')
        commandEntry.grid(row=1, column=1, sticky='WE')

    def shortcutSettings(self):
        print('SHORTCUT')

    def menubar(self, frame):
        button1 = self.buttonMenubar(frame, 'Global', self.parent.globalSettings)
        button1.grid(row=0, column=0, sticky='WE')
        button2 = self.buttonMenubar(frame, 'Shortcut', self.parent.shortcutSettings)
        button2.grid(row=1, column=0, sticky='WE')

    def buttonMenubar(self, frame, text, command):
        return tkinter.Button(frame, text=text, bd=0, height=2, highlightthickness=0, fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR,bg=consts.MENU_COLOR, justify='left', anchor='w', relief='flat', command = command)
