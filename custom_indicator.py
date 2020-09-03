#!/usr/bin/env python3
import subprocess
import os
import signal
import gi
import consts
import settings
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
from os.path import expanduser
home = expanduser("~")

currpath = os.path.dirname(os.path.realpath(__file__))
iconpath = currpath+"/cog.png"
commandpath = home

class Indicator():
    def __init__(self):
        self.app = 'update_setting'
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath,
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label(consts.NAME_MENU, self.app)

    def get_menu(self, commands):
        for key in commands.keys():
            menuitem = Gtk.MenuItem.new_with_label(key)
            menuitem.connect("activate", self.run_script, consts.COMMANDS[key])
            self.menu.append(menuitem)
        self.menu.append(Gtk.SeparatorMenuItem())
        menuitem = Gtk.MenuItem.new_with_label("Settings")
        menuitem.connect("activate", self.settings)
        self.menu.append(menuitem)

    def create_menu(self):
        self.menu = Gtk.Menu()
        self.get_menu(consts.COMMANDS)
        self.menu.show_all()
        return self.menu

    def run_script(self, widget, script):
        subprocess.Popen(["/bin/bash", "-c", script])

    def settings(self, widget):
        settings.Window()

    def stop(self, source):
        Gtk.main_quit()

Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
