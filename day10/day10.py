with open("day10/input.txt","r") as file:
    f = [x.replace("\n","").split() for x in file.readlines()]

pixels = list("⬛" * 40 * 6)

def check_cycles(cycles):
    if cycles == 20:
        return True
    elif (cycles-20)%40 == 0:
        return True


def draw(cycle, x):
    if (cycle-1) % 40 in [x-1,x,x+1]: pixels[cycle-1] = '⬜'

def count():
    cycles = 0
    count = 1
    register = {}
    row = ""
    for x in f:
        if "noop" == x[0]:
            cycles += 1
            register[cycles] =  count
            draw(cycles, count)
        else:
            cycles += 1
            register[cycles] =  count
            draw(cycles, count)
            cycles += 1
            register[cycles] =  count
            draw(cycles,count)
            count += int(x[1])
    return register


part1 = count()
cycles = [x for x in range(20,221,40)]
print("task1: ", sum(part1[x] * x for x in part1 if x in cycles))
print("task2:")
for i in range(0, 201, 40):
	print("".join(pixels[i: i + 40]))


