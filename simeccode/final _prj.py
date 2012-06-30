import wx

from classes import *

class Frame(wx.Frame):
    def OnInit(self):
        
                

        
        # create a list of all elements
        self.position = []        
        self.pos_dict = {}
        self.pos_l = []
        self.last = []        
        self.capclist = []
        self.indrlist = []
        self.element_list = []
        self.volt_dict = {}
        self.res= Resistor()
        self.bulb = Bulb()
        self.batr = Dcbattery()
        self.acbatr = Acbattery()
        self.wire = Wire()
        self.capc = Capacitor()
        self.indr = Inductor()
        self.voltm = Voltmeter()
        self.countac = [0]
        self.countdc = [0]
        self.maxmx = [0]
        self.maxmy = [0]
        self.submitflag = [0]
        self.panel2 = wx.Panel(self, pos = (0,0))
        self.panel2.overlay = wx.Overlay()
        self.panel2.SetBackgroundColour('White')
        
        # Displaying Buttons on panel
        res = wx.Image("resistor.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button1 = wx.BitmapButton(self.panel2, -1, res, pos=(25, 10), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnRes, self.button1)
        self.button1.Bind(wx.EVT_ENTER_WINDOW, self.OnResButton)
        self.button1.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
                          
        res1 = wx.Image("resistor1.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button1a = wx.BitmapButton(self.panel2, -1, res1, pos=(85, 10), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnRes1, self.button1a)
        self.button1a.Bind(wx.EVT_ENTER_WINDOW, self.OnResButton)
        self.button1a.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        
        bulb = wx.Image("bulb.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button2 = wx.BitmapButton(self.panel2, -1, bulb, pos=(25,70), size = (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnBulb, self.button2)
        self.button2.Bind(wx.EVT_ENTER_WINDOW, self.OnBulbButton)
        self.button2.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        batr = wx.Image("battery.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel2, -1, batr, pos=(25,130), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVolt, self.button3)
        self.button3.Bind(wx.EVT_ENTER_WINDOW, self.OnBatteryButton)
        self.button3.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        batr1 = wx.Image("battery1.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button31 = wx.BitmapButton(self.panel2, -1, batr1, pos=(85,130), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVolt1, self.button31)
        self.button31.Bind(wx.EVT_ENTER_WINDOW, self.OnBatteryButton)
        self.button31.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        batr2 = wx.Image("battery2.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button32 = wx.BitmapButton(self.panel2, -1, batr2, pos=(25,190), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVolt2, self.button32)
        self.button32.Bind(wx.EVT_ENTER_WINDOW, self.OnBatteryButton)
        self.button32.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        batr3 = wx.Image("battery3.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button33 = wx.BitmapButton(self.panel2, -1, batr3, pos=(85,190), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVolt3, self.button33)
        self.button33.Bind(wx.EVT_ENTER_WINDOW, self.OnBatteryButton)
        self.button33.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        batrac = wx.Image("battery_ac.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button4 = wx.BitmapButton(self.panel2, -1, batrac, pos=(25,250), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVoltac, self.button4)
        self.button4.Bind(wx.EVT_ENTER_WINDOW, self.OnBatteryacButton)
        self.button4.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        batrac1 = wx.Image("battery_ac1.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button41 = wx.BitmapButton(self.panel2, -1, batrac1, pos=(85,250), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVoltac1, self.button41)
        self.button41.Bind(wx.EVT_ENTER_WINDOW, self.OnBatteryacButton)
        self.button41.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        voltm = wx.Image("voltmeter.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button5 = wx.BitmapButton(self.panel2, -1, voltm, pos=(25,310), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnVoltmeter, self.button5)
        self.button5.Bind(wx.EVT_ENTER_WINDOW, self.OnVoltmeterButton)
        self.button5.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        amm = wx.Image("ammeter.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button6 = wx.BitmapButton(self.panel2, -1, amm, pos=(85,310), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnAmmeter, self.button6)
        self.button6.Bind(wx.EVT_ENTER_WINDOW, self.OnAmmeterButton)
        self.button6.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        capc = wx.Image("capacitor.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button7 = wx.BitmapButton(self.panel2, -1, capc, pos=(25,370), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnCapc, self.button7)
        self.button7.Bind(wx.EVT_ENTER_WINDOW, self.OnCapcButton)
        self.button7.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        indr = wx.Image("inductor.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button8 = wx.BitmapButton(self.panel2, -1, indr, pos=(85,370), size= (50,50))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnIndr, self.button8)
        self.button8.Bind(wx.EVT_ENTER_WINDOW, self.OnIndrButton)
        self.button8.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        self.button9 = wx.Button(self.panel2, label="Connecting Wires", pos=(25,430), size = (100,20))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnWire, self.button9)
        self.button9.Bind(wx.EVT_ENTER_WINDOW, self.OnWireButton)
        self.button9.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        self.button10 = wx.Button(self.panel2, label="Thevenin Equivalent", pos=(25,460), size = (100,20))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnThevenin, self.button10)
        self.button10.Bind(wx.EVT_ENTER_WINDOW, self.OnThevButton)
        self.button10.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        self.button11 = wx.Button(self.panel2, label="Submit", pos=(25,490), size = (100,20))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)
        self.button11.Bind(wx.EVT_ENTER_WINDOW, self.OnSubmitButton)
        self.button11.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        self.button12 = wx.Button(self.panel2, label="Refresh",pos=(25,520), size = (100,20))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnRefresh, self.button12)
        self.button12.Bind(wx.EVT_ENTER_WINDOW, self.OnRefreshButton)
        self.button12.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)

        self.button13 = wx.Button(self.panel2, label = "Remove", pos=(25,550), size = (100,20))
        self.panel2.Bind(wx.EVT_BUTTON, self.OnRemove, self.button13)
        self.button13.Bind(wx.EVT_ENTER_WINDOW, self.OnRemoveButton)
        self.button13.Bind(wx.EVT_LEAVE_WINDOW, self.notonbutton)
        
        self.StatusBar = self.CreateStatusBar()
        self.menubar = wx.MenuBar()
        
        menu2 = wx.Menu()
        self.menubar.Append(menu2,"&Help")
        menu2.Append(wx.NewId(), "About", '')
        self.SetMenuBar(self.menubar)
        
    def OnResButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT RESISTOR')
        event.Skip()

    def OnBulbButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT BULB')
        event.Skip()

    def OnBatteryButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT DC VOLTAGE SOURCE')
        event.Skip()

    def OnBatteryacButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT AC VOLTAGE SOURCE')
        event.Skip()

    def OnVoltmeterButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT VOLTMETER')
        event.Skip()

    def OnAmmeterButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT AMMETER')
        event.Skip()

    def OnThevButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('FIND THEVENIN EQUIVALENT CIRCUIT')
        event.Skip()
        
    def OnWireButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT WIRE')
        event.Skip()

    def OnCapcButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT CAPACITOR')
        event.Skip()

    def OnIndrButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SELECT INDUCTOR')
        event.Skip()

    def OnSubmitButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('SUBMIT THE CIRCUIT')
        event.Skip()

    def OnRefreshButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('REFRESH THE SCREEN')
        event.Skip()

    def OnRemoveButton(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.StatusBar.SetStatusText('REMOVE AN ELEMENT FROM CIRCUIT')
        event.Skip()

    def notonbutton(self,event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.StatusBar.SetStatusText(' ')
        event.Skip()
        
    
    
        
    
        

    
        
    def OnRes(self, event):
        '''  To input the value of Resistance '''
        
        dlg = wx.TextEntryDialog(None, "Value of resistance (in Ohm) used : ",'Resistance', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.res.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Res)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)
        else:
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
            
            

    def On_Click_Res(self,event=None):
         
         odc = wx.DCOverlay(self.panel2.overlay, dc) 
         odc.Clear() 
         del odc
         self.panel2.overlay.Reset() 
         if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Res)
            return
         else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Res)
                return
            self.res.initial = (self.maxmx[0],event.GetY())
            self.res.getfinalpos()
            for x in self.element_list:
                if (x.initial == self.res.initial and x.final ==  self.res.final) or (x.initial == self.res.final and x.final ==  self.res.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.res = Resistor()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        return
            self.pos_l.append(self.res.initial)
            self.pos_l.append(self.res.final)
            self.StatusBar.SetStatusText(str([self.res.initial, self.res.final]))
            self.last.append(self.res.initial)
            dc.SetPen(wx.Pen("RED", 1))
            dc.DrawLine(event.GetX(),event.GetY(),event.GetX(),event.GetY())
            dc.DrawBitmap(bmp1, self.res.initial[0]+1, self.res.initial[1]-7, True)
            
            if self.res.initial in self.pos_dict:
                self.pos_dict[self.res.initial].append(self.res)
            else:
                self.pos_dict[self.res.initial] = [self.res]
            if self.res.final in self.pos_dict:
                self.pos_dict[self.res.final].append(self.res)
            else:
                self.pos_dict[self.res.final] = [self.res]
            self.element_list.append(self.res)
            self.res = Resistor()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)

        
    def OnRes1(self, event):
        '''  To input the value of Resistance '''
        dlg = wx.TextEntryDialog(None, "Value of resistance (in Ohm) used : ",'Resistance', 'Enter value here')
        
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.res.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Res1)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)
        else:
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
            

    def On_Click_Res1(self,event=None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Res1)
            return
        else:
            if self.maxmy[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Res1)
                return
            self.res.initial = (event.GetX(),self.maxmy[0])
            self.res.getfinalpos1()
            for x in self.element_list:
                if (x.initial == self.res.initial and x.final ==  self.res.final) or (x.initial == self.res.final and x.final ==  self.res.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.res = Resistor()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        return
            self.pos_l.append(self.res.initial)
            self.pos_l.append(self.res.final)
            self.StatusBar.SetStatusText(str([self.res.initial, self.res.final]))
            self.last.append(self.res.initial)
            dc.SetPen(wx.Pen("RED", 1))
            dc.DrawLine(event.GetX(),event.GetY(),event.GetX(),event.GetY())
            dc.DrawBitmap(bmp11, self.res.initial[0]-7, self.res.initial[1]+1, True)
            
            if self.res.initial in self.pos_dict:
                self.pos_dict[self.res.initial].append(self.res)
            else:
                self.pos_dict[self.res.initial] = [self.res]
            if self.res.final in self.pos_dict:
                self.pos_dict[self.res.final].append(self.res)
            else:
                self.pos_dict[self.res.final] = [self.res]
            self.element_list.append(self.res)
            self.res = Resistor()
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)

    

    def OnWire(self,event):
        ''' To input initialing and ending points '''
        self.position = []
        self.panel2.Bind(wx.EVT_MOTION, None)
        self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Wire1)
        self.StatusBar.SetStatusText(str((self.position)))
        self.panel2.Bind(wx.EVT_MOTION, self.select_wire_motion)

    def select_wire_motion(self, event):
        if event.GetPosition() in pointlist:
            self.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))
            
        
    def On_Click_Wire1(self,event):
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            seelf.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Wire1)
            return
        else:
            if event.GetPosition() not in pointlist:
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                return
            self.position.append(event.GetX())
            self.position.append(event.GetY())
            self.wire.initial = (self.position[0], self.position[1])
            self.pos_l.append(self.wire.initial)
            self.StatusBar.SetStatusText(str(self.wire.initial))
            self.StatusBar.SetStatusText(str((self.position)))
            self.panel2.Bind(wx.EVT_MOTION, self.cursor)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Wire2)

    def cursor(self,event):
        odc = wx.DCOverlay(self.panel2.overlay, dc)
        odc.Clear()        
        dc.SetPen(wx.Pen("RED", 1))
        dc.DrawLine(200,self.position[1],1000, self.position[1]) 
        dc.DrawLine(self.position[0],0,self.position[0], 700)
        dummypos_l = self.pos_l[:-1]
        pos_lx = [l[0] for l in dummypos_l]
        pos_ly = [l[1] for l in dummypos_l]
        if event.GetX() in pos_lx:
            y=[]
            for l in self.pos_l:
                if event.GetX() == l[0]:
                    y.append(l[1])
            
            dc.SetPen(wx.Pen("GREEN", 1))
            dc.DrawLine(200,event.GetY(),1000, event.GetY())
            dc.DrawLine(event.GetX(),0,event.GetX(), 700)
            dc.SetPen(wx.Pen("YELLOW", 1))
            for m in y:
                dc.DrawLine(200,m,1000,m)
            
            
        if event.GetY() in pos_ly:
            x=[]
            for l in self.pos_l:
                if event.GetY() == l[1]:
                    x.append(l[0])
            dc.SetPen(wx.Pen("GREEN", 1))
            dc.DrawLine(event.GetX(),0,event.GetX(), 700)
            dc.DrawLine(200,event.GetY(),1000, event.GetY())
            dc.SetPen(wx.Pen("YELLOW", 1))
            for m in x:
                dc.DrawLine(m,0,m, 700)
        else:
            dc.SetPen(wx.Pen("RED", 1))
            dc.DrawLine(event.GetX(),0,event.GetX(), 700)
            dc.DrawLine(200,event.GetY(),1000, event.GetY())
        
        
        del odc 
        self.StatusBar.SetStatusText(str((self.position, (event.GetX(),event.GetY()))))
        if event.GetX() == self.position[0] or event.GetY()== self.position[1]:
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            if event.GetPosition() in pointlist:
                self.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))
        else:
            self.SetCursor(wx.StockCursor(wx.CURSOR_NO_ENTRY))
                
    def On_Click_Wire2(self,event):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc 
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Wire2)
            return
        else:
            if event.GetPosition() not in pointlist:
                self.position = []
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                return
            
            self.panel2.Bind(wx.EVT_MOTION, None)
            self.position.append(event.GetX())
            self.position.append(event.GetY())
            self.wire.final = (self.position[2],self.position[3])
            for x in self.element_list:
                if (x.initial == self.wire.initial and x.final ==  self.wire.final) or (x.initial == self.wire.final and x.final ==  self.wire.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.wire = Wire()
                        self.position = []
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            if self.position[0] == self.position[2] and self.position[1] == self.position[3]:
                self.wire = Wire()
                m= self.pos_l.pop()
            else:
                self.pos_l.append(self.wire.final)
            
                self.StatusBar.SetStatusText(str((self.position)))
                dc.SetPen(wx.Pen("BLACK", 2))
                if self.position[0] == self.position[2] or self.position[1] == self.position[3]:
            
                    dc.DrawLine(self.position[0],self.position[1],self.position[2], self.position[3])      
                    self.last.append(self.wire.final)
                
                    if self.wire.initial in self.pos_dict:
                        self.pos_dict[self.wire.initial].append(self.wire)
                    else:
                        self.pos_dict[self.wire.initial] = [self.wire]
                    if self.wire.final in self.pos_dict:
                        self.pos_dict[self.wire.final].append(self.wire)
                    else:
                        self.pos_dict[self.wire.final] = [self.wire]
            self.element_list.append(self.wire)
            self.wire = Wire()
            self.position = []
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
            


   
    def OnBulb(self, event = None):
        frame = TextFrame()
        frame.Show()
        self.panel2.Bind(wx.EVT_MOTION, self.bulbcheck)

    def bulbcheck(self, event):
       
        if b.access =='YES':
            self.bulb.voltage = b.voltage
            self.bulb.power = b.power
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Bulb)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)
            b.access = 'NO'
        
        

    def On_Click_Bulb(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
        else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Bulb)
                return
            
            self.bulb.initial = (self.maxmx[0],event.GetY())
            self.bulb.getfinalpos()
            for x in self.element_list:
                if (x.initial == self.bulb.initial and x.final ==  self.bulb.final) or (x.initial == self.bulb.final and x.final ==  self.bulb.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.bulb = Bulb()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.bulb.initial)
            self.pos_l.append(self.bulb.initial)
            self.pos_l.append(self.bulb.final)
            dc.DrawBitmap(bmp4, self.bulb.initial[0]+1, self.bulb.initial[1]-8, True)
            
            if self.bulb.initial in self.pos_dict:
                self.pos_dict[self.bulb.initial].append(self.bulb)
            else:
                self.pos_dict[self.bulb.initial] = [self.bulb]
            if self.bulb.final in self.pos_dict:
                self.pos_dict[self.bulb.final].append(self.bulb)
            else:
                self.pos_dict[self.bulb.final] = [self.bulb]
            self.element_list.append(self.bulb)
            self.bulb =  Bulb()
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)

    def OnVolt(self, event= None):
        dlg = wx.TextEntryDialog(None, "Value of voltage (in V) used : ",'EMF', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.batr.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def OnVolt1(self, event= None):
        dlg = wx.TextEntryDialog(None, "Value of voltage (in V) used : ",'EMF', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.batr.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt1)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def OnVolt2(self, event= None):
        dlg = wx.TextEntryDialog(None, "Value of voltage (in V) used : ",'EMF', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.batr.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt2)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def OnVolt3(self, event= None):
        dlg = wx.TextEntryDialog(None, "Value of voltage (in V) used : ",'EMF', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.batr.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt3)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def OnVoltac(self, event= None):
        print 'yesdsnf'
        self.panel2.Bind(wx.EVT_MOTION, self.accheck)
        frame = TextFrame1()
        frame.Show()
        

    def accheck(self, event):
        print ac.access
        if ac.access =='YES':
            self.acbatr.phase = ac.phase
            self.acbatr.value = ac.value
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltac)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)
            ac.access = 'NO'

        '''
        dlg = wx.TextEntryDialog(None, "Value of voltage (in V) used : ",'EMF', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.acbatr.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltac)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)
        '''
    def OnVoltac1(self, event= None):
        frame = TextFrame1()
        frame.Show()
        self.panel2.Bind(wx.EVT_MOTION, self.accheck1)

    def accheck1(self, event):
       
        if ac.access =='YES':
            self.acbatr.phase = ac.phase
            self.acbatr.value = ac.value
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltac1)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)
            ac.access = 'NO'

        
    def On_Click_Volt(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt)
            return
        else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt)
                return
            self.batr.initial = (self.maxmx[0], event.GetY())            
            self.batr.getfinalpos()
            self.countdc[0] += 1
            self.batr.ID = self.countdc[0]
            print self.batr.ID
            for x in self.element_list:
                if (x.initial == self.batr.initial and x.final ==  self.batr.final) or (x.initial == self.batr.final and x.final ==  self.batr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.batr = Dcbattery()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.batr.initial)
            self.pos_l.append(self.batr.initial)
            self.pos_l.append(self.batr.final)
            self.StatusBar.SetStatusText(str([self.batr.initial, self.batr.final]))
            if self.batr.initial in self.pos_dict:
                self.pos_dict[self.batr.initial].append(self.batr)
            else:
                self.pos_dict[self.batr.initial] = [self.batr]
            if self.batr.final in self.pos_dict:
                self.pos_dict[self.batr.final].append(self.batr)
            else:
                self.pos_dict[self.batr.final] = [self.batr]
            dc.DrawBitmap(bmp2, self.batr.initial[0]+1, self.batr.initial[1]-9, True)
            self.element_list.append(self.batr)
            self.batr = Dcbattery()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def On_Click_Voltac(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEEFT_DOWN, self.On_Click_Voltac)
            return
        else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltac)
                return
            self.acbatr.initial = (self.maxmx[0], event.GetY())
            self.acbatr.getfinalpos()
            self.countac[0] += 1
            if self.countac[0] > 0:
                self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitAC, self.button11)
            else:
                self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)
            self.acbatr.ID = self.countac[0]
            print self.acbatr.ID
            for x in self.element_list:
                if (x.initial == self.acbatr.initial and x.final ==  self.acbatr.final) or (x.initial == self.acbatr.final and x.final ==  self.acbatr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.acbatr = Acbattery()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.acbatr.initial)
            self.pos_l.append(self.acbatr.initial)
            self.pos_l.append(self.acbatr.final)
            self.StatusBar.SetStatusText(str([self.acbatr.initial, self.acbatr.final]))
            if self.acbatr.initial in self.pos_dict:
                self.pos_dict[self.acbatr.initial].append(self.acbatr)
            else:
                self.pos_dict[self.acbatr.initial] = [self.acbatr]
            if self.acbatr.final in self.pos_dict:
                self.pos_dict[self.acbatr.final].append(self.acbatr)
            else:
                self.pos_dict[self.acbatr.final] = [self.acbatr]
            dc.DrawBitmap(bmp3, self.acbatr.initial[0]+1,self.acbatr.initial[1]-8, True)
            self.element_list.append(self.acbatr)
            
            self.acbatr = Acbattery()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def On_Click_Volt1(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt1)
            return
        else:
            if self.maxmy[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt1)
                return
            self.batr.initial = (event.GetX(), self.maxmy[0])
            self.batr.getfinalpos1()
            self.countdc[0] += 1
            self.batr.ID = self.countdc[0]
            for x in self.element_list:
                if (x.initial == self.batr.initial and x.final ==  self.batr.final) or (x.initial == self.batr.final and x.final ==  self.batr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.batr = Dcbattery()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.batr.initial)
            self.pos_l.append(self.batr.initial)
            self.pos_l.append(self.batr.final)
            self.StatusBar.SetStatusText(str([self.batr.initial, self.batr.final]))
            if self.batr.initial in self.pos_dict:
                self.pos_dict[self.batr.initial].append(self.batr)
            else:
                self.pos_dict[self.batr.initial] = [self.batr]
            if self.batr.final in self.pos_dict:
                self.pos_dict[self.batr.final].append(self.batr)
            else:
                self.pos_dict[self.batr.final] = [self.batr]
            dc.DrawBitmap(bmp21, self.batr.initial[0]-9,self.batr.initial[1]+1, True)
            self.element_list.append(self.batr)
            self.batr = Dcbattery()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def On_Click_Voltac1(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltac)
            return
        else:
            if self.maxmy[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltac1)
                return
            self.acbatr.initial = (event.GetX(), self.maxmy[0])
            self.acbatr.getfinalpos1()
            self.countac[0] +=1
            if self.countac[0] > 0:
                self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitAC, self.button11)
            else:
                self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)
            self.acbatr.ID = self.countac[0]
            for x in self.element_list:
                if (x.initial == self.acbatr.initial and x.final ==  self.acbatr.final) or (x.initial == self.acbatr.final and x.final ==  self.acbatr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.acbatr = Acbattery()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.acbatr.initial)
            self.pos_l.append(self.acbatr.initial)
            self.pos_l.append(self.acbatr.final)
            self.StatusBar.SetStatusText(str([self.acbatr.initial, self.acbatr.final]))
            if self.acbatr.initial in self.pos_dict:
                self.pos_dict[self.acbatr.initial].append(self.acbatr)
            else:
                self.pos_dict[self.acbatr.initial] = [self.acbatr]
            if self.acbatr.final in self.pos_dict:
                self.pos_dict[self.acbatr.final].append(self.acbatr)
            else:
                self.pos_dict[self.acbatr.final] = [self.acbatr]
            dc.DrawBitmap(bmp31, self.acbatr.initial[0]-8,self.acbatr.initial[1]+1, True)
            self.element_list.append(self.acbatr)
            self.acbatr = Acbattery()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def On_Click_Volt2(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt2)
            return
        else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt2)
                return
            self.batr.initial = (self.maxmx[0], event.GetY())
            self.batr.getfinalpos2()
            self.countdc[0] += 1
            self.batr.ID = self.countdc[0]
            for x in self.element_list:
                if (x.initial == self.batr.initial and x.final ==  self.batr.final) or (x.initial == self.batr.final and x.final ==  self.batr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.batr = Dcbattery()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.batr.initial)
            self.pos_l.append(self.batr.initial)
            self.pos_l.append(self.batr.final)
            self.StatusBar.SetStatusText(str([self.batr.initial, self.batr.final]))
            if self.batr.initial in self.pos_dict:
                self.pos_dict[self.batr.initial].append(self.batr)
            else:
                self.pos_dict[self.batr.initial] = [self.batr]
            if self.batr.final in self.pos_dict:
                self.pos_dict[self.batr.final].append(self.batr)
            else:
                self.pos_dict[self.batr.final] = [self.batr]
            dc.DrawBitmap(bmp22, self.batr.initial[0]+1,self.batr.initial[1]-9, True)
            self.element_list.append(self.batr)
            self.batr = Dcbattery()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    
    def On_Click_Volt3(self, event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt3)
            return
        else:
            if self.maxmy[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Volt3)
                return
            self.batr.initial = (event.GetX(), self.maxmy[0])            
            self.batr.getfinalpos3()
            self.countdc[0] += 1
            self.batr.ID = self.countdc[0]
            for x in self.element_list:
                if (x.initial == self.batr.initial and x.final ==  self.batr.final) or (x.initial == self.batr.final and x.final ==  self.batr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.batr = Dcbattery()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.batr.initial)
            self.pos_l.append(self.batr.initial)
            self.pos_l.append(self.batr.final)
            self.StatusBar.SetStatusText(str([self.batr.initial, self.batr.final]))
            if self.batr.initial in self.pos_dict:
                self.pos_dict[self.batr.initial].append(self.batr)
            else:
                self.pos_dict[self.batr.initial] = [self.batr]
            if self.batr.final in self.pos_dict:
                self.pos_dict[self.batr.final].append(self.batr)
            else:
                self.pos_dict[self.batr.final] = [self.batr]
            dc.DrawBitmap(bmp23, self.batr.initial[0]-9,self.batr.initial[1]+1, True)
            self.element_list.append(self.batr)
            self.batr = Dcbattery()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def OnCapc(self, event):
        '''  To input the value of Capacitance '''
        dlg = wx.TextEntryDialog(None, "Value of Capacitance (in Microfarad) used : ",'Capacitance', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.capc.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Capc)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def On_Click_Capc(self,event=None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Capc)
            return
        else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Capc)
                return
            self.capc.initial = (self.maxmx[0],event.GetY())
            self.capc.getfinalpos()
            for x in self.element_list:
                if (x.initial == self.capc.initial and x.final ==  self.capc.final) or (x.initial == self.capc.final and x.final ==  self.capc.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.capc = Capacitor()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.last.append(self.capc.initial)
            self.pos_l.append(self.capc.initial)
            self.pos_l.append(self.capc.final)
            self.StatusBar.SetStatusText(str([self.capc.initial, self.capc.final]))
            dc.DrawBitmap(bmp7, self.capc.initial[0]+1, self.capc.initial[1]-7, True)
            
            if self.capc.initial in self.pos_dict:
                self.pos_dict[self.capc.initial].append(self.capc)
            else:
                self.pos_dict[self.capc.initial] = [self.capc]
            if self.capc.final in self.pos_dict:
                self.pos_dict[self.capc.final].append(self.capc)
            else:
                self.pos_dict[self.capc.final] = [self.capc]
            
            self.capclist.append(self.capc)
            self.element_list.append(self.capc)
            self.capc = Capacitor()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def OnIndr(self, event):
        '''  To input the value of Resistance '''
        dlg = wx.TextEntryDialog(None, "Value of Inductance (in Henry) used : ",'Inductance', 'Enter value here')
        if dlg.ShowModal() == wx.ID_OK:
            self.panel2.Bind(wx.EVT_MOTION, None)
            x = dlg.GetValue()
            if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    self.indr.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                    return
            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Indr)
            self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def On_Click_Indr(self,event = None):
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear() 
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Indr)
            return
        else:
            if self.maxmx[0] == -1:
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Indr)
                return
            self.indr.initial = (self.maxmx[0],event.GetY())
            self.indr.getfinalpos()
            for x in self.element_list:
                if (x.initial == self.indr.initial and x.final ==  self.indr.final) or (x.initial == self.indr.final and x.final ==  self.indr.initial):
                    dlg = wx.MessageDialog(None, 'REPLACE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_CANCEL:
                        self.indr = Inductor()
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
                        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
                        return
            self.pos_l.append(self.indr.initial)
            self.pos_l.append(self.indr.final)
            self.StatusBar.SetStatusText(str([self.indr.initial, self.indr.final]))
            self.last.append(self.indr.initial)
            dc.DrawBitmap(bmp8, self.indr.initial[0]+1, self.indr.initial[1]-9, True)
            
            if self.indr.initial in self.pos_dict:
                self.pos_dict[self.indr.initial].append(self.indr)
            else:
                self.pos_dict[self.indr.initial] = [self.indr]
            if self.indr.final in self.pos_dict:
                self.pos_dict[self.indr.final].append(self.indr)
            else:
                self.pos_dict[self.indr.final] = [self.indr]
            self.element_list.append(self.indr)
            self.indrlist.append(self.indr)
            self.indr = Inductor()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def OnSubmitDC(self, event = None):
        
        for j in self.pos_dict:
            print self.pos_dict
            print self.last
            if self.pos_dict[j][0] is self.pos_dict[j][-1]:
                dlg = wx.MessageDialog(None, 'CIRCUIT INCOMPLETE','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()
                break
        
    
        else:
            self.submitflag[0] = 1
            if self.pos_dict != {}:
                import DCalgo 
                no = [0]
                nodelist = []
                l = []
                flg = []
                DCalgo.traverse(self.pos_dict, self.last[-1], curr = (0,0), prev = (0,0), i = no, node_list =  nodelist, count = l, flag = flg)
                equations = []
                m = len(l)
                for x in range(m):
                    equations.append([0]*(m+1))
                j = [0]
                print equations
                print l
                var = [0]
                rng = len(l)
                h = l[:]
                h.sort()
                for x in range(rng):
                    if ['i%s'%var[0]] in h:
                        print 'no'
                        print var[0]
                        var[0] += 1
                        n = h.pop(0)
                        print h
                    else:

                        print 'yes'
                        h[0][0] = 'i%s'%var[0]
                        print var[0]
                        var[0] +=1
                        print h
                         
                nodelist1 = []
                for x in self.capclist:
                    x.current[0] = 0
                for x in self.indrlist:
                    x.type == "WIRE"
                    x.value = 0
                
                DCalgo.current_law(self.pos_dict, equations, self.last[-1], self.last[-1], nodelist1, j, m)
                print equations
                x = [[0]*(no[0]+1)]
                print j[0]
                for y in equations[:j[0]+1]:
                    if y==x:
                        print 'yes'
                
                print 'counter = %s'% l
                poslist = []
                looplast = [0]
                if nodelist != []:
                    looplast[0] = nodelist[0]
                else:
                    looplast[0] = self.last[-1]
                node_list = []
                flag = []
                print self.last
                stc = []
                import loop_law_modified
                loop_law_modified.loop_law(pos_dict=self.pos_dict, pos_list = poslist, stack = stc, element_list = self.element_list, equation = equations, i=j, counter=m, nodelist= node_list, last =looplast[0]) 
                print equations
                from scipy import mat
                from scipy import linalg
                
                from ech import ToReducedRowEchelonForm
                ToReducedRowEchelonForm(equations)
                print equations
                
                for x in range(len(equations)):
                    for y in range(len(equations[0])-1):
                        print x,y
                        print equations[x][y]
                        if equations[x][y] != 0:
                            print l[y]
                            l[y][0] = equations[x][-1]
                            print 'yes'
                            print l[y]

                print l
                for x in self.element_list:
                    x.displaycurrent = [str(x.current)]
                    print x.type, x.current, x.displaycurrent
                
                self.StatusBar.SetStatusText(str(l))
                self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)

                
    def OnSubmitAC(self, event = None):
        import copy
        print 'ACsubmit called'
        
        for j in self.pos_dict:
            print self.pos_dict
            print self.last
            if self.pos_dict[j][0] is self.pos_dict[j][-1]:
                dlg = wx.MessageDialog(None, 'CIRCUIT INCOMPLETE','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()
                break
        
    
        else:
            self.submitflag[0] = 1
            if self.pos_dict != {}:
                import ACalgo_modified
                
                i = 0
                while self.countac[0] > 0 or self.countdc[0] > 0:
                    print 'got agn in main loop'
                    i += 1
                    print i
                    print 'countac'
                    print self.countac
                    print 'countdc'
                    print self.countdc
                    for x in self.element_list:
                        x.current=[0]
                        x.direction=(0,0)
                        print x.type,
                        print x.direction

                    batterylist = []
                    for x in self.element_list:
                        if self.countac[0] > 0:
                            
                            if x.type == "ACBATTERY" and x.ID != self.countac[0]:
                                print x.type, x.ID, self.countac[0]
                                x.valuer = copy.copy(x.value)
                                x.value = 0
                                batterylist.append(x)
                                print 'value changed to zero'
                            if x.type == 'DCBATTERY':
                                print x.type, x.ID, self.countac[0]
                                x.valuer = copy.copy(x.value)
                                x.value = 0
                                batterylist.append(x)
                                print 'value changed to zero'
                            
                       
                        elif self.countac[0] == 0:
                            
                            if x.type == "DCBATTERY" and x.ID != self.countdc[0]:
                                x.valuer = copy.copy(x.value)
                                x.value = 0
                                batterylist.append(x)
                                print 'value changed to zero'
                            if x.type == 'ACBATTERY':
                                x.valuer = copy.copy(x.value)
                                x.value = 0
                                batterylist.append(x)
                                print 'value changed to zero'
                            
                    if self.countac != [0]:
                        self.countac[0] -=1
                    else:
                        self.countdc[0] -= 1
                        
                    print batterylist  
                    for x in self.element_list:
                        print x.type,
                        print x.direction
                    no = [0]
                    nodelist = []
                    l = []
                    flg = []
                    currentlist = []
                    ACalgo_modified.traverse(self.pos_dict, self.last[-1], curr = (0,0), prev = (0,0), i = no, node_list =  nodelist, count = l, flag = flg)
                    equations = []
                    m = len(l)
                    for x in range(m):
                        equations.append([0]*(m+1))
                    j = [0]
                    print equations
                    print l
                    var = [0]
                    rng = len(l)
                    h = l[:]
                    h.sort()
                    for x in range(rng):
                        if ['i%s'%var[0]] in h:
                            print 'no'
                            print var[0]
                            var[0] += 1
                            n = h.pop(0)
                            print h
                        else:

                            print 'yes'
                            h[0][0] = 'i%s'%var[0]
                            print var[0]
                            var[0] +=1
                            print h
                         
                    nodelist1 = []
                    for x in self.element_list:
                        print x.type,
                        print x.direction
                
                    ACalgo_modified.current_law(self.pos_dict, equations, self.last[-1], self.last[-1], nodelist1, j, m)
                    print equations
                    x = [[0]*(no[0]+1)]
                    print j[0]
                    for y in equations[:j[0]+1]:
                        if y==x:
                            print 'yes'
                
                    print 'counter = %s'% l
                    poslist = []
                    looplast = [0]
                    if nodelist != []:
                        looplast[0] = nodelist[0]
                    else:
                        looplast[0] = self.last[-1]
                    node_list = []
                    flag = []
                    print self.last
                    stc = []
                    for x in self.element_list:
                        print x.type,
                        print x.direction
                    
                        
                    ACalgo_modified.loop_law(pos_dict=self.pos_dict, pos_list = poslist, stack = stc, element_list = self.element_list, equation = equations, i=j, counter=m, nodelist= node_list, last =looplast[0]) 
                    
                    #solve
                    from ech import ToReducedRowEchelonForm
                    ToReducedRowEchelonForm(equations)
                    print equations
                
                    for x in range(len(equations)):
                        for y in range(len(equations[0])-1):
                            print x,y
                            print equations[x][y]
                            if equations[x][y] != 0:
                                print l[y]
                                l[y][0] = equations[x][-1]
                                print 'yes'
                                print l[y]
                    


                    print 'l = ',
                    print l
                    if currentlist == []:
                        currentlist.append(l)
                        print currentlist
                    else:
                        for a in range(len(l)):
                            print 'l[a][0] = ',
                            print l[a][0]
                            print 'currentlist[a][0]'
                            print currentlist[a][0]
                            
                            currentlist[a][0] += l[a][0]
                                
                            print currentlist
                        
                    print currentlist
                    for x in batterylist:
                        x.value = copy.copy(x.valuer)
                        print x.type
                        print x.value
            import math    
            for x in self.element_list:
                if x.current[0].real==0:
                    x.displaycurrent=[str(math.sqrt(x.current[0].real**2 + x.current[0].imag**2)) +'<'+str(math.pi/2)]
    
                else:
                    x.displaycurrent = [str(math.sqrt(x.current[0].real**2 + x.current[0].imag**2)) + '<' + str(numpy.arctan(x.current[0].imag/x.current[0].real))]
                print x.type, x.current, x.displaycurrent
            self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)
                

        
    def OnRefresh(self, event = None):
        dc.Clear()
        
        #self.panel2.Refresh()
        self.position = []        
        self.pos_dict = {}
        self.pos_l = []
        self.last = []        
        self.capclist = []
        self.indrlist = []
        self.element_list = []
        self.volt_dict = {}
        self.res= Resistor()
        self.bulb = Bulb()
        self.batr = Dcbattery()
        self.acbatr = Acbattery()
        self.wire = Wire()
        self.capc = Capacitor()
        self.indr = Inductor()
        self.voltm = Voltmeter()
        self.countac = [0]
        self.countdc = [0]
        self.maxmx = [0]
        self.maxmy = [0]
        b.access = 'NO'
        ac.access = 'NO'
        self.submitflag = [0]
        
        self.panel2.SetBackgroundColour('White')
        self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)
        self.panel2.Bind(wx.EVT_BUTTON, self.OnThevenin, self.button10)
        dc.SetPen(wx.Pen("BLACK", 1))
        for x in pointlist:
            dc.DrawLine(x[0] - 3, x[1], x[0] + 3, x[1])
            dc.DrawLine(x[0], x[1] - 3, x[0], x[1] + 3)
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
        

    def OnRemove(self, event = None):
        self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.SelectRemove_element)

    def SelectRemove_element(self, event):
        pos_lx = [ l[0] for l in self.pos_l]
        pos_ly = [ l[1] for l in self.pos_l]
        if event.GetX() not in pos_lx and event.GetY() not in pos_ly:
            dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
        else:
            y = []
            x = []
            for l in self.pos_l:
                if event.GetX() == l[0]:
                    y.append(l[1])
            for l in self.pos_l:
                if event.GetY() == l[1]:
                    x.append(l[0])
            if y != []:
                if len(y) > 1:                          
                    maxm = -1
                    minm = 2000
                    for l in y:
                        if l > maxm and l < event.GetY():
                            maxm = l
                        if l < minm and l > event.GetY():
                            minm = l
                    for l in self.element_list:
                        if (event.GetX(),maxm) == l.initial and (event.GetX(), minm) == l.final:
                            dc.SetPen(wx.Pen("RED", 1))
                            dc.DrawLine(event.GetX()-3, l.initial[1], event.GetX()+3, l.initial[1])
                            dc.DrawLine(event.GetX()-3, l.final[1], event.GetX()+3, l.final[1])
                            dlg = wx.MessageDialog(None, 'REMOVE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                            if dlg.ShowModal() == wx.ID_OK:
                                self.element_list.remove(l)
                                self.pos_dict[l.initial].remove(l)
                                self.pos_dict[l.final].remove(l)
                                self.pos_l.remove(l.initial)
                                self.pos_l.remove(l.final)
                                if l in capclist:
                                    self.capclist.remove(l)
                                if l in indrlist:
                                    self.indrlist.remove(l)
                                
                                if l.type == 'WIRE' and l not in self.indrlist:
                                    dc.SetPen(wx.Pen("WHITE", 2))
                                    dc.DrawLine(l.initial[0],l.initial[1],l.final[0],l.final[1])
                                    break
                                elif l.final[0] == l.initial[0]:
                                    x = (l.initial[0]-10,l.initial[1])
                                    y = (l.final[0]+10,l.final[1])
                                                                 
                                else:
                                    x = (l.initial[0],l.initial[1]-10)
                                    y = (l.final[0],l.final[1]+10)
                                    
                                rect = wx.RectPP(x,y)
                                dc.SetPen(wx.Pen("WHITE", 1))
                                dc.DrawRectangleRect(rect)
                            break
                        elif (event.GetX(),maxm) == l.final and (event.GetX(), minm) == l.initial:
                            dc.DrawLine(l.initial[0]-3, l.initial[1], l.initial[0]+3, l.initial[1])
                            dc.DrawLine(l.final[0]-3, l.final[1], l.final[0]+3, l.final[1])
                            dlg = wx.MessageDialog(None, 'REMOVE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                            if dlg.ShowModal() == wx.ID_OK:
                                self.element_list.remove(l)
                                self.pos_dict[l.initial].remove(l)
                                self.pos_dict[l.final].remove(l)
                                self.pos_l.remove(l.initial)
                                self.pos_l.remove(l.final)
                                if l in capclist:
                                    self.capclist.remove(l)
                                if l in indrlist:
                                    self.indrlist.remove(l)
                                
                                if l.type == 'ACBATTERY':
                                    self.countac[0] -= 1
                                    if self.countac[0] > 0:
                                        self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitAC, self.button11)
                                    else:
                                        self.panel2.Bind(wx.EVT_BUTTON, self.OnSubmitDC, self.button11)
                                        
                                
                                
                                if l.type == 'WIRE' and l not in self.indrlist:
                                    dc.SetPen(wx.Pen("WHITE", 2))
                                    dc.DrawLine(l.initial[0],l.initial[1],l.final[0],l.final[1])
                                    break
                                elif l.final[0] == l.initial[0]:
                                    x = (l.initial[0]-10,l.initial[1])
                                    y = (l.final[0]+10,l.final[1])
                                                                 
                                else:
                                    x = (l.initial[0],l.initial[1]-10)
                                    y = (l.final[0],l.final[1]+10)
                                    
                                rect = wx.RectPP(x,y)
                                dc.SetPen(wx.Pen("WHITE", 1))
                                dc.DrawRectangleRect(rect)
                            break

                
            if x != []:
                if len(x) > 1:
                    maxm = -1
                    minm = 2000
                    for l in x:
                        if l > maxm and l < event.GetX():
                            maxm = l
                        if l < minm and l > event.GetX():
                            minm = l
                    for l in self.element_list:
                        if (maxm, event.GetY()) == l.initial and ( minm, event.GetY()) == l.final:
                            dc.SetPen(wx.Pen("RED", 1))
                            dc.DrawLine(l.initial[0], l.initial[1]-3, l.initial[0], l.initial[1]+3)
                            dc.DrawLine(l.final[0], l.final[1]-3, l.final[0], l.final[1]+3)
                            dlg = wx.MessageDialog(None, 'REMOVE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                            if dlg.ShowModal() == wx.ID_OK:
                                self.element_list.remove(l)
                                self.pos_dict[l.initial].remove(l)
                                self.pos_dict[l.final].remove(l)
                                self.pos_l.remove(l.initial)
                                self.pos_l.remove(l.final)
                                if l in capclist:
                                    self.capclist.remove(l)
                                if l in indrlist:
                                    self.indrlist.remove(l)
                                
                                
                                if l.type == 'WIRE' and l not in self.indrlist:
                                    dc.SetPen(wx.Pen("WHITE", 2))
                                    dc.DrawLine(l.initial[0],l.initial[1],l.final[0],l.final[1])
                                    break
                                elif l.final[0] == l.initial[0]:
                                    x = (l.initial[0]-10,l.initial[1])
                                    y = (l.final[0]+10,l.final[1])
                                                                 
                                else:
                                    x = (l.initial[0],l.initial[1]-10)
                                    y = (l.final[0],l.final[1]+10)
                                    
                                rect = wx.RectPP(x,y)
                                dc.SetPen(wx.Pen("WHITE", 1))
                                dc.DrawRectangleRect(rect)      
                            
                        elif (maxm, event.GetY()) == l.final and (minm, event.GetY()) == l.initial:
                            dc.DrawLine(event.GetX()-3, l.initial[1], event.GetX()+3, l.initial[1])
                            dc.DrawLine(event.GetX()-3, l.final[1], event.GetX()+3, l.final[1])
                            dlg = wx.MessageDialog(None, 'REMOVE ELEMENT?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
                            if dlg.ShowModal() == wx.ID_OK:
                                self.element_list.remove(l)
                                self.pos_dict[l.initial].remove(l)
                                self.pos_dict[l.final].remove(l)
                                self.pos_l.remove(l.initial)
                                self.pos_l.remove(l.final)
                                if l in capclist:
                                    self.capclist.remove(l)
                                if l in indrlist:
                                    self.indrlist.remove(l)
                                
                                
                                if l.type == 'WIRE' and l not in self.indrlist:
                                    dc.SetPen(wx.Pen("WHITE", 2))
                                    dc.DrawLine(l.initial[0],l.initial[1],l.final[0],l.final[1])
                                    break
                                elif l.final[0] == l.initial[0]:
                                    x = (l.initial[0]-10,l.initial[1])
                                    y = (l.final[0]+10,l.final[1])
                                                                 
                                else:
                                    x = (l.initial[0],l.initial[1]-10)
                                    y = (l.final[0],l.final[1]+10)
                                    
                                rect = wx.RectPP(x,y)
                                dc.SetPen(wx.Pen("WHITE", 1))
                                dc.DrawRectangleRect(rect)        
                    
                else:
                    dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()

        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    def OnThevenin(self,event):
        self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.select_element_thev)
    

    def select_element_thev(self,event):
        from copy import deepcopy
        resist[0] = 0
        for j in self.pos_dict:
            print self.pos_dict
            print self.last
            if self.pos_dict[j][0] is self.pos_dict[j][-1]:
                dlg = wx.MessageDialog(None, 'CIRCUIT INCOMPLETE','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()
                return
        
        pos_lx = [ l[0] for l in self.pos_l]
        pos_ly = [ l[1] for l in self.pos_l]
        if event.GetX() not in pos_lx and event.GetY() not in pos_ly:
            dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.select_element_thev)            
            return
        else:
            y = []
            x = []
            for l in self.pos_l:
                if event.GetX() == l[0]:
                    y.append(l[1])
            for l in self.pos_l:
                if event.GetY() == l[1]:
                    x.append(l[0])
            if y != []:
                if len(y) > 1:                          
                    maxm = -1
                    minm = 2000
                    for l in y:
                        if l > maxm and l < event.GetY():
                            maxm = l
                        if l < minm and l > event.GetY():
                            minm = l
                    for l in self.element_list:
                        
                        if (event.GetX(),maxm) == l.initial and (event.GetX(), minm) == l.final:
                            resist[0] = l
                            dc.SetPen(wx.Pen("RED", 1))
                            dc.DrawLine(event.GetX()-3, l.initial[1], event.GetX()+3, l.initial[1])
                            dc.DrawLine(event.GetX()-3, l.final[1], event.GetX()+3, l.final[1])
                            break
                                
                        elif (event.GetX(),maxm) == l.final and (event.GetX(), minm) == l.initial:
                            resist[0] = l
                            dc.DrawLine(l.initial[0]-3, l.initial[1], l.initial[0]+3, l.initial[1])
                            dc.DrawLine(l.final[0]-3, l.final[1], l.final[0]+3, l.final[1])
                            break
                                  
            if x != []:
                if len(x) > 1:
                    maxm = -1
                    minm = 2000
                    for l in x:
                        if l > maxm and l < event.GetX():
                            maxm = l
                        if l < minm and l > event.GetX():
                            minm = l
                    for l in self.element_list:
                        
                        if (maxm, event.GetY()) == l.initial and ( minm, event.GetY()) == l.final:
                            resist[0] = l
                            dc.SetPen(wx.Pen("RED", 1))
                            dc.DrawLine(l.initial[0], l.initial[1]-3, l.initial[0], l.initial[1]+3)
                            dc.DrawLine(l.final[0], l.final[1]-3, l.final[0], l.final[1]+3)
                            break    
                            
                        elif (maxm, event.GetY()) == l.final and (minm, event.GetY()) == l.initial:
                            resist[0] = l
                            dc.DrawLine(event.GetX()-3, l.initial[1], event.GetX()+3, l.initial[1])
                            dc.DrawLine(event.GetX()-3, l.final[1], event.GetX()+3, l.final[1])
                            break
                            
                else:
                    dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                    self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.select_element_thev)            
                    return
                
        dlg = wx.MessageDialog(None, 'CONTINUE?','MessageDialog', wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_CANCEL:
            
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
            return
        
        

        for x in self.element_list:
            print x.type,
            print x.value,
            print x.current,
            print x.direction
        import DCalgo
        no = [0]
        nodelist = []
        l = []
        flg = []
        DCalgo.traverse(self.pos_dict, self.last[-1], curr = (0,0), prev = (0,0), i = no, node_list =  nodelist, count = l, flag = flg)
        for x in self.element_list:
            print x.type,
            print x.value,
            print x.current,
            print x.direction
        
        print l
        equations = []
        m = len(l)
        for x in range(m):
            equations.append([0]*(m+1))
        j = [0]
        print equations
        print l
        var = [0]
        rng = len(l)
        h = l[:]
        h.sort()
        for x in range(rng):
            if ['i%s'%var[0]] in h:
                print 'no'
                print var[0]
                var[0] += 1
                n = h.pop(0)
                print h
            else:
                print 'yes'
                h[0][0] = 'i%s'%var[0]
                print var[0]
                var[0] +=1
                print h
        print l
        resist[0].current[0] = 0             
        nodelist1 = []
        for x in self.capclist:
            x.current[0] = 0
        for x in self.indrlist:
            x.type == "WIRE"
            x.value = 0
        print l         
        DCalgo.current_law(self.pos_dict, equations, self.last[-1], self.last[-1], nodelist1, j, m)
        print equations
        x = [[0]*(no[0]+1)]
        print j[0]
        for y in equations[:j[0]+1]:
            if y==x:
                print 'yes'
        
            print 'counter = %s'% l
            poslist = []
            looplast = [0]
            if nodelist != []:
                looplast[0] = nodelist[0]
            else:
                looplast[0] = self.last[-1]
            node_list = []
            flag = []
            print self.last
            stc = []
            #DCalgo.loop_law(self.pos_dict, equations, self.last, (0,0), j, no, pos_list, node_list, m, [])
            import loop_law_modified
            loop_law_modified.loop_law(pos_dict=self.pos_dict, pos_list = poslist, stack = stc, element_list = self.element_list, equation = equations, i=j, counter=m, nodelist= node_list, last =looplast[0])
            print equations
            #solve
            from ech import ToReducedRowEchelonForm
            ToReducedRowEchelonForm(equations)
            print equations
            for x in range(len(equations)):
                for y in range(len(equations[0])-1):
                    print x,y
                    print equations[x][y]
                    if equations[x][y] != 0:
                        print l[y]
                        l[y][0] = equations[x][-1]
                        print 'yes'
                        print l[y]
                    

            print l

            for x in self.element_list:
                if x.type == 'DCBATTERY':
                    print x.positive,
                print x.type,
                print x.value,
                print x.current,
                print x.direction
            
            voltm = Voltmeter()
            voltm.initial = resist[0].initial
            voltm.final = resist[0].final
            import vovoltmeter
            self.volt_dict[looplast[0]] = 0
            poslist = []
            node_list = []
            vovoltmeter.voltmeter(pos_dict = self.pos_dict, voltdict = self.volt_dict, pos_list = poslist, element_list = self.element_list, nodelist = node_list, last= looplast[0], curr = (0,0))           
            for x in self.pos_dict:
                if x in self.volt_dict:
                    print x, self.volt_dict[x]
                else:
                    print x,
                    print 'not present'
            print self.pos_dict
            print resist[0]
            if voltm.initial not in self.volt_dict:
                count = [0]
                while(count[0] != 1):
                    for x in self.pos_dict:
                        for y in self.pos_dict[x]:
                            if (y.initial == voltm.initial or y.final == voltm.initial) and y != resist[0]:
                                print y
                                if x in self.volt_dict:
                                    self.volt_dict[voltm.initial] = self.volt_dict[x]
                                    count[0] = 1
                                    break
                                else:
                                    if voltm.initial == y.initial:
                                        voltm.initial = y.final
                                    else:
                                        voltm.initial = y.final

            if voltm.final not in self.volt_dict:
                count = [0]
                while(count[0] != 1):
                    for x in self.pos_dict:
                        for y in self.pos_dict[x]:
                            if (y.initial == voltm.final or y.final == voltm.final) and y != resist[0]:
                                print y
                                
                                
                                if x in self.volt_dict:
                                    self.volt_dict[voltm.final] = self.volt_dict[x]
                                    count[0] = 1
                                    break
                                else:
                                    if voltm.final == y.initial:
                                        voltm.final = y.final
                                    else:
                                        voltm.final = y.final
                            
            voltage = self.volt_dict[voltm.final]-self.volt_dict[voltm.initial]
            self.StatusBar.SetStatusText(' Potential difference = ' + str(voltage))
            print ' Potential difference = ' + str(voltage)
            from copy import deepcopy
            res = deepcopy(resist[0])
            batr = Dcbattery(EMF = 10)
            batr.initial = resist[0].initial
            batr.final = resist[0].final
            batr.direction = (batr.initial, batr.final)

            for x in self.element_list:
                if x.type == 'DCBATTERY':
                    x.value = 0
                    
            print resist[0]
            print resist[0].initial
            print resist[0].final
                    
            indx1 = self.pos_dict[resist[0].initial].index(resist[0])
            indx2 = self.pos_dict[resist[0].final].index(resist[0])
            indx3 = self.element_list.index(resist[0])
            
            self.pos_dict[resist[0].initial].remove(resist[0])
            self.pos_dict[resist[0].final].remove(resist[0])
            self.element_list.remove(resist[0])

            self.pos_dict[resist[0].initial].insert(indx1,batr)
            self.pos_dict[resist[0].final].insert(indx2,batr)
            self.element_list.insert(indx3,batr)

            print self.pos_dict
            print self.element_list

            for x in self.element_list:
                x.current = [0]
                x.direction = (0,0)
                     
            no = [0]
            nodelist = []
            l = []
            flg = []
            for x in self.element_list:
                print x.type,
                print x.value,
                print x.current,
                print x.direction
            DCalgo.traverse(self.pos_dict, self.last[-1], curr = (0,0), prev = (0,0), i = no, node_list =  nodelist, count = l, flag = flg)
            for x in self.element_list:
                print x.type,
                print x.value,
                print x.current,
                print x.direction
            equations = []
            m = len(l)
            for x in range(m):
                equations.append([0]*(m+1))
            j = [0]
            print equations
            print l
            var = [0]
            rng = len(l)
            h = l[:]
            h.sort()
            for x in range(rng):
                if ['i%s'%var[0]] in h:
                    print 'no'
                    print var[0]
                    var[0] += 1
                    n = h.pop(0)
                    print h
                else:
                    print 'yes'
                    h[0][0] = 'i%s'%var[0]
                    print var[0]
                    var[0] +=1
                    print h
                         
            nodelist1 = []
            for x in self.capclist:
                x.current[0] = 0
            for x in self.indrlist:
                x.type == "WIRE"
                x.value = 0                
            DCalgo.current_law(self.pos_dict, equations, self.last[-1], self.last[-1], nodelist1, j, m)
            print equations
            x = [[0]*(no[0]+1)]
            print j[0]
            for y in equations[:j[0]+1]:
            
                if y==x:
                    print 'yes'
            
                print 'counter = %s'% l
                poslist = []
                looplast = [0]
                if nodelist != []:
                    looplast[0] = nodelist[0]
                else:
                    looplast[0] = self.last[-1]
                node_list = []
                flag = []
                print self.last
                stc =[]
                #DCalgo.loop_law(self.pos_dict, equations, self.last, (0,0), j, no, pos_list, node_list, m, [])
                import loop_law_modified
                loop_law_modified.loop_law(pos_dict=self.pos_dict, pos_list = poslist, stack = stc, element_list = self.element_list, equation = equations, i=j, counter=m, nodelist= node_list, last =looplast[0]) 
                print equations
                #solve
                from ech import ToReducedRowEchelonForm
                ToReducedRowEchelonForm(equations)
                print equations
                
                for x in range(len(equations)):
                    for y in range(len(equations[0])-1):
                        print x,y
                        print equations[x][y]
                        if equations[x][y] != 0:
                            print l[y]
                            l[y][0] = equations[x][-1]
                            print 'yes'
                            print l[y]
                    

            
                print l
                
                
                print 'batr.current',
                print batr.current
                resistance = 10.0/batr.current[0]
                print resistance
                self.makediagram(resistance,voltage)
                return
                #self.panel2.Bind(wx.EVT_BUTTON, self.ref, self.button10)       
                        

    def makediagram(self, r,l):
        print resist[0], resist[0].value
        print r, l
        self.OnRefresh()
        res = Resistor(value = resist[0].value, initial = resist[0].initial, final = resist[0].final)
        self.pos_l.append(res.initial)
        self.pos_l.append(res.final)
        self.StatusBar.SetStatusText(str([res.initial, res.final]))
        self.last.append(res.initial)
        dc.SetPen(wx.Pen("RED", 1))
        if res.initial[1] == res.final[1]:
            dc.DrawBitmap(bmp1, res.initial[0]+1, res.initial[1]-7, True)
        else:
            dc.DrawBitmap(bmp11, res.initial[0]-7, res.initial[1]+1, True)
        if res.initial in self.pos_dict:
            self.pos_dict[res.initial].append(res)
        else:
            self.pos_dict[res.initial] = [res]
        if res.final in self.pos_dict:
            self.pos_dict[res.final].append(res)
        else:
            self.pos_dict[res.final] = [res]
        self.element_list.append(res)
        batry = Dcbattery(countdc =1, EMF = l)
        last =[(0,0)]
        last1 = [(0,0)]
        if l > 0:
            print '1'
            batry.initial = res.initial
            last[0] = res.final
        else:
            print '2'
            batry.initial = res.final
            last[0] = res.initial
        print batry.initial
        if res.initial[0] == res.final[0]:
            print '1'
            batry.getfinalpos()
            dc.DrawBitmap(bmp2, batry.initial[0]+1, batry.initial[1]-9, True)
        else:
            print '2'
            batry.getfinalpos1()
            dc.DrawBitmap(bmp21, batry.initial[0]-9, batry.initial[1]+1, True)

        self.pos_l.append(batry.initial)
        self.pos_l.append(batry.final)
        self.StatusBar.SetStatusText(str([batry.initial, batry.final]))
        self.last.append(batry.initial)
        
        if batry.initial in self.pos_dict:
            self.pos_dict[batry.initial].append(batry)
        else:
            self.pos_dict[batry.initial] = [batry]
        if batry.final in self.pos_dict:
            self.pos_dict[batry.final].append(batry)
        else:
            self.pos_dict[batry.final] = [batry]
        self.element_list.append(batry)
        
        res1 = Resistor(value = r)
        if batry.initial[0] == batry.final[0]:
            if res.initial == batry.initial:
                res1.initial = batry.final
                res1.getfinalpos()
                last1[0] = res1.final
            else:
                res1.initial = (batry.final[0]-44, batry.final[1])
                res1.getfinalpos()
                last1[0] = res1.initial
            
            dc.DrawBitmap(bmp1, res1.initial[0]+1, res1.initial[1]-7, True)
        else:
            if res.initial == batry.initial:
                res1.initial = batry.final
                res1.getfinalpos1()
                last1[0] = res1.final
            else:
                res1.initial = (batry.final[0], batry.final[1]-44)
                res1.getfinalpos1()
                last1[0] = res1.initial
            
            dc.DrawBitmap(bmp11, res1.initial[0]-7, res1.initial[1]+1, True)
            
        self.pos_l.append(res1.initial)
        self.pos_l.append(res1.final)
        self.last.append(res1.initial)        
        if res1.initial in self.pos_dict:
            self.pos_dict[res1.initial].append(res1)
        else:
            self.pos_dict[res1.initial] = [res1]
        if res1.final in self.pos_dict:
            self.pos_dict[res1.final].append(res1)
        else:
            self.pos_dict[res1.final] = [res1]
        self.element_list.append(res1)

        wire = Wire(initial = last[0], final = last1[0])
        print last, last1
        dc.SetPen(wx.Pen("BLACK", 2))
        dc.DrawLine(last[0][0],last[0][1],last1[0][0], last1[0][1])

        self.pos_l.append(wire.initial)
        self.pos_l.append(wire.final)
        self.last.append(wire.initial)        
        if wire.initial in self.pos_dict:
            self.pos_dict[wire.initial].append(wire)
        else:
            self.pos_dict[wire.initial] = [wire]
        if wire.final in self.pos_dict:
            self.pos_dict[wire.final].append(wire)
        else:
            self.pos_dict[wire.final] = [wire]
        self.element_list.append(wire)
        
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
        self.panel2.Bind(wx.EVT_MOTION, self.default_motion)

        
        


    def ref(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        dlg = wx.MessageDialog(None, 'RESFRESH THE SCREEN','MessageDialog', wx.OK | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()

    def OnVoltmeter(self,event):
        ''' To input initialing and ending points '''
        self.panel2.Bind(wx.EVT_MOTION, None)
        self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltm1)
        self.StatusBar.SetStatusText(str((self.position)))
        self.panel2.Bind(wx.EVT_MOTION, self.select_motion)

    def select_element_motion(self, event):
        if event.GetX() < 150 :
            self.StatusBar.SetStatusText(' ')
            self.SetCursor(wx.StockCursor(wx.CURSOR_NO_ENTRY))
        else:
            pos_lx = [ l[0] for l in self.pos_l]
            pos_ly = [ l[1] for l in self.pos_l]
            if event.GetX() not in pos_lx and event.GetY() not in pos_ly:
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            else:
                y = []
                x = []
                for l in self.pos_l:
                    if event.GetX() == l[0]:
                        y.append(l[1])
               
                for l in self.pos_l:
                    if event.GetY() == l[1]:
                        x.append(l[0])
               
                if y != []:
                    if len(y) > 1:                          
                        maxmy = -1
                        minmy = 2000
                        for l in y:
                            if l > maxmy and l < event.GetY():
                                maxmy = l
                            if l < minmy and l > event.GetY():
                                minmy = l
                       
                        if maxmy < event.GetY() < minmy:
                            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
                            
                if x != []:
                    
                    if len(x) > 1:
                        maxmx = -1
                        minmx = 2000
                        for l in x:
                            if l > maxmx and l < event.GetX():
                                maxmx = l
                            if l < minmx and l > event.GetX():
                                minm = l
                      
                        if maxmx < event.GetX() < minmx:
                            self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))                            
            
        
    def On_Click_Voltm1(self,event):
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
        else:
            self.position = []
            self.position.append(event.GetX())
            self.position.append(event.GetY())
            self.voltm.initial = (self.position[0], self.position[1])
            #self.panel2.Bind(wx.EVT_LEFT_DOWN, self.select_element)
            self.StatusBar.SetStatusText(str((self.position)))
            self.panel2.Bind(wx.EVT_MOTION, self.voltmcursor)
            if event.GetPosition() not in self.pos_l:
                dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()
                
            
            else:
                self.panel2.Bind(wx.EVT_MOTION, self.voltmcursor)
                self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Voltm2)

    def voltmcursor(self,event):
        odc = wx.DCOverlay(self.panel2.overlay, dc)
        odc.Clear()        

        dc.SetPen(wx.Pen("RED", 1))
        dc.DrawLine(self.position[0],self.position[1],event.GetX(), event.GetY())
        if event.GetPosition() in self.pos_l:
            self.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))
        else:
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        self.StatusBar.SetStatusText(str((self.position, (event.GetX(),event.GetY()))))
        del odc
        
        
    def On_Click_Voltm2(self,event):
        self.panel2.Bind(wx.EVT_MOTION, None)
        odc = wx.DCOverlay(self.panel2.overlay, dc) 
        odc.Clear()
        del odc
        self.panel2.overlay.Reset() 
        if event.GetX() < 150 :
            dlg = wx.MessageDialog(None, 'RESTRICTED AREA','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
        else:
            if self.submitflag[0] == 0:
                self.StatusBar.SetStatusText('Potential Difference = 0')
                return
            self.panel2.Bind(wx.EVT_MOTION, None)
            self.position.append(event.GetX())
            self.position.append(event.GetY())
            self.voltm.final = (self.position[2],self.position[3])
            looplast = [self.last[-1]]
            self.volt_dict[looplast[0]] = 0
            import vovoltmeter
            poslist = []
            node_list = []
            vovoltmeter.voltmeter(pos_dict = self.pos_dict, voltdict = self.volt_dict, pos_list = poslist, element_list = self.element_list, nodelist = node_list, last= looplast[0], curr = (0,0))           
            l = self.volt_dict[self.voltm.final]-self.volt_dict[self.voltm.initial]
            self.StatusBar.SetStatusText(' Potential difference = ' + str(l))
            
            print ' Potential difference = ' + str(l)
            self.voltm = Voltmeter()
            self.position = []
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)

    
    def OnAmmeter(self, event):
        self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Ammeter)

    def On_Click_Ammeter(self, event):
        x = (event.GetX(), event.GetY())
        pos_lx = [ l[0] for l in self.pos_l]
        pos_ly = [ l[1] for l in self.pos_l]
        if event.GetX() not in pos_lx and event.GetY() not in pos_ly:
            print 'heres the trouble'
            dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
            self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Ammeter)
            return
        else:
            y = []
            x = []
            for l in self.pos_l:
                if event.GetX() == l[0]:
                    y.append(l[1])
            for l in self.pos_l:
                if event.GetY() == l[1]:
                    x.append(l[0])
            print y, x
            if y != []:
                if len(y) > 1:                          
                    maxm = -1
                    minm = 2000
                    for l in y:
                        if l > maxm and l < event.GetY():
                            maxm = l
                        if l < minm and l > event.GetY():
                            minm = l
                    for l in self.element_list:
                        if (event.GetX(),maxm) == l.initial and (event.GetX(), minm) == l.final:
                            self.StatusBar.SetStatusText(str([l.displaycurrent,l.direction]))
                            print l.current, l.displaycurrent
                                
                        elif (event.GetX(),maxm) == l.final and (event.GetX(), minm) == l.initial:
                            self.StatusBar.SetStatusText(str([l.displaycurrent,l.direction]))
                            print l.current, l.displaycurrent
                        
                                  
            if x != []:
                if len(x) >1:
                    maxm = -1
                    minm = 2000
                    for l in x:
                        if l > maxm and l < event.GetX():
                            maxm = l
                        if l < minm and l > event.GetX():
                            minm = l
                    for l in self.element_list:                        
                        if (maxm, event.GetY()) == l.initial and ( minm, event.GetY()) == l.final:
                            self.StatusBar.SetStatusText(str([l.displaycurrent,l.direction]))
                            print l.current, l.displaycurrent
                            
                        elif (maxm, event.GetY()) == l.final and (minm, event.GetY()) == l.initial:
                            self.StatusBar.SetStatusText(str([l.displaycurrent,l.direction]))
                            print l.current, l.displaycurrent
                            
                else:
                    print 'err'
                    dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.panel2.Bind(wx.EVT_MOTION, self.select_element_motion)
                    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.On_Click_Ammeter)
                    return

        
        
        '''
        if x in self.pos_l:
            if len(self.pos_dict[x]) < 3:
                if self.soln_current != []:
                    y = str(self.soln_current[int(self.pos_dict[x][0].current[0][1:])])
                    self.StatusBar.SetStatusText(str(y))
                else:
                    self.StatusBar.SetStatusText(str(self.pos_dict[x][0].current[0]))
                    
        '''

    def default(self, event):
        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        dlg = wx.MessageDialog(None, 'PLEASE SELECT AN ELEMENT FIRST','MessageDialog', wx.OK | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()

    def select_motion(self, event = None):
        self.StatusBar.SetStatusText(str(event.GetPosition()))
        if event.GetX() <150:
            self.SetCursor(wx.StockCursor(wx.CURSOR_NO_ENTRY))
            self.StatusBar.SetStatusText(' ')
            
        else:
            odc = wx.DCOverlay(self.panel2.overlay, dc)
            odc.Clear()
            dc.SetPen(wx.Pen("RED", 1))
            maxmx = [-1]
            minmx = [2000]
            maxmy = [-1]
            minmy = [2000]
            pointxlist = [ x[0] for x in pointlist]
            pointylist = [ x[1] for x in pointlist]
            if event.GetX() in pointxlist:
                for x in pointylist:                    
                    if x > maxmx[0] and x < event.GetY():
                        maxmx[0] = x
                        self.maxmy[0] = maxmx[0]
                    if x < minmx[0] and x > event.GetY():
                        minmx[0] = x
                        
                    #print maxmx, minmx
                dc.DrawLine(event.GetX(),maxmx[0], event.GetX(), minmx[0])
            
                            
            elif event.GetY() in pointylist:
                for x in pointxlist:
                    if x > maxmy[0] and x < event.GetX():
                        maxmy[0] = x
                        self.maxmx[0] = maxmy[0]
                    if x < minmy[0] and x > event.GetX():
                        minmy[0] = x
                        
                    #print maxmy, minmy
                dc.DrawLine(maxmy[0],event.GetY(), minmy[0], event.GetY())

            else:
                #del odc
                self.maxmx[0] = -1
                self.maxmy[0] = -1
            del odc
                
            if event.GetPosition() in self.pos_l:
                
                self.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))
            else:
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            
    
    def default_motion(self, event = None):
        curr_pos = event.GetPosition()
        
        if event.GetX() < 150:
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            self.StatusBar.SetStatusText(' ')
        else:
            self.StatusBar.SetStatusText(str((curr_pos)))
            if event.GetPosition() in pointlist:
                self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            else:
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        pos_lx = [ l[0] for l in self.pos_l]
        pos_ly = [ l[1] for l in self.pos_l]
        if 0:
            pass
        else:
            y = []
            x = []
            for l in self.pos_l:
                if event.GetX() == l[0]:
                    y.append(l[1])
            
            for l in self.pos_l:
                if event.GetY() == l[1]:
                    x.append(l[0])
              
            if y != []:
                if len(y) > 1:                          
                    maxmy = [-1]
                    minmy = [2000]
                    
                    for l in y:
                        if l > maxmy[0] and l < event.GetY():
                            maxmy[0] = l                            
                        if l < minmy[0] and l > event.GetY():
                            minmy[0] = l                            
                    if maxmy[0] < event.GetY() < minmy[0]:
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        inifinele = [((x.initial, x.final),(x.type,x.value)) for x in self.element_list]
                        inifin = [ x[0] for x in inifinele]                                               
                        
                        if((event.GetX(),maxmy[0]), (event.GetX(),minmy[0]))in inifin:
                            indx = inifin.index(((event.GetX(),maxmy[0]),(event.GetX(),minmy[0])))                
                            self.StatusBar.SetStatusText(str(inifinele[indx][1]))
                        elif ((event.GetX(),minmy[0]), (event.GetX(),maxmy[0])) in inifin:
                            indx = inifin.index(((event.GetX(),minmy[0]),(event.GetX(),maxmy[0])))
                            self.StatusBar.SetStatusText(str(inifinele[indx][1]))
                            
                        else:
                            self.StatusBar.SetStatusText(str(event.GetPosition()))
                        
                                                      
                        
            elif x != []:
                    
                if len(x) > 1:
                    maxmx = [-1]
                    
                    minmx = [2000]
                    for l in x:
                        if l > maxmx[0] and l < event.GetX():
                            maxmx[0] = l
                        if l < minmx[0] and l > event.GetX():
                            minmx[0] = l
                   
                    if maxmx[0] < event.GetX() < minmx[0]:                       
                        self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
                        inifinele = [((x.initial, x.final),(x.type,x.value)) for x in self.element_list]
                        inifin = [ x[0] for x in inifinele]
                        
                        if((maxmx[0],event.GetY()), (minmx[0], event.GetY()))in inifin:
                           
                            indx = inifin.index(((maxmx[0],event.GetY()),(minmx[0], event.GetY())))                            
                            self.StatusBar.SetStatusText(str(inifinele[indx][1]))
                        elif ((minmx[0],event.GetY()), (maxmx[0], event.GetY())) in inifin:
                            indx = inifin.index(((minmx[0],event.GetY()),(maxmx[0], event.GetY())))
                            self.StatusBar.SetStatusText(str(inifinele[indx][1]))
                            
                        else:
                            self.StatusBar.SetStatusText(str(event.GetPosition()))
                        
                             


        
