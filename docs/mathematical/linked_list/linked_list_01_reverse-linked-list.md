# Formal Mathematical Specification: Reverse Linked List

## 1. Definitions and Notation

Let a singly linked list be defined as a tuple $L = (V, E, h)$, where:
*   $V = \{v_1, v_2, \dots, v_n\}$ is a finite set of nodes.
*   $E \subset V \times V$ is a set of directed edges representing the `next` pointers. The list structure implies that $E$ forms a simple path: $v_{i} \to v_{i+1}$ for $1 \le i < n$.
*   $h \in V$ is the head of the list, where $h = v_1$.
*   The terminal node $v_n$ satisfies $\nexists u \in V$ such that $(v_n, u) \in E$. We denote the terminal state as $\text{null}$.

The state of the algorithm at any iteration $k$ is defined by the triple $\mathcal{S}_k = (\text{prev}_k, \text{curr}_k, \text{next\_node}_k)$, where $\text{prev}_k, \text{curr}_k \in V \cup \{\text{null}\}$.

The goal is to define a transformation function $f: L \to L'$ such that $L' = (V, E', h')$, where:
*   $E' = \{ (v_{i+1}, v_i) \mid 1 \le i < n \}$.
*   $h' = v_n$.

## 2. Algebraic Characterization

The algorithm proceeds by maintaining a loop invariant that ensures the partial reversal of the list. Let $E_k$ be the set of edges at iteration $k$.

**Loop Invariant:**
At the start of each iteration $k$ (where $k=0$ corresponds to the initial state), the list is partitioned into two segments:
1.  A reversed segment: $v_k \to v_{k-1} \to \dots \to v_1 \to \text{null}$.
2.  An unreversed segment: $v_{k+1} \to v_{k+2} \to \dots \to v_n \to \text{null}$.

Formally, for $0 \le k \le n$:
*   $\text{prev}_k = v_k$ (with $v_0 = \text{null}$).
*   $\text{curr}_k = v_{k+1}$ (with $v_{n+1} = \text{null}$).
*   The edges $E_k$ are defined as:
    $$E_k = \{ (v_j, v_{j-1}) \mid 2 \le j \le k \} \cup \{ (v_j, v_{j+1}) \mid k+1 \le j < n \}$$

**State Transition:**
The transition from $\mathcal{S}_k$ to $\mathcal{S}_{k+1}$ is governed by the following atomic updates:
1.  $\text{next\_node}_{k+1} = \text{curr}_k.\text{next}$
2.  $\text{curr}_k.\text{next} = \text{prev}_k$
3.  $\text{prev}_{k+1} = \text{curr}_k$
4.  $\text{curr}_{k+1} = \text{next\_node}_{k+1}$

The algorithm terminates when $\text{curr}_k = \text{null}$, at which point $\text{prev}_k = v_n$, which is the new head $h'$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single traversal of the linked list. Let $T(n)$ be the number of operations required for a list of length $n$.
The loop executes exactly $n$ times, as $\text{curr}$ transitions from $v_1$ to $v_n$ and finally to $\text{null}$. Within each iteration, the operations (pointer assignment, variable updates) are constant time, $O(1)$.
The total time complexity is given by the summation:
$$T(n) = \sum_{k=1}^{n} c = c \cdot n = O(n)$$
Thus, the algorithm is linear with respect to the number of nodes $n$.

### Space Complexity
The space complexity $S(n)$ is the sum of the auxiliary space used by the algorithm.
The algorithm maintains a fixed number of pointers: $\text{prev}$, $\text{curr}$, and $\text{next\_node}$. Regardless of the input size $n$, the memory allocated for these pointers is constant:
$$S(n) = S_{\text{aux}} + S_{\text{input}} = O(1) + O(n)$$
Since we are interested in the auxiliary space complexity (the additional space required beyond the input structure), we have:
$$S_{\text{aux}} = O(1)$$
This satisfies the requirement for an in-place transformation.