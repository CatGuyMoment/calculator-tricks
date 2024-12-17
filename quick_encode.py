a = int(input('a = ?'))
b = int(input('b = ?'))

while True:
    letter = ord(input('letter = ?').lower()) - ord('a')

    print('start ordinal:',letter)

    new_letter = (a*letter + b ) %26

    print('end ordinal:',new_letter)

    print(chr(new_letter + ord('a')))