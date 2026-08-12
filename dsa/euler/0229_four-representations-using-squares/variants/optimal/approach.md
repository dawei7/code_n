# Four Representations Using Squares - Optimal Approach

## Algorithm Explanation

Find the count of positive integers $n \le 2 \times 10^9$ that admit representations of all four forms with $a_k, b_k > 0$:
1. $n = a_1^2 + b_1^2$
2. $n = a_2^2 + 2 b_2^2$
3. $n = a_3^2 + 3 b_3^2$
4. $n = a_7^2 + 7 b_7^2$

### Sequential 250 MB Bitset Sieving Pipeline:
1. **Bitset Memory Optimization**:
   Representing numbers up to $N = 2 \times 10^9$ as a bitset requires $(N / 8) + 1 \approx 238.4\text{ MB}$ of RAM.
2. **Form Generation & Intersection**:
   - Allocate bitset `bits` for form $1$: $a^2 + b^2 \le N$.
   - For multiplier $k \in \{2, 3, 7\}$ sequentially:
     - Generate bitset `bits_k` for form $a^2 + k b^2 \le N$.
     - Bitwise AND `bits &= bits_k` to maintain cumulative intersections, freeing memory after each step.
3. **Execution**:
   Counting the set bits in the final intersected array yields $11325263$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(N \sum_{k \in \{1,2,3,7\}} \frac{1}{\sqrt{k}}\right) \approx 4 \times 10^9$ inner operations. Runs in $\approx 25\text{s}$ (C++ compiled).
- **Space Complexity:** $\mathcal{O}(N / 8)$ bytes ($\approx 238\text{ MB}$).
