data=[]
p=int(input("How many data points: "))
dataIn=True
while dataIn==True:
  newData=input("Data: ")
  if newData.lower()=="n":
      dataIn=False
  else:
      data.append(float(newData))
print("Data input",data)
meCalc=True
meData=[]
j=0
while meCalc==True:
  meData.append(data[j+1]-data[j])
  j+=1
  try:
    data[j+1]
  except:
    meCalc=False
meTotal=0
for i in meData:
  meTotal+=i
meDiff=meTotal/p
print("Mean Common Difference: ",meData,"\n",meDiff)