
def task_1(f):
    """if input gives you what to play
    rock X, paper Y, scissors Z"""
    total_score = 0
    play_scr = {
        "X": 1,
        "Y": 2,
        "Z": 3}
    #rock, paper, scissors
    win_lose  = {
        "A": ["Z", "X", "Y"],
        "B": ["X", "Y", "Z"],
        "C": ["Y", "Z", "X"]
    } #[lose, draw, win]
    for line in f:
        play = line.split()
        total_score += play_scr[play[1]]
        ind = win_lose[play[0]].index(play[1])
        if ind == 1:
            total_score+=3
        if ind == 2:
            total_score+=6
    return total_score

def task_2(f):
    """if input tells you to lose, draw or win
    x lose, y draw, z win"""
    total_score = 0
    play_scr = {
        "X": 0,
        "Y": 3,
        "Z": 6}
    #draw, lose, win
    win_lose  = {
        "A": [3, 1, 2],
        "B": [1, 2, 3],
        "C": [2, 3, 1]
    } #[lose, draw, win]
    for line in f:
        play = line.split()
        score = play_scr[play[1]]
        total_score += score
        
        if score == 0:
            total_score+= win_lose[play[0]][0]
        elif score == 3:
            total_score+= win_lose[play[0]][1]
        else:
            total_score+= win_lose[play[0]][2]
    return total_score

file = open("day2/input.txt","r")
f = file.readlines()
file.close()
result = task_1(f)
result2 = task_2(f)
print("task1: ", result)
print("task2: ", result2)

