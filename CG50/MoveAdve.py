data=[]
p=int(input("How many points is the moving adverage: "))
dataIn=True
while dataIn==True:
    newData=input("Data: ")
    if newData.lower()=="n":
        dataIn=False
    else:
        data.append(float(newData))
print("Data input",data)
advCalc=True
advData=[]
j=0
while advCalc==True:
    calc=0
    for i in range(0,p):
        calc+=data[j+i]
    j+=1
    advData.append(calc/p)
    try:
        data[j+p-1]
    except:
        advCalc=False
print("Moving adverages:",advData)