import random


def createChromosome(n):
    ch = ""
    for i in range(n):
        x = random.randint(0, n - 1)
        ch = ch + str(x)
    return ch


def chromosomeToBoard(ch):
    b = []
    n = len(ch)

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        b.append(row)

    for col in range(n):
        row = int(ch[col])
        b[row][col] = 1

    return b


def printBoard(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], end=" ")
        print()


def findAttack(ch):
    attack = 0
    n = len(ch)

    for i in range(n):
        for j in range(i + 1, n):
            row_i = int(ch[i])
            row_j = int(ch[j])
            if row_i == row_j:
                attack += 1
            elif abs(row_i - row_j) == abs(i - j):
                attack += 1

    return attack


def nonAttackingpair(ch):
    n = len(ch)
    total_pairs = n * (n - 1) // 2
    attack_pairs = findAttack(ch)
    return total_pairs - attack_pairs


def createPopulation(n, psize):
    pop = []
    for i in range(psize):
        ch = createChromosome(n)
        # b = chromosomeToBoard(ch)
        # a = findAttack(ch)
        # nona = nonAttackingpair(ch)
        pop.append(ch)
    return pop


def fitness(p):
    fit = {}
    for i in range(len(p)):
        ch = p[i]
        nona = nonAttackingpair(ch)
        fit[ch] = nona
    return fit


def selection(pf):
    spf = sorted(pf.items(), key=lambda x: x[1])
    print(spf)
    parent1 = spf[-1]
    parent2 = spf[-2]
    return parent1, parent2


def crossover(p1, p2):
    # p1 and p2 are tuples: (chromosome, fitness)
    p1 = p1[0]
    p2 = p2[0]
    if len(p1) == 1:
        return p1, p2
    point = random.randint(1, len(p1) - 1)  # avoid 0 to ensure mixing
    print(point)
    ch1 = p1[0:point] + p2[point:]
    ch2 = p2[0:point] + p1[point:]
    return ch1, ch2


def mutation(ch1, ch2):
    if len(ch1) == 0:
        return ch1, ch2
    point = random.randint(0, len(ch1) - 1)
    value = random.randint(0, len(ch1) - 1)
    print(value, point)
    offs1 = ch1[0:point] + str(value) + ch1[point + 1:]
    offs2 = ch2[0:point] + str(value) + ch2[point + 1:]
    return offs1, offs2


if __name__ == "__main__":
    n = 8
    psize = 4
    pop = createPopulation(n, psize)
    print(pop)
    f = fitness(pop)
    print(f)
    p1, p2 = selection(f)
    print(p1, p2)
    ch1, ch2 = crossover(p1, p2)
    print(ch1, ch2)
    offs1, offs2 = mutation(ch1, ch2)
    print(offs1, offs2)