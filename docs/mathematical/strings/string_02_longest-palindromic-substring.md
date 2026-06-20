# Formal Mathematical Specification: Longest Palindromic Substring

## 1. Definitions and Notation
Let $S \in \Sigma^*$ be a string of length $n$.
A string $P$ is a palindrome if $P = P^R$, where $P^R$ denotes the reversal of $P$.
We define $S[i \dots j]$ as the substring starting at index $i$ and ending at $j$ (1-indexed).

## 2. Objective
Find $i^*, j^*$ such that $1 \leq i^* \leq j^* \leq n$, $S[i^* \dots j^*]$ is a palindrome, and the length $(j^* - i^* + 1)$ is maximized over all palindromic substrings.

## 3. Algebraic Characterization
A substring $S[i \dots j]$ is a palindrome if and only if:
1. Base cases: $j - i \leq 0 \implies$ True.
2. Inductive step: $S[i] = S[j]$ and $S[i+1 \dots j-1]$ is a palindrome.

## 4. Algorithm Formalization (Dynamic Programming)
Let $P(i, j)$ be a boolean predicate denoting whether $S[i \dots j]$ is a palindrome.
Recurrence relation:
$$ P(i, j) = \begin{cases} 
\text{True} & \text{if } i \geq j \\
S[i] = S[j] \land P(i+1, j-1) & \text{if } i < j
\end{cases} $$

The optimal substring is $\arg\max_{i, j \mid P(i, j)} (j - i + 1)$.

## 5. Algorithm Formalization (Expand Around Center)
For each potential center $c \in \{1, 1.5, 2, \dots, n-0.5, n\}$, define the maximal radius $r(c) \geq 0$ such that $S[\lfloor c - r(c) \rfloor \dots \lceil c + r(c) \rceil]$ is a palindrome.
The algorithm iteratively increments $r(c)$ until the condition fails.
The maximum palindrome length is $\max_c (2 r(c) + 1)$ for integer centers, and $\max_c (2 r(c))$ for half-integer centers.

## 6. Complexity Analysis
- **Time Complexity:** The number of centers is $2n - 1$. Expansion takes at most $n/2$ steps. Thus, time complexity is bounded by $O(n^2)$.
- **Space Complexity:** The Expand Around Center algorithm maintains $O(1)$ state (center indices and current max length). Space is strictly $O(1)$.
