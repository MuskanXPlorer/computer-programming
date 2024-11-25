'''count the vowels and consonants in a string'''
str = input("Enter the string: ")
vowel = 0
cons = 0
  for i in range(len(str)):
    if str[i]!=' ':
         if str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u" or str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U":
            vowel = vowel + 1
         else:
             cons = cons + 1
 print("total vowels: ",vowel)
 print("total consonants: ",cons)
