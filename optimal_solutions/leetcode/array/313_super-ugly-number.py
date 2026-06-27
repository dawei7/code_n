import heapq

def solve(n: int, primes: list[int]) -> int:
    # dp[i] will store the (i+1)-th super ugly number
    dp = [0] * n
    dp[0] = 1
    
    # pointers[i] tracks the index in dp that primes[i] should multiply next
    pointers = [0] * len(primes)
    
    # We use a min-heap to efficiently find the minimum of (primes[j] * dp[pointers[j]])
    # The heap stores tuples: (value, prime_index)
    pq = []
    for i in range(len(primes)):
        heapq.heappush(pq, (primes[i] * dp[pointers[i]], i))
        
    for i in range(1, n):
        # The smallest value in the heap is the next super ugly number
        val, idx = heapq.heappop(pq)
        dp[i] = val
        
        # Advance the pointer for the prime that produced the minimum
        pointers[idx] += 1
        
        # Push the next potential candidate for this prime into the heap
        next_val = primes[idx] * dp[pointers[idx]]
        heapq.heappush(pq, (next_val, idx))
        
        # Handle duplicates: if the next smallest value is the same as the current
        # one we just added, skip it by advancing the pointer again.
        while pq and pq[0][0] == dp[i]:
            val, idx = heapq.heappop(pq)
            pointers[idx] += 1
            next_val = primes[idx] * dp[pointers[idx]]
            heapq.heappush(pq, (next_val, idx))
            
    return dp[n - 1]
