# Formal Mathematical Specification: Implement Queue using Stacks

## 1. Definitions and Notation

Let $\Sigma$ be the set of all possible elements that can be stored in the queue. We define the state of the system as a pair of stacks, $S = (S_{in}, S_{out})$, where each stack is an ordered sequence of elements from $\Sigma$.

*   **Stack Definition:** A stack $S$ is a finite sequence $(s_1, s_2, \dots, s_k)$ where $s_k$ is the top element. We define the operations:
    *   $\text{push}(S, x) = (s_1, \dots, s_k, x)$
    *   $\text{pop}(S) = (s_1, \dots, s_{k-1})$ with return value $s_k$
    *   $\text{peek}(S) = s_k$
    *   $\text{empty}(S) \iff |S| = 0$

*   **Queue State:** The logical queue $Q$ is represented by the concatenation of the elements in $S_{in}$ and the reversal of $S_{out}$. Specifically, if $S_{in} = (i_1, i_2, \dots, i_n)$ and $S_{out} = (o_1, o_2, \dots, o_m)$, the logical queue is:
    $$Q = (o_m, o_{m-1}, \dots, o_1, i_1, i_2, \dots, i_n)$$

*   **Operations:**
    *   $\text{Push}(x)$: $S_{in} \leftarrow \text{push}(S_{in}, x)$
    *   $\text{Pop}()$: If $S_{out}$ is empty, $S_{out} \leftarrow \text{reverse}(S_{in})$ and $S_{in} \leftarrow \emptyset$. Then return $\text{pop}(S_{out})$.

## 2. Algebraic Characterization

The correctness of the implementation relies on the invariant that the logical queue $Q$ is preserved across all operations.

**Invariant:** At any time $t$, the sequence of elements in the queue is given by the mapping $\mathcal{M}: (S_{in}, S_{out}) \to Q$ defined as:
$$\mathcal{M}(S_{in}, S_{out}) = \text{reverse}(S_{out}) \cdot S_{in}$$
where $\cdot$ denotes sequence concatenation.

**Transition Rules:**
1.  **Push:** For an element $x \in \Sigma$, the new state $(S'_{in}, S'_{out})$ satisfies:
    $$\mathcal{M}(S'_{in}, S'_{out}) = \text{reverse}(S_{out}) \cdot (S_{in} \cdot x) = \mathcal{M}(S_{in}, S_{out}) \cdot x$$
    This confirms the FIFO property for insertion.

2.  **Pop/Peek:** Let $Q = (q_1, q_2, \dots, q_k)$.
    *   If $S_{out} \neq \emptyset$, then $q_1 = \text{peek}(S_{out})$.
    *   If $S_{out} = \emptyset$, then $S_{in} = (q_k, q_{k-1}, \dots, q_1)$. After the transfer $S_{out} = \text{reverse}(S_{in}) = (q_1, q_2, \dots, q_k)$, the top of $S_{out}$ is $q_1$.
    In both cases, the operation retrieves the head of the logical queue $q_1$ and updates the state to $Q' = (q_2, \dots, q_k)$.

## 3. Complexity Analysis

### Time Complexity
We employ the **Aggregate Method** for amortized analysis. Let $n$ be the total number of operations.

*   **Push:** Each `push` operation involves exactly one `push` to $S_{in}$, which is $O(1)$.
*   **Pop/Peek:** A `pop` operation takes $O(1)$ if $S_{out} \neq \emptyset$. If $S_{out} = \emptyset$, it takes $O(k)$ where $k = |S_{in}|$.
*   **Amortized Cost:** Each element $x$ is pushed onto $S_{in}$ once, moved from $S_{in}$ to $S_{out}$ at most once, and popped from $S_{out}$ at most once.
    Let $c_i$ be the cost of the $i$-th operation. The total cost $T(n)$ is:
    $$T(n) = \sum_{i=1}^n c_i \leq n + 2n = 3n$$
    The amortized cost per operation is $\frac{T(n)}{n} = O(1)$.

### Space Complexity
The space complexity is determined by the storage of $N$ elements across two stacks.
*   **Total Space:** Since each element $x$ exists in exactly one of $S_{in}$ or $S_{out}$ at any given time, the total space is:
    $$|S_{in}| + |S_{out}| = N$$
*   **Auxiliary Space:** The algorithm requires $O(N)$ space to maintain the elements, which is optimal for a queue of size $N$.