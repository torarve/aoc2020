import functools

def get_inputs():
    with open('input13.txt') as f:
        e = int(f.readline().strip())
        t = [int(x) for x in f.readline().strip().split(",") if x!="x"]
        return e, t

earliest, timestamps = get_inputs()

next_departures = [(x, (1+earliest//x)*x) for x in timestamps]
route, departure_time = min(next_departures, key=lambda x: x[-1])

print(f"Answer: {(departure_time-earliest)*route}")

def get_inputs_part2():
    with open('input13.txt') as f:
        f.readline().strip()
        return f.readline().strip().split(",")

diffs = [(int(x), i) for (i,x) in enumerate(get_inputs_part2()) if x.isnumeric()]

# NOTE: The following is based on https://martin-thoma.com/solve-linear-congruence-equations/

def egcd(a, b):
    """
        Calculates the gcd(a,b) and values x and y such that
            gcd(a,b) == a*x + b*y (Bézout's identity)

        Assumes a>b.

        :returns:
            tuple containing gcd(a,b), x, y
    """
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q*s1
        t0, t1 = t1, t0 - q*t1

    return a*s0 + b*t0, s0, t0

def solve(ys, moduli):
    """
    Solve a system of linear congruences:
        x mod moduli[i] = ys[i], for all x
    """
    x = 0
    M = functools.reduce(lambda x, y: x * y, moduli)
    for mi, yi in zip(moduli, ys):
        Mi = M // mi
        _, s, _ = egcd(Mi, mi)
        e = s * Mi
        x += yi * e

    return x % M

res = solve([x-i for x, i in diffs], [x for x,i in diffs])

print(res)