import os

def show(sResult):
    print(f'\r | {result} | \n',end='')

def calc(numi,operator,numii):
    if operator == "+":
        return numi + numii
    elif operator == "-":
        return numi - numii
    elif operator == "*":
        return numi * numii
    elif operator == "/":
        return numi / numii
    elif operator == "**":
        return numi ** numii

def trans(iP):
    mL = False
    #change to list
    if len(iP) == 1:
        iP = list(iP)
    elif len(iP) > 1:
        iPn = []
        for i in iP:
            iPn.append(i)
        iP=iPn
        
    #trans number before middel and last
    if len(iP) > 1:
        
        iPm=[]
        if type(iP[-1-1]) == str and type(iP[-1]) == str:
            if iP[-1] != "i":
                if iP[-1-1] != iP[-1]:
                    
                    mL = True
                    iPm.append(iP[-1-1])
                    iPm.append(iP[-1])
                    del iP[-1-1] 
                    del iP[-1]
                    
                    for key,value in enumerate (iPm):
                        if value == "i":
                            iPm[key] = 1
                        elif value == "v":
                            iPm[key] = 5
                        elif value == "x":
                            iPm[key] = 10
                        elif value == "l":
                            iPm[key] = 50
                        elif value == "c":
                            iPm[key] = 100  
                    iP.append(iPm[1]-iPm[0])
    #trans normal numbers if len == 1
    if len(iP) == 1:   
        if iP[0] == "i":
            iP[0]  = 1
        elif iP[0] == "v":
            iP[0]  = 5
        elif iP[0] == "x":
            iP[0]  = 10
        elif iP[0] == "l":
            iP[0]  = 50
        elif iP[0] == "c":
            iP[0] = 100
    #trans normal numbers if len >= 2
    elif len(iP)>= 2:
        plusCount = 0
        for key,value in enumerate (iP):
            if value == "i":
                iP[key] = 1
            elif value == "v":
                iP[key] = 5
            elif value == "x":
                iP[key] = 10
            elif value == "l":
                iP[key] = 50
            elif value == "c":
                iP[key] = 100
    
    #sum all indexs without last and add it
    if len(iP) > 1:
        if mL == True:
            mLV = iP[-1]
            iP = iP[:-1]
            iPm = 0
            while len(iP) > 1:
                x = iP[0] 
                y = iP[1]
                del iP[1]
                del iP[0]
                iPm = y+x
                iP.append(iPm)
                iPm = 0
            x = iP[0]
            iP = int(str(x)+str(mLV))    
        else:
            iPm = 0
            while len(iP) > 1 :
               x = iP[0] 
               y = iP[1]
               del iP[1]
               del iP[0]
               iPm = y+x
               iP.append(iPm)
               iPm = 0
    
    return iP[0]
 
total = 0
operator = "+"
numList =["i","v","x","l","c"]
operList =["+","-","*","/","**"]
while True:
    while True:     
        num = input("num\n:> ").strip().lower()
        os.system("clear")
        if num == "e" or num == "exit":
            quit()
        if len(num) == 1:
            if num in numList:
                break
        elif len(num) > 1:
            value = False
            for i in num:
                if i not in numList:
                    value = True
            if value == False:
                break            
    num = trans(num)
    result = calc(num,operator,total)
    total = result
    show(total)
    while True:     
        operator = input("operator\n:> ").strip()
        if operator == "e" or operator == "exit":
            quit()
        if len(operator) == 1:
            if operator in operList:
                break
        