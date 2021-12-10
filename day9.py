def p2(f):
    with open('day9.txt') as f:
        f = [[int(i) for i in l] for l in f.read().strip().split('\n')]

    ymax = len(f)
    xmax = len(f[0])    
    
    field = set((x,y) for x in range(xmax) for y in range(ymax) if f[y][x]<9)
    basins = []

    def basin(j0,k0):
        if (j0,k0) not in field:
            return 0
        field.remove((j0,k0))
        return 1 + sum(basin(j,k) for j,k in ((j0-1,k0), (j0+1,k0), (j0,k0-1), (j0,k0+1)))
        
    while field:
        x, y = field.pop()
        field.add((x,y))
        basins.append(basin(x,y))

    res = 1
    for v in sorted(basins)[-3:]:
        res *= v
    
    return res

def adjacents(data, i, j):
    left = data[i][j-1] if j > 0 else -1
    right = data[i][j+1] if j < (len(data[0])-1) else -1
    above = data[i-1][j] if i > 0 else -1
    below = data[i+1][j] if i < (len(data)-1) else -1
    
    return [a for a in (left, right, above, below) if a != -1]

def p1(f):
    lowpoints = []
    for i in range(len(f)):
        for j in range(len(f[0])):
            if all(a > f[i][j] for a in adjacents(f, i, j)):
                lowpoints.append(int(f[i][j]))

    return sum(lowpoints) + len(lowpoints)

def main(f):
    f = [item.strip() for item in open('day9.txt', 'r').readlines()]
    print(p1(f), p2(f))
   
if __name__ == '__main__':   
    main('day9.txt') 