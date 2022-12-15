max_calories = 0
counter = 0

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\01\\input.txt') as f:
    data = f.read().split('\n')
    for line in data:
        if line == '':
            if counter > max_calories:
                max_calories = counter
            counter = 0
        else:
            counter += int(line)

    print("Final max_calories: " + str(max_calories))