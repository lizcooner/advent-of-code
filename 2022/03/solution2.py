total_priority = 0
priority_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33,
    'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
    'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49,
    'X': 50, 'Y': 51, 'Z': 52,
}

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\03\\input.txt') as f:
    data = f.read().split('\n')
    groups = int(len(data) / 3)
    pointer = 0

    # Build a list for each group
    for i in range(groups):
        group_list = []
        for j in range(3):
            group_list.append(data[pointer])
            pointer+=1

        # Now check for the matching item
        for item in group_list[0]:
            if item in group_list[1] and item in group_list[2]:
                total_priority += priority_dict[item]
                break

print('Total priority: ' + str(total_priority))
        
