with open("day8/input.txt", "r") as file:
    f = file.read().split("\n")


trees = [[int(y) for y in x] for x in f]


#task1
visible = 0
for i in range(len(trees[0])):
        for j in range(len(trees)):
            left = [x for x in range(len(trees[0])) if trees[i][x] >= trees[i][j] and j < x]
            right = [x for x in range(len(trees[0])) if trees[i][x] >= trees[i][j] and j > x]
            up = [x for x in range(len(trees)) if trees[x][j] >= trees[i][j] and i < x]
            down = [x for x in range(len(trees)) if trees[x][j] >= trees[i][j] and i > x]
            if left == [] or up == [] or down == [] or right == []:
                visible += 1

print("task1: ", visible)

#task2
prev = 0
for i in range(len(trees[0])):
        for j in range(len(trees)):
            left, right, up, down = 0,0,0,0
            for x in range(j, -1, -1): #left
                if trees[i][x] < trees[i][j] and j > x: left += 1
                elif j == x: continue
                else:
                    left += 1
                    break
            for x in range(j,len(trees[0])): #right
                if trees[i][x] < trees[i][j] and j < x: right += 1
                elif j == x: continue
                else:
                    right += 1
                    break
            for x in range(i, -1, -1): #top
                if trees[x][j] < trees[i][j] and i > x: up += 1
                elif i == x: continue
                else:
                    up += 1
                    break
            for x in range(i, len(trees)): #down
                if trees[x][j] < trees[i][j] and i < x: down += 1
                elif i == x: continue
                else:
                    down += 1
                    break
            score = left * down * right * up
            if score > prev:
                prev = score

print("task2: ", prev)


