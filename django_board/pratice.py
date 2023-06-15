# 
# angle = int(input("각도를 입력해주세요:"))
# if angle < 90 :
#     answer = 1
# elif angle == 90:
#     answer = 2
# elif 90 < angle < 180:
#     answer = 3
# elif angle == 180:
#     answer =4
# print(answer)

# num_list = [1,2,3,4,5]
# answer = []
# result = []
# for a in num_list:
#     if a % 2 == 0:
#         answer.append(a)
#     elif a % 2 != 0:
#         result.append(a)
# print(answer)
# print(result)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(sum(numbers)/len(numbers))
# num = 0
# for a in numbers:
#     num += a
# print(num/len(numbers))

# array = [1,1,2,3,4,5]
# print(array.count(1))

# s1 = ["a","b","c"]
# s2 = ["com","b","d","p","c"]
# answer = 0
# for a in s1:
#     if a in s2:
#         answer += 1
# print(answer)

# for a in s2: # a는 com, b, d p c
#     if a in s1:
#         answer += 1
# print(answer)

# array = [1,2,7,10,11]
# print(len(array)//2)
# print(array[2])

# my_string = "abcdef"
# letter = "f"
# # result = "abcde"
# print(my_string.replace(letter, ""))

# 피자 조각 수 slice와 피자를 먹는 사람의 n이 매개변수로 주어질 때
# n명의 사람이 최소 한조각 이상을 먹으려면 최소 피자 몇판을 시켜야 하는가?

# slice = int(input("피자 조각 수 : "))
# n = int(input("사람의 수 : "))
# answer = 0
# if n%slice != 0:
#     print(n//slice + 1)
# elif n % slice == 0:
#     print(n//slice)

# strlist = ["we","are","the","world!"]
# result = [2,3,3,6]
# answer = []
# for a in strlist:
#     answer.append(len(a))
# print(answer)

# mySting = "aBcDefg"
# print(mySting.upper())

# n = 1234
# num = 0
# for a in str(n):
#     num += int(a)
# print(num)

# str1 = "aaaaa"
# str2 = "bbbbb"
# answer = ""
# print(str1[-1])
# print(len(str1))
# for a in range(len(str1)):
#     answer += str1[a]+str2[a]
# print(answer)
# str[a]도 가능하다

# num_list = [3,4,5,2,1]
# result = 393 # 351+42
# A1 = []
# A2 = []
# answer = 0
# for a in num_list:
#     if a % 2 != 0:
#         A1.append(a)
#     elif a % 2 == 0:
#         A2.append(a)
# print(int("".join(map(str,A1)))+int("".join(map(str,A2))))
# map 함수는 첫번째는 매개변수로 함수가 오고, 
# 두번째는 반복가능한 자료형이온다
# 두번째 인자로 들어온 자료형을 첫번째 들어온 함수에 하나씩 집어넣는다
# "".join(리스트) ["a","b","c"] = "abc"
# '_'.join(리스트) = "a_b_c"

# start = 3
# end = 10
# answer = []
# for a in range(start, end+1):
#     answer.append(a)
#     answer.sort(reverse=True)
# print(answer)
# list.sort(reverse=True) 리스트 거꾸로 정렬하기

# my_string = "cvsgiorszzzmrpaqpe"
# index_list = [16,6,5,3,12,14,11,11,17,12,7]
# lista = list(my_string)
# print(lista)
# answer = []
# for a in index_list:
#     answer.append(lista[a])
# print(answer)
# print("".join(answer))

# print("".join([my_string[i] for i in index_list]))

# my_string = "banana"
# is_suffix = "ana"
# # result = 1
# for a in my_string:
#     if a in is_suffix:
#         answer = 1
# print(answer)

# answer_list = [my_string[i:] for i in range(len(my_string))]
# # 1 if is_suffix in answer_list else 0
# if is_suffix in answer_list:
#     answer = 1
# else:
#     answer = 0
# print(answer)

# strArr = ["and","notad","abcd"]
# # remove = ad
# for a in strArr:
#     if "ad" not in a:
#         print(a)

