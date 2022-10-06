name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name) #题目提供的代码

counts=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From '): #from后面必须要有空格，要不然会算上‘From:'开头的
        words = line.split()
        time = words[5] #09:14:16
        hour = time[0:2] #取上面的时间块的第1个和第2个数字：09
        counts[hour]=counts.get(hour,0)+1 #累计


for key,value in sorted(counts.items()): 
    print(key,value)
        
