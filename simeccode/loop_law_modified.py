import copy
def loop_law(pos_dict, pos_list, stack, element_list, equation, i, counter, nodelist, last, curr = (0,0), prev = (0,0)):

    def on_wrong_entry(l,c,p):
        print 'current = 0 or element encountered twice'
        equation[i[0]] = [0]*(counter+1)
        lenstc = len(stack)
        for x in range(lenstc):
            stack.pop()
        print 'stack ',
        print stack
        print 'break occured ',
        print c[0]
        if pos_list == []:
            return
        t = pos_list.pop()
        print 'pos_list',
        print pos_list
        l[0] = t[0]
        c[0] = t[1]
        p[0] = l[0]
        print 'new last, new curr',
        print l[0], c[0]
        for x in element_list:
            if x.direction == (p[0], c[0]):
                if i[0] < counter:
                    print 'element added to equation'
                    print x.type
                    if x.current == [0]:
                        on_wrong_entry(l,c,p)                        
                    elif x.type == 'DCBATTERY':
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        else:
                            equation[i[0]][-1] -= x.value
                    elif x.current != [0]:
                        equation[i[0]][int(x.current[0][1:])] += x.value
                    print 'equation',
                    print equation
                    break
                else:
                    print 'maximum equations reached'
                    return
            elif x.direction == (c[0], p[0]):
                if i[0] < counter:
                    print 'element added to equation, with opposite current'
                    print x.type
                    if x.current == [0]:
                        on_wrong_entry(l,c,p)
                    elif x.type == 'DCBATTERY':
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        else:
                            equation[i[0]][-1] -= x.value
                    elif x.current != [0]:
                        equation[i[0]][int(x.current[0][1:])] -= x.value
                    print 'equation',
                    print equation
                    break
                else:
                    print 'maximum equations reached'
                    return
    if last == 0 or prev == 0:
        return
    print 'last =',
    print last   
    if i[0]>=counter:
        return
    
    elif last == curr:
        lenstc = len(stack)
        for l in range(lenstc):
            stack.pop()
        print 'stack ',
        print stack
        print 'last = curr'
        if pos_list == []:
            return
        t = pos_list.pop()
        print 'pos_list',
        print pos_list
        last = t[0]
        curr = t[1]
        print 'last,curr',
        print t
        
        from ech import ToReducedRowEchelonForm
        eqn = copy.deepcopy(equation)
        ToReducedRowEchelonForm(eqn)
        
        if eqn[i[0]] != [0]*(counter+1):
            print 'yes'
            i[0] += 1
        else:
            equation[i[0]] = [0]*(counter+1)
            
        prev = last
        for x in element_list:
            if x.direction == (last, curr):
                if i[0] < counter:
                    print 'element added to equation',
                    print x.type
                    if x.current == [0]:
                        l = [0]
                        c = [curr]
                        p = [0]
                        on_wrong_entry(l,c,p)
                        last = l[0]
                        curr = c[0]
                        prev = p[0]
                    elif x.type == 'DCBATTERY':
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        else:
                            equation[i[0]][-1] -= x.value
                    elif x.current != [0]:
                        equation[i[0]][int(x.current[0][1:])] += x.value
                    print 'equation',
                    print equation
                    break                    
                else:
                    print 'maximum equations reached'
                    return
            elif x.direction == (curr, last):
                if i[0] < counter:
                    print 'element added to equation, with opposite current'
                    print x.type
                    if x.current == [0]:
                        l = [0]
                        c = [curr]
                        p = [0]
                        on_wrong_entry(l,c,p)
                        last = l[0]
                        curr = c[0]
                        prev = p[0]
                    elif x.type == 'DCBATTERY':
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        elif x.current != [0]:
                            equation[i[0]][-1] -= x.value
                    else:                        
                        equation[i[0]][int(x.current[0][1:])] -= x.value
                    print 'equation',
                    print equation
                    break
                else:
                    print 'maximum equations reached'
                    return
        
        
    
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
                print 'check node',
                print prev
                print 'not to be added previous element and elemnt to be traversed next',
                print temp_prev,
                print curr
                if prev not in nodelist:
                    nodelist.append(prev)
                    print "nodelist",
                    print nodelist
                    for x in t:
                        if x != temp_prev[0] and x != curr:
                            pos_list.append((prev, x))
                            print 'pos_list',
                            print pos_list

                
                    

                for x in element_list:
                    if x.direction == (prev, curr):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                            print 'element added to equation'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                    elif x.direction == (curr, prev):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)                        
                            print 'element added to equation, with opposite current'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                

            else:
                t = []
                for x in pos_dict[curr]:
                    if x.initial==curr:
                        t.append(x.final)
                    else:
                        t.append(x.initial)
                nodelist.append(curr)
                curr = t[0]
                prev = last
                print 'going to ',
                print curr
                print 'nodelist',
                print nodelist
                for x in t[1:]:
                    pos_list.append((prev,x))
                    print 'pos_list',
                    print pos_list
                for x in element_list:
                    if x.direction == (prev, curr):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                        
                            print 'element added to equation'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                    elif x.direction == (curr, prev):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                        
                            print 'element added to equation, with opposite current'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                print equation

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
                print 'pos_list',
                print pos_list
                print 'going to, append %s'%t
                
                for x in element_list:
                    if x.direction == (prev, curr):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                        
                            print 'element added to equation'
                            print x.type
                            print (prev, curr)
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                    elif x.direction == (curr, prev):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                        
                            print 'element added to equation, with opposite current'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                
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
                l = [0]
                c = [curr]
                p = [0]
                if temp_prev[0] == prev[0] and temp_prev[1] < prev[1] and curr[0] > prev[0]:
                    #wrong                    
                    on_wrong_entry(l,c,p)
                    last = l[0]
                    curr = c[0]
                    prev = p[0]


                elif temp_prev[0] > prev[0] and temp_prev[1] == prev[1] and curr[1] > prev[1]:
                    #wrong                    
                    on_wrong_entry(l,c,p)
                    last = l[0]
                    curr = c[0]
                    prev = p[0]


                elif temp_prev[0] == prev[0] and temp_prev[1] > prev[1] and curr[0] < prev[0]:
                    #wrong                    
                    on_wrong_entry(l,c,p)
                    last = l[0]
                    curr = c[0]
                    prev = p[0]


                elif temp_prev[0] < prev[0] and temp_prev[1] == prev[1] and curr[1] < prev[1]:
                    #wrong                    
                    on_wrong_entry(l,c,p)
                    last = l[0]
                    curr = c[0]
                    prev = p[0]

                '''
                if 0:
                    pass
                else:
                    print 'everything is normal at corner'
                    for x in element_list:
                        if x.direction == (prev, curr):
                            if x in stack:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            
                            elif i[0] < counter:
                                stack.append(x)
                            
                                print 'element added to equation'
                                print x.type
                                if x.current == [0]:
                                    l = [0]
                                    c = [curr]
                                    p = [0]
                                    on_wrong_entry(l,c,p)
                                    last = l[0]
                                    curr = c[0]
                                    prev = p[0]
                                if x.type == 'DCBATTERY':
                                    if x.direction[0] == x.positive:
                                        equation[i[0]][-1] += x.value
                                    else:
                                        equation[i[0]][-1] -= x.value
                                elif x.current != [0]:
                                    equation[i[0]][int(x.current[0][1:])] += x.value
                                print 'equation',
                                print equation
                                break
                            else:
                                print 'maximum equations reached'
                                return
                        elif x.direction == (curr, prev):
                            if x in stack:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            
                            elif i[0] < counter:
                                stack.append(x)                            

                                print 'element added to equation, with opposite current'
                                print x.type
                                if x.current == [0]:
                                    l = [0]
                                    c = [curr]
                                    p = [0]
                                    on_wrong_entry(l,c,p)
                                    last = l[0]
                                    curr = c[0]
                                    prev = p[0]
                                if x.type == 'DCBATTERY':
                                    if x.direction[0] == x.positive:
                                        equation[i[0]][-1] += x.value
                                    else:
                                        equation[i[0]][-1] -= x.value
                                elif x.current != [0]:
                                    equation[i[0]][int(x.current[0][1:])] -= x.value
                                print 'equation',
                                print equation
                                break
                            else:
                                print 'maximum equations reached'
                                return
                    print equation
                            
                            

           
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
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                        
                            print 'element added to equation'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
                    elif x.direction == (curr, prev):
                        if x in stack:
                            l = [0]
                            c = [curr]
                            p = [0]
                            on_wrong_entry(l,c,p)
                            last = l[0]
                            curr = c[0]
                            prev = p[0]
                            
                        elif i[0] < counter:
                            stack.append(x)
                            
                            print 'element added to equation, with opposite current'
                            print x.type
                            if x.current == [0]:
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            elif x.type == 'DCBATTERY':
                                if x.direction[0] == x.positive:
                                    equation[i[0]][-1] += x.value
                                else:
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.value
                            print 'equation',
                            print equation
                            break
                        else:
                            print 'maximum equations reached'
                            return
    print 'prev ',
    print prev,
    print 'curr ',
    print curr
    print 'last',
    print last
    print 'calling next loop'
    loop_law(pos_dict, pos_list, stack, element_list, equation, i, counter, nodelist, last, curr, prev )
            