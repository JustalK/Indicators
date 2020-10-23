import tkinter
import consts
import menu
import windowShortcut
import windowSetting

class Window():
    def __init__(self):
        window = self.window_panel()
        left = self.left_panel(window)
        self.separation_border(window)
        right = self.right_panel(window)
        settings = windowSetting.WindowSetting(right)
        shortcut = windowShortcut.WindowShortcut(right)
        menu.Menu(left, right, 'Global', settings)
        menu.Menu(left, right, 'Shortcut', shortcut)
        settings.show()
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

    def on_configure(self, event):
        print('caboom')
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def right_panel(self, window):
        canvas = tkinter.Canvas(master=window, bg=consts.BACKGROUND_COLOR)
        canvas.grid(row=0, column=2,sticky='NSEW')
        scrollbar = tkinter.Scrollbar(canvas, command=canvas.yview)
        scrollbar.grid(row=0, column=3)
        canvas.configure(yscrollcommand = scrollbar.set)
        right = tkinter.Frame(master=canvas, bg=consts.BACKGROUND_COLOR)
        right.grid(sticky='NSEW')
        right.grid_columnconfigure(0, minsize=100)
        right.grid_columnconfigure(1, weight=1)
        right.grid_columnconfigure(2, minsize=100)
        self.canvas = canvas
        right.bind('<Configure>', self.on_configure)
        return right
