import tkinter
import consts

class WindowSetting():
    def __init__(self, right):
        self.right = right
        self.row = 0

    def show(self):
        self.title_section('New shortcut')
        new_shortcut_section = self.wrap_section();
        self.text_section(new_shortcut_section, 'Label')
        self.text_section(new_shortcut_section, 'Commands')
        self.title_section('All shortcut')
        all_shortcut_section = self.wrap_section();
        self.show_section(all_shortcut_section, 'Label')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')
        self.show_section(all_shortcut_section, 'Commands')

    def title_section(self, title):
        element_title = tkinter.Label(self.right, text=title, justify='left', height=2, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, font='Helvetica 11 bold')
        element_title.grid(row=self.row, column=1, pady=(40, 0), sticky='W')
        element_title.grid_columnconfigure(0)
        self.row+=1

    def wrap_section(self):
        wrapper_external = tkinter.LabelFrame(self.right, bg='black', bd=1, relief='flat')
        wrapper_external.grid(row=self.row, column=1, sticky='WE')
        wrapper_external.grid_columnconfigure(0, weight=1)
        wrapper_internal = tkinter.LabelFrame(wrapper_external, bg=consts.MENU_COLOR, fg='red', bd=5, relief='flat')
        wrapper_internal.grid(row=self.row, column=0, sticky='NEWS')
        wrapper_internal.grid_columnconfigure(0, minsize=125)
        wrapper_internal.grid_columnconfigure(1, weight=1)
        wrapper_internal.row=0
        self.row+=1
        return wrapper_internal

    def text_section(self, frame, label):
        element_label = tkinter.Label(frame, text=label, height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        element_label.grid(row=frame.row, column=0, sticky='WE')
        element_entry = tkinter.Entry(frame, bg=consts.BACKGROUND_COLOR, fg=consts.MENU_TEXT_COLOR, bd=5, highlightbackground=consts.BACKGROUND_COLOR, relief='flat')
        element_entry.grid(row=frame.row, column=1, sticky='WE')
        frame.row+=1

    def show_section(self, frame, label):
        element_label = tkinter.Label(frame, text=label, height=2, bg=consts.MENU_COLOR, justify='left', anchor='w', fg=consts.MENU_TEXT_COLOR, activeforeground=consts.MENU_TEXT_COLOR, activebackground=consts.MENU_TEXT_ACTIVE_COLOR)
        element_label.grid(row=frame.row, column=0, sticky='WE')
        element_edit_button = tkinter.Button(
            frame,
            text='EDIT',
            bd=0,
            height=2,
            highlightthickness=0,
            fg=consts.MENU_TEXT_COLOR,
            activeforeground=consts.MENU_TEXT_COLOR,
            activebackground=consts.MENU_TEXT_ACTIVE_COLOR,
            bg=consts.MENU_COLOR,
            justify='left',
            anchor='w',
            relief='flat')
        element_edit_button.grid(row=frame.row, column=1, sticky='E')
        element_remove_button = tkinter.Button(
            frame,
            text='REMOVE',
            bd=0,
            height=2,
            highlightthickness=0,
            fg=consts.MENU_TEXT_COLOR,
            activeforeground=consts.MENU_TEXT_COLOR,
            activebackground=consts.MENU_TEXT_ACTIVE_COLOR,
            bg=consts.MENU_COLOR,
            justify='left',
            anchor='w',
            relief='flat')
        element_remove_button.grid(row=frame.row, column=2, sticky='E')
        frame.row+=1

    def clean_panel(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.right.pack_forget()
