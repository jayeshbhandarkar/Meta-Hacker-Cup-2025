import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

MOD = 10**9 + 7

def pow(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def inv(x, m):
    return pow(x, m - 2, m)

MAX_R = 60
fact = [1] * (MAX_R + 1)
inv_fact = [1] * (MAX_R + 1)

for i in range(1, MAX_R + 1):
    fact[i] = (fact[i - 1] * i) % MOD
inv_fact[MAX_R] = inv(fact[MAX_R], MOD)

for i in range(MAX_R - 1, 1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    num = 1
    for i in range(r):
        num = (num * ((n - i) % MOD)) % MOD
    return (num * inv_fact[r]) % MOD

def factors(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def ways(val, n):
    if val == 1:
        return 1
    f = factors(val)
    res = 1
    for _, e in f.items():
        res = (res * nCr(e + n - 1, e)) % MOD
    return res

def solve():
    line = sys.stdin.readline()
    if not line:
        return False
    try:
        n, a, b = map(int, line.split())
    except:
        return False

    pf = factors(b)
    primes = list(pf.keys())
    total = 0

    def dfs(idx, div):
        nonlocal total
        if idx == len(primes):
            if div <= a:
                x = div
                y = b // x
                ways_x = ways(x, n)
                ways_y = ways(y, n)
                total = (total + ways_x * ways_y) % MOD
            return
        p = primes[idx]
        for exp in range(pf[p] + 1):
            dfs(idx + 1, div)
            if exp < pf[p]:
                div *= p

    dfs(0, 1)
    return total

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    res = solve()
    if res is not False:
        sys.stdout.write(f"Case #{i}: {res}\n")
    else:
        break

sys.stdout.close()
sys.stdin.close()
