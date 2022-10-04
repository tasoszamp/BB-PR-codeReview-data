import json
import numpy as np
import matplotlib.pyplot as plt

with open('last1000.json') as f:
   data = json.load(f)

appr_time = []

for d in data:
    appr_time.append(d["Approved"])

fig1 = plt.hist(appr_time, bins=10)
plt.show()

print ("breakpoint")