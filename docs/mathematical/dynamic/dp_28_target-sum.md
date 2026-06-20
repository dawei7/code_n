# Formal Mathematical Specification: Target Sum

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_n\}$ be a multiset of $n$ non-negative integers, where $a_i \in \mathbb{N}_0$. Let $T \in \mathbb{Z}$ be the target integer. We define the total sum of the multiset as $\Sigma = \sum_{i=1}^n a_i$.

We seek the number of sequences of signs $\sigma = (\sigma_1, \sigma_2, \dots, \sigma_n)$ where $\sigma_i \in \{+1, -1\}$ such that:
$$\sum_{i=1}^n \sigma_i a_i = T$$

Let $P \subseteq \{1, \dots, n\}$ be the set of indices such that $\sigma_i = +1$, and $N \subseteq \{1, \dots, n\}$ be the set of indices such that $\sigma_i = -1$. By definition, $P \cup N = \{1, \dots, n\}$ and $P \cap N = \emptyset$. The expression becomes:
$$\sum_{i \in P} a_i - \sum_{j \in N} a_j = T$$

Given $\sum_{i \in P} a_i + \sum_{j \in N} a_j = \Sigma$, we add the two equations to obtain:
$$2 \sum_{i \in P} a_i = T + \Sigma \implies \sum_{i \in P} a_i = \frac{T + \Sigma}{2}$$

Let $S = \frac{T + \Sigma}{2}$. The problem is equivalent to finding the number of subsets $P \subseteq \{1, \dots, n\}$ such that the sum of elements in $P$ equals $S$.

## 2. Algebraic Characterization

We define the state space $\mathcal{S} = \{0, 1, \dots, S\}$. Let $dp[k][s]$ denote the number of subsets of the first $k$ elements $\{a_1, \dots, a_k\}$ that sum to exactly $s$.

**Base Case:**
For $k=0$, the only subset is the empty set $\emptyset$, which sums to 0.
$$dp[0][0] = 1, \quad dp[0][s] = 0 \text{ for } s > 0$$

**Recurrence Relation:**
For each element $a_k$, we have two choices: either exclude $a_k$ from the subset or include it (provided $s \geq a_k$). The transition is defined as:
$$dp[k][s] = dp[k-1][s] + dp[k-1][s - a_k]$$
where $dp[k-1][s - a_k] = 0$ if $s < a_k$.

**Space-Optimized Invariant:**
By observing that $dp[k]$ depends only on $dp[k-1]$, we can reduce the state to a 1D array $dp[s]$. To ensure we use values from the previous iteration $k-1$ when computing iteration $k$, we iterate $s$ in descending order:
$$dp_{new}[s] = dp_{old}[s] + dp_{old}[s - a_k]$$
The invariant maintained at the start of each iteration $k$ is that $dp[s]$ represents the number of subsets of $\{a_1, \dots, a_{k-1}\}$ that sum to $s$.

**Constraints for Existence:**
A solution exists if and only if:
1. $(T + \Sigma) \equiv 0 \pmod 2$
2. $|T| \leq \Sigma$
If these conditions are not met, the number of ways is 0.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of an outer loop iterating through each of the $n$ elements of the input array. The inner loop iterates through the possible sums from $S$ down to $a_k$.
The total number of operations is given by the summation:
$$T(n, S) = \sum_{k=1}^n (S - a_k + 1) \approx O(n \cdot S)$$
Since $S = \frac{T + \Sigma}{2}$, the time complexity is $O(n \cdot \Sigma)$, where $\Sigma$ is the sum of the elements in the input array.

### Space Complexity
The algorithm utilizes a 1D array of size $S+1$ to store the number of ways to reach each partial sum.
$$Space = \Theta(S) = \Theta\left(\frac{T + \Sigma}{2}\right) = O(\Sigma)$$
The auxiliary space is $O(S)$ as we only maintain the state of the current subset sum counts, effectively performing a rolling update on the DP table.