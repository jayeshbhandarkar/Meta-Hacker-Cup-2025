import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve():
    try:
        T_line = sys.stdin.readline()
        if not T_line:
            return
        T = int(T_line.strip())
    except:
        return

    output = []
    
    for i in range(1, T + 1):
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            N, M = map(int, line.split())
        except Exception:
            continue

        result = "NO"
        
        if N >= M and N <= 2 * M - 2:
            result = "YES"
        
        if N % 2 == 0 and N >= 2 * M:
            result = "YES"
        
        output.append(f"Case #{i}: {result}")

    sys.stdout.write('\n'.join(output) + '\n')

solve()