import sys
V0 = []
V1 = []
DP = [0] * 100010

def MaxSumSubarray(V):
    """
    Implements Kadane's algorithm to find the maximum sum of a contiguous subarray.
    Uses the global DP array for intermediate calculations.
    """
    if not V:
        return -float('inf')
    DP[0] = V[0]
    for i in range(1, len(V)):
        DP[i] = max(V[i], V[i] + DP[i - 1])
    ret = DP[0]
    for i in range(1, len(V)):
        ret = max(ret, DP[i])
    return ret

def solve():
    """
    Main function to handle test cases and problem logic.
    """
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        V0.clear()
        V1.clear()
        A_vals = [0] * n
        T_vals = [0] * n
        for i in range(n):
            A_vals[i] = int(sys.stdin.readline())
        for i in range(n):
            T_vals[i] = int(sys.stdin.readline())
        for i in range(n):
            if T_vals[i] == 0:
                V0.append(A_vals[i])
            else:
                V1.append(A_vals[i])
        result = max(MaxSumSubarray(V0), MaxSumSubarray(V1))
        print(result)


if __name__ == "__main__":
    solve()
