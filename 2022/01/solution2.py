max_calories = []
counter = 0

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\01\\input.txt') as f:
    data = f.read().split('\n')
    for line in data:
        if line == '':
            if len(max_calories) < 3:
                max_calories.append(counter)
            elif counter > min(max_calories):
                max_calories.remove(min(max_calories))
                max_calories.append(counter)
            counter = 0
        else:
            counter += int(line)
    
    # Final counter check for EOF
    if counter > min(max_calories):
        max_calories.remove(min(max_calories))
        max_calories.append(counter)

    print("Total max_calories: " + str(sum(max_calories)))