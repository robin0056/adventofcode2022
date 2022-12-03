rs = []
a = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open('input.txt') as text: 
    for line in text: rs.append((line.strip()))
def calc_sums(rs, p2):
    s = 0
    for r in rs: s += a.index(list(set.intersection(*[set(t) for t in [r[:len(r)//2], r[len(r)//2:]]]))[0]) if not p2 else 0
    for i in range(0, len(rs), 3): s += a.index(list(set.intersection(*[set(t) for t in [rs[i], rs[i+1], rs[i+2]]]))[0]) if p2 else 0
    return s
print(calc_sums(rs, False), calc_sums(rs, True))

