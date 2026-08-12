# Permutations of Project - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $T(10^{12}) \bmod 10^9$, where $T(n)$ is the number of strings of length $n$ on the 7-letter alphabet $A = \{\text{c}, \text{e}, \text{j}, \text{o}, \text{p}, \text{r}, \text{t}\}$ containing no contiguous 7-letter substring that is a permutation of "project".

### Suffix Distinct-Letter DFA & $6 \times 6$ Matrix Exponentiation:
1. **DFA State Characterization**:
   A 7-character substring is a permutation of "project" iff all 7 characters are distinct.
   We track the length $k \in \{1, 2, 3, 4, 5, 6\}$ of the longest suffix of distinct characters.
   Reaching state $k = 7$ is forbidden.
2. **State Transition Matrix**:
   From state $k$:
   - Choosing a new character (out of $7 - k$ remaining) advances to state $k + 1$.
   - Choosing a character already present in the suffix resets the distinct suffix to length $j \in \{1, \dots, k\}$ (with $1$ choice for each $j$).
   This gives a $6 \times 6$ transition matrix $M$:
   $$M_{k, k+1} = 7 - k, \quad M_{k, j} = 1 \text{ for } 1 \le j \le k$$
3. **Binary Exponentiation**:
   For $n = 10^{12}$, $T(10^{12}) \bmod 10^9$ is evaluated in $\mathcal{O}(6^3 \log n)$ time using $6 \times 6$ matrix binary exponentiation.
4. **Execution**:
   Evaluating $T(10^{12}) \bmod 10^9$ yields last 9 digits $423341841$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K^3 \log n)$ for $K = 6$ states and $n = 10^{12}$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(K^2)$.
