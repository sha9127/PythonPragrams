n=int(input('Enter Number To print Fibonacci Series : '))

x,y=0,1
temp=0

if n==1:
    print(x)
elif n==2:
    print(x,y)
elif n>2:
    print(x,y,end=' ')
    while (n>2):

        temp=x+y
        print(temp, end=' ')
        x,y=y,temp
        n-=1

else:
    print('Invalid Selection')