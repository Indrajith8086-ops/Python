list1=set()
list2=set()
n1= int(input("Enter the number of colours:"))
print("Enter the colours of list1:")
for i in range (n1):
    colour = input()
    list1.add(colour)
n2 = int(input("Enter the number ofcolours:"))
for i in range (n2):
    colour = input()
    list2.add(colour)
diff = list1.difference(list2)
print("The colours are:", diff)
