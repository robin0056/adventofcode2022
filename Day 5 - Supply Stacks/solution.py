import re

input = []
with open('input.txt') as text: 
    for line in text: input.append(line)

def move_box(stacks, a, b):
    stacks[b-1].append(stacks[a-1].pop())
    return stacks

def move_n_boxes(stacks, a, b, n):
    print("moving a b n", a, b, n)
    for i in range(n):
        stacks = move_box(stacks, a, b)
    return stacks

def move_n_boxes_same_order(stacks, a, b, n):
    moved_boxes = []
    for i in range(n):
        moved_boxes.append(stacks[a-1].pop())
    print(moved_boxes)
    moved_boxes.reverse()
    print(moved_boxes)
    for box in moved_boxes:
        stacks[b-1].append(box)
    return stacks

stacks = [[], [], [], [], [], [], [], [], []]
for line in range(7, -1, -1):
    tmp_stack = 0
    for stack_index in range(1, 34, 4):
        if not input[line][stack_index] == " ":
            stacks[tmp_stack].append(input[line][stack_index])
        tmp_stack += 1
for x in stacks: print(x)

for line in range(10, len(input), 1):
    print("")
    print("new move", line)
    print(input[line])
    tmp_move = list(re.sub("[^0-9]", "", input[line]))
    b = int(tmp_move.pop())
    a = int(tmp_move.pop())
    print("debug", tmp_move)
    n = int(''.join(tmp_move))
    stacks = move_n_boxes_same_order(stacks, a, b, n)
    for i in range(1, 10, 1):
        print(i, stacks[i-1])

        