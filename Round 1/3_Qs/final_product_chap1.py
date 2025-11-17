import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        N, A, B = map(int, line.split())
    except EOFError:
        return
    except ValueError:
        return

    C_N = 1  
    
    for i in range(A, 0, -1):
        if B % i == 0:
            C_N = i
            break
            
    R = B // C_N
    lst = []
    
    lst.append(C_N)
    for _ in range(N - 1):
        lst.append(1)
        
    lst.append(R)
    for _ in range(N - 1):
        lst.append(1)
        
    return " ".join(map(str, lst))

def main():
    try:
        T = int(sys.stdin.readline())
    except:
        return
    
    for i in range(1, T + 1):
        result = solve()
        if result is not None:
            sys.stdout.write(f"Case #{i}: {result}\n")

if __name__ == "__main__":
    main()

sys.stdin.close()
sys.stdout.close()