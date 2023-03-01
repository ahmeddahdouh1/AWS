
# name = "ahmed"
#
# age = 26
#
# num = 180.1
#
# is_dev = True
#
# print(name)
#
# age = input("your age : ")
# print(age)

# first_name = "ahmed"
# age = 0

# first_name = input("Enter your name : ")
# color = input("what is your fav color ? :  ")
#
# print(first_name +  " likes " + color )
# first_name = "ahmed"
# para = f"my name is {first_name} "
# print(para)

# first_name = "ahmed"
# last_name = "dahdouh"
# hight = 175
# age = 20
# address = "gaza"
# para = f"""my first name {first_name}
# my last name {last_name}
# my hight {hight}
# my age {age}
# my address {address} """
# print(para)

# weight = input("your weight (kg)..... ")
# conn = float(weight) / 0.45
# print(f"your weight {conn} pounds")


# first_name = "ahmed dahdouh"
# x = first_name.upper()
# y = len(first_name)
# z = first_name.lower()
# q = first_name.find("dahdouh")
# w = first_name.replace("a","A" ,1)
# n = 10 % 3
# t = 5
# t += 5
# e = (5*2)**2
# print(e)

# ////////////////////////////////////

# if


# color = input("please enter your color : ")
#
# if color == "red":
#     print("otmani")
# elif color == "gray":
#     print("modern")
# else:
#     print("please enter your color")




# text = input("enter : ")
#
# if text == "hot":
#     print(f"""its a hot day .
# drink plenty of water""")
#
# elif text == "cold":
#     print(f"""its a cold day .
# Wear warm clothes""")
# else:
#     print(" It's a lovely day")


# price = 1000000
# state  = True
# discount = 0.2
# discount_of_good = 0.1
#
# if state == True:
#     print(f" price {price - price * discount_of_good} $")
# else:
#     print(f" price {price - price * discount} $ ")


# high_income = True
# good_credit = True
#
# if high_income and good_credit:
#     print("Eligible for loan")
# else:
#     print("not Eligible ")


# name = input("enter : ")
#
# if len(name) < 3 :
#     print("name must be at lest 3 char log")
# elif len(name) < 10 :
#     print("name can be a max of 10 char ")
# else:
#     print("name looks good")


# avg = float(input("enter avg : "))
#
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("c")
# elif avg >= 60:
#     print("D")
# else:
#     print("gg")


# x = input(" kg , ibs ")
#
# if x == "ibs":
#     weight = float(input("enter weight kg : "))
#     print(f""" your weight {weight / 0.45} ibs""")
# elif x == "kg":
#     weight = float(input("enter weight ibs : "))
#     print(f""" your weight {weight * 0.45} kg""")
# else:
#     print("gg")


# i = 0
#
# while i < 10:
#
#     i = i + 1
#     if i == 5:
#      continue
#     print(i)
#
# print("done")
#


# i = 0
#
# x = input(" kg , ibs ")
# while i < 3:
#     if x == "ibs":
#         weight = float(input("enter weight kg : "))
#         print(f""" your weight {weight / 0.45} ibs""")
#     elif x == "kg":
#         weight = float(input("enter weight ibs : "))
#         print(f""" your weight {weight * 0.45} kg""")
#     else:
#         print("gg")



# s_num = 5
# i = 0
#
# while i < 3:
#     x = int(input("enter num : "))
#     i += 1
#     if x == s_num:
#         print("you win ....")
#         break
#     else:
#         print("you filed")
# else:
#     print("--------")
#


# secret_num = 5
#
#
# i = 1
# num =  int(input("Enter the secret number : "))
# while i < 3:
#   if num == 5:
#       print("Correct Number")
#       break
#   else:
#       print("Error Code Number!!")
#       num = int(input("Enter The number again :"))
#   i += 1
# else:
#   print("sorry")


# list = [1,3,5,6,8]
# print(list)
#
# name = "aaa"
# x = name
# print(x)
# name = "dddd"
# print(name)


# students = ["ahmed", "ali", "walaa", "sajed"]
# print(students)

# list = [10 ,20 ,30 ,30 ,10 ]
# i = 0
# length = len(list)
# sum = 0
# while i < length:
#     sum +=  list[i]
#     i += 1
# print(sum)

# list = [1,2,3,4,5,6]
# sum = 0
# for item in list :
#     sum += item
# print(sum)

# list_of_numbers = [10,3,5,76,324,-4234,656]
# m = list_of_numbers[0]
# n = list_of_numbers[0]
# for i in list_of_numbers:
#     if i > m:
#         m=i
#     if i < n:
#         n = i
# print(n)
# print(m)


# for x in range(3):
#     for y in range(3):
#         print(f" x : {x} y : {y}")
#

# ////////////////////////////////
# state = True
# car = ""
#
# while car != "QUIT":
#     car = input("START, STOP, QUIT , HELP ")
#     if car == "START":
#         if state:
#             print("car is already started ")
#         else:
#             print("car is started")
#     elif car == "STOP":
#         if state:
#             print("car is already STOP ")
#         else:
#             print("car is stop")
#     elif car == "HELP":
#         print("""to start the car
#             stop - to stop the car
#             quit - to quit""")
#     else:
#         print("gg")
# print("quit")
# ////////////////////////////////////////

# emojies = {
#     "happy": ":)",
#     "sad": ":("
# }
# sen = input(" enter : ")
#
# list = sen.split(" ")
# res = ""
# for item in list:
#     res += emojies.get(item , item) + " "
# print(res)

# nums = {
#     "1": "one",
#     "2": "tow",
#     "3": "three"
# }
# sen = input("enter : ")
# res = ""
# list = sen.split(" ")
#
# for item in list:
#    res += nums.get(item ,"!" ) + " "
# print(res)

# nums = {
#     "1": "one",
#     "2": "tow",
#     "3": "three"
# }
# def ret_num(nums):
#
#     sen = input("enter : ")
#     res = ""
#     list = sen.split(" ")
#
#     for item in list:
#        res += nums.get(item ,"!" ) + " "
#     print(res)
# ret_num(nums)

# def whatever(limt,addvalu,*number):
#
#     for num in number:
#         if num > limt :
#             print(num)
#         else:
#             print(num + addvalu)
# whatever(5,2,2,3,8,7)


class Student:
    def __init__(self,first_name):
        self.first_name = first_name

    def display(self):
        print(f"hello {self.first_name}")

ahmed = Student("ahmed")
ahmed.display()


