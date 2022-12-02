input = []
with open('input.txt') as text: 
    for line in text: input.append((line.strip().split(" ")))

def calc_round_score(i):
    round_score = 0
    if i[0] == "X" and i[1] == "Y" or i[0] == "Y" and i[1] == "Z" or i[0] == "Z" and i[1] == "X":
        round_score += 6
    elif i[0] == i[1]:
        round_score += 3
    if i[1] == "X":
        round_score += 1
    elif i[1] == "Y":
        round_score += 2
    else:
        round_score += 3
    return round_score

def decrypt_openent(i):
    if i[0] == "A":
        i[0] = "X"
    elif i[0] == "B":
        i[0] = "Y"
    else:
        i[0] = "Z"
    return i

def loose(selection):
    if selection == "X":
        return "Z"
    elif selection == "Y":
        return "X"
    else:
        return "Y"

def draw(selection):
    return selection

def win(selection):
    if selection == "X":
        return "Y"
    elif selection == "Y":
        return "Z"
    else:
        return "X"

def select_strategy(i):
    if i[1] == "X":
        i[1] = loose(i[0])
    elif i[1] == "Y":
        i[1] = draw(i[0])
    else:
        i[1] = win(i[0])
    return i

def calc_overall_score(input, isTask2):
    score = 0
    for i in input:
        i = decrypt_openent(i)
        print(i)
        if isTask2:
            i = select_strategy(i)
            print("new", i)
        score = score + calc_round_score(i)
    return score

print(calc_overall_score(input, False))
#print(calc_overall_score(input, True))