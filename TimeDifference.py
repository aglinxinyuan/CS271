# Elapsed Time     Predicted Time To Go
learning = 1
discounting = 1

table = [[0, 60],
         [5, 60],
         [15, 65],
         [35, 45],
         [60, 20],
         [85, 2],
         [87, 0]]

for t in range(len(table) - 1, 0, -1):
    table[t][0] -= table[t - 1][0]

for t in range(len(table) - 1):
    res = table[t][1] + discounting * (table[t + 1][0] + learning * table[t + 1][1] - table[t][1])
    print('S' + str(t) + ": ", res)
