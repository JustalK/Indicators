import tkinter
import consts
import menu
import windowShortcut
import windowSetting

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
        menu.Menu(left, 'Global', windowSetting.WindowSetting(self.right))
        menu.Menu(left, 'Shortcut', windowShortcut.WindowShortcut())
        window.mainloop()
