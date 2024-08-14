
import sys
#reads in file and returns it in a 2d list
def readfile (file):
    list = []
    with open(file, "r") as cpt:
        lines = cpt.readlines()
        for lines in lines:
            values = lines.strip().split(",")
            list.append(values)
    return list

#hidden markov model, takes in file, performs filtering, and return with probabilties
def hmm(file):
    variablesList = readfile(file)
    probabilities = []
    #goes through each line
    for line in variablesList:
        #assign variables a through e, *e is a list of true or false
        a,b,c,d,f, *e = [float(x) if '.' in x else x.lower() == 't' for x in line]
        #applies filtering
        prob =filtering(a,b,c,d,f,e)
        #add the filtered probability to a list
        probabilities.append(prob)
    
    #returns the result
    return result(variablesList,probabilities)

#peforms filtering based on a,b,c,d,f,e
def filtering(a,b,c,d,f,e):
    xT = a
    xF = 1-a
    for i in (e):
    #prediction
        newxT = (b * xT) + (c *xF)
        newxF = ((1-b) * xT ) + ((1-c) *xF)

    #update based on if e is true/false
        if i == True:
            updateXT = (d * newxT) 
            updateXF = (f * newxF) 
        else:
            updateXT = (1-d) * newxT
            updateXF = (1-f) * newxF    
        #normalize current t/f  
        xT = updateXT / (updateXT+updateXF)
        xF = updateXF / (updateXT+updateXF)
    return xT,xF
        
#prints the result
def result(line, prob):
    result =""
    for i, subList in enumerate(line):
        result += ','.join(subList) + f"--><{prob[i][0]:.4f},{prob[i][1]:.4f}>\n"
    return result

print(hmm(str(sys.argv[1])))




