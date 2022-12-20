total_overlaps = 0

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\04\\input.txt') as f:
    for line in f.readlines():
        line = line.rstrip('\n').replace('-', ',').split(',')
        line = [int(x) for x in line]
        
        pair_one_size = line[1] - line[0] + 1
        pair_two_size = line[3] - line[2] + 1
        
        # Same size
        if pair_one_size == pair_two_size:
            if line[0] == line[2]:
                total_overlaps += 1
        
        # One > Two
        elif pair_one_size > pair_two_size:
            if line[2] >= line[0] and line[3] <= line[1]:
                total_overlaps += 1
        
        # Two > One
        else:
            if line[0] >= line[2] and line[1] <= line[3]:
                total_overlaps += 1
        
    print('Total pairs that overlap: ' + str(total_overlaps))