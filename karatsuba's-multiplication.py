#! /usr/bin/python


def karatsuba(x, y):

    shift = int(len(str(x)) /2)
    shift2 = int(len(str(y)) /2)

    if(shift == 1 or shift2 == 1  or shift == 0 or shift2 == 0):
        return x * y

    a = int(x / (10 ** shift))

    b = int(x - (a* (10 ** shift)))

    print(a)
    print(b)

    c = (int(y / (10 ** shift))) 

    d = int(y - (c* (10 ** shift)))

    print(c)
    print(d)
    
    res1 = karatsuba(a, c)


    res2 = karatsuba(a, d)
 

    res3 = karatsuba(b, c)


    res4 = karatsuba(b, d)


    return ((10 ** (shift*2))* res1) + ((10**shift)*(res2 + res3)) + res4

    


ans = karatsuba(1234, 5678)

print(" 1234 x 5678 = ", ans)

    