# my_string = " programers "
# answer = my_string.strip().split()
# print(answer)
# split과 strip을 같으 쓰거싶거든
# strip을 먼저 쓰고 split을 쓰면 된다.

# arr = [5,1,4]
# answer = []
# for a in arr: # a = 5, 1, 4
#     temp = [a]*a # [5]*f 
#     answer += temp
# print(answer)
# Arr = [1,2,3]
# print(Arr[0]*4)
# A = [5]*5
# print(A) list의[a] 번째를 인덱싱 하면 애는 list의 숫자값이 나오고
# 반면이 [] 빈 리스트에다가 숫자를 곱하면 리스트가 나오니까
# 위는 값 * 숫자, 아래는 리스트 * 숫자가 되는것이다. 

# num_str = "123456789"
# num = 0
# for a in num_str:
#     num += int(a)
# print(num)

# num = list(map(int, num_str))
# print(sum(num))

#####################################################

# arr = [293, 1000, 395, 678, 94]
# delete = [94,777,104,1000,1,12]
# answer = []
# for a in arr:
#     if a not in delete:
#         answer.append(a)
# print(answer)

# array = [1,8,3]
# result = [8,1]
# max1 = max(array)
# print(array.index(max1))
# answer = []
# answer.append(max1)
# answer.append(array.index(max1))
# print(answer)

# my_string = "hello"
# lista = list(my_string)
# num1 = 1
# num2 = 2
# temp = []
# temp = lista[num1] # e 
# lista[num1] = lista[num2] # e = l
# lista[num2] = temp # l = e 
# answer = ''.join(lista)
# print(answer)

# i = 1
# j = 13
# k = 1
# answer = 0
# num = []
# for a in range(i, j+1):
#     if str(k) in str(a):
#         num.append(a)
# str(num)
# answer = str(num).count(str(k))
# print(answer)

# answer = 0
# num =  []
# for a in range(i, j+1):
#     if str(k) in str(a):
#         num.append(a)
# print(str(num))
# answer = str(num).count(str(k))
# print(answer)

# score = [[80,70],[90,50],[40,70],[50,80]]
# # result = [1,2,4,3]

# avg = []
# print(sum(score[0]))
# for a in range(len(score)):
#     avg.append(sum(score[a])/len(score[0])) 평균까지 구했어
# result = sorted(avg)
# result.reverse()
# answer = []
# for i in avg:
#     answer.append(result.index(i)+1)
# print(answer)

# 리스트.sort() 는 
# 본체의 리스트를 정렬해서 변환하는 것이고,
# sorted(리스트) 는 
# 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.

# numbers = [1,2,3]
# direction = "right"
# result = [3,1,2]
# numbers = [4,455,6,4,-1,45,6]
# direction = "left"
# result = [455,6,4,-1,45,6,4]
# answer = []
# if direction == "right":
#     a = numbers.pop()
#     numbers.insert(0, a)
# elif direction == "left":
#     b = numbers.pop(0)
#     numbers.append(b)
# print(numbers)

# emergency = [3, 76, 24]
# # result = [3,1,2]
# emergency.sort()
# emergency.reverse()
# print(emergency)
# # A = emergency.index(76)
# # for a in emergency:
# max1 = emergency[0]
# max2 = emergency[1]
# min1 = emergency[2]
# A = emergency.index(max1)+1
# print(A)
# answer = []
# B = emergency.index(max2)+1
# C = emergency.index(min1)+1
# answer.append(A)
# answer.append(B)
# answer.append(C)
# print(answer)

# emergency = [3, 76, 24]
# answer = []
# temp = sorted(emergency, reverse=True) # 76 24 3 
# for a in emergency:
#     answer.append(temp.index(a)+1)
# print(answer)    

# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# # result = [[4,6],[7,9]]
# # answer = arr1[0][0]+arr2[0][0]
# # A = arr1[0]
# # B = arr1[1]
# # print(arr1+arr2)
# num = []
# for a in range(len(arr1)): # a = 0, 1
#     num.append(arr1[0][a]+arr2[0][a])
# print(num)
# for a in range(len(arr1)):
#     num.append(arr1[1][a]+arr2[1][a])
# print(num)

# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# answer = []
# for a in range(len(arr1)):  # a = 0, 1
#     temp = []
#     for b in range(len(arr1[a])): # b = 0, 1    
#         temp.append(arr1[a][b]+arr2[a][b])
#     answer.append(temp)
# print(answer)

# lista = ['A',"A","B","O","O","AB","AB"]
# dicta = {}
# for a in lista:
#     if a not in dicta.keys():
#         dicta[a] = lista.count(a)
# print(dicta)

# sum = 0
# a = 0
# while a<100:
#     a += 1
#     if a%2 != 0:
#         sum += a
# print(sum)

# sum = 0
# a = 0
# while a< 100:
#     a += 1
#     if a%2 ==0:
#         sum += a
# print(sum)

# for b in range(1, 10):
#     for a in range(1, 10):
#        print(f"{b} x {a} = {b*a}")

# # 이중 for문 사용하여 구구단 출력하기
# for a in range(1, 10):
#     for b in range(1, 10):
#         print(f"{a} X {b} = {a*b}")

# temp = []
# lista = [93,45,21,30,20,94,66,71,45]
# for a in range(len(lista)-1): # 자릿수를 정헤야 하고 -1하는 이유는 마지막 숫자는 비교할 필요가 없기때문에
#     for b in range(a+1, len(lista)): #a+1은 자기자신과의 비교를 피하기 위해, 
#                                         #범위를 a번째로 설정해야 하나씩 줄여나갈 수 있다.
#         if lista[a] > lista[b]:
#             temp = lista[a]
#             lista[a] = lista[b]
#             lista[b] = temp
# print(lista)    

# add = lambda x,y : x+y
# print(add(1,2))
# mul = lambda x,y : x*y
# print(mul(2,3))
# minus = lambda x, y : x-y
# print(abs(minus(1,3)))

# def oddTest(x):
#     if x %2 ==0:
#         return True
#     else :
#         return False
# print(oddTest(2))
# oddornot = lambda x : True if x%2 ==0 else False
# print(oddornot(3))

# lista = [10,20,30,40,50]
# def recur(lista, total_list, temp_list, n, m):
#     if m == 0:
#         total_list.append(temp_list[:])
#         return
#     for a in range(n, len(lista)):
#         temp_list.append(lista[a])
#         recur(lista,total_list,temp_list,a+1, m-1)
#         temp_list.pop()
# input1 = [10,20,30,40,50]
# total_list = []
# input2 = 3
# recur(input1, total_list, [], 0, input2)
# print(total_list)

# import math
# lista = [1.1, 2.2, 3.3]
# # A = list(map(int, lista))
# # print(A)
# # B = list(map(str, lista))
# # print(B)
# A = lambda x : x**2
# print(A(5))

# a = 12345
# A = list(map(int,str(a).split()))
# print(A)
# lista = []
# for a in A:
#     lista.append(str(a))
# print(lista)

# for a in range(1,10):
#     for i in range(1, a+1):
#         print('*', end="")

# class Person:
#     def __init__(self, name, age, gender, email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#     def register(self):
#         self.myinfo = self.name + " " + self.age + " "+ self.gender + " " + self.email
# p1 = Person("홍길동", "19", "남","hong@naver.com")
# p1.register()
# print(p1.myinfo)

# while True:
#     first = int(input("분자를 입력해주세요"))
#     second = int(input("분모를 입력해주세요"))
#     try:
#         first = int(input("분자를 입력해주세요"))
#         second = int(input("분모를 입력해주세요"))
#         first/second
#     except Exception:
#         print("오류입니다")    

# class Bird:
#     def fly(self):
#         raise Exception
# class Eagle(Bird):
#     def fly(self):
#         print("fly fly")
#     pass
# eagle1 = Eagle()
# eagle1.fly()

