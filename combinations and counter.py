from itertools import combinations
from collections import Counter
import pandas as pd
dt=pd.read_csv("heh.csv")
count = Counter()
for row in dt['grouped']:
    rowl = row.split(",")
    count.update(combinations(rowl, 2))
for key, value in count.most_common(10):
    print(key, value)
rd=pd.DataFrame(count.most_common(10),columns=["products","count"])
print(rd)
