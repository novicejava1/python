#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class ArenaGame(GridLayout):
    pass

class ArenaApp(App):
    def build(self):
        return ArenaGame()

if __name__ == '__main__':
    ArenaApp().run()
