from collections import defaultdict

thing = defaultdict(int)

for i in open('left'):
    thing[i] += 1

for i in open('right'):
    thing[i] += 1

print(thing)
print(len(thing))
