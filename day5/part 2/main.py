with open('2022\\day5\\input.txt') as f:
    data_realy_rough = f.read()

data_rough1 = data_realy_rough.split('\n\n')

crates_rough = data_rough1[0]
movement_rough = data_rough1[1].split('\n')

movement = []
crates = []
indexes = []

for i in movement_rough:
    i_data = i.split(' ')

    movement.append([int(i_data[1]), int(i_data[3])-1, int(i_data[5])-1])

crates_lines = crates_rough.split('\n')

stacks = 0
count = 0
for i in crates_lines[-1]:
    if not i == ' ':
        stacks += 1
        crates.append([])
        indexes.append(count)

    count += 1

for i in crates_lines:
    count = 0
    for index in indexes:
        if not i[index] == ' ':
            crates[count].insert(0, i[index])

        count += 1

for i in crates:
    del i[0]

for i in movement:
    how_many_to_move = i[0]
    to_move = crates[i[1]][int(len(crates[i[1]])-how_many_to_move):]
    for a in to_move:
        crates[i[2]].append(a)
    del crates[i[1]][int(len(crates[i[1]])-how_many_to_move):]

result = ''
for i in crates:
    result += i[-1]

print('RESULT:', result)