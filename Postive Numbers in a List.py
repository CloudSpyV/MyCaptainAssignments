#Code For Printing Positive numbers in a List
lst1=[]
lst2=[]
i=0
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    x=int(input("Enter The Number: "))
    lst1+=[x,]
for x in lst1:
    if x>0:
        lst2+=[x,]
print(lst2)
