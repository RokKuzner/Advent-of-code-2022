with open('\\Advent of code\\2022\\day3\\input.txt') as f:
    rough_data1 = f.read()

alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'I':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

rough_data2 = rough_data1.split('\n')

data = []
for i in rough_data2:
    data.append([i[0:int(len(i)/2)], i[int(len(i)/2):]])

same_lettrs = []

for i in data:
    comp1 = i[0]
    comp2 = i[1]

    the_same_letters = ''
    for letter in comp1:
        for l in comp2:
            if letter == l:
                the_same_letters += letter
    
    if len(the_same_letters) > 0:
        same_lettrs.append(the_same_letters[0])

my_sum = 0
for i in same_lettrs:
    my_sum += alphabet[i]

print(my_sum)
