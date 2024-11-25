'''Write aprogram to check a  string is a pallindrome.'''
#input from user
st = input("enter your string: ")
#reverse of the string
out = st[::-1]
#pallin check
if st==out:
    print(True)
else:
    print(False)
