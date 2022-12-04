pairs = []
with open('input.txt') as input: 
    for pair in input: pairs.append([[int(x)for x in sections.split("-")] for sections in pair.strip().split(",")])

def contain(pair):
    a_includes_b = pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]
    b_includes_a = pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]
    return a_includes_b or b_includes_a

def overlap(pair):
    a_overlaps_b = pair[0][0] <= pair[1][0] <= pair[0][1] or pair[0][0] <= pair[1][1] <= pair[0][1]
    aboverlaps_a = pair[1][0] <= pair[0][0] <= pair[1][1] or pair[1][0] <= pair[0][1] <= pair[1][1]
    return a_overlaps_b or aboverlaps_a

counter_a, counter_b = 0, 0
for pair in pairs:
    counter_a += contain(pair)
    counter_b += overlap(pair)
print(counter_a, counter_b)

