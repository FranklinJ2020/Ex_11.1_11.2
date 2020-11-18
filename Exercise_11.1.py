import re
count = 0
imp = input('Enter regular expression: ')
reg_exp = str(imp)

fname = 'mbox.txt'
handle = open(fname)

for line in handle:
    line = line.rstrip()
    if re.findall(reg_exp, line) != []:
        count += 1
print(fname + 'had' + str(count) + 'matching lines' + reg_exp)
