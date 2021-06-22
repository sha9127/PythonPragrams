n=int(input('Enter a number to check Prime Number: '))
#x=True

for i in range(2,n):
    if n%i==0:
        x=False
        break
    else:
        x=True

if x==True:
    print('No is  Prime')
else:
    print('No is not Prime')