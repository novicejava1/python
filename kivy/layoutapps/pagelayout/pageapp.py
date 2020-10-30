#!/usr/bin/env python

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class MyImage(Image):

    roadimg = ObjectProperty(None)
    fallimg = ObjectProperty(None)
    dropimg = ObjectProperty(None)
    canyonimg = ObjectProperty(None)
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.source == 'road.jpg':
                print("The road image has been selected")
                pop = Popup(title='road image', content=Image(source='road.jpg'),
                    size_hint=(None, None), size=(700, 350))
                pop.open()
                touch.grab(self)
                return True
            elif self.source == 'fall.jpg':
                print("The fall image has been selected")
                pop = Popup(title='fall image', content=Image(source='fall.jpg'),
                    size_hint=(None, None), size=(700, 350))
                pop.open()
                touch.grab(self)
                return True
            elif self.source == 'drop.jpg':
                print("The drop image has been selected")
                pop = Popup(title='drop image', content=Image(source='drop.jpg'),
                    size_hint=(None, None), size=(700, 350))
                pop.open()
                touch.grab(self)
                return True
            elif self.source == 'canyon.jpg':
                print("The canyon image has been selected")
                pop = Popup(title='canyon image', content=Image(source='canyon.jpg'),
                    size_hint=(None, None), size=(700, 350))
                pop.open()
                touch.grab(self)
                return True


        return super(MyImage, self).on_touch_down(touch) 
    
    def on_touch_up(self, touch):
        if touch.grab_current is self:
            print("The image has been released")
            touch.ungrab(self)
            return True
        super(MyImage, self).on_touch_up(touch)


class MyPageLayout(PageLayout):
    pass

class PageApp(App):
    def build(self):
        pl = MyPageLayout()
        #pl.checkMode()
        return pl

if __name__ == '__main__':
    PageApp().run()
