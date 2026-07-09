#Assignment

# beatles = []
# beatles.append("John lennon")
# beatles.append("paul McCartney")
# beatles.append("George Harrison")
# for i in range(2):
#    member = input("Enter a band member:")
#    beatles.append(member)
# print("\n The beatles list:")
# beatles.remove("Stu Sutcliffe")
# beatles.remove("Pete Best")
# print(beatles)
# beatles.insert(0,"Ringo starr")
# print(beatles)


#Questions

# name,marks,rank = "vivek patel",32,4
# first_name = input("enter fname:" )
# last_name = input("enter lname:" )
# NAME = first_name + " " + last_name
# AGE = input("enter age:" )
# CITY = input("enter city:" )
# SKILL = input("enter skill:")
# print("-" *32)
# print(f'NAME :{NAME:<15}\nAGE :{AGE  :}\nCITY :{CITY}\nSKILL :{SKILL}\n')
# print(("|" + " "*30 + "|\n")* 10, end="")
# print("-" *32)

#question 
#list creation
lst = [1,2,3,4,5,6,7]
print(lst)
#remove element
lst.remove(5)
print(lst)
#user input
num = int(input('Enter a number:')) 
#find middle number
middle=len(lst)//2
lst[middle]=num
print(lst)

