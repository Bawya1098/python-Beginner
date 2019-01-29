list = [-1, 0, 0, 1, 100]
positivecount=0
negativecount=0
Zerocount=0
for i in list:
    if i == 0:
        Zerocount += 1
    if i > 0:
         positivecount += 1
    else:
        negativecount += 1
print("Zero count=",Zerocount)
print("positive count=",positivecount)
print("negative count=",negativecount)