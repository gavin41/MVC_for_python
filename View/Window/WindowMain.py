# -*- coding: utf-8 -*- 

###########################################################################
##
## File     : WindowMain.py
## Project  : MVCStudy
## Date     : 2018-11-14
##
## Blog     : https://www.wangsansan.com/
## Author   : WangSansan
## 
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class WindowMain
###########################################################################
class WindowMain(wx.Frame):
    def __init__(self, parent, 
                    id      = wx.ID_ANY, 
                    title   = u"Main Window", 
                    pos     = wx.DefaultPosition, 
                    size    = wx.Size(1024, 576), 
                    style   = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL):

        wx.Frame.__init__(  self , 
                            parent=parent, id=id, title=title , pos=pos, size=size, style=style )

        #################################
        # 创建控件
        #################################
        ## 布局控件
        self.S_Palace = wx.GridBagSizer(1, 1)

        ## 按钮 & 编辑框
        self.B_Attack = wx.Button(self, -1, "Start Task")
        self.T_Target = wx.TextCtrl(self, -1, "This is input.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.T_Output = wx.TextCtrl(self, -1, "This is output.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)

        #################################
        # 布局设置
        #################################
        ## 添加控件到布局位置
        #B_Attack.SetPosition(wx.Point(100 , 200 ))
        #T_Output.SetPosition(wx.Point(100 , 200 ))
        self.S_Palace.Add(self.T_Output, (1, 0), (2, 2), wx.EXPAND|wx.ALL, 5)
        self.S_Palace.Add(self.B_Attack, (0, 1), (1, 1), wx.ALL, 5)
        self.S_Palace.Add(self.T_Target, (0, 0), wx.DefaultSpan, wx.EXPAND|wx.ALL, 5)

        ## 需要自适应的控件所属布局位置
        self.S_Palace.AddGrowableRow(1)
        self.S_Palace.AddGrowableCol(0)

        ## 尺寸
        #T_Target.SetSize(wx.Size( -1, 26    ))
        #T_Output.SetSize(wx.Size( 1008,466   ))

        #################################
        # 窗口
        #################################
        self.SetSizerAndFit(self.S_Palace)       # 初始化布局窗口
        self.SetSize(size)                  # 设置窗口大小
        self.Centre()                       # 窗口居中显示

    def __del__(self):
        pass

