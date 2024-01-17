n=int(input("Num of data points: "))
diff=[]
for i in range(0,n):
  diff.append((float(input("X: "))-float(input("Y: ")))**2)
outs=(1-((6*sum(diff)))/(n*((n**2)-1)))
print("SRCC:",outs)