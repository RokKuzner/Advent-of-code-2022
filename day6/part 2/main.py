with open('2022\\day6\\input.txt') as f:
    data = f.read()

count = 0
charecters_procesed = 0

for i in range(int(len(data))-13):
    possible_marker = data[count:count+14]

    letters_in_marker = []
    for letter in possible_marker:
        letters_in_marker.append(letter)

    is_unique = True
    allready_checked = []
    for letter in letters_in_marker:
        if letter in allready_checked:
            is_unique = False
        allready_checked.append(letter)
    
    if is_unique == True:
        charecters_procesed = count+14
        break

    count += 1

print(charecters_procesed)