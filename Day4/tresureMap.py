r1=["_","_","_"]
r2=["_","_","_"]
r3=["_","_","_"]
map=[r1,r2,r3]

print(f"{r1}\n{r2}\n{r3}")

cordinate=input("\nEnter a coordinate:")

col=int(cordinate[0])
row=int(cordinate[1])

map[row-1][col-1]="X"

print(f"{r1}\n{r2}\n{r3}")
