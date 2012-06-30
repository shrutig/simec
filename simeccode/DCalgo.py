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
            if j.direction[0] == curr:
                if j.current != [0]:
                    equation[i[0]][int(j.current[0][1:])] += 1
            else:
                if j.current != [0]:
                    equation[i[0]][int(j.current[0][1:])] -= 1
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
    

def loop_law(pos_dict, equation, last, curr, i, counter, pos_list, nodelist, l, prev = (0,0)):
    print equation
    print i
    print counter
    print l
    if i[0]>=counter[0]:
        return
    direction_list = [ j.direction for j in pos_list]
    cnt = 0
    x = [0]
    print direction_list
    for l in direction_list:
        if l == (prev, curr) or l == (curr, prev) :
            cnt += 1
            
    print (prev, curr)
    
    if cnt >=2:
        
        print 'success'
        print cnt
        
        return
    elif last == curr: 
        print "done! bye"
        print equation
        cnt = 0
        flg =0
        print pos_list
        if i[0] <= l:
            for j in pos_list:
                print pos_dict[j.final]
                l =len(pos_dict[j.final])
                for m in range(l):
                    print pos_dict[j.final][m].flag
                    if pos_dict[j.final][m].flag == 1:
                        cnt +=1
                    print cnt                    
                if cnt<2:
                    flg = 1
                    break
                cnt = 0
            q = equation[:i[0]]
            for l in q:
                if l == equation[i[0]]:
                    print 'yes'
                    flg = 1
                    break
            
        for j in pos_list:
            j.flag = 0
        pos_list = []
        node_list = []
            
        if flg == 1:
            equation[i[0]] = [0]*(counter[0]+1)
            return
        i[0] += 1
        return
    
    else:
        if curr == (0,0):
            curr = last
        if pos_dict[curr][-1] != pos_dict[curr][1]:
            
            print '='
            print curr
            if curr in nodelist:
                print 'hi'
                y = [0]
                
                for l in pos_dict[curr]:
                    if l.flag == 0:
                        y[0] = l
                if y == [0]:
                    for l in pos_list:
            
                        if (prev,curr) == l.direction:
                            equation[i[0]][int(l.current[0][1:])] -= l.value
                        else:
                            equation[i[0]][int(l.current[0][1:])] += l.value
                        return
                
                x = y[0]
                print x
                if x.type == 'RESISTOR':
                    print 'res'
                    print curr
                
                    #   print equation[i[0]][int(j.current[0][1:])]
                    print x.current
                    print i
                    print equation
                    print x.value
                    if i[0]>=counter[0]:
                        return
                    if curr == x.direction[0]:
                        equation[i[0]][int(x.current[0][1:])] += x.value
                    else:
                        equation[i[0]][int(x.current[0][1:])] -= x.value
                    x.flag = 1
                
                elif x.type == 'DCBATTERY':
                    print 'bat'
                    print curr
                    if i[0]>=counter[0]:
                        return
                    if x.direction[0] == x.positive:
                        equation[i[0]][-1] += x.value
                    else:
                        equation[i[0]][-1] -= x.value
                    x.flag = 1
                elif x.type == 'WIRE':
                    print 'wire1'
                    print curr
                    x.flag = 1
                
                prev = curr
                if curr == x.initial:
                    curr = x.final
                else:
                    curr = x.initial
                print prev
                print curr
                loop_law(pos_dict,  equation, last, curr, i, counter, pos_list, nodelist, l, prev)

            else:
                print 'nope'
                nodelist.append(curr)    
                stack = pos_dict[curr]
        
                for x in stack:
                    if x.flag ==1:
                        #x.flag =0
                        print 'bye'
                        continue
                    pos_list.append(x)
            
                    if x.type == 'RESISTOR':
                        print 'res'
                        print curr
                
                        #   print equation[i[0]][int(j.current[0][1:])]
                        print x.current
                        print i
                        print equation
                        print x.value
                        if i[0]>=counter[0]:
                            return
                        if curr == x.direction[0]:
                            equation[i[0]][int(x.current[0][1:])] += x.value
                        else:
                            equation[i[0]][int(x.current[0][1:])] -= x.value
                        x.flag = 1
                
                    elif x.type == 'DCBATTERY':
                        print 'bat'
                        print curr
                        if i[0]>=counter[0]:
                            return
                        if x.direction[0] == x.positive:
                            equation[i[0]][-1] += x.value
                        else:
                            equation[i[0]][-1] -= x.value
                        x.flag = 1
                    elif x.type == 'WIRE':
                        print 'wire1'
                        print curr
                        x.flag = 1
                    temp_last = curr
                    print 'd'
                    temp_prev = curr
                    if curr == x.initial:
                        print 'e'
                        temp_curr = x.final
                    else:
                        print 'f'
                        temp_curr = x.initial      
        

                    loop_law(pos_dict,  equation, last, temp_curr, i, counter, pos_list, nodelist, l, temp_prev)

                if pos_dict[curr][0].initial == prev or pos_dict[curr][0].final == prev:
                    prev = curr
                    print 'a'
                    if curr == pos_dict[curr][1].initial:
                        print 'b'
                        curr = pos_dict[curr][1].final
                    else:
                        print 'c'
                        curr = pos_dict[curr][1].initial
                else:
                    print 'd'
                    prev = curr
                    if curr == pos_dict[curr][0].initial:
                        print 'e'
                        curr = pos_dict[curr][0].final
                    else:
                        print 'f'
                        curr = pos_dict[curr][0].initial
                loop_law(pos_dict,  equation, last, curr, i, counter, pos_list, nodelist, l, prev)


                    
                    
        else:
            print ')'
        
            for j in pos_dict[curr]:
                pos_list.append(j)
                if j.type == 'RESISTOR':
                    print 'res1'
                    print curr
                    if j.flag != 1:
                        #print equation[i[0]][int(j.current[0][1:])]
                        print j.current
                        print i
                        print equation
                        print j.value
                        if i[0]>=counter[0]:
                            return
                        if curr == j.direction[0]:
                            equation[i[0]][int(j.current[0][1:])] += j.value
                        else:
                            equation[i[0]][int(j.current[0][1:])] -= j.value
                        j.flag = 1
                    
                elif j.type == 'DCBATTERY':
                    print 'batry'
                    print curr
                    if j.flag != 1:
                        if i[0]>=counter[0]:
                            return
                        if j.direction[0] == j.positive:
                            equation[i[0]][-1] += j.value
                        else:
                            equation[i[0]][-1] -= j.value
                        j.flag = 1
                elif j.type == 'WIRE':
                    print 'wire'
                    print curr
                    j.flag = 1
            if pos_dict[curr][0].initial == prev or pos_dict[curr][0].final == prev:
                prev = curr
                print 'a'
                if curr == pos_dict[curr][1].initial:
                    print 'b'
                    curr = pos_dict[curr][1].final
                else:
                    print 'c'
                    curr = pos_dict[curr][1].initial
            else:
                print 'd'
                prev = curr
                if curr == pos_dict[curr][0].initial:
                    print 'e'
                    curr = pos_dict[curr][0].final
                else:
                    print 'f'
                    curr = pos_dict[curr][0].initial      
        
    
            loop_law(pos_dict, equation, last, curr, i, counter,pos_list, nodelist, l, prev)
    
    
    
    
        
