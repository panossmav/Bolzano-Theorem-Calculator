import math

i=0
f = [None]*10000
while True:
    if i == 0:
        t = input('Type constant value (c) \n >>> ')
    else:
        t = input(f"Enter coefficient of x in {i}th degree. ('-' to stop input) \n >>>")
    
    if t == '-':
        break
    else:
        t = float(t)
        f[i]=t
        i+=1

i-=1
print(f"The degree of the polynomial is {i} \n")


x1 = float(input('Value 1 of closed interval \n >>> '))
x2 = float(input('Value 2 of closed interval \n >>>'))
while x1>x2:
    print('Error!\n' \
    'Value 1 must be smaller than Value 2')
    x1 = float(input('Value 1 of the closed interval \n >>> '))
    x2 = float(input('Value 2 of the closed interval \n >>>'))

print(f"Searching for roots in: [{x1},{x2}] \n")


f1 = 0
for s in range(i+1):
    term= f[s]*(pow(x1,s))
    f1+=term
print(f"f(1)={f1}")

f2 = 0
for s in range(i+1):
    term= f[s]*(pow(x2,s))
    f2+=term
print(f"f(2)={f2}")

if f1*f2 == 0:
    if f1 == 0:
        print(f"Root was found! ξ={f1}")
    else:
        print(f"Root was found! ξ={f2}")
elif f1*f2<0:
    print(f"At least one real root exists in  ({x1},{x2}) (Bolzano Theorem)\n")

else:
    print(f"There are no real roots of this function in [{x1},{x2}]. \n")
    if f1>0:
        print(f"The function is <0 in [{x1},x2]")
    else:
        print(f"The function is <0 in [{x1},x2]")







