def task_1():
    """find elf with more item calories"""
    file = open("day1/input.txt", "r")
    count = 0
    save = []
    for line in file.readlines():
        if line.replace("\n","").isnumeric():
            count += int(line.replace("\n",""))
        else:
            save.append(count)
            count = 0
    save.append(count)
    return sorted(save, reverse=True)



def task_2(cal):
    """sum of the item calories of the 3 elfs with most calories"""
    return sum(calories[:3])


calories = task_1()
print(max(calories))
print(task_2(calories))
