'''Write a function to check if one string is a rotation of another string.'''
#input the string 
str1 = input("enter the string1: ")
str2 = input("enter the string2: ")
flag = 0
#rotating the string
for i in range(len(str1)):
     str1 = str1[-1] + str1[:len(str1)-1]
     if str1 == str2:
          flag = 1
          break
#check the string
if flag == 1:
     print(True)
else:
     print(False)

 
