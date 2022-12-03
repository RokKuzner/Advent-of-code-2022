with open('\\Advent of code\\2022\\day1\\puzzle1\\input-real.txt') as f:
    input_rough_rough = f.read()

input_rough = input_rough_rough.split('\n\n')

my_input_real = []

for i in input_rough:
    my_input_real.append(i.split('\n'))

biggest = 0
biggest2 = 0
biggest3 = 0

for i in my_input_real:
    total_calories = 0

    for calory in i:
        total_calories += int(calory)

    if total_calories > biggest:
        if total_calories == biggest:
            pass
        else:
            biggest3 = biggest2
            biggest2 = biggest
            biggest = total_calories
    elif total_calories > biggest2:
        if total_calories == biggest2:
            pass
        else:
            biggest3 = biggest2
            biggest2 = total_calories
    elif total_calories > biggest3:
        if total_calories == biggest3:
            pass
        else:
            biggest3 = total_calories

print('Biggest:', biggest)
print('Three biggest sum:', int(int(biggest)+int(biggest2)+int(biggest3)))
