# -*- coding: utf-8 -*- 

###########################################################################
##
## File     : Model.py
## Project  : MVCStudy
## Date     : 2018-11-14
##
## Blog     : https://www.wangsansan.com/
## Author   : WangSansan
## 
###########################################################################

from .Test import test

###########################################################################
## Class Model
###########################################################################
class Model:
    def __init__(self):
        self.Data = None
        self.Callbacks = {}
        pass

    def __del__(self):
        pass

    def add_callback(self, func):
        self.Callbacks[func] = func

    def del_callback(self, func):
        del self.Callbacks[func]

    def do_callback(self):
        for func in self.Callbacks:
            func(self.Data)

    def clear(self):
        self.Data = None

    def start(self, url):
        self.Data = test.test()
        self.do_callback()

