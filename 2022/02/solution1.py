total_score = 0
score_dict = {
    ('A', 'X'): 4, # 1 for rock + 3 for draw
    ('A', 'Y'): 8, # 2 for paper + 6 for win
    ('A', 'Z'): 3, # 3 for scissors + 0 for loss
    ('B', 'X'): 1, # 1 for rock + 0 for loss
    ('B', 'Y'): 5, # 2 for paper + 3 for draw
    ('B', 'Z'): 9, # 3 for scissors + 6 for win
    ('C', 'X'): 7, # 1 for rock + 6 for win
    ('C', 'Y'): 2, # 2 for paper + 0 for loss
    ('C', 'Z'): 6, # 3 for scissors + 3 for draw
}

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\02\\input.txt') as f:
    for line in f.readlines():
        game = tuple(line.rstrip('\n').split(' '))
        score = score_dict[game]
        total_score += score
    
    print('Total score: ' + str(total_score))
