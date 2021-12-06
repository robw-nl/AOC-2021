def p1p2(coords):
    fcoords = [l for l in coords if l[0] == l[2] or l[1] == l[3]]
    covered = {}

    for l in fcoords:
        for x in range(min(l[0], l[2]), max(l[0], l[2])+1):
            for y in range(min(l[1], l[3]), max(l[1], l[3])+1):
                if f"{x},{y}" in covered:
                    covered[f"{x},{y}"] += 1
                else:
                    covered[f"{x},{y}"] = 1

    a = sum(i > 1 for i in covered.values())

    dcoords = [l for l in coords if l[0] != l[2] and l[1] != l[3]]

    for l in dcoords:
        d1 = int(l[2] > l[0]) or -1
        d2 = int(l[3] > l[1]) or -1
        for i in range(abs(l[2] - l[0]) + 1):
            x = l[0] + d1 * i
            y = l[1] + d2 * i
            if f"{x},{y}" in covered:
                covered[f"{x},{y}"] += 1
            else:
                covered[f"{x},{y}"] = 1

    b = sum(i > 1 for i in covered.values())
    return a, b

def main(f):
    with open(f, "r") as f:
        coords = [[int(i) for j in line.strip().split(" -> ") for i in j.split(",")] for line in f.readlines()]

    print(p1p2(coords))

if __name__ == '__main__':   
    main('day5.txt')