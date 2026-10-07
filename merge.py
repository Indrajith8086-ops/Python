mydict1={}
print("Enter the elements of th first disk:")
while True:
       key=input("enter a key(or 'q' to quit):")
       if key == 'q':
        break
       value = int(input("enter a value:"))
       mydict1[key]=value
mydict2={}
print("Enter the elements of the second disk:")
while True:
       key=input("enter a key(or 'q' to quit):")
       if key == 'q':
        break
       value = int(input("enter a value:"))
       mydict2[key]=value
print(mydict1|mydict2)

