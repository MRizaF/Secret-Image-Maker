import os
import wx
import wx.adv
import assets.gui as gui
from pathlib import Path


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        self.window.pathfiles.extend(filenames)
        self.window.set_files(self.window.pathfiles)


class MainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.pathimage = ""
        self.pathfiles = []

        self.InfoFiles.SetDropTarget(MyFileDropTarget(self))

        self.InfoFiles.InsertColumn(
            0, 'File Name', width=280)
        self.InfoFiles.InsertColumn(
            1, 'File Size', width=75)

        hint = [
            "  How to : 1) Choose image",
            "                  2) Add files / drag files here",
            "                  3) Create secret image"
        ]
        for text in hint:
            index = self.InfoFiles.InsertItem(
                self.InfoFiles.GetItemCount(), text)

    def ShowAbout(self, event):
        info = wx.adv.AboutDialogInfo()
        info.SetName('Secret Image Maker')
        info.SetVersion('1.0')
        info.SetDescription("Hide your files in image!")
        info.SetCopyright('(C) 2020')
        info.SetWebSite('https://github.com/MRizaF')
        info.AddDeveloper('Mohammad Riza Farhandhy')

        wx.adv.AboutBox(info)

    def ChooseImage(self, event):
        with wx.FileDialog(self, "Choose image file", "", wildcard="Image file|*.png;*.jpg;*.jpeg;*.bmp", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.pathimage = fileDialog.GetPath()
            self.InfoImage.SetValue(self.pathimage.split("\\")[-1])

    def AddFiles(self, event):
        with wx.FileDialog(self, "Choose files to be added", "", wildcard="Any files|*.*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.pathfiles.extend(fileDialog.GetPaths())
            self.set_files(self.pathfiles)

    def DeleteSelection(self, event):
        a = self.InfoFiles.GetSelectedItemCount()

        if a != 0:
            if wx.MessageBox("Delete selection?", "Confirmation", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return

            for i in range(a):
                b = self.InfoFiles.GetFirstSelected()

                self.pathfiles.pop(b)
                self.InfoFiles.DeleteItem(b)

    def ClearFiles(self, event):
        if len(self.pathfiles) != 0:
            if wx.MessageBox("Clear files?", "Confirmation", wx.ICON_QUESTION | wx.YES_NO | wx.CENTRE, self) == wx.NO:
                return

        self.pathfiles = []
        self.InfoFiles.DeleteAllItems()

    def CreateImage(self, event):
        if self.pathimage == "":
            wx.MessageBox("Please choose image to hide files",
                          "No image choosen", wx.OK | wx.CENTRE, self)
            return

        if len(self.pathfiles) == 0:
            wx.MessageBox("Please add at least one file to hide in the image",
                          "No files added", wx.OK | wx.CENTRE, self)
            return

        if wx.MessageBox("Create secret image with all added files?", "Confirmation", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
            return

        imageext = os.path.splitext(self.pathimage)[-1]

        with wx.FileDialog(self, "Save secret image as", "", "Secret Image", wildcard=imageext[1:].upper() + " file|*"+imageext, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            secretimage = str(fileDialog.GetPath())

        self.set_status("Preparing", 25)

        dlg = wx.TextEntryDialog(
            self, "Input password : (empty it to skip)", "Lock file with password", "", wx.OK | wx.CENTRE)
        dlg.SetWindowStyle(wx.CAPTION)
        dlg.ShowModal()
        pw = dlg.GetValue()
        dlg.Destroy()

        if pw != "":
            pw = " -p" + str(pw)

        self.set_status("Packing Files", 50)

        f = open("Secret Text.txt", "w")
        f.write("\n".join(self.pathfiles))
        f.close()
        os.system('7za a -tzip "Secret Files.zip" "@Secret Text.txt" -mx9' + pw)
        os.remove("Secret Text.txt")

        self.set_status("Hiding Files", 75)

        os.system('cmd /c copy /b "' + str(self.pathimage) +
                  '" + "Secret Files.zip" "' + secretimage + '"')
        os.remove("Secret Files.zip")

        self.set_status("Finish", 100)

        wx.MessageBox("Success creating secret image",
                      "Secret Image Created", wx.OK, self)

        self.set_status("Waiting", 0)

    def convert_bytes(self, bytes_number):
        tags = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        double_bytes = bytes_number
        while (i < len(tags) and bytes_number >= 1024):
            double_bytes = bytes_number / 1024.0
            i = i + 1
            bytes_number = bytes_number / 1024
        return str(round(double_bytes, 2)) + " " + tags[i]

    def set_files(self, pathfiles):
        self.InfoFiles.DeleteAllItems()
        for file in pathfiles:
            file_size = os.stat(file).st_size

            index = self.InfoFiles.InsertItem(
                self.InfoFiles.GetItemCount(), file.split("\\")[-1])
            self.InfoFiles.SetItem(index, 1, self.convert_bytes(file_size))

    def set_status(self, status, gauge):
        self.StaticText3.SetLabel("Status : " + status)
        self.Gauge1.SetValue(gauge)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
