# Formal Mathematical Specification: K-th Smallest / Order Statistic (Binary Lifting)

## 1. Definitions and Notation

Let $\mathcal{U} = \{1, 2, \dots, M\}$ be the universe of possible values, where $M \in \mathbb{N}$ is the maximum value. We define the state of our collection as a frequency function $f: \mathcal{U} \to \mathbb{N}_0$, where $f(x)$ denotes the number of occurrences of value $x$ in the collection.

The Fenwick Tree (Binary Indexed Tree) is defined as a data structure $\mathcal{B}$ representing the prefix sums of $f$. Specifically, for any index $i \in \{1, \dots, M\}$, the value stored at $\mathcal{B}[i]$ is:
$$\mathcal{B}[i] = \sum_{j=i - \text{lsb}(i) + 1}^{i} f(j)$$
where $\text{lsb}(i) = i \& (-i)$ is the value of the least significant bit of $i$.

The prefix sum function $P(x)$ is defined as:
$$P(x) = \sum_{j=1}^{x} f(j) = \sum_{k \in \text{path}(x)} \mathcal{B}[k]$$
where $\text{path}(x)$ is the set of indices traversed by the standard Fenwick query.

The objective is to find the order statistic $x^*$, defined as:
$$x^* = \min \{ x \in \mathcal{U} \mid P(x) \ge K \}$$
given a target rank $K \in \{1, \dots, \sum_{x \in \mathcal{U}} f(x)\}$.

## 2. Algebraic Characterization

The algorithm utilizes binary lifting to perform a search over the bit-representation of the index space. Let $L = \lfloor \log_2 M \rfloor$. We represent the target index $x^*$ as a sum of powers of two: $x^* = \sum_{i=0}^{L} b_i 2^i$, where $b_i \in \{0, 1\}$.

We maintain two variables during the iteration:
1. `idx`: The current prefix index, initialized to $0$.
2. `remaining`: The remaining rank to satisfy, initialized to $K$.

**Loop Invariant:** At the start of each iteration $j$ (where $j$ ranges from $L$ down to $0$), let $S = 2^j$. The invariant holds that:
$$P(\text{idx}) < K \quad \text{and} \quad P(\text{idx} + S) \text{ is evaluated to determine if } x^* \in (\text{idx}, \text{idx} + S]$$

The transition logic is defined by the property of the Fenwick Tree structure: $\mathcal{B}[\text{idx} + 2^j]$ stores the sum of frequencies in the interval $(\text{idx}, \text{idx} + 2^j]$. 
The update rule is:
$$\text{idx}_{new} = \begin{cases} \text{idx} + 2^j & \text{if } \text{idx} + 2^j \le M \text{ and } \mathcal{B}[\text{idx} + 2^j] < \text{remaining} \\ \text{idx} & \text{otherwise} \end{cases}$$
$$\text{remaining}_{new} = \begin{cases} \text{remaining} - \mathcal{B}[\text{idx} + 2^j] & \text{if condition met} \\ \text{remaining} & \text{otherwise} \end{cases}$$

Upon termination, the invariant ensures that $\text{idx}$ is the largest integer such that $P(\text{idx}) < K$. Consequently, the $K$-th smallest element is $x^* = \text{idx} + 1$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of a single loop iterating through the bits of $M$. Let $L = \lfloor \log_2 M \rfloor$. 
- The loop executes exactly $L+1$ times.
- Inside each iteration, the operations (addition, bitwise comparison, and subtraction) are performed in constant time, $O(1)$.
- The total time complexity is given by the summation:
$$T(M) = \sum_{j=0}^{\lfloor \log_2 M \rfloor} O(1) = O(\log M)$$
This is strictly optimal, as it avoids the $O(\log^2 M)$ complexity associated with performing a binary search over the prefix sum function $P(x)$.

### Space Complexity
- **Auxiliary Space:** The algorithm requires $O(1)$ additional space for the variables `idx`, `bitmask`, and `remaining`.
- **Total Space:** The Fenwick Tree $\mathcal{B}$ requires an array of size $M+1$ to store the frequency sums. Thus, the total space complexity is $O(M)$. 
- Note: If the universe $\mathcal{U}$ is sparse or the range of values is large, coordinate compression is required, mapping the distinct values to the range $[1, N]$ where $N \le \text{number of elements}$, resulting in $O(N)$ space.