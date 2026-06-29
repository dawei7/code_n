def solve(N, X, A):
    # Initialize the DP table
    # dp[0][i] represents not adding X to the current element
    # dp[1][i] represents adding X to the current element
    dp = [[0] * N for _ in range(2)]
    
    # Base case: for the first element
    dp[0][0] = 0
    dp[1][0] = 0
    
    # Variable to keep track of the maximum XOR sum
    max_xor_sum = 0
    
    for i in range(1, N):
        # Case 1: Not adding X to the current element
        dp[0][i] = max(
            dp[0][i-1] + (A[i-1] ^ A[i]),  # Not adding X to previous element
            dp[1][i-1] + ((A[i-1] + X) ^ A[i])  # Adding X to previous element
        )
        
        # Case 2: Adding X to the current element
        dp[1][i] = max(
            dp[0][i-1] + (A[i-1] ^ (A[i] + X)),  # Not adding X to previous element
            dp[1][i-1] + ((A[i-1] + X) ^ (A[i] + X))  # Adding X to previous element
        )
        
        # Update the maximum XOR sum
        max_xor_sum = max(max_xor_sum, dp[0][i], dp[1][i])
    
    return max_xor_sum

# Read input
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, X, A))


if __name__ == "__main__":
    solve()
