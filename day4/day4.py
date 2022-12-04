

#task1
def task_1(f):
    """find how many elves with their numbers entirely in the other"""
    count = 0
    for line in f:
        line = line.replace("\n","").split(",")
        elf1 = line[0].split("-")
        elf2 = line[1].split("-")
        elf1 = [x for x in range(int(elf1[0]), int(elf1[1])+1)]
        elf2 = [x for x in range(int(elf2[0]), int(elf2[1])+1)]
        elf2in1 = [c in elf1 for c in elf2]
        elf1in2 = [c in elf2 for c in elf1]
        if False not in elf2in1 or False not in elf1in2:
            count += 1

    return count

#task2
def task_2(f):
    """find how many elves have their numbers in others"""
    count = 0
    for line in f:
        line = line.replace("\n","").split(",")
        elf1 = line[0].split("-")
        elf2 = line[1].split("-")
        elf1 = [x for x in range(int(elf1[0]), int(elf1[1])+1)]
        elf2 = [x for x in range(int(elf2[0]), int(elf2[1])+1)]
        elf2in1 = [c in elf1 for c in elf2]
        if any(elf2in1):
            count += 1
    return count



file = open("day4/input.txt", "r")
f = file.readlines()
file.close()
print("task_1: ", task_1(f))
print("task_2: ", task_2(f))