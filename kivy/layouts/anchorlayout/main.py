#!/usr/bin/env python

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class MyAnchorLayout(AnchorLayout):
    pass

class LayoutsApp(App):
    def build(self):
        return MyAnchorLayout()

if __name__ == "__main__":
    LayoutsApp().run()
