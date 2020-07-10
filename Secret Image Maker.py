import os
import wx
import wx.adv
import assets.gui_sim as gui
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

    def ShowAbout(self, event):
        # about app
        info = wx.adv.AboutDialogInfo()
        info.SetName('Secret Image Maker')
        info.SetVersion('1.0')
        info.SetDescription("Hide your files in image!")
        info.SetCopyright('(C) 2020')
        info.SetWebSite('https://github.com/MRizaF')
        info.AddDeveloper('Mohammad Riza Farhandhy')
        wx.adv.AboutBox(info)

    def ChooseImage(self, event):
        # get image file
        with wx.FileDialog(self, "Choose image file", "", wildcard="Image file|*.png;*.jpg;*.jpeg;*.bmp", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            # check if image already has file
            path = fileDialog.GetPath()
            # print list of files in image to "ImageCheck.txt"
            os.system('7za l "' + path + '" > "assets\ImageCheck.txt"')
            f = open('assets\ImageCheck.txt', 'r')
            check = f.read()
            f.close()
            os.remove('assets\ImageCheck.txt')
            if "Errors:" not in check:
                wx.MessageBox("Please choose another image", "This image already contains file",
                              wx.OK | wx.CENTRE, self)
                return
            # save image path and display image name
            self.pathimage = path
            self.InfoImage.SetValue(self.pathimage.split("\\")[-1])

    def AddFiles(self, event):
        # get files
        with wx.FileDialog(self, "Choose files to be added", "", wildcard="Any files|*.*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            # save files path and display files name
            self.pathfiles.extend(fileDialog.GetPaths())
            self.set_files(self.pathfiles)

    def DeleteSelection(self, event):
        # delete selected files
        a = self.InfoFiles.GetSelectedItemCount()
        if a != 0:
            if wx.MessageBox("Delete selection?", "Confirmation", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return
            for i in range(a):
                b = self.InfoFiles.GetFirstSelected()
                self.pathfiles.pop(b)
                self.InfoFiles.DeleteItem(b)

    def ClearFiles(self, event):
        # clear all files
        if len(self.pathfiles) != 0:
            if wx.MessageBox("Clear files?", "Confirmation", wx.ICON_QUESTION | wx.YES_NO | wx.CENTRE, self) == wx.NO:
                return
        self.pathfiles = []
        self.InfoFiles.DeleteAllItems()

    def CreateImage(self, event):
        # check image already choosen
        if self.pathimage == "":
            wx.MessageBox("Please choose image to hide files",
                          "No image choosen", wx.OK | wx.CENTRE, self)
            return
        # check files already added
        if len(self.pathfiles) == 0:
            wx.MessageBox("Please add at least one file to hide in the image",
                          "No files added", wx.OK | wx.CENTRE, self)
            return
        # confirmation to create secret image
        if wx.MessageBox("Create secret image with all added files?", "Confirmation", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
            return

        # get new path file
        imageext = os.path.splitext(self.pathimage)[-1]
        with wx.FileDialog(self, "Save secret image as", "", "Secret Image", wildcard=imageext[1:].upper() + " file|*"+imageext, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            secretimage = str(fileDialog.GetPath())

        # get password for zip
        self.set_status("Preparing", 25)
        dlg = wx.TextEntryDialog(
            self, "Input password : (empty it to skip)", "Lock file with password", "", wx.OK | wx.CENTRE)
        dlg.SetWindowStyle(wx.CAPTION)
        dlg.ShowModal()
        pw = dlg.GetValue()
        dlg.Destroy()
        if pw != "":
            pw = " -p"+str(pw)

        # create zip file that contain all added files
        self.set_status("Packing Files", 50)
        f = open("assets\Secret Text.txt", "w")
        f.write("\n".join(self.pathfiles))
        f.close()
        # create "Secret Files.zip" that contain all files in list "Secret Text.txt", with mx9 (ultra compression) and p (password)
        os.system(
            '7za a -tzip "assets\Secret Files.zip" "@assets\Secret Text.txt" -mx9' + pw + ' >nul')
        os.remove("assets\Secret Text.txt")

        # combine image and zip
        self.set_status("Hiding Files", 75)
        # copy in binary mode image + zip
        os.system('cmd /c copy /b "' + str(self.pathimage) +
                  '" + "assets\Secret Files.zip" "' + secretimage + '" >nul')
        os.remove("assets\Secret Files.zip")

        # show finish message
        self.set_status("Finish", 100)
        wx.MessageBox("Success creating secret image",
                      "Secret Image Created", wx.OK, self)

        self.set_status("Waiting", 0)

    # https://tutorialspoint4all.com/python-program-to-convert-bytes-to-kilobytes-megabytes-gigabytes-and-terabytes/
    def convert_bytes(self, bytes_number):
        tags = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        double_bytes = bytes_number
        while (i < len(tags) and bytes_number >= 1024):
            double_bytes = bytes_number / 1024.0
            i = i + 1
            bytes_number = bytes_number / 1024
        return str(round(double_bytes, 2)) + " " + tags[i]

    # update list files
    def set_files(self, pathfiles):
        self.InfoFiles.DeleteAllItems()
        for file in pathfiles:
            file_size = os.stat(file).st_size
            index = self.InfoFiles.InsertItem(
                self.InfoFiles.GetItemCount(), file.split("\\")[-1])
            self.InfoFiles.SetItem(index, 1, self.convert_bytes(file_size))

    # update loading status
    def set_status(self, status, gauge):
        self.StaticText3.SetLabel("Status : " + status)
        self.Gauge1.SetValue(gauge)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
