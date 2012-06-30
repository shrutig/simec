import copy
def traverse(pos_dict, last, curr, node_list, prev , i, count, flag):
    print 'last = ',
    print last
    print 'curr = ',
    print curr
    if last == curr:
        print 'last = curr, bbye'
        return
    if curr == (0,0):
        print 'just enterd in loop, curr assigned to last'
        curr = last
    stack = []
    
    print 'position dictionary at current point= '
    print pos_dict[curr]
    if pos_dict[curr][-1] != pos_dict[curr][1]:
        print 'node encountered'
        if curr in node_list:
            print 'bye'
            return
        node_list.append(curr)
        print 'current node list',
        print node_list

        print 'assign currents wherever not assigned'        
        for j in pos_dict[curr]:
            if j.current == [0]:
                
                j.current[0] = 'i%s'%i[0]
                if j.current not in count:
                    count.append(j.current)
                print 'count = %s'%count
                if prev == j.initial or prev == j.final:
                    j.currentdirection(prev, curr)
                else:
                    if curr == j.initial:
                        j.currentdirection(j.initial, j.final)
                    else:
                        j.currentdirection(j.final, j.initial)
                print 'current details : ',
                print j.current,
                print j.direction
                i[0] += 1
                
        print 'assignment done'        
        for j in pos_dict[curr]:
            stack.append(j)
        print 'creating stack at node',
        print stack
        
        for x in stack:
            prev = curr
            if x.initial == curr:
                curr = x.final
            else:
                curr = x.initial
            print 'traversing in stack, last, curr, prev',
            print last,
            print curr,
            print prev
        
            traverse(pos_dict, last, curr, node_list, prev, i, count, flag)
            
       
    else:
        print 'currents flowing from a place, not a node';
        print pos_dict[curr][0].current
        print pos_dict[curr][0].direction
        print pos_dict[curr][1].current
        print pos_dict[curr][1].direction
        if pos_dict[curr][0].current !=[0] and pos_dict[curr][1].current!= [0] and pos_dict[curr][0].current != pos_dict[curr][1].current:
            print 'currents are different and both not zero'
            if pos_dict[curr][0].current[0] < pos_dict[curr][1].current[0]:
                if pos_dict[curr][1].current in count:
                    count.remove(pos_dict[curr][1].current)
                print 'count = ',
                print count
                pos_dict[curr][1].current = pos_dict[curr][0].current
                if pos_dict[curr][0].direction[0] == curr:
                    if curr == pos_dict[curr][1].initial:
                        pos_dict[curr][1].direction = (pos_dict[curr][1].final, pos_dict[curr][1].initial)
                    else:
                        pos_dict[curr][1].direction = (pos_dict[curr][1].initial, pos_dict[curr][1].final)
                else:
                    if curr == pos_dict[curr][1].initial:
                        pos_dict[curr][1].direction = (pos_dict[curr][1].initial, pos_dict[curr][1].final)
                    else:
                        pos_dict[curr][1].direction = (pos_dict[curr][1].final, pos_dict[curr][1].initial)
                print 'after modification'
                print pos_dict[curr][0].current
                print pos_dict[curr][0].direction
                print pos_dict[curr][1].current
                print pos_dict[curr][1].direction
            else:
                if pos_dict[curr][0].current in count:
                    count.remove(pos_dict[curr][0].current)
                print 'count = %s'%count
                pos_dict[curr][0].current = pos_dict[curr][1].current
                if pos_dict[curr][1].direction[0] == curr:
                    if curr == pos_dict[curr][0].initial:
                        pos_dict[curr][0].direction = (pos_dict[curr][0].final, pos_dict[curr][0].initial)
                    else:
                        pos_dict[curr][0].direction = (pos_dict[curr][0].initial, pos_dict[curr][0].final)
                else:
                    if curr == pos_dict[curr][0].initial:
                        pos_dict[curr][0].direction = (pos_dict[curr][0].initial, pos_dict[curr][0].final)
                    else:
                        pos_dict[curr][0].direction = (pos_dict[curr][0].final, pos_dict[curr][0].initial)
                print 'after modification'
                print pos_dict[curr][0].current
                print pos_dict[curr][0].direction
                print pos_dict[curr][1].current
                print pos_dict[curr][1].direction
            
                
            if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                
                prev = curr
                if curr == pos_dict[curr][1].initial:
                    
                    curr = pos_dict[curr][1].final
                else:
                    curr = pos_dict[curr][1].initial
            else:
                prev = curr
                if curr == pos_dict[curr][0].initial:
                    prev = curr
                    curr = pos_dict[curr][0].final
                else:
                    curr = pos_dict[curr][0].initial
            print 'dummy traversal with last,prev,curr',
            
            
            dummylast = prev
            dummynode_list = []
            print dummylast,
            print prev,
            print curr
            traverse(pos_dict, dummylast, curr, dummynode_list, prev, i, count, flag)

            'traverse after dummy traversal with last,prev,curr',
            print last,
            print prev,
            print curr

            traverse(pos_dict, last, curr, node_list, prev, i, count, flag)

        elif (pos_dict[curr][0].current !=[0] and pos_dict[curr][0].current == pos_dict[curr][1].current and
              (pos_dict[curr][0].direction[1] == curr and pos_dict[curr][1].direction[1] == curr) or
              (pos_dict[curr][0].direction[0] == curr and pos_dict[curr][1].direction[0] == curr)) :
                print 'currents are same, not equal to zero and in opposite directions'
                if curr == pos_dict[curr][1].initial:
                    pos_dict[curr][1].direction = (pos_dict[curr][1].initial, pos_dict[curr][1].final)
                else:
                    pos_dict[curr][1].direction = (pos_dict[curr][1].final, pos_dict[curr][1].initial)
                
                if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                    prev = curr
                    if curr == pos_dict[curr][1].initial:
                    
                        curr = pos_dict[curr][1].final
                    else:
                        curr = pos_dict[curr][1].initial
                else:
                    prev = curr
                    if curr == pos_dict[curr][0].initial:
                        prev = curr
                        curr = pos_dict[curr][0].final
                    else:
                        curr = pos_dict[curr][0].initial
                print 'dummy traversal with last,prev,curr',
                
            
                dummylast = prev
                dummynode_list = []
                print dummylast,
                print prev,
                print curr
                traverse(pos_dict, dummylast, curr, dummynode_list, prev, i, count, flag)

                print 'traverse after dummy traversal with last,prev,curr',
                print last,
                print prev,
                print curr
            

                traverse(pos_dict, last, curr, node_list, prev, i, count, flag)
                
        elif pos_dict[curr][0].current !=[0] and pos_dict[curr][0].current == pos_dict[curr][1].current:
            'currents are same, not equal to zero, same direction'
            if curr in flag:
                return
            flag.append(curr)
            if pos_dict[curr][0].direction[0] == curr and pos_dict[curr][1].direction[0] == curr :
                if curr == pos_dict[curr][1].initial:
                    pos_dict[curr][1].direction = (pos_dict[curr][1].final, pos_dict[curr][1].initial)
                else:
                    pos_dict[curr][1].direction = (pos_dict[curr][1].initial, pos_dict[curr][1].final)
                
                if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                    prev = curr
                    if curr == pos_dict[curr][1].initial:
                    
                        curr = pos_dict[curr][1].final
                    else:
                        curr = pos_dict[curr][1].initial
                else:
                    prev = curr
                    if curr == pos_dict[curr][0].initial:
                        prev = curr
                        curr = pos_dict[curr][0].final
                    else:
                        curr = pos_dict[curr][0].initial
                print 'dummy traversal with last,prev,curr',
                
            
                dummylast = prev
                dummynode_list = []
                print dummylast,
                print prev,
                print curr
                traverse(pos_dict, dummylast, curr, dummynode_list, prev, i, count, flag)

                print 'traverse after dummy traversal with last,prev,curr',
                print last,
                print prev,
                print curr
            

                traverse(pos_dict, last, curr, node_list, prev, i, count, flag)
                
            
            else:
                if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                    prev = curr
                    if curr == pos_dict[curr][1].initial:
                    
                        curr = pos_dict[curr][1].final
                    else:
                        curr = pos_dict[curr][1].initial
                else:
                    prev = curr
                    if curr == pos_dict[curr][0].initial:
                        prev = curr
                        curr = pos_dict[curr][0].final
                    else:
                        curr = pos_dict[curr][0].initial
                print 'traverse with last, prev,curr',
                print last
                print prev
                print curr
                traverse(pos_dict, last, curr, node_list, prev, i, count, flag)
            
            
            
        elif pos_dict[curr][0].initial == prev or pos_dict[curr][0].final == prev:
            print 'naf'
            pos_dict[curr][1].current =  pos_dict[curr][0].current
            if prev == pos_dict[curr][1].initial or prev == pos_dict[curr][1].final:
                pos_dict[curr][1].currentdirection(prev, curr)
            else:
                if curr == pos_dict[curr][1].initial:
                    pos_dict[curr][1].currentdirection(pos_dict[curr][1].initial, pos_dict[curr][1].final)
                else:
                    pos_dict[curr][1].currentdirection(pos_dict[curr][1].final, pos_dict[curr][1].initial)
            
            
                
            if pos_dict[curr][1].current == [0]:
                pos_dict[curr][1].current[0] = 'i%s'%i[0]
                if pos_dict[curr][1].current not in count:
                    count.append(pos_dict[curr][1].current)
                print 'count = %s'%count
                print pos_dict[curr][1].current
                print pos_dict[curr][1].direction
                i[0] += 1
                if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                    pos_dict[curr][0].currentdirection(prev, curr)
                else:
                    if curr == pos_dict[curr][0].initial:
                        pos_dict[curr][0].currentdirection(pos_dict[curr][0].initial, pos_dict[curr][0].final)
                    else:
                        pos_dict[curr][0].currentdirection(pos_dict[curr][0].final, pos_dict[curr][0].initial)
            
            
            print pos_dict[curr][0].current[0]
            print pos_dict[curr][1].current[0]
            print pos_dict[curr][1].direction
            print pos_dict[curr][0].direction
        
            prev = curr
            if curr == pos_dict[curr][1].initial:
                curr = pos_dict[curr][1].final
            else:
                curr = pos_dict[curr][1].initial
            print prev
            print curr
            traverse(pos_dict, last, curr, node_list, prev, i, count, flag)
        else:
            print 'isa'
            pos_dict[curr][0].current =  pos_dict[curr][1].current
            if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                pos_dict[curr][0].currentdirection(prev, curr)
            else:
                if curr == pos_dict[curr][0].initial:
                    pos_dict[curr][0].currentdirection(pos_dict[curr][0].initial, pos_dict[curr][0].final)
                else:
                    pos_dict[curr][0].currentdirection(pos_dict[curr][0].final, pos_dict[curr][0].initial)
            
            if pos_dict[curr][0].current == [0]:
                pos_dict[curr][0].current[0] = 'i%s'%i[0]
                if pos_dict[curr][0].current not in count:
                    count.append(pos_dict[curr][0].current)
                print 'count = %s'%count
                print pos_dict[curr][0].current
                print pos_dict[curr][0].direction
                i[0] += 1
                if prev == pos_dict[curr][1].initial or prev == pos_dict[curr][1].final:
                    pos_dict[curr][1].currentdirection(curr, prev)
                else:
                    if curr == pos_dict[curr][1].initial:
                        pos_dict[curr][1].currentdirection(pos_dict[curr][1].final, pos_dict[curr][1].initial)
                    else:
                        pos_dict[curr][1].currentdirection(pos_dict[curr][1].initial, pos_dict[curr][1].final)
            
                
            print pos_dict[curr][0].current[0] 
            print pos_dict[curr][1].current[0]
            print pos_dict[curr][0].direction
            print pos_dict[curr][1].direction
            
            
            if prev == pos_dict[curr][0].initial or prev == pos_dict[curr][0].final:
                prev = curr
                if curr == pos_dict[curr][1].initial:
                    
                    curr = pos_dict[curr][1].final
                else:
                    curr = pos_dict[curr][1].initial
            else:
                prev = curr
                if curr == pos_dict[curr][0].initial:
                    prev = curr
                    curr = pos_dict[curr][0].final
                else:
                    curr = pos_dict[curr][0].initial
            print prev
            print curr
        
        traverse(pos_dict, last, curr, node_list, prev, i,count, flag)
    



    

