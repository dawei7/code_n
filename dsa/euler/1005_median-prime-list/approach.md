# Problem 1005: Median Prime List - Mathematical Approach & Analysis

## 1. Problem Formulation & Prime Partitions

A **prime partition** of an integer $N$ is a strictly increasing sequence of primes $(p_1, p_2, \dots, p_k)$ such that:
$$
p_1 < p_2 < \dots < p_k \quad \text{and} \quad \sum_{i=1}^k p_i = N
$$
We sort all valid prime partitions of $N$ in **lexicographical order**.
- Let $M$ be the total number of partitions.
- If $M$ is odd, the median list is the $\frac{M+1}{2}$-th list.
- If $M$ is even, we disregard the last list and choose the $\frac{M}{2}$-th list.

We seek the product $\prod_{i=1}^k p_i \bmod 10^9$ of the median prime list of $N = 2026$.

---

## 2. Dynamic Programming for Partition Counts

Let $C(s, i)$ denote the number of strictly increasing prime partitions of the integer $s$ using only primes from $\{p_i, p_{i+1}, \dots\}$.
The recurrence relation is:
$$
C(s, i) = C(s, i+1) + C(s - p_i, i+1)
$$
with base cases:
- $C(0, i) = 1$ for all $i$,
- $C(s, i) = 0$ if $s < 0$ or $p_i > s$.

We compute the 2D table $C(s, i)$ for all $0 \le s \le 2026$ and primes $p_i \le 2026$.
The total number of partitions of $2026$ is $M = C(2026, 0)$.

---

## 3. Lexicographic Bisection & Median Extraction

To extract the target $K$-th partition $(p_1, p_2, \dots)$ in lexicographic order:
1. Initialize remaining sum $S = 2026$, remaining rank $R = K$, and candidate prime index $i = 0$.
2. For each candidate prime $p_i$:
   - If we choose $p_i$ as the next element, the number of completions is $W = C(S - p_i, i+1)$.
   - If $R \le W$, we MUST select $p_i$, append $p_i$ to our list, set $S \leftarrow S - p_i, i \leftarrow i+1$, and repeat.
   - If $R > W$, we skip $p_i$, decrement $R \leftarrow R - W$, and test the next prime $i \leftarrow i+1$.
3. When $S = 0$, the list $(p_1, \dots, p_k)$ is the exact median prime partition.

Computing the product modulo $10^9$:
$$
\prod_{i=1}^k p_i \equiv 826079755 \pmod{10^9}
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(N \cdot \pi(N))$ for the 2D partition table and $O(\pi(N))$ for greedy bisection.
- **Space Complexity**: $O(N \cdot \pi(N))$ DP table.
- **Sample Verification**: For $N = 20$, partitions are $(2, 5, 13), (2, 7, 11), (3, 17), (7, 13) \implies$ median is $(2, 7, 11)$.
