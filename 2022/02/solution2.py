total_score = 0
score_dict = {
    ('A', 'X'): 3, # 3 for scissors(you) + 0 for loss
    ('A', 'Y'): 4, # 1 for rock(you) + 3 for draw
    ('A', 'Z'): 8, # 2 for paper(you) + 6 for win
    ('B', 'X'): 1, # 1 for rock(you) + 0 for loss
    ('B', 'Y'): 5, # 2 for paper(you) + 3 for draw
    ('B', 'Z'): 9, # 3 for scissors(you) + 6 for win
    ('C', 'X'): 2, # 2 for paper(you) + 0 for loss
    ('C', 'Y'): 6, # 3 for scissors(you) + 3 for draw
    ('C', 'Z'): 7, # 1 for rock(you) + 6 for win
}

with open('C:\\\\Users\\elizabeth.cooner\\Dev\\advent-of-code\\2022\\02\\input.txt') as f:
    for line in f.readlines():
        game = tuple(line.rstrip('\n').split(' '))
        score = score_dict[game]
        total_score += score
    
    print('Total score: ' + str(total_score))
