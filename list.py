# list1 =[5,4,3,2,1]
# print(list1)
# print(f'lrngth of list1 is :{len(list1)}')
# list1.append(6)
# print(list1)
# print(f'length of list1:{len(list1)}')
# #print("hello how are you ")

# list1 =[5,4,3,2,1]
# print(len(list1))
# print(list1)
# list1.append(4)

# print(len(list1))
# print(list1)
# list1.insert(0,222)
# print(len(list1))
# print(list1)
# l1 = [1,2,3,4,5]
# # for i in l1:
# #     print(i)
# for count in range(len(l1)):
#     print(l1[count])

# my_list = [1,23,4,56,78]
# for count in range(len(my_list)):
#     print(my_list[count])


# list1 = []
# for count in range(1,11):
#  list1.append(count)
# print(list1)

# my_list=[]
# num = 1 
# while num<=10:
#     my_list.append(num)
#     num+=1
# print(my_list)

# my_list = [10,20,30,40,50,60,70,80,90,100]
# for i in range(10):
#     my_list[i]+=1
# print(my_list)

# list1= []
# for  i in range(10,101,10):
#     list1.append(i+1)
# print(list1)

'''list ke sare element ka sum'''
# my_list = [10,20,30,40,50,60,70,80,90,100]
# sum = 0
# for i in range(len(my_list)):
#     sum +=my_list[i]
# print("sum:",sum)

'''swap two number'''
# a = 20
# b = 10
# print("a:",a)
# print("b:",b)
# #
# a,b=b,a
# print("a:",a)
# print("b:",b)

# my_list=[10,2,8,3,5]
# print(my_list)
# my_list[0],my_list[4]=my_list[4],my_list[0]


'''bubble sorting'''
# my_list= [1,2,3,4]
# swapped = 0 
# print(my_list)
# count = 0
# for index in range(len(my_list)-1):
#      for index in range(len(my_list)-1-index):
#        count += 1
#        if (my_list[index] > my_list[index + 1]):
#            my_list[index], my_list[index+1]=my_list[index+1], my_list[index]
#            swapped = 1
#      if swapped == 0:
#          break

# print(my_list)
# print("my program is run for:",count,"times")


'''
4 = 5th element sorted
3 = 4th element sorted
2 = 3rd element sorted
1 = 2nd element sorted
'''

# my_list= [1,2,3,4,5]
# swapped =  True
# count = 0 
# while swapped :
#     swapped = False 
#     for i in range (len(my_list)-1):
#         count += 1
#         if my_list[i] > my_list[i + 1]:
#             swapped = True 
#             my_list[i],my_list[i + 1 ]=my_list[i + 1 ],my_list[i]
# print(my_list)
# print("loops are running  for:",count,"times")

'''function sorting'''

# my_list= [1,9,3,2,5]
# my_list.sort()
# print(my_list)

'''
[a,b,c,d,e]
0 = -1
1= -2
0 = -1 = (-1 *(index + 1))
index = (-1 *(index +1))
index = len(lst)-(index +1)
 
 '''

# lst= [1,9,3,2,5]
# #print(my_list[::-1])
# for index in range(len(lst)//2):
#     #print(len[index])
#     #lst[index],lst[(-1 *(index + 1))]=lst[(-1 *(index + 1))],lst[index]
#     lst[index],lst
# print(lst) 


'''module 3
'''
# lst =["A","F","a","b"]
# lst.sort()
# print(lst)
# print("a"<"A")

# a= 3
# b =1 
# c = 2
# lst = [a,c,b]
# lst.sort()
# print(lst)

#reverse list
a = "A"
b = "B"
c = "c"
d = " "
lst = [a,b,c,d]
lst.reverse()
print(lst)