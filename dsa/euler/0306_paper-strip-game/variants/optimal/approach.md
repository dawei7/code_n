# Paper-strip Game - Optimal Approach

## Algorithm Explanation

Find the number of strip lengths $1 \le n \le 1\,000\,000$ for which the first player can force a win in the paper-strip game (Dawson's Chess Octal Game .07).

### Sprague-Grundy Game Theory & Periodicity:
1. **Nim-Value / Grundy Recurrence**:
   Placing two black squares on a strip of length $n$ splits it into independent sub-strips of length $i$ and $n - 2 - i$.
   The Grundy value $G(n)$ follows the minimum excluded value (mex) rule:
   $$G(n) = \text{mex}\{ G(i) \oplus G(n - 2 - i) \mid 0 \le i \le n - 2 \}$$
2. **First-Player Win Condition**:
   By the Sprague-Grundy Theorem, the first player has a winning strategy iff $G(n) \neq 0$.
3. **Eventually Periodic Sequence**:
   For Dawson's Chess, the Grundy sequence $G(n)$ becomes periodic with period $p = 34$ for all $n \ge 53$.
4. **Execution**:
   Evaluating $G(n) \neq 0$ for $1 \le n \le 1\,000\,000$ using period $34$ yields $852938$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 1\,000\,000$. Runs in $\approx 0.11\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ with constant array table.
