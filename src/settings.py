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
        window.grid_columnconfigure(1, minsize=1)
        window.grid_columnconfigure(2, weight=1)
        window.grid_rowconfigure(0, weight=1)
        left = tkinter.Frame(master=window, width=consts.MENU_SIZE, bg=consts.MENU_COLOR)
        left.grid(row=0, column=0, sticky='NSEW')
        left.grid_columnconfigure(0, weight=1)
        border = tkinter.Frame(master=window, bg=consts.BORDER_COLOR)
        border.grid(row=0, column=1, sticky='NSEW')
        right = tkinter.Frame(master=window, bg=consts.BACKGROUND_COLOR)
        right.grid(row=0, column=2,sticky='NSEW')
        right.grid_rowconfigure(0, weight=1)
        right.grid_columnconfigure(0, weight=1)
        self.menubar(left)
        window.mainloop()

    def menubar(self, frame):
        button1 = self.buttonMenubar(frame, 'Button 1')
        button1.grid(row=0, column=0, sticky='WE')
        button2 = self.buttonMenubar(frame, 'Button 2')
        button2.grid(row=1, column=0, sticky='WE')
        button3 = self.buttonMenubar(frame, 'Button 3')
        button3.grid(row=2, column=0, sticky='WE')
        button4 = self.buttonMenubar(frame, 'Button 4')
        button4.grid(row=3, column=0, sticky='WE')

    def buttonMenubar(self, frame, text):
        return tkinter.Button(frame, text=text, bd=0, height=2, highlightthickness=0, fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR,bg=consts.MENU_COLOR, justify='left', anchor='w', relief='flat')
