#!/usr/bin/env python3
import indicator
import signal
from gi.repository import Gtk

class Init():
    def __init__(self):
        indicator.Indicator()
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        Gtk.main()
