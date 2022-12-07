import re

with open("day7/input.txt", "r") as file:
    f = file.read()
    f = f.split("\n")

locs = []

class Dir:
    def __init__(self, name, parent):
        self.name, self.parent = name, parent
        self.children = {}
        self.file_size = 0
        locs.append(self)
    
    def addChildren(self, name):
        self.children[name] = Dir(name, self)
    
    def addFileSize(self, add):
        self.file_size += add

    def getParent(self):
        return self.parent

    def getChild(self, name):
        return self.children[name]
    
    def getSize(self):
        return self.file_size + sum([x.getSize() for x in self.children.values()])

dir = Dir("/", None)

for x in range(1, len(f)):
    if "dir" in f[x]: dir.addChildren(f[x][4:])
    if re.findall("\d+", f[x]): dir.addFileSize(int(f[x].split()[0]))
    if "$ cd .." == f[x]: dir = dir.getParent()
    elif "$ cd " in f[x]: dir = dir.getChild(f[x][5:])

print("task1: ", sum([dir.getSize() for dir in locs if dir.getSize() <= 100000]))



l = [dir.getSize() for dir in locs if  70000000 - locs[0].getSize() + dir.getSize() >= 30000000]
print("task2: ", sorted(l)[0])