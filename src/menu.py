# -*- coding: utf-8 -*-
import tkinter
import consts

class Menu():
    count_menu = 0

    def __init__(self, left, right, text, command):
        button = tkinter.Button(
            left,
            text=text,
            bd=0,
            height=2,
            highlightthickness=0,
            fg=consts.MENU_TEXT_COLOR,
            activeforeground=consts.MENU_TEXT_COLOR,
            activebackground=consts.MENU_TEXT_ACTIVE_COLOR,
            bg=consts.MENU_COLOR,
            justify='left',
            anchor='w',
            relief='flat',
            command = command.show)
        button.grid(row=Menu.count_menu, column=0, sticky='WE')
        Menu.count_menu += 1
