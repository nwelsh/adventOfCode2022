import re

total = 0 
with open('test1.txt') as fp:
    list = fp.readlines()
    total = 0 
    for entry in list:
        all_digits = re.findall(r'\d+', entry)
        total += int(all_digits[0] + all_digits[-1])
print(total)