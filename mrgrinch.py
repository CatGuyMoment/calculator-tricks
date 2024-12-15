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



amount = int(input('degree = ? '))

 

silly_list = []

for i in range(amount,-1,-1):
    silly_list.append(float(input('input for degree '+ str(i)+' ')))

 

c = float(input('factor: (x + ?)  '))

 

new_list = factorise(silly_list,c)


print('quotient: ' + draw_poly(new_list[:-1]))
print('remainder: ' + str(new_list[-1]))
    
# print('= [ ' + draw_poly([1,c]) + ' ] * [ ' + draw_poly(new_list[:-1]) + ']  + ' + str(new_list[-1]))