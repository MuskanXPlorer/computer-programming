'''Write a Python program that takes an encrypted message and a shift value, then prints the decrypted message.'''
#input from user
message = input("enter your message")
shift = int(input("enter the shift: "))
decrypt = ''
#decrypted the message
for i in message:
    if 'A' <= i <= 'Z':
        new_i = chr(((ord(i) - ord('A') - shift )%2 )+ ord('A'))
        decrypt = decrypt + new_i 
    elif 'a' <= i<= 'z':
        new_i = chr(((ord(i) - ord('a')-shift)%2 + ord('a')))
        decrypt = decrypt + new_i
    else:
        decrypt = decrypt + i
#output
print(decrypt)
        
        
