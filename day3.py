# p1: Use the binary numbers in the report to calculate gamma and epsilon rate, then multiply them together
# p2 Use the binary numbers in the report to calculate oxygen generator and CO2 scrubber rating by multiplying them

def solver(f):
    x = 0

    binary = ''
    least = ''
    for i in range(len(f[0])):
        binaries = [x[i] for x in f]
        if binaries.count('1') > len(binaries)//2:
            binary += '1'
            least += '0'
        else:
            binary += '0'
            least += '1'

    oxygen = co2 = 0
    crit_ox = crit_co2 = f.copy()

    for i in range(len(f[0])):
        bin_ox = [x[i] for x in crit_ox]
        bin_co2 = [x[i] for x in crit_co2]
        
        if bin_ox.count('1') >= bin_ox.count('0'):
            crit_ox = [x for x in crit_ox if x[i] == '1']
        else:
            crit_ox = [x for x in crit_ox if x[i] == '0']
        if bin_co2.count('1') < bin_co2.count('0'):
            crit_co2 = [x for x in crit_co2 if x[i] == '1']
        else:
            crit_co2 = [x for x in crit_co2 if x[i] == '0']
        
        if len(crit_ox) == 1:
            oxygen = int(crit_ox[0],2)
        if len(crit_co2) == 1:
            co2 = int(crit_co2[0],2)

    return int(binary,2) * int(least,2), co2 * oxygen
    
def main(f):
    f = [item.strip() for item in open(f, 'r').readlines()]
    print(solver(f))

if __name__ == '__main__':   
    main('day3.txt')