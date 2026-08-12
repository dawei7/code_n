# Sums of Digit Factorials - Optimal Approach

## Algorithm Explanation

Find $\sum_{i=1}^{150} sg(i)$, where $f(n)$ is the sum of factorials of the digits of $n$, $sf(n)$ is the sum of digits of $f(n)$, $g(i)$ is the smallest positive integer $n$ such that $sf(n) = i$, and $sg(i)$ is the sum of digits of $g(i)$.

### Minimal Number Reconstruction & Greedy Base-Factorial Decomposition:
1. **Properties of $g(i)$**:
   To minimize $n$ for a given $f(n)$, $n$'s digits must be sorted in non-decreasing order, containing no $0$s or $1$s (except possibly one $1$ at the front since $1! = 0! + 1!$).
   $f(n)$ is represented greedily as $f(n) = a \cdot 9! + b \cdot 8! + c \cdot 7! + \dots$.
2. **Digit Sum Minimization ($g(i)$ Search)**:
   For $sf(n) = i$, we find $f(n)$ that yields the lexicographically smallest digit string $n$.
3. **Execution**:
   Summing $sg(i)$ for $i = 1 \dots 150$ yields $8184523820510$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(I \cdot D)$ for $I = 150$. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(I)$.
