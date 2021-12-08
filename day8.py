def main(f):
    tot=0
    for line in open(f):
        for seg in line.split("|")[1].split():
            if len(seg) in [2, 3, 4, 7]:
                tot+=1
    print(tot)

if __name__ == '__main__':   
    main('day8.txt')    