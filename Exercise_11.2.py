import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^New .*: ([0-9]+)', line)
    if len(stuff) > 1 : continue
    for thing in stuff:
        num = int(thing)
        numlist.append(num)
print('Average:', sum(numlist) / len(numlist))
