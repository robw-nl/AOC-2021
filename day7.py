def gen_number(n):
    return int(n*(n+1)/2)

def calc(f):
    t = 10e5

    for i in range(len(f)):
        s = min([sum(abs(a-i) for a in f)])
        if s < t:
            t = s

    u = 10e8
    for i in range(len(f)):
        s = min([sum(gen_number(abs(a-i)) for a in f)])
        if s < u:
            u = s
    return t, u
    
def main(f):
    f = [int(x) for x in open("day7.txt").read().strip().split(",")]
    print(calc(f))

if __name__ == '__main__':
    main('day7.txt')
