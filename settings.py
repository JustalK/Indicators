import tkinter
import consts

class Window():
    def __init__(self):
        window = tkinter.Tk()
        window.title(consts.NAME_SETTING)
        width  = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        x = int(width/2 - width/3)
        y = int(height/2 - height/4)
        window.geometry("{}x{}+{}+{}".format(int(width*2/3), int(height/2), x, y))
        left = tkinter.Frame(master=window, width=consts.MENU_SIZE, bg=consts.MENU_COLOR)
        left.pack(fill=tkinter.Y, side=tkinter.LEFT)
        right = tkinter.Frame(master=window, bg=consts.BACKGROUND_COLOR)
        right.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
        window.mainloop()
