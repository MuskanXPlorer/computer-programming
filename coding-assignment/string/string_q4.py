'''Write a program to find the first character in a string that does not repeat.'''   
st = input("enter your string")
for i in st:
     if st.count(i)==1:
       print(i)
       break 
print()