class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Bulb Input', size=(300,150))
        panel = wx.Panel(self, -1) 
        Label1 = wx.StaticText(panel, -1, "Power")
        self.Text1 = wx.TextCtrl(panel, -1, size=(175, -1))
        self.Text1.SetInsertionPoint(0)
        Label2 = wx.StaticText(panel, -1, "Voltage")
        self.Text2 = wx.TextCtrl(panel, -1, size=(175, -1))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([Label1, self.Text1, Label2, self.Text2])
        panel.SetSizer(sizer)
        runBtn = wx.Button(panel, -1, pos = (90,60), label ='OK', )
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, runBtn)
        cancelbtn = wx.Button(panel, -1, pos = (170,60), label ='Cancel', )
        self.Bind(wx.EVT_BUTTON, self.OnSubmit1, cancelbtn)

    def OnSubmit(self,evt):
        x= self.Text1.GetValue()
        if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    b.voltage = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.Close()
                    return
        x = self.Text2.GetValue()
        if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    b.power = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.Close()
                    return
        
        b.access = "YES"
        self.Close()

    def OnSubmit1(self, evt):
        self.Close()

class TextFrame1(wx.Frame):
    def __init__(self):
        ac = Acbattery()
        wx.Frame.__init__(self, None, -1, 'Voltage Input', size=(300,150))
        panel = wx.Panel(self, -1) 
        Label1 = wx.StaticText(panel, -1, 'Value')
        self.Text1 = wx.TextCtrl(panel, -1, size=(175, -1))
        self.Text1.SetInsertionPoint(0)
        Label2 = wx.StaticText(panel, -1, "Phase")
        self.Text2 = wx.TextCtrl(panel, -1, size=(175, -1))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([Label1, self.Text1, Label2, self.Text2])
        panel.SetSizer(sizer)
        runBtn = wx.Button(panel, -1, pos = (90,60), label ='OK', )
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, runBtn)
        cancelbtn = wx.Button(panel, -1, pos = (170,60), label ='Cancel', )
        self.Bind(wx.EVT_BUTTON, self.OnSubmit1, cancelbtn)

    def OnSubmit(self,evt):
        x= self.Text1.GetValue()
        if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    ac.value = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.Close()
                    return
        x= self.Text2.GetValue()
        if x.find('.') == x.rfind('.'):
                y = x.replace('.','')
                if y.isdigit():                    
                    ac.phase = float(x)
                else:
                    dlg = wx.MessageDialog(None, 'VALUE NOT SUPPORTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                    result = dlg.ShowModal()
                    dlg.Destroy()
                    self.Close()
                    
                    return
        
        ac.access = "YES"
        self.Close()

    def OnSubmit1(self, evt):
        self.Close()
        



class App(wx.App):
    def OnInit(self):
        #position= []
        
        self.frame = Frame(parent=None, title='Electric Circuit Simulation', style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER |wx.MAXIMIZE_BOX |wx.MINIMIZE_BOX), size= (700,700))
        self.frame.OnInit()
        global dc
        dc= wx.ClientDC(self.frame.panel2)
        self.frame.Show()    
        global pointx
        global pointy
        pointx = 200
        global pointlist
        pointlist = []
        while pointx < 950:
            pointy = 20
            while pointy < 650:
                pointlist.append((pointx,pointy))
                pointy += 44
                
            pointx += 44
            
        
        for x in pointlist:
            dc.DrawLine(x[0] - 3, x[1], x[0] + 3, x[1])
            dc.DrawLine(x[0], x[1] - 3, x[0], x[1] + 3)
        self.SetTopWindow(self.frame)
        
        
        global b
        b = Bulb()
        global ac
        ac = Acbattery()
        image_file1 = 'resistor.bmp'
        image_file11 = 'resistor1.bmp'
        image_file2 = 'battery.bmp'
        image_file21 = 'battery1.bmp'
        image_file22 = 'battery2.bmp'
        image_file23 = 'battery3.bmp'
        image_file3 = 'battery_ac.bmp'
        image_file31 = 'battery_ac1.bmp'
        image_file4 = 'bulb.bmp'
        image_file5 = 'voltmeter.bmp'
        image_file6 = 'ammeter.bmp'
        image_file7 = 'capacitor.bmp'
        image_file8 = 'inductor.bmp'
        
        global bmp1
        global bmp11
        global bmp2
        global bmp21
        global bmp22
        global bmp23
        global bmp3
        global bmp31
        global bmp4
        global bmp5
        global bmp6
        global bmp7
        global bmp8
        global position
        global resist
        resist = [0]
        bmp1 = wx.Bitmap(image_file1)
        bmp11 = wx.Bitmap(image_file11)
        bmp2 = wx.Bitmap(image_file2)
        bmp21 = wx.Bitmap(image_file21)
        bmp22 = wx.Bitmap(image_file22)
        bmp23 = wx.Bitmap(image_file23)
        bmp3 = wx.Bitmap(image_file3)
        bmp31 = wx.Bitmap(image_file31)
        bmp4 = wx.Bitmap(image_file4)
        bmp5 = wx.Bitmap(image_file5)
        bmp6 = wx.Bitmap(image_file6)
        bmp7 = wx.Bitmap(image_file7)
        bmp8 = wx.Bitmap(image_file8)
        return True



if __name__ == '__main__':
    app = App()
    app.MainLoop()
