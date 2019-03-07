import math

def bunnies(rabbits, foxes, years):
    A = 0.04
    B = 0.0005
    G = 0.2
    S = 0.00005
    R = []
    F = []
    list = []
    R.append(rabbits)
    F.append(foxes)
    for x in range(1, years + 1):
        R.append(R[x - 1] + (math.floor(R[x - 1] * (A - B * F[x -1]))))
        F.append(F[x - 1] - (math.floor(F[x - 1] * (G - S * R[x -1]))))
    list.append(R[len(R)-1])
    list.append(F[len(F)-1])
    return list
if __name__ == "__main__":
    print('Welcome to Predator-Prey Model.')
    r_init = int(input('Enter Initial Rabbit Population:\n'))
    f_init = int(input('Enter Initial Fox Population:\n'))
    year = int(input('Enter Number of Years to Simulate:\n'))
    print('After %d years there will be %d rabbits.' % (year, bunnies(r_init, f_init, year)[0]))
    print('After %d years there will be %d foxes.' % (year, bunnies(r_init, f_init, year)[1]))
