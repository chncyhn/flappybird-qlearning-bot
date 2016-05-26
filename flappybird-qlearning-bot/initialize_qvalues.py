import json
from itertools import chain

# Script to create Q-Value JSON file, initilazing with zeros

qval = {}
# X -> [-40,-30...120] U [140, 210 ... 490]
# Y -> [-300, -290 ... 160] U [180, 240 ... 420]
for x in chain(list(range(-40,140,10)), list(range(140,421,70))):
    for y in chain(list(range(-300,180,10)), list(range(180,421,60))):
        for v in range(-10,11):
            qval[str(x)+'_'+str(y)+'_'+str(v)] = [0,0]


fd = open('qvalues.json', 'w')
json.dump(qval, fd)
fd.close()
