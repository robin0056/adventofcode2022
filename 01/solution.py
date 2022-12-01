# import input
input = []
with open('input.txt') as text: 
    for line in text: input.append((line.strip()))

# variables
tmp_calory_sum = 0
calory_sums = []

# calculate calory sums
for calory_value in input:
    if calory_value != '':
        tmp_calory_sum += int(calory_value)
    else:
        calory_sums.append(int(tmp_calory_sum))
        tmp_calory_sum = 0

# print result
calory_sums.sort(reverse = True)
print('Part 1:', calory_sums[1], '- Part 2:', sum(calory_sums[:3]))




