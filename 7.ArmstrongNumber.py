n=input('Enter Number to Reverse :')

order=len(n)
temp=int(n);
sum=0
while(temp!=0):
    rem=temp%10
    sum=sum+rem**order
    temp=temp//10

print('Armstrong no is :',sum)

if sum==int(n):
    print('No is ArmStrong')
else:
    print('No is not ArmStrong')
