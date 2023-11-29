
totals = []

with open('test1.txt') as fp:
    list = fp.readlines()
    total = 0 
    for entry in list:
        # refactor this
        if(entry.strip() != ''):
            total += int(entry)
        else:
            totals.append(total)
            total = 0
    totals.append(total)

print('here are all the totals: ' + str(totals))
print('the max is: ' + str(max(totals)))