# Digit Factorial Chains - Optimal Approach

## Algorithm Explanation

Find how many starting numbers $N < 1000000$ produce a non-repeating digit-factorial chain of length exactly $60$.

### Strategy:
1. Define digit factorial transition $f(n) = \sum d!$ using precomputed factorial table.
2. Track trajectory paths using a hash map `memo[n]` storing total non-repeating chain lengths.
3. For each starting number $n \in [1, 999999]$:
   - Trace sequence until reaching a cached node or detecting a loop.
   - Assign exact non-repeating lengths to all trajectory nodes in $\mathcal{O}(1)$ amortized steps per node.
4. Count and return numbers with length equal to $60$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1000000$. Runs in $< 0.5\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Memoization hash map.
