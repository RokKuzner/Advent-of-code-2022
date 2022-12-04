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

fully_contain_the_other = 0

for i in data:
    first_IDs = i[0]
    second_IDs = i[1]

    first_in_second = True
    second_in_first = True

    for a in first_IDs:
        if a in second_IDs:
            pass
        else:
            first_in_second = False
    
    for a in second_IDs:
        if a in first_IDs:
            pass
        else:
            second_in_first = False
    
    if second_in_first == True or first_in_second == True:
        fully_contain_the_other += 1

print(fully_contain_the_other)