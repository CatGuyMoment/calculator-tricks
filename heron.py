square_root_to_calculate = float(input('x = ? '))
guess2 = 1
guess = square_root_to_calculate

iterations = int(input('iterations = ? '))

for i in range(iterations):
    guess = (guess + guess2) / 2
    guess2 = square_root_to_calculate / guess
    print(guess)