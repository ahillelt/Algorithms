import math

def base10_size(num): #alternative exists
    string_num = str(num)
    length = len(string_num)
    return int(length)

def karatsuba(x,y):
    if x<10 or y<10: #or len(str(x)) == 1 or len(str(y)) == 1, but single comparison felt more efficient then converting to string and then calling len
        return (x*y)
    else:
        n = max(base10_size(x),base10_size(y)) #or we can call in-line "max(len(str(x)),len(str(y)))". essentially same
        middle = int(n/2)

        a= int(x/pow(10,middle))
        b= int(x%pow(10,middle))
        c= int(y/pow(10,middle))
        d= int(y%pow(10,middle))

        p = a+b
        q = c+d

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        pq = karatsuba(p,q)
        adbc = pq - ac - bd

        result =(pow(10,middle*2)*ac) + (pow(10,middle)*adbc) + bd
        return result

###################################

num1 = int(input("num1: "))
num2 = int(input("num2: "))

results = karatsuba(num1,num2)
print("result: ", results)
