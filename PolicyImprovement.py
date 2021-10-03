reward = 0
discount = 1
p = [0.8, 0.1, 0, 0.1]
goal = (3, 3)
env = [[8, 10, 12,100],
       [7, "---", 6, -10],
       [6, 5, 3, -5]]


row = len(env)
col = len(env[0])
unreachable = None
goal = (goal[0] - 1, row-goal[1])
for r in range(row):
    for c in range(col):
        if env[r][c] == "---":
            unreachable = (r, c)
            break

for r in range(row):
    for c in range(col):
        upper = r if (r - 1, c) == unreachable else max(r - 1, 0)
        right = c if (r, c + 1) == unreachable else min(c + 1, col - 1)
        left = c if (r, c - 1) == unreachable else max(c - 1, 0)
        down = r if (r + 1, c) == unreachable else min(r + 1, row - 1)
        if (r, c) != unreachable:
            res = {"up":(p[0]*(reward+discount*env[upper][c])+p[1]*(reward+discount*env[r][left])+p[2]*(reward+discount*env[down][c])+p[3]*(reward+discount*env[r][right])),
                   "down":(p[0]*(reward+discount*env[down][c])+p[1]*(reward+discount*env[r][right])+p[2]*(reward+discount*env[upper][c])+p[3]*(reward+discount*env[r][left])),
                   "left":(p[0]*(reward+discount*env[r][left])+p[1]*(reward+discount*env[down][c])+p[2]*(reward+discount*env[r][right])+p[3]*(reward+discount*env[upper][c])),
                   "right":(p[0]*(reward+discount*env[r][right])+p[1]*(reward+discount*env[upper][c])+p[2]*(reward+discount*env[r][left])+p[3]*(reward+discount*env[down][c]))}
            print(max(res, key=res.get), end=' ')
        else:
            print("---", end=' ')
    print()
