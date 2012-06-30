def ToReducedRowEchelonForm(equation):
    if not equation:
        return
    lead = 0
    rowCount = len(equation)
    columnCount = len(equation[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while equation[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        equation[i],equation[r] = equation[r],equation[i]
        lv = equation[r][lead]
        equation[r] = [ mrx / lv for mrx in equation[r]]
        for i in range(rowCount):
            if i != r:
                lv = equation[i][lead]
                equation[i] = [ iv - lv*rv for rv,iv in zip(equation[r],equation[i])]
        lead += 1
    
            

