# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MainFrame
###########################################################################


class MainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Secret Image Maker", pos=wx.DefaultPosition, size=wx.Size(
            430, 415), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

        img_icon = wx.Bitmap(
            u"assets\Secret Image Maker - Icon.png", wx.BITMAP_TYPE_ANY)
        img_banner = wx.Bitmap(
            u"assets\Secret Image Maker - Banner.png", wx.BITMAP_TYPE_ANY)

        icon = wx.Icon()
        icon.CopyFromBitmap(img_icon)
        self.SetIcon(icon)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        Sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.ButtonAbout = wx.StaticBitmap(
            self, wx.ID_ANY, img_banner, wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer1.Add(self.ButtonAbout, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        Sizer2 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Preview :"), wx.VERTICAL)

        Sizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.ButtonChoose = wx.Button(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"Choose Image", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer3.Add(self.ButtonChoose, 0, wx.ALL, 5)

        self.StaticText1 = wx.StaticText(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"Image File Name :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
        self.StaticText1.Wrap(-1)
        Sizer3.Add(self.StaticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Sizer2.Add(Sizer3, 0, wx.EXPAND, 5)

        self.InfoImage = wx.TextCtrl(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT | wx.TE_READONLY)
        self.InfoImage.Enable(False)

        Sizer2.Add(self.InfoImage, 0, wx.BOTTOM |
                   wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        Sizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.ButtonAdd = wx.Button(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"Add Files", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer4.Add(self.ButtonAdd, 0, wx.ALL, 5)

        self.StaticText2 = wx.StaticText(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"Files Name :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
        self.StaticText2.Wrap(-1)
        Sizer4.Add(self.StaticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Sizer2.Add(Sizer4, 0, wx.EXPAND, 5)

        self.InfoFiles = wx.ListCtrl(Sizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(
            -1, 60), wx.LC_HRULES | wx.LC_NO_HEADER | wx.LC_REPORT | wx.LC_VRULES)
        Sizer2.Add(self.InfoFiles, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        Sizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.ButtonDelete = wx.Button(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"Delete Selection", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer5.Add(self.ButtonDelete, 1, wx.EXPAND | wx.BOTTOM | wx.LEFT, 5)

        self.ButtonClear = wx.Button(Sizer2.GetStaticBox(
        ), wx.ID_ANY, u"Clear Files", wx.DefaultPosition, wx.DefaultSize, 0)
        Sizer5.Add(self.ButtonClear, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 5)

        Sizer2.Add(Sizer5, 0, wx.ALIGN_TOP | wx.EXPAND, 5)

        Sizer1.Add(Sizer2, 0, wx.EXPAND | wx.ALL, 5)

        Sizer6 = wx.BoxSizer(wx.VERTICAL)

        self.ButtonCreate = wx.Button(
            self, wx.ID_ANY, u"Create Secret Image", wx.DefaultPosition, wx.Size(-1, 40), 0)
        Sizer6.Add(self.ButtonCreate, 1, wx.ALL | wx.EXPAND, 5)

        self.StaticText3 = wx.StaticText(
            self, wx.ID_ANY, u"Status : Waiting", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
        self.StaticText3.Wrap(-1)
        Sizer6.Add(self.StaticText3, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.Gauge1 = wx.Gauge(
            self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.Gauge1.SetValue(0)
        Sizer6.Add(self.Gauge1, 1, wx.EXPAND | wx.ALL, 5)

        Sizer1.Add(Sizer6, 1, wx.EXPAND, 5)

        self.SetSizer(Sizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.InfoFiles.InsertColumn(
            0, 'File Name', width=285)
        self.InfoFiles.InsertColumn(
            1, 'File Size', width=80)

        hint = [
            "  How to : 1) Choose image",
            "                  2) Add files / drag files here",
            "                  3) Create secret image"
        ]
        for text in hint:
            index = self.InfoFiles.InsertItem(
                self.InfoFiles.GetItemCount(), text)

        # Connect Events
        self.ButtonAbout.Bind(wx.EVT_LEFT_DOWN, self.ShowAbout)
        self.ButtonChoose.Bind(wx.EVT_BUTTON, self.ChooseImage)
        self.ButtonAdd.Bind(wx.EVT_BUTTON, self.AddFiles)
        self.ButtonDelete.Bind(wx.EVT_BUTTON, self.DeleteSelection)
        self.ButtonClear.Bind(wx.EVT_BUTTON, self.ClearFiles)
        self.ButtonCreate.Bind(wx.EVT_BUTTON, self.CreateImage)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ShowAbout(self, event):
        event.Skip()

    def ChooseImage(self, event):
        event.Skip()

    def AddFiles(self, event):
        event.Skip()

    def DeleteSelection(self, event):
        event.Skip()

    def ClearFiles(self, event):
        event.Skip()

    def CreateImage(self, event):
        event.Skip()
