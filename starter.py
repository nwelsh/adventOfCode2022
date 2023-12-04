
with open('test2.txt') as fp:
    lines = fp.readlines()
    for entry in lines:
        print(entry)
