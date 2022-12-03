import string

#task1
def task_1(dic,f):
    """find the duplicate item in each inventory 
    and get the total value of items duplicated"""
    val = 0
    for x in f:
        x = x.replace("\n","")
        st1, st2 = x[:int(len(x)/2)], x[int(len(x)/2):]
        dup = [c for c in st1 if c in st2]
        val += dic[dup[0]]
    return val

#task2
def task_2(dic,f):
    """get the equal item (badge)for each team of elfs (3 elfs per team)
    and get the total value of badges """
    val = 0
    for x in range(0,len(f),3):
        elf1, elf2, elf3 = f[x].replace("\n",""), f[x+1], f[x+2]
        dup = [c for c in elf1 if c in elf2 and c in elf3]
        val += dic[dup[0]]
    return val



cha = string.ascii_letters

dic = {}
for ind in range(len(cha)):
    dic[cha[ind]] = ind+1

file = open("day3/input.txt", "r")
f = file.readlines()
file.close()

print(task_1(dic, f))
print(task_2(dic, f))