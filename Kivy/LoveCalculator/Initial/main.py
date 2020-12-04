import kivy

from kivy.app import App
from KivyTesting.KivyScreen import lovecal
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

class Manager(ScreenManager):

    result = StringProperty(None)
    percentage = StringProperty(None)

    def results(self):
        print(self.ids.firstname.text)
        print(self.ids.secondname.text)
        first = self.ids.firstname.text
        second = self.ids.secondname.text
        results = lovecal.calculator(first, second)
        self.result = results['result']
        self.percentage = results['percentage']
        print(self.result)
        print(self.percentage)
        #print(str(results['percentage']))
        #print(str(results['result']))

class ScreenApp(App):
    def build(self):
        self.sm = Manager()
        return self.sm

if __name__ == '__main__':
    ScreenApp().run()