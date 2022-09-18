from tkinter import CENTER
Score=0
q=" Quiz Game "
print(q.center(80,"*"))
x=str(input("Enter your name :)"))
print("HI",x)
a=str(input("There are 5 quctions Are you ready ::) say Yes = "))
if a.lower()!="yes":
    quit()
b=str(input("1.What is CPU  ?: = "))
if b.lower()!="central processing unit" :   # 1 start
    print("Wrong")
else:
    print("Correct:)")
    Score+=1      #    1 st
c=str(input("2.What is GPU  ?: = "))      #2 start 
if c.lower()!="graphics processing unit" :
    print("Wrong")
else:
    print("Correct:)")
    Score+=1      # 2 nd    
d=str(input("3.What is ALU  ?: = "))      # 3 start 
if d.lower()!="arithmetic logic unit" :
    print("Wrong")
else:
    print("Correct:)")
    Score+=1      # 3 nd    
e=str(input("4.What is LAN  ?: = "))      # 4 start 
if e.lower()!="local area network" :
    print("Wrong")
else:
    print("Correct:)")
    Score+=1      # 4 nd    
f=str(input("5.What is WAN  ?: = "))      # 5 start 
if f.lower()!="wide area network" :
    print("Wrong")
else:
    print("Correct:)")
    Score+=1      # 5 nd 
print("      Your Score is : ",Score) 
if Score<1:
    print("Keep learning and Try again")     
g="Thanks for Play"
print(g.center(80,"*"))  





