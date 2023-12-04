total = 0 
with open('test1.txt') as fp:
    list = fp.readlines()
    total = 0 
    for entry in list:
        winning_nums = [f for f in (entry.partition(':')[2].split('|')[0].strip().split(' ')) if f]
        numbers = entry.partition(':')[2].split('|')[1].strip().split(' ')
        points = 0 
        for win in winning_nums:
            if win in numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points
print("total", str(total))