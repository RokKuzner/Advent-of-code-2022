with open('C:\\Users\\LENOVO\\Documents\\Advent of code\\2022\\day2\\input.txt') as f:
    data_rough = f.read()

data = data_rough.split('\n')

score = 0
for i in data:
    one_score = 0

    look = ''

    if i[2] == 'X':

        if i[0] == 'A':
            look = 'A Z'
        elif i[0] == 'B':
            look = 'B X'
        elif i[0] == 'C':
            look = 'C Y'
        else:
            print('ELSE IN FIRST SUBMAIN')

    elif i[2] == 'Y':

        if i[0] == 'A':
            look = 'A X'
        elif i[0] == 'B':
            look = 'B Y'
        elif i[0] == 'C':
            look = 'C Z'
        else:
            print('ELSE IN FIRST SUBMAIN')

    elif i[2] == 'Z':

        if i[0] == 'A':
            look = 'A Y'
        elif i[0] == 'B':
            look = 'B Z'
        elif i[0] == 'C':
            look = 'C X'
        else:
            print('ELSE IN FIRST SUBMAIN')











    if look[2] == 'X':
        one_score += 1

        if look[0] == 'A':
            one_score += 3
        elif look[0] == 'B':
            one_score += 0
        elif look[0] == 'C':
            one_score += 6
        else:
            print('ELSE IN SUBMAIN')

    elif look[2] == 'Y':
        one_score += 2

        if look[0] == 'A':
            one_score += 6
        elif look[0] == 'B':
            one_score += 3
        elif look[0] == 'C':
            one_score += 0
        else:
            print('ELSE IN SUBMAIN')

    elif look[2] == 'Z':
        one_score += 3

        if look[0] == 'A':
            one_score += 0
        elif look[0] == 'B':
            one_score += 6
        elif look[0] == 'C':
            one_score += 3
        else:
            print('ELSE IN SUBMAIN')
    else:
        print('ELSE IN THE MAIN')

    score += one_score



print('SCORE:', score)