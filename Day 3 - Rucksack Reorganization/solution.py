rucksacks = []
with open('input.txt') as text: 
    for line in text: rucksacks.append((line.strip()))

def split_rucksack(rucksack_string):
    rucksack_len = len(rucksack_string)
    rucksack_first_half = rucksack_string[:rucksack_len//2]
    rucksack_second_half = rucksack_string[rucksack_len//2:]
    return [rucksack_first_half, rucksack_second_half]

def find_duplicate(list_of_strings):
    set_list = [set(string) for string in list_of_strings]
    return list(set.intersection(*set_list))[0]

def calc_prio(character):
    character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return character_list.index(character)+1

def calc_overall_prio_sum(rucksacks, is_part_two):
    sum = 0
    if not is_part_two:
        for rucksack in rucksacks:
            sum += calc_prio(find_duplicate(split_rucksack(rucksack)))
    else:
        for i in range(0, len(rucksacks), 3):
            group = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
            sum += calc_prio(find_duplicate(group))
    return sum

print(calc_overall_prio_sum(rucksacks, False), calc_overall_prio_sum(rucksacks, True)) 




