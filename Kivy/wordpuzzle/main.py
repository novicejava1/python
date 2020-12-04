#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    pass

class PuzzleApp(App):
    def build(self):
        game = MyGridLayout()
        return game

if __name__ == "__main__":
    PuzzleApp().run()

