# Formal Mathematical Specification: Partition Equal Subset Sum

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_n\}$ be a multiset of $n$ positive integers, where $a_i \in \mathbb{Z}^+$. We define the total sum of the multiset as $S = \sum_{i=1}^n a_i$.

The objective is to determine the existence of a partition of $A$ into two disjoint subsets $A_1, A_2 \subset A$ such that $A_1 \cup A_2 = A$, $A_1 \cap A_2 = \emptyset$, and $\sum_{x \in A_1} x = \sum_{y \in A_2} y$.

Let the target sum be $T = \frac{S}{2}$. The problem is equivalent to determining the existence of a subset $A_1 \subseteq A$ such that $\sum_{x \in A_1} x = T$.

We define the state space $\mathcal{S} = \{0, 1, \dots, T\}$. Let $dp[s]$ be a boolean predicate defined as:
$$dp[s] = \begin{cases} 1 & \text{if } \exists A' \subseteq \{a_1, \dots, a_i\} \text{ such that } \sum_{x \in A'} x = s \\ 0 & \text{otherwise} \end{cases}$$

## 2. Algebraic Characterization

### Necessary Condition
For a partition to exist, the total sum $S$ must be even. If $S \equiv 1 \pmod 2$, then $\sum_{x \in A_1} x = \sum_{y \in A_2} y$ implies $2 \sum_{x \in A_1} x = S$, which is a contradiction for integer sums. Thus, if $S$ is odd, the solution is $\bot$ (False).

### Recurrence Relation
Given $S$ is even, we define the transition for the inclusion of the $i$-th element $a_i$. Let $dp_i[s]$ denote the reachability of sum $s$ using a subset of the first $i$ elements. The recurrence is:
$$dp_i[s] = dp_{i-1}[s] \lor dp_{i-1}[s - a_i]$$
where $dp_i[s] = 0$ if $s < 0$. The base case is $dp_0[0] = 1$ and $dp_0[s] = 0$ for $s > 0$.

### Invariant
The algorithm maintains the invariant that after processing the $i$-th element, the set of reachable sums $\mathcal{R}_i = \{s \in \mathcal{S} \mid dp_i[s] = 1\}$ satisfies:
$$\mathcal{R}_i = \mathcal{R}_{i-1} \cup \{s + a_i \mid s \in \mathcal{R}_{i-1}, s + a_i \leq T\}$$
The algorithm terminates with a solution if $T \in \mathcal{R}_n$.

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through $n$ elements. For each element $a_i$, we perform a linear scan (or set update) over the range $[0, T]$. 
The total number of operations is bounded by:
$$T(n) = \sum_{i=1}^n \sum_{s=0}^T 1 = O(n \cdot T)$$
Substituting $T = \frac{S}{2}$, the complexity is $O(n \cdot S)$. In the worst case, where $S$ is proportional to $n \cdot \max(A)$, the complexity is $O(n^2 \cdot \max(A))$.

### Space Complexity
By utilizing a 1D array (or a bitset) of size $T+1$ to store the reachability of each sum, we avoid the $O(n \cdot T)$ space requirement of the naive 2D DP table.
The auxiliary space required is:
$$S(n) = O(T) = O\left(\frac{\sum_{i=1}^n a_i}{2}\right)$$
Since $T$ is the maximum value we need to track, the space complexity is strictly $O(S)$. In terms of the input parameters, this is $O(n \cdot \bar{a})$, where $\bar{a}$ is the average value of the elements in $A$.