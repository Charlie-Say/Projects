#! /usr/bin/env python3
# # coding=utf-8
'''
The program will open the graph charts functions from chartfuncs.py and
create a graph for the corresponding cryptocurrency. It will be initiated
with a button widget from the file buttons.kv in the GUI.

Charlie Say
CS 161 10:00AM

___PSEUDO__

create a class with buttons
make buttons graph charts in html
'''


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('modules', 'monitor', '')
import chartfuncs



class Controller(GridLayout):
    '''
    uses buttons.kv widget functions for GUI.
    set buttons to open graphs from chartfuncs.py
    '''

    def __init__(self):
        super(Controller, self).__init__()

    def bitcoin_click(self):
        chartfuncs.bitcoinchart()
        
    def ethereum_click(self):
        chartfuncs.ethereumchart()
        
    def litecoin_click(self):
        chartfuncs.litecoin()


class ButtonsApp(App):
    '''
    button widget
    '''

    def build(self):
        return Controller()


myApp = ButtonsApp()
myApp.run()