import tkinter
import consts
import menu
import windowShortcut
import windowSetting

class Window():

    right = None

    def __init__(self):
        window = self.window_panel()
        left = self.left_panel(window)
        self.separation_border(window)
        right = self.right_panel(window)
        settings = windowSetting.WindowSetting(right)
        shortcut = windowShortcut.WindowShortcut(right)
        menu.Menu(left, right, 'Global', settings)
        menu.Menu(left, right, 'Shortcut', shortcut)
        window.mainloop()

    def window_panel(self):
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
        return window

    def left_panel(self, window):
        left = tkinter.Frame(master=window, width=consts.MENU_SIZE, bg=consts.MENU_COLOR)
        left.grid(row=0, column=0, sticky='NSEW')
        left.grid_columnconfigure(0, weight=1)
        return left

    def separation_border(self, window):
        border = tkinter.Frame(master=window, bg=consts.BORDER_COLOR)
        border.grid(row=0, column=1, sticky='NSEW')

    def right_panel(self, window):
        right = tkinter.Frame(master=window, bg=consts.BACKGROUND_COLOR)
        right.grid(row=0, column=2,sticky='NSEW')
        right.grid_columnconfigure(0, minsize=100)
        right.grid_columnconfigure(1, weight=1)
        right.grid_columnconfigure(2, minsize=100)
        return right
