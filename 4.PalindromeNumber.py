n=int(input('Enter Number to Reverse :'))

temp=n;
rev=0
while(temp!=0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10

print('Revesesd no is :',rev)

if rev==n:
    print('No is Palindrome')
else:
    print('No is not Palindrome')
