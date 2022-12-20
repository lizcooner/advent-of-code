"""
Alternate solution using sets.
"""
total_overlaps = 0

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\04\\input.txt') as f:
    for line in f.readlines():
        line = line.rstrip('\n').replace('-', ',').split(',')
        line = [int(x) for x in line]
        
        pair_one = {item for item in range(line[0], line[1] + 1)}
        pair_two = {item for item in range(line[2], line[3] + 1)}

        check_pair_one = pair_one.difference(pair_two)
        check_pair_two = pair_two.difference(pair_one)

        if len(check_pair_one) == 0 or len(check_pair_two) == 0:
            total_overlaps += 1
        
    print('Total pairs that overlap: ' + str(total_overlaps))