
from copy import deepcopy

def get_cargo(f):
    """get cargo list"""
    l = [[] for i in range(9)]
    cargo = f[:8]
    for ind in range(len(cargo)):
        place = 0
        for j in range(1,35,4):
            if " " != cargo[ind][j]:
                l[place].append(cargo[ind][j])
            place += 1
    return l



def task_1(cargo, move):
    """moves cargo"""
    for x in move:
        mov = x.split()
        to_move = cargo[int(mov[1])-1][:int(mov[0])] #tz
        cargo[int(mov[1])-1] = cargo[int(mov[1])-1][int(mov[0]):]
        for to in to_move:
            cargo[int(mov[2])-1].insert(0, to)
    return cargo


def task_2(cargo, move):
    """moves cargo in the same order"""
    for x in move:
        mov = x.split()
        to_move = cargo[int(mov[1])-1][:int(mov[0])] #tz
        to_move = to_move[-1::-1] # zt cuz z on top
        cargo[int(mov[1])-1] = cargo[int(mov[1])-1][int(mov[0]):]
        for to in to_move:
            cargo[int(mov[2])-1].insert(0, to)
    return cargo



file = open("day5/input.txt", "r")
f = file.readlines()
file.close()
move = [x.replace("\n","").replace("move","").replace("from","").replace("to","") for x in f[10:]]
cargo1 = get_cargo(f)
cargo2 = deepcopy(cargo1)
cargo = task_1(cargo1, move)
print("task_1: ", "".join(cargo[i][0] for i in range(len(cargo))))
cargo = task_2(cargo2, move)
print("task_2: ", "".join(cargo[i][0] for i in range(len(cargo))))