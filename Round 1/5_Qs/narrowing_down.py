import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve():
    try:
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
    except:
        return

    P = [0] * (N + 1)
    curr_xor = 0
    for i in range(N):
        curr_xor ^= A[i]
        P[i+1] = curr_xor
    
    total = 0
    for i in range(1, N + 1):
        total += i * (N - i + 1)

    counts = {}
    for val in P:
        counts[val] = counts.get(val, 0) + 1
    
    sub_total = 0
    
    for V, K in counts.items():
        if K >= 2:
            K_2 = K * (K - 1) // 2
            sub_total += K_2
        
        if K >= 3:
            K_3 = K * (K - 1) * (K - 2) // 6
            sub_total += K_3
            
    res = total - sub_total
    return res

def main():
    try:
        T = int(sys.stdin.readline())
    except:
        T = 0

    for t in range(1, T + 1):
        res = solve()
        print(f"Case #{t}: {res}")

if __name__ == "__main__":
    main()
