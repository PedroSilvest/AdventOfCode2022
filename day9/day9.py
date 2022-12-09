with open("day9/input.txt", "r") as file:
    movs = [x.replace("\n","").split() for x in file.readlines()]


def move_head(head, direction):
    if direction == "R":
        head["x"] += 1
    elif direction == "L":
        head["x"] -= 1
    elif direction == "U":
        head["y"] += 1
    elif direction == "D":
        head["y"] -= 1
    return head

def move_tail(knot, above_knot):
    x_diff = above_knot["x"] - knot["x"]
    y_diff = above_knot["y"] - knot["y"]
    if y_diff > 1:  # head above tail
        knot["y"] += 1
        if x_diff > 0:
            knot["x"] += 1
        elif x_diff < 0:
            knot["x"] -= 1
    elif y_diff < -1:  # head below tail
        knot["y"] -= 1
        if x_diff > 0:
            knot["x"] += 1
        elif x_diff < 0:
            knot["x"] -= 1
    elif x_diff < -1:  # head left of tail
        knot["x"] -= 1
        if y_diff > 0:
            knot["y"] += 1
        elif y_diff < 0:
            knot["y"] -= 1
    elif x_diff > 1:  # head right of tail
        knot["x"] += 1
        if y_diff > 0:
            knot["y"] += 1
        elif y_diff < 0:
            knot["y"] -= 1
    return knot

def vis_positions(part, movs):
    if part == 1:
        n_knots = 2
    elif part == 2:
        n_knots = 10

    knots = {knot: {"x": 0, "y": 0} for knot in range(n_knots)}
    visit_pos = set()
    visit_pos.add((0,0))

    for direction, length in movs:
        for i in range(int(length)):
            for key, knot in knots.items():
                if key == 0:
                    move_head(knots[0], direction)
                else:
                    knots[key] = move_tail(knot, knots[key - 1])
            visit_pos.add((knots[n_knots - 1]["x"], knots[n_knots - 1]["y"]))
    return len(visit_pos)


print("task1: ", vis_positions(1, movs))
print("task2: ", vis_positions(2, movs))