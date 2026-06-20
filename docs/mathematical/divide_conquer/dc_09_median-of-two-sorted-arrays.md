# Formal Mathematical Specification: Median of Two Sorted Arrays

## 1. Definitions and Notation

Let $A = \{a_0, a_1, \dots, a_{m-1}\}$ and $B = \{b_0, b_1, \dots, b_{n-1}\}$ be two sequences of real numbers such that $a_i \le a_{i+1}$ for all $0 \le i < m-1$ and $b_j \le b_{j+1}$ for all $0 \le j < n-1$. Without loss of generality, assume $m \le n$.

Let $S = A \cup B$ be the multiset union of $A$ and $B$, where $|S| = N = m + n$. The median $\mu$ of $S$ is defined as:
- If $N$ is odd: $\mu = \text{select}(S, \lceil N/2 \rceil)$, where $\text{select}$ returns the $k$-th smallest element.
- If $N$ is even: $\mu = \frac{1}{2} (\text{select}(S, N/2) + \text{select}(S, N/2 + 1))$.

We define a partition index $i \in \{0, \dots, m\}$ for $A$ and $j \in \{0, \dots, n\}$ for $B$. These indices define the left and right subsets:
$L_A = \{a_k \mid k < i\}, R_A = \{a_k \mid k \ge i\}$
$L_B = \{b_k \mid k < j\}, R_B = \{b_k \mid k \ge j\}$

## 2. Algebraic Characterization

The objective is to find a partition $(i, j)$ such that the union of the left partitions $L = L_A \cup L_B$ and the right partitions $R = R_A \cup R_B$ satisfy the following conditions:

1. **Cardinality Constraint:** $|L| = \lfloor \frac{m+n+1}{2} \rfloor$. Given $i$, $j$ is uniquely determined as $j = \lfloor \frac{m+n+1}{2} \rfloor - i$.
2. **Boundary Condition:** Every element in $L$ must be less than or equal to every element in $R$. Formally:
   $$\max(L_A \cup L_B) \le \min(R_A \cup R_B)$$
   
   Defining the boundary values (with $\pm \infty$ as sentinels for empty sets):
   - $\text{maxLeft}_A = a_{i-1}$ (if $i>0$, else $-\infty$)
   - $\text{maxLeft}_B = b_{j-1}$ (if $j>0$, else $-\infty$)
   - $\text{minRight}_A = a_i$ (if $i<m$, else $+\infty$)
   - $\text{minRight}_B = b_j$ (if $j<n$, else $+\infty$)

The partition is valid if and only if:
$$\text{maxLeft}_A \le \text{minRight}_B \quad \land \quad \text{maxLeft}_B \le \text{minRight}_A$$

If $\text{maxLeft}_A > \text{minRight}_B$, then $i$ is too large; we must decrease $i$. If $\text{maxLeft}_B > \text{minRight}_A$, then $i$ is too small; we must increase $i$. This monotonicity allows for a binary search over the domain $i \in [0, m]$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a binary search over the index $i \in [0, m]$. In each iteration of the binary search, we perform a constant number of comparisons and arithmetic operations, $O(1)$. 

The search space is reduced by half in each step:
$$T(m) = T(m/2) + O(1)$$
By the Master Theorem, where $a=1, b=2, f(n)=O(1)$, we have $T(m) = \Theta(\log m)$. Since we enforce $m \le n$ by swapping if necessary, the complexity is:
$$T(m, n) = O(\log(\min(m, n)))$$

### Space Complexity
The algorithm maintains a fixed set of scalar variables ($i, j, \text{lo}, \text{hi}, \text{half}, \text{left\_max}, \text{right\_min}$) regardless of the input size $m$ and $n$. No auxiliary data structures (such as arrays or recursion stacks) are allocated that scale with input size. Thus, the auxiliary space complexity is:
$$S(m, n) = O(1)$$