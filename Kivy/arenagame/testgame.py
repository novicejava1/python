#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class RectBlock(Widget):
    
    def pushRight(self):
        print("Pushing the Button Right")
        self.x = self.x + 5

    def pushLeft(self):
        print("Pushing the Button Left")
        self.x = self.x - 5

    def pushTop(self):
        print("Pushing the Button Top")
        self.y = self.y + 5

    def pushBottom(self):
        print("Pushing the Button Bottom")
        self.y = self.y - 5


class TestGame(Widget):

    block = ObjectProperty(None)

    def moveRight(self):
        print("Moving the Button Right")

    def moveLeft(self):
        print("Moving the Button Left")

    def moveTop(self):
        print("Moving the Button Top")

    def moveBottom(self):
        print("Moving the Button Bottom")


class TestApp(App):
    def build(self):
        gameInst = TestGame()
        return gameInst

if __name__ == '__main__':
    TestApp().run()
