# Formal Mathematical Specification: Next Greater Element (Monotonic Stack)

## 1. Definitions and Notation

Let $A = \langle a_0, a_1, \dots, a_{n-1} \rangle$ be a sequence of $n$ integers, where $a_i \in \mathbb{Z}$. We define the domain of indices as $I = \{0, 1, \dots, n-1\}$.

The **Next Greater Element (NGE)** function, $f: I \to \mathbb{Z} \cup \{-1\}$, is defined as:
$$f(i) = \begin{cases} a_j & \text{where } j = \min \{k \in I \mid k > i \land a_k > a_i\} \\ -1 & \text{if } \{k \in I \mid k > i \land a_k > a_i\} = \emptyset \end{cases}$$

The algorithm maintains a state represented by a stack $S$, which is an ordered sequence of indices $\langle s_0, s_1, \dots, s_m \rangle$ such that $s_m$ is the top of the stack. The stack satisfies the **monotonicity invariant**:
$$\forall j \in \{0, \dots, m-1\}, \quad a_{s_j} \ge a_{s_{j+1}}$$
This ensures that the values corresponding to the indices in the stack are non-increasing from bottom to top.

## 2. Algebraic Characterization

The algorithm processes the sequence $A$ through a single pass. Let $S_i$ denote the state of the stack after processing index $i$. The transition from $S_{i-1}$ to $S_i$ is governed by the following operations:

1. **Pop Phase:** Let $S_{i-1} = \langle s_0, \dots, s_m \rangle$. We iteratively remove elements from the top of the stack as long as the condition $a_i > a_{s_m}$ holds. Let $k$ be the number of elements popped. The new stack $S'$ is $\langle s_0, \dots, s_{m-k} \rangle$. For each popped index $s_j$ (where $j \in \{m-k+1, \dots, m\}$), we assign:
   $$f(s_j) = a_i$$
2. **Push Phase:** The current index $i$ is appended to the stack:
   $$S_i = S' \oplus \langle i \rangle$$

**Correctness Invariant:**
At any step $i$, for all $j \in I$ such that $j < i$ and $f(j)$ has not been assigned, $j$ is contained in the stack $S_i$. Furthermore, for any $j \in S_i$, $a_j$ is the value of the most recent element to the left of $i$ that has not yet found its NGE. Because the stack is monotonically decreasing, if $a_i > a_{s_m}$, then $a_i$ is the *first* element to the right of $s_m$ that is strictly greater than $a_{s_m}$, satisfying the definition of $f(s_m)$.

## 3. Complexity Analysis

### Time Complexity
We define the total time complexity $T(n)$ as the sum of the costs of all operations. Let $P$ be the total number of `push` operations and $Q$ be the total number of `pop` operations.

*   Each index $i \in \{0, \dots, n-1\}$ is pushed onto the stack exactly once. Thus, $P = n$.
*   Since an index can only be popped if it has previously been pushed, the total number of `pop` operations is bounded by the number of `push` operations: $Q \le P = n$.
*   The work performed in each iteration $i$ consists of one `push` and $k_i$ `pop` operations, where $k_i$ is the number of elements popped at step $i$. The total time complexity is:
    $$T(n) = \sum_{i=0}^{n-1} (1 + k_i) = n + \sum_{i=0}^{n-1} k_i$$
    Since $\sum k_i = Q \le n$, we have $T(n) \le 2n$. Therefore, $T(n) = O(n)$.

### Space Complexity
The space complexity $S(n)$ is determined by the auxiliary storage required for the stack and the result array.
*   The result array requires $O(n)$ space to store the $n$ values of $f(i)$.
*   In the worst-case scenario (e.g., a strictly decreasing input sequence $a_0 > a_1 > \dots > a_{n-1}$), no elements are popped until the end, and the stack grows to size $n$.
*   Thus, the total space complexity is:
    $$S(n) = O(n) + O(n) = O(n)$$