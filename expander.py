#nah, i'd win. DOMAIN EXPANSION!

def factorise(thingy,coeff):
    silly = 0
    new_list = []
    for i in thingy:
        silly = i + silly
        new_list.append(silly)
        silly = silly * -coeff
    return new_list


def draw_poly(lst):
    string = '('
    for i,v in enumerate(lst):
        if v != 0:
            power = len(lst) - i - 1
            if power == 0:
                string = string + str(v) + ') + ('

            elif v == 1:
                string = string +  'x^' + str(power) + ') + ('

            else:
                string = string + str(v) + 'x^' + str(power) + ') + ('


    return string[:-4]
 
def factors(n):
    result = []
    for i in range(1, int(abs(n)**0.5) + 1):
        if n % i == 0:
            result.append(i)
            result.append(-i)
            if i != abs(n) // i:
                result.append(n // i)
                result.append(-(n // i))
    return result




amount = int(input('degree = ? '))

 

silly_list = []

for i in range(amount,-1,-1):
    silly_list.append(float(input('input for degree '+ str(i)+' ')))


index = 0
factorList =  factors(silly_list[-1])
while index < len(factorList):
    factor = factorList[index]
    index += 1

    attempt = factorise(silly_list,factor)

    if attempt[-1] == 0:
        print('FACTOR: ' + draw_poly([1, factor]) )
        index = 0
        silly_list = attempt[:-1]

print('L. FACTOR: ', draw_poly(silly_list))
    


 
