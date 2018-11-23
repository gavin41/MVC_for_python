# -*- coding: utf-8 -*- 

###########################################################################
##
## File     : Controller.py
## Project  : MVCStudy
## Date     : 2018-11-14
##
## Blog     : https://www.wangsansan.com/
## Author   : WangSansan
## 
###########################################################################


import wx
import sys
#import argparse

from Model import Model
from View.View import View


###########################################################################
## Class Controller
###########################################################################
class Controller:
    Version = 1.0

    def __init__(self):

        #################################
        # 全局变量
        #################################
        self.Conf = {
                'url'       : None ,
                'urlFile'   : None ,
                'outFile'   : None ,
                'runMode'   : View.RunMode_Console
        }

        #################################
        # 参数检查
        #################################
        self.usage_check()

        #################################
        # Model & View 
        #################################
        ## Model
        self.model = Model.Model()

        ## View
        self.view = View(isinit=0)

        #################################
        # 初始化
        #################################
        print(self.Conf)
        self.view.init(target=self.Conf['url'], mode=self.Conf['runMode']  )

        #################################
        # 连接 Model & View
        #################################
        ## 设置回调函数
        self.model.add_callback(self.finish)
        self.view.set_evt_start_work(self.do_work)

    def __del__(self):
        pass

    def run(self):
        self.view.run()

    def do_work(self, evt=None):
        target = self.Conf['url']
        self.view.show("target: " + str(target))
        self.model.start(target)

    def finish(self, data):
        self.view.show(data)

    def usage_check(self):
        weight = 0              # 参数权重总和
        runWeight = 100         # 可运行条件最低权重值
        unitWeight = 20         # 单位权重值, 用来给其它数值做加数

        #################################
        # Initialization self.Conf
        #################################
        i = 1
        while(i < len(sys.argv)):
            arg = sys.argv[i]

            if(arg == "show"):
                self.Conf['runMode'] = View.RunMode_GUI
                weight = runWeight
            elif(arg == "-h" or arg == "--help"):
                self.usage()
            elif(arg == "-u" or arg == "--url"):
                i = i + 1
                self.Conf['url'] = sys.argv[i]
                weight = weight + runWeight
            elif(arg == "-m" or arg == "--multi"):
                i = i + 1
                self.Conf['urlFile'] = sys.argv[i]
                weight = weight + runWeight
            elif(arg == "-o" or arg == "--output"):
                i = i + 1
                self.Conf['outFile'] = sys.argv[i]
                weight = weight + unitWeight

            i = i + 1

        #################################
        # Check self.Conf
        #################################
        if(weight < runWeight):
            self.usage()

    def usage(self):
        print("Version " + str(Controller.Version) + "  - http://xxx.xxx.xxx ")
        print("Usage: python " + sys.argv[0] + " [show|<Options>]")
        print("")
        print(" show \t\t\t Start GUI")
        print(" ------")
        print(" Options: ")
        print("     -h, --help \t\t\t Help.")
        print("")
        print("     <Target>: \t\t\t\t Choose one of them, The priority of \"-u(--url)\" is greater than \"-m(--multi)\"")
        print("         -u, --url <url> \t\t Target link.")
        print("         -m, --multi <filename> \t Read target list from a file. The 1 row is a target.")
        print("")
        print("     -o, --output <filename> \t\t Output result data to a file.")
        exit()

