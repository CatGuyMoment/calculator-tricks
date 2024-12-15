import math 
print("x^2 + ax + b = (x+j)(x+k)")
a = int(input("a = ?"))
b = int(input("b = ?"))
answer1 = 0
answer2 = 0
answer3 = 0
answer4 = 0
try:
    answer1 = (a+math.sqrt((a*a)-(4*b)))/2
    answer2 = (a-math.sqrt((a*a)-(4*b)))/2
    answer3 = (-a+math.sqrt((a*a)-(4*b)))/-2
    answer4 = (-a-math.sqrt((a*a)-(4*b)))/-2
    print( "j=",answer1,"k=",answer2, ";","j=",answer3,"k=",answer4)
except:
    print('failed: no "real" answer found')
