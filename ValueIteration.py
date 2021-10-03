reward = -1
discount = 1
p = 0.8
iteration = 3
env = [[reward, reward, reward],
       [reward, reward, 0],
       [reward, reward, reward]]

env.reverse()
result = [env]
row = len(env)
col = len(env[0])
goal = None

for r in range(row):
    for c in range(col):
        if env[r][c] == 0:
            goal = (r, c)
            break

for i in range(iteration-1):
    print("Iteration", i+2, )
    result.append([])
    for r in range(row):
        col_list = []
        for c in range(col):
            if (r, c) == goal:
                col_list.append(0)
                print('', 0.0, end=' ')
                continue
            upper = max(r - 1, 0)
            right = min(c + 1, col - 1)
            res = max((reward + discount * (p * result[i][upper][c] + (1 - p) * result[i][r][right])),  # upper
                      (reward + discount * (p * result[i][r][right] + (1 - p) * result[i][upper][c])))  # right
            col_list.append(res)
            print('{0:.2f}'.format(res), end=' ')
        result[i + 1].append(col_list)
        print()
    print()
