fhand = open("1.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    else:
        words = line.split()
        print(words(1))