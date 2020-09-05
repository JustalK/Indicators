import tkinter
import consts

class Settings():
    def __init__(self):
        window = tkinter.Tk()
        window.title(consts.NAME_SETTING)
        width  = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        x = int(width/2 - width/3)
        y = int(height/2 - height/4)
        window.geometry("{}x{}+{}+{}".format(int(width*2/3), int(height/2), x, y))
        window.grid_columnconfigure(0, minsize=consts.MENU_SIZE)
        window.grid_columnconfigure(1, weight=1)
        window.grid_rowconfigure(0, weight=1)
        left = tkinter.Frame(master=window, width=consts.MENU_SIZE, bg=consts.MENU_COLOR)
        left.grid(row=0, column=0, sticky='NSEW')
        #left.pack(fill=tkinter.Y, side=tkinter.LEFT)
        left.grid_rowconfigure(0, weight=1)
        left.grid_columnconfigure(0, weight=1)
        right = tkinter.Frame(master=window, bg=consts.BACKGROUND_COLOR)
        right.grid(row=0, column=1,sticky='NSEW')
        right.grid_rowconfigure(0, weight=1)
        right.grid_columnconfigure(0, weight=1)
        #right.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

        button1 = tkinter.Button(left, text='Hello')
        button1.grid(row=1, column=0, sticky='WE')

        window.mainloop()

    def menubar(self, root):
        menubar = tkinter.Menu(root)
        pageMenu = tkinter.Menu(menubar)
        pageMenu.add_command(label="PageOne")
        menubar.add_cascade(label="PageOne", menu=pageMenu)
        return menubar
