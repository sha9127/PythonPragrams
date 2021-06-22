s=input('Enter string to Reverse :')

x=''
for i in s:
    x=i+x
print(x)

if s==x:
    print('String is palindrome')
else:
    print('String is not Palindrome')