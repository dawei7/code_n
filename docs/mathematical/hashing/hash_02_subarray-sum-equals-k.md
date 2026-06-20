# Formal Mathematical Specification: Subarray Sum Equals K

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of integers where $a_i \in \mathbb{Z}$ for all $i \in \{0, \dots, n-1\}$. Let $k \in \mathbb{Z}$ be the target sum.

We define the **prefix sum sequence** $P = [p_0, p_1, \dots, p_n]$ such that:
- $p_0 = 0$
- $p_j = \sum_{i=0}^{j-1} a_i$ for $1 \le j \le n$

A **contiguous subarray** $A[i \dots j-1]$ (where $0 \le i < j \le n$) has a sum $S(i, j)$ defined as:
$$S(i, j) = \sum_{m=i}^{j-1} a_m = p_j - p_i$$

The objective is to compute the cardinality of the set of index pairs $\mathcal{I} = \{ (i, j) \in \mathbb{Z}^2 \mid 0 \le i < j \le n \text{ and } S(i, j) = k \}$.

Let $f: \mathbb{Z} \to \mathbb{N}_0$ be a frequency map (hash map) where $f(v)$ denotes the number of times a value $v$ has appeared in the prefix sum sequence processed thus far.

## 2. Algebraic Characterization

The condition $S(i, j) = k$ is equivalent to the algebraic identity:
$$p_j - p_i = k \iff p_i = p_j - k$$

For a fixed index $j \in \{1, \dots, n\}$, the number of valid starting indices $i < j$ such that the subarray sum equals $k$ is exactly the number of times the value $(p_j - k)$ has occurred in the set $\{p_0, p_1, \dots, p_{j-1}\}$.

Let $C_j$ be the count of subarrays ending at index $j-1$ with sum $k$. Then:
$$C_j = \sum_{i=0}^{j-1} \mathbb{I}(p_i = p_j - k)$$
where $\mathbb{I}(\cdot)$ is the indicator function. The total count $T$ is:
$$T = \sum_{j=1}^{n} C_j = \sum_{j=1}^{n} f_{j-1}(p_j - k)$$
where $f_{j-1}(v) = |\{m \in \{0, \dots, j-1\} : p_m = v\}|$.

**Loop Invariant:** At the start of iteration $j$ (where $j$ ranges from $0$ to $n-1$), the frequency map $f$ satisfies:
$$f(v) = \sum_{m=0}^{j} \mathbb{I}(p_m = v)$$
This invariant ensures that when processing $p_{j+1}$, the map $f$ contains the counts of all preceding prefix sums, allowing the algorithm to satisfy the requirement $p_i = p_{j+1} - k$ in $O(1)$ expected time.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single pass over the array $A$ of length $n$. 
1. In each iteration $j \in \{0, \dots, n-1\}$, we perform:
   - One addition to update the running prefix sum: $O(1)$.
   - One hash map lookup for $p_j - k$: $O(1)$ expected time.
   - One hash map update for $p_j$: $O(1)$ expected time.

The total time complexity is given by the summation:
$$T(n) = \sum_{j=0}^{n-1} (O(1) + O(1) + O(1)) = O(n)$$
Under the assumption of a uniform hash distribution, the average-case complexity is $\Theta(n)$. In the worst case (e.g., hash collisions), the complexity is $O(n^2)$, though this is mitigated by robust hash function implementations.

### Space Complexity
The space complexity is determined by the storage requirements of the frequency map $f$.
- In the worst case, all prefix sums $\{p_0, p_1, \dots, p_n\}$ are distinct.
- The map stores at most $n+1$ entries.
- Each entry consists of a key (the prefix sum) and a value (the frequency).

Thus, the auxiliary space complexity is $O(n)$. Total space complexity is $O(n)$ to store the input array and the hash map.