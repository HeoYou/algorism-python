import sys
sys.setrecursionlimit(10000)

t = int(input())

b, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global b, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if b[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)

def process():
    global b, ck

    m, n, k = map(int, input().split())
    
    b = [[0 for i in range(m + 2)] for _ in range(n + 2)]
    ck = [[0 for i in range(m + 2)] for _ in range(n + 2)]


    for _ in range(k):
        x, y = map(int, input().split())
        b[y+1][x+1] = 1

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if b[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j) 
            ans += 1
    print(ans)



for _ in range(t):
    process()