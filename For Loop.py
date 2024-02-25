for i in range(1,11):
    print(i)
for i in list(range(1,59)):
    print(i)
for i in list(range(1,44)):
    print(i)
Rows = int(input("Enter Your Number:"))
for i in range(0,Rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print("")
squars = int(input("enter numbers:"))
for i in range(0,squars):
    for j in range(i,squars):
        print("*",end=" ")
    squars+=1
    print("")
random = int(input("enter number:"))
i=0
for i in range(0,random):
    for j in range(1,i):
        print("*",end=" ")
    print("")