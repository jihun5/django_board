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
