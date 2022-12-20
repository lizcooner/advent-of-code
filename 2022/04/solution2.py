total_overlaps = 0

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\04\\input.txt') as f:
    for line in f.readlines():
        line = line.rstrip('\n').replace('-', ',').split(',')
        line = [int(x) for x in line]
        
        pair_one = [item for item in range(line[0], line[1] + 1)]
        pair_two = [item for item in range(line[2], line[3] + 1)]

        if max(pair_one) in pair_two or max(pair_two) in pair_one:
            total_overlaps += 1
        
    print('Total pairs that overlap: ' + str(total_overlaps))