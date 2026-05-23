l=[]
n=int(input("Please enter your number: "))
for i in range(n):
    m=int(input("Enter the number: "))
    l.append(m)

even=0
odd=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(even,odd)




a=max(l)
print(a)

ins=int(input("Enter the element which we have to insert"))
l[2]=ins
print(l)

dele=int(input("Enter the element which we have to delete"))
l.remove(dele)
print(l)




