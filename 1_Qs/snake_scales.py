import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def solve_case():
    try:
        n_line = sys.stdin.readline().strip()
        if not n_line:
            return None
        N = int(n_line)
    except ValueError:
        return None
    
    try:
        heights_line = sys.stdin.readline().strip()
        if not heights_line:
            return None
        A = list(map(int, heights_line.split()))
    except ValueError:
        pass

    if N <= 1:
        return 0
    
    max_required_height = 0

    for i in range(N - 1):
        vertical_gap = abs(A[i+1] - A[i])
        
        if vertical_gap > max_required_height:
            max_required_height = vertical_gap

    return max_required_height

def main():
    try:
        t_line = sys.stdin.readline().strip()
        if not t_line:
            num_test_cases = 0
        else:
            num_test_cases = int(t_line)
    except:
        num_test_cases = 0

    for case_num in range(1, num_test_cases + 1):
        result = solve_case()
        if result is not None:
            print(f"Case #{case_num}: {result}")

if __name__ == "__main__":
    main()
