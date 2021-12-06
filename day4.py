def p1p2(f):
    parts = [0,0]
    calls = [int(n) for n in f[0].split(',')]
    wonturns = len(calls)
    lostturns = -wonturns

    for line in f[1:-1]:
#        cardrows = [[0]*5]*5 why da fuck geeft dit een ander eindresultaat???
        cardrows = [[0 for _ in range(5)] for _ in range(5)]
        cardcols = [[0 for _ in range(5)] for _ in range(5)]

        turns = -1
        bingo = False
        cardtotal = 0

        for i, line in enumerate(line.split('\n')):
            for j, num in enumerate(line.split()):
                cardrows[i][j] = int(num)
                cardcols[j][i] = int(num)
                cardtotal += int(num)
    
        while not bingo:
            turns += 1
            for i in range(len(cardrows)):
                for j in range(len(cardrows[0])):
                    if cardrows[i][j] == calls[turns]:
                        cardtotal -= calls[turns]
                        cardrows[i][j] = -1
                        cardcols[j][i] = -1

                for line in cardrows + cardcols:
                    if line == [-1,-1,-1,-1,-1]:
                        bingo = True

        if turns < wonturns:
            wonturns = turns
            parts[0] = cardtotal*calls[turns]

        if turns > lostturns:
            lostturns = turns
            parts[1] = cardtotal*calls[turns]
    return parts

def main(f):
    with open(f) as txt:
        f = txt.read().strip().split("\n\n")
    print(p1p2(f))

if __name__ == '__main__':   
    main('day4.txt')