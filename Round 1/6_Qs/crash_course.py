import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve():
    ALICE = "Alice"
    BOB = "Bob"
    
    try:
        n1 = sys.stdin.readline().strip()
        if not n1:
            return ""
        N = int(n1)
    except:
        return ""
        
    S = sys.stdin.readline().strip()
    S_lst = list(S)
    
    W = [['' for _ in range(N + 1)] for _ in range(N + 1)]
    L = [['' for _ in range(N + 1)] for _ in range(N + 1)]
    
    for i in range(N + 1):
        W[i][i] = BOB
        L[i][i] = ALICE
        
    for len in range(1, N + 1):
        for i in range(N - len + 1):
            j = i + len 
            
            bob_moves = [k for k in range(i, j) if S_lst[k] == 'B']
            
            if not bob_moves:
                pass 
            else:
                bob_win = False
                for k in bob_moves:
                    if W[i][k] == BOB:
                        bob_win = True
                        break
                        
                if bob_win:
                    L[i][j] = BOB
                else:
                    L[i][j] = ALICE
                 
            alice_moves = [k for k in range(i, j) if S_lst[k] == 'A']
            
            if not alice_moves:
                W[i][j] = L[i][j] 
            else:
                alice_win = False
                for k in alice_moves:
                    if L[k + 1][j] == ALICE:
                        alice_win = True
                        break
                
                if alice_win:
                    W[i][j] = ALICE
                else:
                    W[i][j] = BOB

            if not bob_moves:
                 L[i][j] = W[i][j]
                 
    return W[0][N]

try:
    t1 = sys.stdin.readline().strip()
    if t1:
        T = int(t1)
    else:
        T = 0
except ValueError:
    T = 0
    
for t in range(1, T + 1):
    res = solve()
    if res:
        print(f"Case #{t}: {res}")
