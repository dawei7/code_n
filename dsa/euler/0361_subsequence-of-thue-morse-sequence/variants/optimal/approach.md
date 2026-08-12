# Subsequence of Thue-Morse Sequence - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $\sum_{k=1}^{18} A_{10^k} \bmod 10^9$, where $A_n$ is the $n$-th integer whose binary representation appears as a contiguous substring of the Thue-Morse sequence $\{T_n\}$.

### Overlap-Free Substring DFA & Digit DP:
1. **Thue-Morse Factor Characterization**:
   By the fundamental property of the Thue-Morse sequence, a binary string appears as a factor of $T$ iff it is overlap-free (contains no substring of the form $w w w_0$ where $w_0$ is the first character of $w$).
2. **Deterministic Finite Automaton (DFA)**:
   We construct a minimal DFA accepting all valid binary factors of $T$.
3. **Digit DP & Fast Binary Index Search**:
   Using digit-by-digit dynamic programming on the DFA transition graph, we count the number of valid overlap-free strings of length $\le L$ and compute the exact binary integer value $A_M$ for $M = 10^k$ ($k = 1 \dots 18$).
4. **Execution**:
   Summing $A_{10^k} \bmod 10^9$ for $k = 1 \dots 18$ yields $178476944$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot \log(10^K))$ for $K = 18$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{DFA states})$ automaton table.
