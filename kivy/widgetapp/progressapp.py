#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class MyProgressBar(ProgressBar):
    pass

class ProgressBarApp(App):
    def build(self):
        return MyProgressBar()

if __name__ == '__main__':
    pba = ProgressBarApp()
    pba.run()