def current_law(pos_dict, equation, last, curr, node_list, i, counter, prev = (0,0)):
    
    
   
    print pos_dict[curr][-1]
    print pos_dict[curr][1]
    if pos_dict[curr][-1] != pos_dict[curr][1]:
        if curr in node_list:
            print 'bye'
            return

        print '&'
        node_list.append(curr)
        for j in pos_dict[curr]:
            print i[0]
            print j.current
            
            print j.direction
            print j.current[0]
            if j.direction[0] == curr:
                if j.current != [0]:
                    equation[i[0]][int((j.current[0])[1:])] += 1
            else:
                if j.current != [0]:
                    equation[i[0]][int((j.current[0])[1:])] -= 1
            print equation
        
        
        print equation
        print '!'
        stack = []
        for j in pos_dict[curr]:
            stack.append(j)
        print stack
        flg = 1
        from ech import ToReducedRowEchelonForm
        eqn = copy.deepcopy(equation)
        ToReducedRowEchelonForm(eqn)
        
        if eqn[i[0]] != [0]*(counter+1):
            i[0] += 1
        else:
            equation[i[0]] = [0]*(counter+1)
        
        for x in stack:
            print '@'
            prev = curr
            if x.initial == curr:
                curr = x.final
            else:
                curr = x.initial     
            current_law(pos_dict, equation, last, curr, node_list, i, counter, prev)
        
    else:
        print '#'
        if pos_dict[curr][0].initial == prev or pos_dict[curr][0].final == prev:
            print '$'
            prev = curr
            if curr == pos_dict[curr][1].initial:
                curr = pos_dict[curr][1].final
            else:
                curr = pos_dict[curr][1].initial
        else:
            print '%'
            prev = curr
            if curr == pos_dict[curr][0].initial:
                curr = pos_dict[curr][0].final
            else:
                curr = pos_dict[curr][0].initial
        print curr
    
        if last == curr:        
            return
        current_law(pos_dict, equation, last, curr, node_list, i, counter, prev)
    

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
                
                    print x.type, x.value, x.impedance
                    
                    if x.current == [0]:
                        on_wrong_entry(l,c,p)                        
                    elif x.type == 'DCBATTERY':
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        else:
                            equation[i[0]][-1] -= x.value
                    elif x.type == 'ACBATTERY':
                            equation[i[0]][-1] += x.value
                    elif x.current != [0]:
                        equation[i[0]][int(x.current[0][1:])] += x.impedance
                    print 'equation',
                    print equation
                    break
                else:
                    print 'maximum equations reached'
                    return
            elif x.direction == (c[0], p[0]):
                if i[0] < counter:
                    print 'element added to equation, with opposite current'
                    print x.type, x.value, x.impedance
                    if x.current == [0]:
                        on_wrong_entry(l,c,p)
                    elif x.type == 'DCBATTERY':
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        else:
                            equation[i[0]][-1] -= x.value
                    elif x.type == 'ACBATTERY':
                            equation[i[0]][-1] -= x.value
                    elif x.current != [0]:
                        equation[i[0]][int(x.current[0][1:])] -= x.impedance
                    print 'equation',
                    print equation
                    break
                else:
                    print 'maximum equations reached'
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
                    print x.type, x.value, x.impedance
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
                    elif x.type == 'ACBATTERY':
                            equation[i[0]][-1] += x.value
                    elif x.current != [0]:
                        equation[i[0]][int(x.current[0][1:])] += x.impedance
                    print 'equation',
                    print equation
                    break                    
                else:
                    print 'maximum equations reached'
                    return
            elif x.direction == (curr, last):
                if i[0] < counter:
                    print 'element added to equation, with opposite current'
                    print x.type, x.value, x.impedance
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
                    elif x.type == 'ACBATTERY':
                            equation[i[0]][-1] -= x.value
                    else:                        
                        equation[i[0]][int(x.current[0][1:])] -= x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] += x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] += x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.impedance
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
                        print x.type
                        print x.value
                        print (prev, curr)
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] += x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.impedance
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
                        print 'type = ',
                        print x.type
                        print x.direction
                        print (prev, curr)
                        
                        if x.direction == (prev, curr):
                            print '1'
                            if x in stack:
                                print '2'
                                l = [0]
                                c = [curr]
                                p = [0]
                                on_wrong_entry(l,c,p)
                                last = l[0]
                                curr = c[0]
                                prev = p[0]
                            
                            elif i[0] < counter:
                                print '3'
                                stack.append(x)
                            
                                print 'element added to equation'
                                print 'type = ',
                                print x.type, x.value, x.impedance
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
                                elif x.type == 'ACBATTERY':
                                        equation[i[0]][-1] += x.value
                                
                                    
                                elif x.current != [0]:
                                    equation[i[0]][int(x.current[0][1:])] += x.impedance
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
                                print x.type, x.value, x.impedance
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
                                elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] -= x.value
                                elif x.current != [0]:
                                    equation[i[0]][int(x.current[0][1:])] -= x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] += x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] += x.impedance
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
                            print x.type, x.value, x.impedance
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
                            elif x.type == 'ACBATTERY':
                                    equation[i[0]][-1] -= x.value
                            elif x.current != [0]:
                                equation[i[0]][int(x.current[0][1:])] -= x.impedance
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
            
