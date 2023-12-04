copies = []
totals = []
all_points = []

def read_card(entry):
    global copy
    winning_nums = [f for f in (entry.partition(':')[2].split('|')[0].strip().split(' ')) if f]
    numbers = entry.partition(':')[2].split('|')[1].strip().split(' ')
    points = 0 
    winning_cards = 0
    for win in winning_nums:
        if win in numbers:
            winning_cards += 1
            # this is wrong 
            if points == 0:
                points = 1
            else:
                points *= 2
    copies.append(winning_cards)
    totals.append(1)
    all_points.append(points)

total = 0 
with open('test1.txt') as fp:
    list = fp.readlines()
    total = 0 
    for entry in list:
        read_card(entry)
    index = 0
    for winners in copies:
        val = totals[index]
        index += 1
        update = index
        for win in range(winners):
            totals[update]+= val
            update += 1
mult = []
for a, b in zip(totals, all_points):
    if(b == 0):
        mult.append(1)
    else:
        mult.append(a * b)
print("total", sum(mult)) #answer: 15268

