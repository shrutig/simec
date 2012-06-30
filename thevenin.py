from copy import deepcopy


    

def select_element_thev(self,event):
    resist[0] = 0
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
            if y[-1] != y[0]:                          
                maxm = -1
                minm = 2000
                for l in y:
                    if l > maxm and l < event.GetY():
                        maxm = l
                    if l < minm and l > event.GetY():
                        minm = l
                for l in self.element_list:
                    resist[0] = l
                    if (event.GetX(),maxm) == l.initial and (event.GetX(), minm) == l.final:
                        dc.SetPen(wx.Pen("RED", 1))
                        dc.DrawLine(event.GetX()-3, l.initial[1], event.GetX()+3, l.initial[1])
                        dc.DrawLine(event.GetX()-3, l.final[1], event.GetX()+3, l.final[1])
                            
                                
                    elif (event.GetX(),maxm) == l.final and (event.GetX(), minm) == l.initial:
                        dc.DrawLine(l.initial[0]-3, l.initial[1], l.initial[0]+3, l.initial[1])
                        dc.DrawLine(l.final[0]-3, l.final[1], l.final[0]+3, l.final[1])
                    
                                  
        if x != []:
            if x[-1] != x[0]:
                maxm = -1
                minm = 2000
                for l in x:
                    if l > maxm and l < event.GetX():
                        maxm = l
                    if l < minm and l > event.GetX():
                        minm = l
                for l in self.element_list:
                    resist[0] = l
                    if (maxm, event.GetY()) == l.initial and ( minm, event.GetY()) == l.final:
                        dc.SetPen(wx.Pen("RED", 1))
                        dc.DrawLine(l.initial[0], l.initial[1]-3, l.initial[0], l.initial[1]+3)
                        dc.DrawLine(l.final[0], l.final[1]-3, l.final[0], l.final[1]+3)
                                
                            
                    elif (maxm, event.GetY()) == l.final and (minm, event.GetY()) == l.initial:
                        dc.DrawLine(event.GetX()-3, l.initial[1], event.GetX()+3, l.initial[1])
                        dc.DrawLine(event.GetX()-3, l.final[1], event.GetX()+3, l.final[1])
                
                            
            else:
                dlg = wx.MessageDialog(None, 'NO ELEMENT SELECTED','MessageDialog', wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()

        
    import DCalgo
    no = [0]
    nodelist = []
    l = []
    flg = []
    DCalgo.traverse(self.pos_dict, self.last[-1], curr = (0,0), prev = (0,0), i = no, node_list =  nodelist, count = l, flag = flg)
    resist[0].current[0] = 0
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
        #DCalgo.loop_law(self.pos_dict, equations, self.last, (0,0), j, no, pos_list, node_list, m, [])
        import loop_law_modified
        loop_law_modified.loop_law(pos_dict=self.pos_dict, pos_list = poslist, element_list = self.element_list, equation = equations, i=j, counter=m, nodelist= node_list, last =looplast[0])
        print equations
        voltm = Voltmeter()
        voltm.initial = resist[0].initial
        voltm.final = resist[0].final
        import vovoltmeter
        poslist = []
        node_list = []
        vovoltmeter.voltmeter(pos_dict = self.pos_dict, voltdict = self.volt_dict, pos_list = poslist, element_list = self.element_list, nodelist = node_list, last= looplast[0], curr = (0,0))           
        l = self.volt_dict[self.voltm.final]-self.volt_dict[self.voltm.initial]
        self.StatusBar.SetStatusText(' Potential difference = ' + str(l))
            
        print ' Potential difference = ' + str(l)

        res = resist[0].deepcopy()
        batr = Dcbattery(EMF = 10)

        self.pos_dict[resist[0].initial].remove(resist[0])
        self.pos_dict[resist[0].final].remove(resist[0])
        self.element_list.remove(resist[0])

        self.pos_dict[resist[0].initial].insert(batr)
        self.pos_dict[resist[0].final].insert(batr)
        self.element_list.insert(batr)
            
            

        for x in element_list:
            if x.type == 'DCBATTERY':
                x.value = 0            
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
            #DCalgo.loop_law(self.pos_dict, equations, self.last, (0,0), j, no, pos_list, node_list, m, [])
            import loop_law_modified
            loop_law_modified.loop_law(pos_dict=self.pos_dict, pos_list = poslist, element_list = self.element_list, equation = equations, i=j, counter=m, nodelist= node_list, last =looplast[0]) 
            print equations
            from scipy import mat
            from scipy import linalg
            b = [ row[-1] for row in equations]    
            B = mat(b)
            a = [ row[:-1] for row in equations]    
            A = mat(a)
            print A
            print B
            C = linalg.solve(A,B)
            self.soln_current = C
            print C
            print l
            i = [0]
            for x in l:
                l[i[0]][0] = C[i[0]][0]
                i[0] +=1
            print l
            self.StatusBar.SetStatusText(str(C))
            self.panel2.Bind(wx.EVT_BUTTON, None, self.button11)
            print 'batr.current',
            print batr.current
            resistance = 10.0/batr.current
            print resistance

            
    self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
    self.panel2.Bind(wx.EVT_MOTION, self.default_motion)
    self.panel2.Bind(wx.EVT_LEFT_DOWN, self.default)
            
            
                
                
        

    