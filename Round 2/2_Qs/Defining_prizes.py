import sys
from collections import Counter

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve():
    try:
        line = sys.stdin.readline()
        if not line: return None
        if not line.strip(): 
             return None
        N, M = map(int, line.split())

    except EOFError:
        return None
    
    except ValueError:
        return 0

    if N == 0:
        try:
            sys.stdin.readline() 
            sys.stdin.readline()
        except:
            pass
        return 0
    
    try:
        A = list(map(int, sys.stdin.readline().split()))
        B_inv = list(map(int, sys.stdin.readline().split()))
    except:
        return 0
    
    B_total = sum(B_inv) 

    C = Counter(A) 
    S = sorted(C.keys())
    U = len(S) 
    
    counts = [C[s] for s in S]
    N_suff = [0] * (U + 1)
    
    for i in range(U - 1, -1, -1):
        N_suff[i] = N_suff[i+1] + counts[i]
        
    P_req = [0] * (U + 1)
    
    for k in range(U - 1, -1, -1):
        N_k = counts[k] 
        N_low = N_suff[k+1] 
        P_low = P_req[k+1] 
        
        P_req[k] = N_k + P_low + N_low
    
    K_max = 0 

    for k in range(U):
        D_k = U - k 

        if D_k > M:
            continue
            
        if P_req[k] <= B_total:
            K_max = N_suff[k]
            break
            
    return K_max

try:
    T_line = sys.stdin.readline()
    if T_line:
        T = int(T_line.strip())
    else:
        T = 0
except ValueError:
    T = 0
except EOFError:
    T = 0

for t in range(1, T + 1):
    result = solve()
    if result is not None:
        print(f"Case #{t}: {result}")
