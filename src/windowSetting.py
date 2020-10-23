import tkinter
import consts

class WindowSetting():
    def __init__(self, right):
        self.right = right

    def show(self):
        title_panel = tkinter.LabelFrame(self.right, bg=consts.BACKGROUND_COLOR, bd=0, relief='flat')
        title_panel.grid(row=0, column=1, pady=(40, 0), sticky='NEWS')
        title_panel.grid_columnconfigure(0, minsize=125)
        title_panel.grid_columnconfigure(1, weight=1)
        titleblock = tkinter.Label(title_panel, text="Shortcut 1", justify='left', height=2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, font='Helvetica 11 bold')
        titleblock.grid(row=0, column=0, sticky='W')
        titleblock.grid_columnconfigure(0)
        add = tkinter.Button(title_panel, text="+", bd=0, highlightthickness=0, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, anchor='w', activebackground=consts.MENU_COLOR, activeforeground=consts.MENU_TEXT_COLOR, justify='left', relief='flat')
        add.grid(row=0, column=1, sticky='E')
        add.grid_columnconfigure(0)
        wrapper_internal = self.wrap_section();
        self.text_section(wrapper_internal, 1, 'Label')
        self.text_section(wrapper_internal, 2, 'Commands')

    def wrap_section(self):
        wrapper_external = tkinter.LabelFrame(self.right, bg='black', bd=1, relief='flat')
        wrapper_external.grid(row=1, column=1, sticky='WE')
        wrapper_external.grid_columnconfigure(0, weight=1)
        wrapper_internal = tkinter.LabelFrame(wrapper_external, bg=consts.MENU_COLOR, fg='red', bd=5, relief='flat')
        wrapper_internal.grid(row=1, column=0, sticky='NEWS')
        wrapper_internal.grid_columnconfigure(0, minsize=125)
        wrapper_internal.grid_columnconfigure(1, weight=1)
        return wrapper_internal;

    def text_section(self, frame, row, label):
        element_label = tkinter.Label(frame, text=label, height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        element_label.grid(row=row, column=0, sticky='WE')
        element_entry = tkinter.Entry(frame, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, bd=5, highlightbackground=consts.BACKGROUND_COLOR, relief='flat')
        element_entry.grid(row=row, column=1, sticky='WE')

    def clean_panel(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.right.pack_forget()
