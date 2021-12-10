def p1p2(f):
    stack = []
    penalties = {')': 3, ']': 57, '}': 1197, '>':25137}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    match = {')': '(', ']': '[', '}': '{', '>': '<'}
    lbrackets = ['(', '[', '{', '<']
    rbrackets = [')', ']', '}', '>']
    tot = 0
    
    for c in f:
        if c in lbrackets:
            stack.append(c)
        elif c in rbrackets and stack.pop() != match[c]:
            tot += penalties[c]

    stack.clear()
    scores = []
    for l in f.split('\n'):
        corrupted = False
        stack = []
        for c in l:
            if c in lbrackets:
                stack.append(c)
            elif c in rbrackets:
                if stack.pop() != match[c]:
                    corrupted = True
                    break
        if not corrupted:
            scores.append(0)
            stack.reverse()
            for c in stack:
                scores[-1] *= 5
                scores[-1] += points[c]

    scores.sort()
    return tot, scores[int(len(scores)/2)]

def main(f):
    with open(f, 'r') as f:
        f = f.read()
    print(p1p2(f))
    
if __name__ == '__main__':   
    main('day10.txt') 