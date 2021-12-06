def sim(f, days):
    freqs = [[int(k.strip()) for k in open(f).readline().split(',')].count(i) for i in range(9)]
    for _ in range(days):
        freqs.append(freqs.pop(0))
        freqs[6]+=freqs[-1]
    return sum(freqs)

def main(f):
    print(sim(f, 80), sim(f, 256))

if __name__ == '__main__':   
    main('day6.txt')