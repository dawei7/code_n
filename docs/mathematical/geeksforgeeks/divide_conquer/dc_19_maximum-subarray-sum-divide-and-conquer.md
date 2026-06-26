# Formal Mathematical Specification: Maximum Subarray Sum (Divide and Conquer)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ integers, where $a_i \in \mathbb{Z}$. 
A contiguous subarray $A[i..j]$ is defined as the sequence $(a_i, a_{i+1}, \dots, a_j)$ for $0 \le i \le j < n$.
The sum of a subarray $A[i..j]$ is given by the function $S(i, j) = \sum_{k=i}^{j} a_k$.

The objective is to find the maximum subarray sum, denoted by $\mathcal{M}(A)$, defined as:
$$\mathcal{M}(A) = \max_{0 \le i \le j < n} S(i, j)$$

We define the domain of the recursive function $f(lo, hi)$ as the maximum subarray sum contained within the index range $[lo, hi] \subseteq \{0, \dots, n-1\}$. The state space $\mathcal{S}$ consists of all valid index pairs $(lo, hi)$ such that $0 \le lo \le hi < n$.

## 2. Algebraic Characterization

The algorithm relies on the principle of optimality for divide and conquer. For any range $[lo, hi]$, let $mid = \lfloor \frac{lo + hi}{2} \rfloor$. The maximum subarray sum $\mathcal{M}(lo, hi)$ must satisfy the following recurrence relation:

$$\mathcal{M}(lo, hi) = \begin{cases} a_{lo} & \text{if } lo = hi \\ \max\left( \mathcal{M}(lo, mid), \mathcal{M}(mid+1, hi), \mathcal{C}(lo, mid, hi) \right) & \text{if } lo < hi \end{cases}$$

Where $\mathcal{C}(lo, mid, hi)$ is the maximum crossing sum, defined as the maximum sum of a subarray that contains both $a_{mid}$ and $a_{mid+1}$:

$$\mathcal{C}(lo, mid, hi) = \left( \max_{lo \le i \le mid} \sum_{k=i}^{mid} a_k \right) + \left( \max_{mid+1 \le j \le hi} \sum_{k=mid+1}^{j} a_k \right)$$

Let $L(lo, mid) = \max_{lo \le i \le mid} \sum_{k=i}^{mid} a_k$ and $R(mid+1, hi) = \max_{mid+1 \le j \le hi} \sum_{k=mid+1}^{j} a_k$. These values are computed in $O(mid - lo + 1)$ and $O(hi - mid)$ time respectively, ensuring that the crossing sum is determined in linear time relative to the size of the current range.

## 3. Complexity Analysis

### Time Complexity
The algorithm follows a divide and conquer paradigm. Let $T(n)$ denote the time complexity for an input of size $n$. The recurrence relation for the work performed is:
$$T(n) = 2T\left(\frac{n}{2}\right) + f(n)$$
where $f(n)$ represents the work required to compute the crossing sum $\mathcal{C}$ and the final comparison. Since the crossing sum requires two linear scans across the range $[lo, hi]$, $f(n) = \Theta(n)$.

Applying the **Master Theorem** for recurrences of the form $T(n) = aT(n/b) + \Theta(n^k)$:
- Here, $a=2, b=2, k=1$.
- Since $\log_b a = \log_2 2 = 1$, and $k = \log_b a$, we fall into Case 2 of the Master Theorem.
- Therefore, $T(n) = \Theta(n^1 \log n) = O(n \log n)$.

### Space Complexity
The space complexity is determined by the maximum depth of the recursion tree and the auxiliary storage used at each stack frame.
1. **Recursion Stack:** The recursion tree has a depth of $\lceil \log_2 n \rceil$. Each frame stores a constant number of variables ($lo, hi, mid, left\_best, right\_best, s, left\_sum, right\_sum$). Thus, the stack space is $O(\log n)$.
2. **Auxiliary Space:** The algorithm operates in-place on the input array $A$. No additional data structures proportional to $n$ are allocated.

Consequently, the total space complexity is $O(\log n)$.