import math


i=0
f = [None]*10000
while True:
    if i == 0:
        t = input("Type constant value (c)\n (You can use e and π by just typing 'e' and 'π' or 'pi') \n >>> ")
    else:
        t = input(f"Enter coefficient of x in {i}th degree. ('-' to stop input) \n (You can use e and π by just typing 'e' and 'π' or 'pi') \n >>>")
    
    if t == '-':
        break
    elif t=='π' or t=='pi' or t=='Π':
        t = math.pi
    elif t=='e' or t=='E':
        t = math.e
    else:
        try:
            t = float(t)
            f[i]=t
            i+=1
        except ValueError:
            print('Please input a real number, π or e')


i-=1
print(f"The degree of the polynomial is {i} \n")


x1 = input("Value 1 of closed interval \n (You can use e and π by just typing 'e' and 'π' or 'pi') \n >>> ")
if x1 == 'π' or x1 == 'pi':
    x1 = math.pi
if x1 == 'e':
    x1 = math.e
x2 = input("Value 2 of closed interval \n (You can use e and π by just typing 'e' and 'π' or 'pi') \n >>> ")
if x2 == 'π' or 'pi':
    x2 = math.pi
if x2 == 'e':
    x2 = math.e
while x1>x2:
    print('Error!\n' \
    'Value 1 must be smaller than Value 2')
    x1 = input("Value 1 of closed interval \n (You can use e and π by just typing 'e' and 'π' or 'pi') \n >>> ")
    if x1 == 'π' or x1 == 'pi':
        x1 = math.pi
    if x1 == 'e':
        x1 = math.e
    x2 = input("Value 2 of closed interval \n (You can use e and π by just typing 'e' and 'π' or 'pi') \n >>> ")
    if x2 == 'π' or 'pi':
        x2 = math.pi
    if x2 == 'e':
        x2 = math.e

if x1 == int(x1):
    x1 = int(x1)

if x2 == int(x2):
    x2 = int(x2)

print(f"Searching for roots in: [{x1},{x2}] \n")


f1 = 0
for s in range(i+1):
    term= f[s]*(pow(x1,s))
    f1+=term
if (f1/math.pi == int(f1/math.pi)):
    print(f"f({x1})={f1/math.pi}π")
elif (f1/math.e == int(f1/math.e)):
    print(f"f({x1})={f1/math.e}e")
else:
    print(f"f({x1})={f1}")

f2 = 0
for s in range(i+1):
    term= f[s]*(pow(x2,s))
    f2+=term
if (f2/math.pi == int(f2/math.pi)):
    print(f"f({x2}) = {f2/math.pi}π")
elif (f2/math.e == int(f2/math.e)):
    print(f"f({x2}) = {f2/math.e}e")
else:
    print(f"f({x2})={f2}")

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
        print(f"The function is >0 in [{x1},{x2}]")
    else:
        print(f"The function is <0 in [{x1},{x2}]")







