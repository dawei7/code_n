def solve(n: int, queries: list[list[int]]) -> list[int]:
    MOD = 10**9 + 7
    
    # Extract powers of 2 from the binary representation of n
    powers = []
    bit = 1
    temp_n = n
    while temp_n > 0:
        if temp_n & 1:
            powers.append(bit)
        temp_n >>= 1
        bit <<= 1
        
    results = []
    for left, right in queries:
        product = 1
        for i in range(left, right + 1):
            product = (product * powers[i]) % MOD
        results.append(product)
        
    return results
