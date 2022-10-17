total = 0
with open("regex_sum_42.txt") as f:
    for line in f:
        y = re.findall("\d+", line)
        if len(y) > 0:
            sum = 0
            for ele in range(0,len(y)):
                sum = sum + int(y[ele])
        total += sum 
print(total)