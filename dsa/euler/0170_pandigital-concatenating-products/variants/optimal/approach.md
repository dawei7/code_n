# Pandigital Concatenating Products - Optimal Approach

## Algorithm Explanation

Find the largest $10$-digit $0 \dots 9$ pandigital concatenated product $P$ of an integer $k$ with two or more integers $(a_1, a_2, \dots, a_m)$ ($m \ge 2$) such that the concatenation of the input numbers $k \, a_1 \, a_2 \dots a_m$ is also $0 \dots 9$ pandigital.

### Descending Permutation Search:
1. **Lexicographical Order**:
   Iterate through all $10$-digit $0 \dots 9$ pandigital permutations $P$ in strictly **descending numerical order** (starting from $9876543210$).
2. **Contiguous Partitioning**:
   For each candidate $P$, partition $P$ into contiguous blocks $p_1, p_2, \dots, p_m$ ($m \ge 2$).
3. **Common Factor Extraction**:
   Compute the greatest common divisor $g = \gcd(p_1, p_2, \dots, p_m)$.
   For each non-trivial divisor $k \mid g$:
   - Derive input terms $a_i = p_i / k$.
   - Concatenate input string $I = k \, a_1 \, a_2 \dots a_m$.
   - Check if $I$ is a valid $10$-digit $0 \dots 9$ pandigital string without leading zero.
4. **Early Termination Guarantee**:
   The first valid product $P$ encountered in descending search order is mathematically guaranteed to be the maximum.

Found result:
$$P = 9857164023 = (27 \times 36508) \, (27 \times 149)$$
with input concatenation $2736508149$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{TestedPermutations} \cdot \text{Divisors})$. Runs in $\approx 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
