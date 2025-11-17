import sys
from collections import deque

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve():
    try:
        N_str = sys.stdin.readline()
        if not N_str:
            return 0
        N = int(N_str)
        
        if N == 0:
            return 0
            
        heights = [0] + list(map(int, sys.stdin.readline().split()))
    except EOFError:
        return 0
    except Exception:
        return 0

    def check(h, N, heights):
        visited = [False] * (N + 1)
        queue = deque()
        
        for i in range(1, N + 1):
            if heights[i] <= h:
                visited[i] = True
                queue.append(i)
        
        while queue:
            u = queue.popleft()
            
            for v in [u - 1, u + 1]:
                if 1 <= v <= N and not visited[v]:
                    if abs(heights[u] - heights[v]) <= h:
                        visited[v] = True
                        queue.append(v)
        
        return all(visited[1:])

    low = 1
    high = max(heights)
    result = high 
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if check(mid, N, heights):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

def main():
    try:
        T_str = sys.stdin.readline()
        if not T_str:
            return
        T = int(T_str)
    except:
        return

    for i in range(1, T + 1):
        r = solve()
        print(f"Case #{i}: {r}")

if __name__ == "__main__":
    main()
