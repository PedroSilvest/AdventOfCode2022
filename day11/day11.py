import operator

with open("day11/input.txt", "r") as file:
    f = file.read().split("\n\n")
    f = [x.split("\n") for x in f]


ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor
}

monkeys = []

class Monkey:
    def __init__(self, name, items, operation, divisible, true, false):
        self.name = name
        self.items = [int(x) for x in items]
        self.worry = []
        self.oper = operation[0]
        self.op = operation[1]
        self.divisible = divisible
        self.true = true
        self.false = false
        self.inspection = 0
        monkeys.append(self)

    def addItem(self, item):
        self.items.append(item)

    def WorryLevel(self, part):
        for index in range(len(self.items)):
            self.inspection += 1
            if self.op == "old":
                new = ops[self.oper](self.items[index], self.items[index])
            else:
                new = ops[self.oper](self.items[index], int(self.op))
            if part == 1:
                new = int(new/3)
            if part == 2:
                #print(new)
                new =  new % 9699690
                #print(new)
            if new % self.divisible == 0:
                #if part == 2:
                    #new = new / self.divisible
                location = [x for x in monkeys if x.name == self.true]
                location[0].addItem(new)
            else:
                #if part == 2:
                location = [x for x in monkeys if x.name == self.false]
                location[0].addItem(new)
        self.items = []
    
import math

print ("Natural logarithm of 14 is : ", end="")
print (math.log(4))




for monk in f:
    items = monk[1].replace("  Starting items: ","").split(", ")
    name = int(monk[0].replace("Monkey","").replace(":",""))
    operation = monk[2].replace("  Operation: new = old ", "").split()
    divisible = int(monk[3].replace("  Test: divisible by ", ""))
    true = int(monk[4].replace("    If true: throw to monkey ",""))
    false = int(monk[5].replace("    If false: throw to monkey ", ""))
    monkey = Monkey(name, items, operation, divisible, true, false)

for _ in range(20):
    for monkey in monkeys:
        monkey.WorryLevel(part = 1)


inspections = sorted([x.inspection for x in monkeys], reverse=True)
print(inspections)
print("task1: ", inspections[0]*inspections[1])



monkeys = []

for monk in f:
    items = monk[1].replace("  Starting items: ","").split(", ")
    name = int(monk[0].replace("Monkey","").replace(":",""))
    operation = monk[2].replace("  Operation: new = old ", "").split()
    divisible = int(monk[3].replace("  Test: divisible by ", ""))
    true = int(monk[4].replace("    If true: throw to monkey ",""))
    false = int(monk[5].replace("    If false: throw to monkey ", ""))
    monkey = Monkey(name, items, operation, divisible, true, false)

for _ in range(10000):
    for monkey in monkeys:
        monkey.WorryLevel(part = 2)

inspections = sorted([x.inspection for x in monkeys], reverse=True)
print(inspections)
print("task2: ", inspections[0]*inspections[1])