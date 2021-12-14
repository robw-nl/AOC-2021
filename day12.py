def p2(caves):
    paths = [(['start'], True)]
    completepaths = []

    while paths:
        path, flag = paths.pop()
        lastcave = path[-1]
        neighbors = caves[lastcave]
        
        for cave in filter(lambda cave: cave != 'start', neighbors):
        # same as for cave in (cave for cave in neighbors if cave != 'start'):
            if cave == 'end':
                completepaths.append((path + [cave], flag))
            elif cave.isupper() or cave not in path:
                paths.append((path + [cave], flag))
            elif flag:
                paths.append((path + [cave], False))

    return len(completepaths)

def p1(caves):
    paths = [['start']]
    completepaths = []

    while paths:
        path = paths.pop()
        lastcave = path[-1]
        neighbors = caves[lastcave]
        for cave in neighbors:
            if cave == 'end':
                completepaths.append(path+[cave])
            elif cave.isupper() or cave not in path:
                paths.append(path+[cave])

    return len(completepaths)

def main(f):
    paths = {}
    with open(f) as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            if a not in paths:
                paths[a] = []
            if b not in paths:
                paths[b] = []
            paths[a] += [b]
            paths[b] += [a] 

    print(p1(paths), p2(paths))

if __name__ == '__main__':   
    main('day12.txt')