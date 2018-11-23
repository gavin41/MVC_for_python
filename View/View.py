# -*- coding: utf-8 -*- 

###########################################################################
##
## File     : View.py
## Project  : MVCStudy
## Date     : 2018-11-14
##
## Blog     : https://www.wangsansan.com/
## Author   : WangSansan
## 
###########################################################################

import wx
from .Window.Main import WindowMain

class View(wx.Frame):

    DefaultSize = (1024, 576)
    DefaultTitle = u"Main winodw"

    RunMode_GUI     = 0
    RunMode_Console = 1

    STATUS_ERROR    = -1
    STATUS_FAILED   =  0
    STATUS_SUCCESS  =  1

    def __init__(self, title=DefaultTitle, size=DefaultSize, isinit=0, mode=RunMode_Console):
        self.size = size
        self.title = title
        self.main = None        # 主窗口
        self.wxApp = None       # wxPython
        self.target = None
        self.runMode = mode     # 运行模式, 默认使用控制台运行
        self.wInitFlag = 0      # GUI窗口是否已经初始化 0:未初始化 1:已经初始化
        self.cbk_start = None   # 开始工作的回调函数

        if(isinit == 1):
            self.window_init()

    def __del__(self):
        pass

    #################################
    # GUI's API
    #################################
    def window_init(self, title=DefaultTitle, size=DefaultSize, target=None, cbk_start=None):

        if(self.wInitFlag == 1):
            return
        self.wxApp = wx.App()
        self.main = WindowMain(None, title=title, size=size)
        self.runMode = View.RunMode_GUI     # 此赋值语句需要放到 Public API 前面, 因为Public API大部分会先判断运行模式

        self.set_target(target)
        self.set_evt_start_work(cbk_start)
        self.main.B_Attack.Bind(wx.EVT_BUTTON, self.evt_start_work)

        self.wInitFlag = View.STATUS_SUCCESS

    def window_run(self, title=DefaultTitle, size=DefaultSize):
        self.window_init(title, size)
        self.window_start()

    def window_start(self):
        self.runMode = View.RunMode_GUI
        self.main.Show()
        self.wxApp.MainLoop()

    def window_show(self, content):
        self.main.T_Output.SetValue(content)

    def window_get_target(self):
        return self.main.T_Target.GetValue()

    #################################
    # Console's API
    #################################
    def console_init(self, target=None, cbk_start=None):
        self.set_target(target)
        self.set_evt_start_work(cbk_start)

    def console_run(self):
        self.runMode = View.RunMode_Console
        self.evt_start_work()

    def console_show(self, content):
        print(content)

    #################################
    # Public's API
    #################################
    def init(self, mode=RunMode_Console, target=None, cbk_start=None):
        if(mode == View.RunMode_GUI):
            self.window_init(target=target, cbk_start=cbk_start)
        else:
            self.console_init(target=target, cbk_start=cbk_start)

    def run(self):
        if(self.runMode == View.RunMode_GUI):
            self.window_run()
        elif(self.runMode == View.RunMode_Console):
            self.console_run()
        else:
            return

    def show(self, content):
        if(self.runMode == View.RunMode_GUI):
            self.window_show(content)
        else:
            self.console_show(content)

    def set_target(self, target):
        if(target != None):
            self.target = target

        if(self.runMode == View.RunMode_GUI):
            if(self.target != None):
                self.main.T_Target.SetValue(self.target)
            else:
                pass
        else:
            pass
        pass

    def set_evt_start_work(self, cbk):
        self.cbk_start = cbk

    def get_target(self):
        target = None
        if(self.runMode == View.RunMode_GUI):
            target = self.window_get_target()
        else:
            target = self.target

        return target

    #################################
    # Events & Callbacks
    #################################
    def evt_start_work(self, evt=None):
        if(self.cbk_start != None):
            self.cbk_start()

