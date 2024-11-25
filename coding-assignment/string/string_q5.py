'''Write a program to remove the Duplicate items in the string'''
st = input("enter your string")
reg = ' '
for i in st:
    if st.count(i)==1:
        if i not in reg:
            reg += i
for i in reg:
    print(i)
