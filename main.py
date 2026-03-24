# import random
# import matrix
# # 1
#
# name = input()
# print("Привет, " + name)
#
# #2
# a = int(input())
# b = int(input())
# print(a+b)
#
# #3
# a1 = int(input())
# b1 = int(input())
# print(f"Площадь прямоугольниак = {a1*b1}")
#
# #4
# a2=int(input())
# print(a2**2)
# #5
# a5 = int(input())
# b5 = int(input())
# c5 = int(input())
# print((a5+b5+c5)/3)
#
# #6
# a = int(input())
# if a%2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")
# # #7
# a = int(input())
# b = int(input())
# print(max(a,b))
# #8
# a = int(input())
# b = int(input())
# c = int(input())
# print(min(c,min(a,b)))
# #9
# a = int(input())
#
# if a > 0:
#     print("+")
# else:
#     print("-")
#
# #10
# a = int(input("Первое число:"))
# b = int(input("Второе число:"))
# c = input("Введите операцию(+,-,*,/,СВО):")
# if c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "*":
#     print(a*b)
# elif c == "/":
#     print(a/b)
# elif c == "СВО":
#     print("ГОЙДА")
#
# #11
# N = int(input())
# for a in range (1, N+1):
#     print(a)
#
# #12
# N = int(input())
# count = 0
# for i in range(1 , N+1):
#     count += i
# print(count)
#
# #13
# a = 5
# for i in range(1, 11):
#     rez = a*i
#     print(f"{a}*{i}={rez}")
#
# #14
# N = int(input())
# for i in range (N):
#     rez = N - i
#     print(rez)
#
# #15
# N = int(input())
# a = 1
# while N>1:
#     a *= N
#     N-=1
#     print(a)
#
# #16
# a = input()
# print(f"Длина строки: {len(a)}")
#
# #17
# a = input()
# b = input()
# print(f"{a} {b}")
#
# #18
# text = input()
# res = text.upper()
# print(res)
#
# #19
# a = input()
# print(a[0])
# print(a[-1])
#
# #20
# a = input()
# N = int(input())
# print(a*N)
#
# #21
# a = ["голубь","жури","нищий","энергетический напиток Бэрн", "Даня жим лёжа 100кг"]
# print(a)
#
# #22
# a = ["голубь","жури","нищий","энергетический напиток Бэрн", "Даня жим лёжа 100кг"]
# print(a[0])
# print(a[-1])
#
# #23
# a = [11,6,4,3, 1]
# print(sum(a))
#
# #24
# a = []
# for i in range(5):
#     number = int(input())
#     a.append(number)
# print(a)
#
# #25
# a = [11,6,4,3, 1]
# print(a)
# del(a[-1])
# print(a)
#
# #26
# def hello(name):
#     print(f"Hello, {name}!")
# hello("Ярик")
#
# #27
# def add(a, b):
#     print(a+b)
# add(int(input()), int(input()))
#
# #28
# def add(a, b):
#     print(max(a, b))
# add(int(input()), int(input()))
#
# #29
# def is_even(n):
#     if n%2==0:
#         print(True)
#     else:
#         print(False)
# is_even(int(input()))
#
# #30
# def area(width, height):
#     s = width*height
#     print(f"Площадь [] = {s}")
# area(int(input()), int(input()))
#
# #31
# print(random.randint(0,10))
#
# #32
# a = ["Даня","Илюха", "Артём","Я","Посхалко"]
# print(random.choice(a))
#
# #33
# print(random.randint(1,6))
#
# #34
# a = [1,2,3,4,5]
# ask = random.choice(a)
# vkl = False
# while vkl == False:
#     ansewer = int(input())
#     if ansewer == ask:
#         vkl = True
#         print("Красава")
#     else:
#         print("Нет")
#
# #35
# a = []
# for i in range(1, 6):
#     s = random.randint(1,20)
#     a.append(s)
# print(a)
#
#
# # 36. Запись (создаст файл рядом с программой)
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Hello, world!")
#
# # 37. Чтение
# with open("output.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print("Содержимое файла:", content)
#
# # 38. Кортеж
# my_tuple = ("яблоко", "банан", "вишня")
# print("Второй элемент кортежа:", my_tuple[1])
#
# # 39. Множество
# my_set = {1, 2, 3, 3, 4}
# print("Множество без дубликатов:", my_set)
#
# # 40. Словарь
# my_dict = {"имя": "Иван"}
# print("Значение по ключу 'имя':", my_dict["имя"])
#41
import random
# a = [1,2,3,4,5,6,7,8,9,10]
# new_a = list(range(a[2],a[8],2))
# print(new_a)
#42
# a = [1,2,3,4,5,6,7,8,9,10]
# a.reverse()
# print(a)
#43
# a = [1,2,3,4,5,6,7,8,9,10]
# maximum = minimum = a[0]
# for i in a:
#     if i > maximum:
#         maximum = i
#     if i < minimum:
#         minimum = i
#
# print(f"Максимум: {maximum}, Минимум: {minimum}")
#44
#
# a = [1,2,3,4,5,6,7,8,9,10]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)
#45
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max1 = float('-inf')
# max2 = float('-inf')
#
# for i in a:
#     if i > max1:
#         max2 = max1
#         max1 = i
#     elif i > max2:
#         max2 = i
#
# print(f"Первое макс. число: {max1}")
# print(f"Второе макс. число: {max2}")
#46
# matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#47
# matrix = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()
#48
# matrix = [[1, 5, 6],
#           [8, 32, 9],
#           [5, 0, 12]]
# a = []
# for row in matrix:
#     for item in row:
#         a.append(item)
# print(sum(a))
#49
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])
# #50
# def transpose(matrix):
#     print(matrix[0][0],matrix[1][0],matrix[2][0])
#     print(matrix[0][1], matrix[1][1], matrix[2][1])
#     print(matrix[0][2], matrix[1][2], matrix[2][2])
#
# transpose([[1,2,3],
#            [4,5,6],
#            [7,8,9]])
#51
# def greet(name, greeting='Hello '):
#     print(greeting + name)
# greet(input('Enter your name: '))
# #52
# def sum_all(*args):
#     sum1 = 0
#     for arg in args:
#         sum1 += arg
#     return sum1
# print(sum_all(1,2,3,4,5,6,7,8,9))
# #53
# def min_max(lst):
#     min_value = min(lst)
#     max_value = max(lst)
#     return min_value, max_value
# min_value, max_value = min_max([1,2,3,4,5,6])
# print(min_value)
# print(max_value)
# #54
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)
# #55
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
# print(result)
# #56
# s = "Дань дурак играл в Клэш Рояль нищий всю практику"
# clean_s = s.lower().replace(" ", "")
# is_palindrome = clean_s == clean_s[::-1]
# print(is_palindrome)
# #57
# text = "Майнкрафт моя жизнь"
# word_count = len(text.split())
# print(word_count)
# #58
# import string
# text = "Дырк,дырк!дырк:дырк"
# clean_text = "".join(char for char in text if char not in string.punctuation)
# print(clean_text)
# #59
# text = "SWAGA"
# shift = 1
# encrypted = "".join(chr(ord(char) + shift) for char in text)
# print(encrypted)
# #60
# s = "Потолок,надо мной"
# print(s.title())
#61
# lst = [3, 1, 2, 3, 4, 1, 5]
# unique_ordered = list(dict.fromkeys(lst))
# #62
# def intersection(set1, set2):
#     return set1 & set2
# #63
# from collections import Counter
# text = "python"
# freq = Counter(text)
# #64
# d = {'a': 1, 'b': 2, 'c': 3}
# inverted = {v: k for k, v in d.items()}
# #65
# keys = ['name', 'age', 'city']
# values = ['Alice', 25, 'NY']
# result = dict(zip(keys, values))
#
# from decimal import Decimal, getcontext
# from fractions import Fraction
# # 66
# getcontext().prec = 6 # задаем общую точность
# result = Decimal(10) / Decimal(3)
# print(round(result, 5))
# # 67
# f1 = "1/3"
# f2 = "1/6"
# sum_fractions = Fraction(f1) + Fraction(f2)
# print(sum_fractions)
# # 68
# c1 = 2 + 3j
# c2 = 1 + 1j
# print(c1 + c2)
# print(c1 * c2)
# # 69
# c = 1 + 1j
# print(c ** 2)
# # 70
# num = 0.75
# print(Fraction(str(num)))


