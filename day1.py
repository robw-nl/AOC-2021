def part1(f): # find the number of occurences higher than the previous one
    return sum(int(f[i]) > int(f[i-1]) for i in range(1, len(f)))
    
def part2(f): # Count larger sums than previous sums in a sliding window of 3
    return sum(int(f[i] + f[i+1] + f[i+2]) < int(f[i+1] + f[i+2] + f[i+3]) for i in range(len(f)-3))
    
def main(f):
    f = [int(item.strip()) for item in open('day1.txt', 'r').readlines()]
    print(part1(f), part2(f))

if __name__ == '__main__':   
    main("day1.txt")
