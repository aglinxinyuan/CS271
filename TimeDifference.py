# Elapsed Time     Predicted Time To Go

learning = 1
discounting = 1
table = [[0, 30],
         [5, 35],
         [15, 15],
         [10, 10],
         [10, 3],
         [3, 0]]

for t in range(len(table)-1):
    res = table[t][1] + discounting * (table[t+1][0] + learning * table[t+1][1] - table[t][1])
    print('S'+str(t)+": ",res)
