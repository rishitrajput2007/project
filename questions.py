# a=input("Enter thr first name ")
# b=input("Enter thr last name ")
#
# print(f"Hello {b},{a}!")


# price=5.50
# item="Apple"
#
# print(f"The price of {item} is {price} dollars.")


# n=input("Enter the string")
# s=n[::-1]
# if s==n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# u=input("Enter the string: ")
# w=u.upper()
# x=u.lower()
# z=u.title()
#
# print(w,x,z)


# s="apple,banana,grapes"
# a=s.split(",")
# print(a)

# word=["python","is","awesome"]
# s=" ".join(word)
# print(s)
#
# x=''' hello
# world
# python '''
#
# z=x.splitlines()
# print(z)
#
# for i in z:
#     print(i)




# a={1,2,3,4,5}
# a.add(6)
#
# print(a)
# a.remove(3)
# print(a)
# print(2 in a)


# a={1,2,3,4}
# b={3,4,5,6}
#
# z=a.union(b)
# print(z)
# x=a.intersection(b)
# print(x)
# y=a.difference(b)
# print(y)

# s={"name": "Alice", "age": 20,"grade":"A"}
# print(s)
# s["city"]="Delhi"
# s["age"]=21
# del s["grade"]
# print(s)



# keys=["id","name","email"]
# values=[1,2,3]
#
# d={}
#
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
#
# print(d)




# s="123"
# l=[1,2,3]
# t=(4,5,6)
# m=[(1,'A'),(2,'B')]
#
# a=int(s)
# print(a)
# b=tuple(l)
# print(b)
# c=list(t)
# print(c)
#
# z=dict(m)
# print(z)



students=[{"id":101,"name":"Alice","score":85},
          {"id":102,"name":"Bob","score":78},
          {"id":103,"name":"Charlie","score":92},]

for i in students:
    print(i["name"])

avg=sum(i["score"] for i in students)/len(students)
print(avg)

students.append({"id":104,"name":"Rishit","score":95})
print(students)
students[1]["id"]=88
print(students)

del students[2]
print(students)
maximum=max(i["score"] for i in students)
print()
print(maximum)
