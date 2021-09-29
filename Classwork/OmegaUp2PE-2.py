info = input()

info = info.split()

trees = 0
ljs = 0 #Lumberjacks

ljs = int(info[0])
trees = int(info[1])

ops = [None] * ljs

for i in range(ljs):
    ops[i] = set()

entry = input()
while entry != '0':
    entry = entry.split()
    ops[int(entry[0]) - 1].add(int(entry[1]))
    entry = input()

max = [ops[0]]

opinions = 1


for i in range(1, ljs):
    match = False
    for j in range(len(max)):
        if ops[i].issubset(max[j]) and max[j].issubset(ops[i]):
            match = True
            break
    if not match:
        opinions += 1
        max.append(ops[i])
    



print(opinions)