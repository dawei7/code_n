# Lexicographical Neighbours - Optimal Approach

## Algorithm Explanation

Find the maximum value of $p(n)$ for $1 \le n \le 26$, where $p(n)$ is the number of length-$n$ strings of distinct English letters for which **exactly one** character comes lexicographically after its immediate left neighbour ($s[i] > s[i-1]$).

### Combinatorial Derivation:
1. **Selecting $n$ Distinct Letters**:
   There are $\binom{26}{n}$ ways to choose $n$ distinct letters out of the $26$ letters of the alphabet.
2. **Permutation with Exactly One Increase**:
   A string with exactly one increase consists of two strictly decreasing subsequences $S_1$ and $S_2$.
   Any non-empty partition of the $n$ letters into two subsets $S_1$ and $S_2$ arranged in decreasing order yields a valid sequence with at most $1$ increase.
   - Total non-strictly decreasing partitions: $2^n - 1$.
   - Excluding the single purely decreasing permutation ($0$ increases): $2^n - n - 1$.

Combinatorial formula:
$$p(n) = \binom{26}{n} \times (2^n - n - 1)$$

Maximum value occurs at $n = 18$:
$$p(18) = \binom{26}{18} \times (2^{18} - 18 - 1) = 409,511,334,375$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 26$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
