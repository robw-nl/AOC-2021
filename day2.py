# Multiply final horizontal position by your final depth by following course forward, down, up
def nav(f):
    depth = hor = 0 # Assuming all numbers 0-9
    for rule in f:
        if rule[0] == "f":
            hor += int(rule[-1])
        elif rule[0] == "d":
            depth += int(rule[-1])
        elif rule[0] == "u":
            depth -= int(rule[-1])
    return depth * hor

# now use aim and recalculate
def nav_aim(f):
    aim = depth = hor = 0
    for rule in f:
        if rule[0] == "f":
            hor += int(rule[-1])
            depth += aim * int(rule[-1])
        elif rule[0] == "d":
            aim += int(rule[-1])
        elif rule[0] == "u":
            aim -= int(rule[-1])
    return depth * hor

def main(f):
    f = open(f, "r").read().split("\n")
    print(nav(f), nav_aim(f), nav_both(f))
    
if __name__ == "__main__":   
    main("day2.txt")
