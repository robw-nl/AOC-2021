def main(f):
    coords, folds = open(f).read().split('\n\n')
    coords = [(int(c.split(',')[0]), int(c.split(',')[1])) for c in coords.splitlines()]
    folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split('=')]]

    axis, foldline = folds[0]
    sum = 0

    for i, (x, y) in enumerate(coords):
        if axis == 'x' and x<foldline:
            sum += 1

        if axis == 'x' and x>foldline and (foldline-(coords[i][0]-foldline), coords[i][1]) not in coords:
            sum+=1

        if axis == 'y' and y<foldline:
            sum += 1
        
        if axis == 'y' and y>foldline and (coords[i][0], foldline-(c1[1]-foldline)) not in coords:
            sum+=1

    print(sum)

if __name__ == '__main__':   
    main('day13.txt')