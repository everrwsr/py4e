name = input("Enter file:")
fh = open(name) #打开文件

counts = dict()#定义dictionary

for line in fh:
    line = line.strip()
    if line.startswith('From:'):
        continue #如果不把带有：的句子去掉，结果会显示10
    if line.startswith('From'):
        words = line.split()
        person=words[1]#第2个words，即为words[1]
        
        counts[person]=counts.get(person,0)+1
            
maxcount = None
maxword = None
for person,count in counts.items():
    if maxcount is None or count>maxcount:
        maxcount = count
        maxword = person

print(maxword,maxcount)