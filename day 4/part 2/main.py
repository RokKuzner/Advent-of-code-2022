with open('2022\\day 4\\input.txt') as f:
    data_rough1 = f.read()

data_rough2 = data_rough1.split('\n')

data_rough3 = []

for i in data_rough2:
    data_rough3.append(i.split(','))

data = []

for i in data_rough3:
    first_elf_IDs_rough = i[0]
    second_elf_IDs_rough = i[1]

    first_elf_IDs = []
    second_elf_IDs = []
    
    for a in range(int(first_elf_IDs_rough.split('-')[0]), int(first_elf_IDs_rough.split('-')[1])+1):
        first_elf_IDs.append(a)
    
    for a in range(int(second_elf_IDs_rough.split('-')[0]), int(second_elf_IDs_rough.split('-')[1])+1):
        second_elf_IDs.append(a)
    
    data.append([first_elf_IDs, second_elf_IDs])

contain_the_other = 0

for i in data:
    first_IDs = i[0]
    second_IDs = i[1]

    first_in_second = False
    second_in_first = False

    for a in first_IDs:
        if a in second_IDs:
            first_in_second = True
        else:
            pass
    
    for a in second_IDs:
        if a in first_IDs:
            second_in_first = True
        else:
            pass
    
    if second_in_first == True or first_in_second == True:
        contain_the_other += 1

print(contain_the_other)