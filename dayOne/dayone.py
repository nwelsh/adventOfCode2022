
totals = []

with open('test1.txt') as fp:
    list = fp.readlines()
    total = 0 
    for entry in list:
        if(entry.strip() != ''):
            total += int(entry)
        if(entry.strip() == '' or entry == list[-1]):
            totals.append(total)
            total = 0

print(max(totals))