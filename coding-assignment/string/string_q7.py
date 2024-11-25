'''Write a program that takes a list of names, rearranges them so that names starting with a vowel come first, and then prints the rearranged list.'''
#input from user
str = input("Enter the string: ")
x = ''
st = ''
v = 'aeiouAEIOU'
l = str.split()
print(l)
#for rearangement
for i in l:
    if i[0] in v:
        st = st + i +' '
    else:
        x = x + i + ' '
#output
print(st + x)
