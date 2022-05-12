with open("numbers.txt") as f:
    numslines = [line.strip() for line in f]
test = int(1)
numslines.sort()
print(numslines[-1]+"\n"+numslines[-2]+"\n"+numslines[-3])
