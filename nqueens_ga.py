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
        # b = chromosomeToBoard(ch)  # not used
        # a = findAttack(ch)         # not used
        # nona = nonAttackingpair(ch)  # not used
        pop.append(ch)
    return pop


def fitness(p):
    # Return a dict of chromosome -> fitness (non-attacking pairs)
    fit = {}
    for i in range(len(p)):
        ch = p[i]
        nona = nonAttackingpair(ch)
        fit[ch] = nona
    return fit


def selection(pf):
    # Sort by fitness descending and pick top two chromosomes
    sorted_pf = sorted(pf.items(), key=lambda x: x[1], reverse=True)
    parent1 = sorted_pf[0][0]
    parent2 = sorted_pf[1][0]
    return parent1, parent2


def crossover(p1, p2):
    # single-point crossover avoiding trivial point at edges
    n = len(p1)
    if n == 1:
        return p1, p2
    point = random.randint(1, n - 1)
    ch1 = p1[:point] + p2[point:]
    ch2 = p2[:point] + p1[point:]
    return ch1, ch2


def mutation(ch, mutation_rate=0.2):
    # Mutate one random gene with given probability
    if random.random() > mutation_rate:
        return ch
    n = len(ch)
    idx = random.randint(0, n - 1)
    val = str(random.randint(0, n - 1))
    if ch[idx] == val:
        val = str((int(val) + 1) % n)
    return ch[:idx] + val + ch[idx + 1:]


if __name__ == "__main__":
    n = 8
    psize = 4
    pop = createPopulation(n, psize)
    print("Population:", pop)

    f = fitness(pop)
    print("Fitness:", f)

    p1, p2 = selection(f)
    print("Parent1:", p1)
    print("Parent2:", p2)

    ch1, ch2 = crossover(p1, p2)
    print("Child1:", ch1)
    print("Child2:", ch2)

    offs1 = mutation(ch1, mutation_rate=0.5)
    offs2 = mutation(ch2, mutation_rate=0.5)
    print("Offspring1:", offs1)
    print("Offspring2:", offs2)