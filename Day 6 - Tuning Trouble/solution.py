input = []
with open('input.txt') as text: 
    for line in text: input.append(line)
input = input[0]

def find_spot(string, sequence_len):
    for i in range(sequence_len, len(string), 1):
        char_list = string[i-sequence_len:i]
        if len(char_list) == len(set(char_list)):
            return i

print(find_spot(input, 4), find_spot(input, 14))