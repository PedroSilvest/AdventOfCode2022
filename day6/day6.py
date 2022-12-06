file = open("day6/input.txt", "r")
f = file.read()
file.close()

#task_1
signal_t1 = [set([f[x],f[x+1], f[x+2], f[x+3]]) for x in range(len(f)-4)]
signal_t1pos = [x+4 for x in range(len(signal_t1)) if len(signal_t1[x]) == 4][0]

#task_2

signal_t2 = [set([f[x+i] for i in range(14)]) for x in range(len(f)-14)]
signal_t2pos = [x+14 for x in range(len(signal_t2)) if len(signal_t2[x]) == 14][0]

print("task1: ", signal_t1pos)
print("task2: ", signal_t2pos)
