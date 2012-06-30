def voltmeter(pos_dict, voltdict, pos_list, element_list, nodelist, last, curr = (0,0), prev = (0,0)):

    def on_wrong_entry(l,c,p):
        print 'current = 0 or element encountered twice'
        
        
        
        print 'break occured ',
        print c[0]
        count = [0]
        for x in pos_dict:
            if x not in voltdict:
                count[0] = 1
                break
        
        if count == [0]:
            return
        if pos_list == []:
            print 'bye'
            return
        t = pos_list.pop()
        print 'pos_list',
        print pos_list
        l[0] = t[0]
        c[0] = t[1]
        p[0] = t[0]
        print 'new last, new curr',
        print l[0], c[0]
        for x in element_list:
            print p[0], c[0]
            print x.direction
            if x.direction == (p[0], c[0]):
                print '1'                   
                if x.current == [0]:
                    print '2'
                    print l,c,p
                    on_wrong_entry(l,c,p)
                    print l,c,p
                elif x.type == 'DCBATTERY':
                    print '3'
                    if p[0] == x.positive:
                        voltdict[c[0]] = voltdict[p[0]] - x.value
                    else:
                        voltdict[c[0]] = voltdict[p[0]] + x.value
                elif x.type == 'ACBATTERY':
                    print '4'
                    voltdict[c[0]] = voltdict[p[0]] + x.value           
                elif x.current != [0]:
                    print '5'
                    voltdict[c[0]] = voltdict[p[0]] - x.current[0]*x.value

                break
                
            elif x.direction == (c[0], p[0]):
                print '6'
                if x.current == [0]:
                    print '7'
                    print l,c,p
                    on_wrong_entry(l,c,p)
                    print l,c,p
                elif x.type == 'DCBATTERY':
                    print '8'
                    if c[0] == x.positive:
                        voltdict[c[0]] = voltdict[p[0]] - x.value
                    else:
                        voltdict[c[0]] = voltdict[p[0]] + x.value
                elif x.type == 'ACBATTERY':
                    print '9'
                    voltdict[c[0]] = voltdict[p[0]] - x.value 

                elif x.current != [0]:
                    print '10'
                    voltdict[c[0]] = voltdict[p[0]] + x.current[0]*x.value
                    
                break
        if c[0] in voltdict:
            
            print 'potential at',
            print c[0],
            print voltdict[c[0]]

    print 'entered new :',
    print ' l,c,p',
    print last,curr,prev
    count = [0]
    for x in pos_dict:
        if x not in voltdict:
            count[0] = 1
            break
        
    if count == [0]:
        return
        
    if last == 0:
        return
    
    if last == curr:
        if pos_list == []:
            return
        t = pos_list.pop()
        
        last = t[0]
        curr = t[1]
        print t
        
        
        flg = 1
        
        prev = last
        for x in element_list:
            if x.direction == (last, curr):
                if x.current == [0]:
                    l = [0]
                    c = [curr]
                    p = [0]
                    on_wrong_entry(l,c,p)
                    last = l[0]
                    curr = c[0]
                    prev = p[0]
                elif x.type == "DCBATTERY":
                    if x.direction[0] == x.positive:
                        voltdict[curr] = voltdict[prev] - x.value
                    else:
                        voltdict[curr] = voltdict[prev] + x.value
                elif x.type == 'ACBATTERY':
                        voltdict[curr] = voltdict[prev] + x.value 
                else:
                    voltdict[curr] = voltdict[prev] - x.current[0]*x.value
            elif x.direction == (curr, prev):
                if x.current == [0]:
                    l = [0]
                    c = [curr]
                    p = [0]
                    on_wrong_entry(l,c,p)
                    last = l[0]
                    curr = c[0]
                    prev = p[0]
                elif x.type == "DCBATTERY":
                    if x.direction[0] == x.positive:
                        voltdict[curr] = voltdict[prev] - x.value
                    else:
                        voltdict[curr] = voltdict[prev] + x.value
                elif x.type == 'ACBATTERY':
                        voltdict[curr] = voltdict[prev] - x.value 
                else:
                    voltdict[curr] = voltdict[prev] + x.current[0]*x.value
        if curr in voltdict:
            print 'potential at',
            print curr,
            print voltdict[curr]

    else:
        if curr == (0,0):
            print 'curr initialized to last'
            curr = last
        
        
        if pos_dict[curr][-1] != pos_dict[curr][1]:
            print 'Loop encountered'

            if prev != (0,0):
                t = []
                for x in pos_dict[curr]:
                    if x.initial==curr:
                        t.append(x.final)
                    else:
                        t.append(x.initial)
                temp_prev = [0]
                if prev[0] == curr[0] and prev[1] < curr[1]:
                    temp_prev[0] = prev
                    count = 0
                    for x in t:
                        if x[0] < curr[0] and x[1] == curr[1]:
                            count = 1
                            prev = curr
                            curr = x
                            break
                    if count == 0:
                        for x in t:
                            if x[0] == curr[0] and x[1] > curr[1]:
                                prev = curr
                                curr = x
                    
                if prev[0] > curr[0] and prev[1] == curr[1]:
                    temp_prev[0] = prev
                    count = 0
                    for x in t:
                        if x[0] == curr[0] and x[1] < curr[1]:
                            count = 1
                            prev = curr
                            curr = x
                            break
                    if count == 0:
                        for x in t:
                            if x[0] < curr[0] and x[1] == curr[1]:
                                prev = curr
                                curr = x
                if prev[0] == curr[0] and prev[1] > curr[1]:
                    temp_prev[0] = prev
                    count = 0
                    for x in t:
                        if x[0] > curr[0] and x[1] == curr[1]:
                            count = 1
                            prev = curr
                            curr = x
                            break
                    if count == 0:
                        for x in t:
                            if x[0] == curr[0] and x[1] < curr[1]:
                                prev = curr
                                curr = x

                if prev[0] < curr[0] and prev[1] == curr[1]:
                    temp_prev[0] = prev
                    count = 0
                    for x in t:
                        if x[0] == curr[0] and x[1] > curr[1]:
                            count = 1
                            prev = curr
                            curr = x
                            break
                    if count == 0:
                        for x in t:
                            if x[0] > curr[0] and x[1] == curr[1]:
                                prev = curr
                                curr = x
                                    
                if prev not in nodelist:
                    nodelist.append(prev)
                    print "nodelist",
                    print nodelist
                    for x in t:
                        if x != temp_prev[0] and x != curr:
                            pos_list.append((prev, x))
                print 'poslist = ',
                print pos_list
                for x in element_list:
                    print x.direction, x.current
                    print prev, curr
                    if x.direction == (prev, curr):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        elif x.type == "DCBATTERY":
                            if prev == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] + x.value 
                        else:
                            voltdict[curr] = voltdict[prev] - x.current[0]*x.value
                    elif x.direction == (curr, prev):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        elif x.type == "DCBATTERY":
                            if curr == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] - x.value 
                        else:
                            voltdict[curr] = voltdict[prev] + x.current[0]*x.value

                if curr in voltdict:
                    print 'potential at',
                    print curr,
                    print voltdict[curr]    
                        

            else:
                nodelist.append(curr)
                t = []
                for x in pos_dict[curr]:
                    if x.initial==curr:
                        t.append(x.final)
                    else:
                        t.append(x.initial)
                curr = t[0]
                prev = last
                for x in t[1:]:
                    pos_list.append((prev,x))
                for x in element_list:
                    if x.direction == (prev, curr):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        if x.type == "DCBATTERY":
                            if prev == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] + x.value 
                        else:
                            voltdict[curr] = voltdict[prev] - x.current[0]*x.value
                    elif x.direction == (curr, prev):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        if x.type == "DCBATTERY":
                            if curr == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] + x.value 
                        else:
                            voltdict[curr] = voltdict[prev] - x.current[0]*x.value
                if curr in voltdict:
                    print 'potential at',
                    print curr,
                    print voltdict[curr]        
                        

        else:
            print 'no loop encounterd'
            t = []
            for x in pos_dict[curr]:
                if x.initial==curr:
                    t.append(x.final)
                else:
                    t.append(x.initial)

            if prev == (0,0):
                print 'just entered into loop'
                curr = t[0]
                prev = last
                pos_list.append((prev,t[1]))
                print 'going to, append %s'%t
                
                for x in element_list:
                    if x.direction == (prev, curr):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        elif x.type == "DCBATTERY":
                            if prev == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] + x.value 
                        else:
                            voltdict[curr] = voltdict[prev] - x.current[0]*x.value
                    elif x.direction == (curr, prev):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c, p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        elif x.type == "DCBATTERY":
                            if curr == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] - x.value 
                        else:
                            voltdict[curr] = voltdict[prev] + x.current[0]*x.value
                if curr in voltdict:
                    print 'potential at',
                    print curr,
                    print voltdict[curr]        
                        

            elif t[0][0] != t[1][0] and t[0][1] != t[1][1]:
                print 'corner encountered'
                temp_prev = prev
                if pos_dict[curr][0].initial == prev or pos_dict[curr][0].final == prev:
                    prev = curr
                    if curr == pos_dict[curr][1].initial:
                        curr = pos_dict[curr][1].final
                    else:
                        curr = pos_dict[curr][1].initial
                else:
                    prev = curr
                    if curr == pos_dict[curr][0].initial:
                        curr = pos_dict[curr][0].final
                    else:
                        curr = pos_dict[curr][0].initial
                '''
                if temp_prev[0] == prev[0] and temp_prev[1] < prev[1] and curr[0] > prev[0]:
                    #wrong
                    on_wrong_entry()

                elif temp_prev[0] > prev[0] and temp_prev[1] == prev[1] and curr[1] > prev[1]:
                    #wrong
                    on_wrong_entry()

                elif temp_prev[0] == prev[0] and temp_prev[1] > prev[1] and curr[0] < prev[0]:
                    #wrong
                    on_wrong_entry()

                elif temp_prev[0] < prev[0] and temp_prev[1] == prev[1] and curr[1] < prev[1]:
                    #wrong
                    on_wrong_entry()
                '''
                if 0: pass
                else:
                    print 'everything is normal at corner'
                    for x in element_list:
                        if x.direction == (prev, curr):
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == "DCBATTERY":
                                if prev == x.positive:
                                    voltdict[curr] = voltdict[prev] - x.value
                                else:
                                    voltdict[curr] = voltdict[prev] + x.value
                            elif x.type == 'ACBATTERY':
                                voltdict[curr] = voltdict[prev] + x.value 
                            else:
                                voltdict[curr] = voltdict[prev] - x.current[0]*x.value
                        elif x.direction == (curr, prev):
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                iter = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == "DCBATTERY":
                                if curr == x.positive:
                                    voltdict[curr] = voltdict[prev] - x.value
                                else:
                                    voltdict[curr] = voltdict[prev] + x.value
                            elif x.type == 'ACBATTERY':
                                voltdict[curr] = voltdict[prev] - x.value 
                            else:
                                voltdict[curr] = voltdict[prev] + x.current[0]*x.value
                    if curr in voltdict:
                        print 'potential at',
                        print curr,
                        print voltdict[curr]            
                            

           
            else:
                
                if pos_dict[curr][0].initial == prev or pos_dict[curr][0].final == prev:
                    prev = curr
                    if curr == pos_dict[curr][1].initial:
                        curr = pos_dict[curr][1].final
                    else:
                        curr = pos_dict[curr][1].initial
                else:
                    prev = curr
                    if curr == pos_dict[curr][0].initial:
                        curr = pos_dict[curr][0].final
                    else:
                        curr = pos_dict[curr][0].initial
                for x in element_list:
                    if x.direction == (prev, curr):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        elif x.type == "DCBATTERY":
                            if prev == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] + x.value 
                        else:
                            voltdict[curr] = voltdict[prev] - x.current[0]*x.value
                    elif x.direction == (curr, prev):
                        if x.current == [0]:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                        elif x.type == "DCBATTERY":
                            if curr == x.positive:
                                voltdict[curr] = voltdict[prev] - x.value
                            else:
                                voltdict[curr] = voltdict[prev] + x.value
                        elif x.type == 'ACBATTERY':
                            voltdict[curr] = voltdict[prev] - x.value 
                        else:
                            voltdict[curr] = voltdict[prev] + x.current[0]*x.value
                if curr in voltdict:
                    print 'potential at',
                    print curr,
                    print voltdict[curr]        
                                    
    print 'calling next loop'
    voltmeter(pos_dict, voltdict, pos_list, element_list, nodelist, last, curr, prev)
            