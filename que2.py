#even and odd num
# i=25 
# if i%2==0:
#  print("even num")
# else:
#  print("odd num")


#palindrome
# s="mom"
# if s==s[::-1]:
#  print("palindrome")
# else: 
#  print("no pallindrome")


#factorial
# num = 5
# fact = 1
# for i in range(1,num +1):
#    fact= fact*i
# print(fact)   


#reverse num
# num = 12345
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)

#reverse num use slicing 
# num = "12345"
# print(num[::-1])

#prime num
# num = 7
# i = 2
# count = 0

# while i < num:
#     if num % i == 0:
#         count = count + 1
#     i = i + 1

# if count == 0:
#     print("Prime number")
# else:
#     print("Not prime number")


#find sqare and cube
# num = 25
# sqare = num**2
# cube = num**3
# print("sqare",sqare)
# print("cube",cube)


#even and odd with list
#list
# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#      if i%2==0:
#       print("even",i)
#      else:
#         print("odd",i) 


#even and odd count num in list
# numbers = [10, 15, 20, 25, 30]

# even = 0
# odd = 0

# for i in numbers:
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even count =", even)
# print("Odd count =", odd)


#only fetch string record in list
#a = [10, "Akshay", 20, "Python", 30, "SQL"]

# for i in a:
#     if type(i) == str:
#         print(i)


#only fetch integer record in list
# a = [10, "Akshay", 20, "Python", 30, "SQL"]

# for i in a:
#      if type(i) == int:
#          print(i)


#show all record in dictionary
#dict
# a={"name":"akshay","age":21,}
# print(a.items())


#show marks in dict
# a={"name":"akshay","age":21,"marks":41}
# print(a.get("marks"))

#show highest marks in record
# marks = {"Akshay": 80,"Rahul": 95,"Amit": 75}

# highest=max(marks.values())
# print(highest)


#show  student records is above 60 marks
# marks = {"Akshay": 80,"Rahul": 95,"Amit": 75}
# for key,value in marks.items():
#     if value > 60:
#         print(key,":",value)


#tuple
# a=(2,3,44,55,77,88)
# print(max(a))
# print(min(a))
# print(sum(a))

#count total len of tuple values not use len
# t = (10, 20, 30, 40, 50)

# count = 0

# for i in t:
#     count = count + 1

# print("total length",count)


#sum in tuple values
# c = (10, 20, 30, 40, 50)

# sum = 0

# for i in c:
#     sum = sum + i

# print("sum :",sum)


#show even and odd num in tuple
# tuple=(1,2,3,4,5,6,7,8,9)
# for i in tuple:
#     if i%2==0:
#      print(i,end=",")


#prime num
# num = 7
# i = 2
# count = 0

# while i < num:
#      if num % i == 0:
#         count = count + 1
#      i = i + 1

# if count == 0:
#    print("Prime number")
# else:
#     print("Not prime number")