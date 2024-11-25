'''Write a program to count the frequency of each character in a given string.'''
st = input("enter your string: ")
reg = ''
for i in st:
     if i not in reg:
       c = st.count(i)
       out = (f'{i}:{c}')
       reg += i
print(out)
