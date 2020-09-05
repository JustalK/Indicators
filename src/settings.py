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
        left.grid_columnconfigure(0, weight=1)
        right = tkinter.Frame(master=window, bg=consts.BACKGROUND_COLOR)
        right.grid(row=0, column=1,sticky='NSEW')
        right.grid_rowconfigure(0, weight=1)
        right.grid_columnconfigure(0, weight=1)
        self.menubar(left)
        window.mainloop()

    def menubar(self, frame):
        button1 = tkinter.Button(frame, text='Hello')
        button1.grid(row=0, column=0, sticky='WE')
        button2 = tkinter.Button(frame, text='Hello 2')
        button2.grid(row=1, column=0, sticky='WE')
        button3 = tkinter.Button(frame, text='Hello 3')
        button3.grid(row=2, column=0, sticky='WE')
        button4 = tkinter.Button(frame, text='Hello 4')
        button4.grid(row=3, column=0, sticky='WE')
