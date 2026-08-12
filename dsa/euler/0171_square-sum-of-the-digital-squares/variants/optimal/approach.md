# Square Sum of the Digital Squares - Optimal Approach

## Algorithm Explanation

Find the last $9$ digits of the sum of all $0 < n < 10^{20}$ such that the sum of the squares of the digits $f(n)$ is a perfect square.

### Digit Dynamic Programming:
For a $20$-digit number string $d_1 d_2 \dots d_{20}$ (with leading zeros if $n < 10^{19}$), evaluate the sum modulo $10^9$.

1. **DP State**:
   Define `dp(idx, sq_sum)` returning pair `(count, sum_val)` modulo $10^9$:
   - `idx`: Current digit position $\in [0, 20]$.
   - `sq_sum`: Accumulated sum of squared digits $\in [0, 1620]$.
2. **Base Case (`idx == 20`)**:
   - If `sq_sum` $\in \{1^2, 2^2, \dots, 40^2\}$, return `(1, 0)`.
   - Else, return `(0, 0)`.
3. **Recursive Transition**:
   For each digit $d \in [0, 9]$:
   - `cnt, val = dp(idx + 1, sq_sum + d * d)`
   - `total_cnt += cnt`
   - `total_val += val + cnt * d * (10^(19 - idx) mod 10^9)`
4. **Memoization**:
   State space size: $20 \times 1620 = 32,400$ states.

Return `val` zero-padded to $9$ digits.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \cdot \text{MaxSqSum} \cdot 10)$ where $L = 20, \text{MaxSqSum} = 1620$ ($\approx 3.2 \times 10^5$ operations). Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(L \cdot \text{MaxSqSum})$ - Memoization dictionary.
