# Formal Mathematical Specification: Min Cost Climbing Stairs

## 1. Definitions and Notation

Let $C = \{c_0, c_1, \dots, c_{n-1}\}$ be a sequence of non-negative integers representing the cost associated with each step $i \in \{0, 1, \dots, n-1\}$, where $n = |C|$. 

We define the state space $\mathcal{S} = \{0, 1, \dots, n\}$ representing the indices of the staircase, where $n$ denotes the "top of the floor" (the destination). 

Let $f(i)$ be the minimum cost to reach step $i$. The objective is to determine $f(n)$, the minimum cost to reach the destination index $n$.

## 2. Algebraic Characterization

The problem is governed by a dynamic programming recurrence relation. To reach step $i$, one must have arrived from either step $i-1$ or step $i-2$. Since the cost $c_j$ is incurred upon departing from step $j$, the total cost to reach step $i$ is the minimum of the costs incurred to reach the previous steps plus the cost of departing from those steps.

### Recurrence Relation
For $i \geq 2$, the optimal substructure is defined as:
$$f(i) = \min(f(i-1) + c_{i-1}, f(i-2) + c_{i-2})$$

### Base Cases
Given that the starting position can be either index $0$ or index $1$ with zero initial cost:
$$f(0) = 0$$
$$f(1) = 0$$

### Objective Function
The goal is to reach index $n$. Since one can arrive at index $n$ from either index $n-1$ or index $n-2$, the final cost is:
$$f(n) = \min(f(n-1) + c_{n-1}, f(n-2) + c_{n-2})$$

### Loop Invariant
Let $p_1^{(k)}$ and $p_2^{(k)}$ denote the values of $f(k)$ and $f(k-1)$ respectively at the start of iteration $k$. The transition maintains the invariant:
$$\forall i \in \{2, \dots, n\}: \text{cur}_i = \min(p_1 + c_{i-1}, p_2 + c_{i-2})$$
where $p_1$ and $p_2$ are updated such that $p_2 \leftarrow p_1$ and $p_1 \leftarrow \text{cur}_i$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single linear pass over the input array $C$. Let $T(n)$ be the number of operations required for an input of size $n$.
The initialization takes $O(1)$ time. The loop executes $n-2$ iterations. Within each iteration, the algorithm performs a constant number of arithmetic operations (addition and comparison), denoted as $k \in \mathbb{R}^+$.
$$T(n) = T_{init} + \sum_{i=2}^{n-1} k = O(1) + (n-2) \cdot O(1) = O(n)$$
Thus, the time complexity is strictly linear, $O(n)$.

### Space Complexity
The algorithm utilizes a fixed number of auxiliary variables ($prev1, prev2, cur$) to store the state of the recurrence. Let $S(n)$ be the auxiliary space complexity.
Since the memory usage does not scale with the input size $n$:
$$S(n) = O(1)$$
The algorithm achieves optimal space efficiency by discarding historical states $f(i-k)$ for $k > 2$, as the recurrence relation exhibits the Markov property—the future state depends only on the two most recent states.