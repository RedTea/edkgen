#!/usr/bin/env python

# author:kernel@verycd.com
# created at 02/01/2007

from ed2k import *

from wx import *
import threading
import os.path

class Working(threading.Thread):
    def __init__(self,dlg):
        threading.Thread.__init__(self)

        self.dlg = dlg

        self.f = PartFile()
        self.f.Attach(dlg.filepath)

    def run(self):
        s = self.f.Go()
        v = True
        while(v):
            v = s.next()
            if(v):
                self.dlg.process.SetValue(int(v*100))
                print str(v * 100)+'% Finished'

        if self.f.IsFinished():
            pass

        self.dlg.start.Enable()
        self.dlg.cancel.Disable()

        ed2k = "ed2k://|file|"+self.f.GetNAME()+"|"+self.f.GetSIZE()+"|"+self.f.GetED2K()+"|h="+self.f.GetAICH()+"|/"
        self.dlg.result.SetValue(ed2k)

    def cancel(self):
        self.f.cancel = True

class ED2KDialog(Dialog):
    def __init__(self, parent, id, title):
        Dialog.__init__(self, parent, id, title)
        self.OnInit()
        self.filepath = None

    def OnInit(self):
        self.start = Button(self, 101, 'Start', (10,50))
        self.start.Disable()
        EVT_BUTTON(self, 101, self.OnStartClick)

        self.cancel = Button(self, 102, 'Cancel', (90,50))
        self.cancel.Disable()
        EVT_BUTTON(self,102, self.OnCancelClick)

        self.open = Button(self, 100, 'Open', (170,50))
        self.open.Enable()
        EVT_BUTTON(self, 100, self.OnOpenClick)

        self.process = Gauge(self,-1,100,(10,20),(240,20))
        self.process.SetValue(0)

        self.result = TextCtrl(self, -1, '', (10,100), (240,50))
        self.result.SetEditable(False)
        self.result.SelectAll()

    def OnOpenClick(self,event):
        filedlg = FileDialog(self,message='Select File', style=wx.FD_OPEN)
        filedlg.ShowModal()
        self.filepath = filedlg.GetDirectory() + u'/' + filedlg.GetFilename()
        if(os.path.isfile(self.filepath)):
            self.start.Enable()
            self.result.SetValue('')
        else:
            self.filepath = ''
            self.start.Disable()
            self.cancel.Disable()

    def OnStartClick(self,event):
        self.start.Disable()
        self.cancel.Enable()

        self.workthread = Working(self)
        self.workthread.start()

    def OnCancelClick(self,event):
        if self.workthread:
            self.workthread.cancel()

        self.start.Enable()
        self.cancel.Disable()

class ED2KApp(App):
    def __init__(self):
        App.__init__(self, redirect=False)

    def OnInit(self):
        self.dlg = ED2KDialog(None, -1, "ED2K Link Creator")
        self.dlg.ShowModal()

        return True

app = ED2KApp()
