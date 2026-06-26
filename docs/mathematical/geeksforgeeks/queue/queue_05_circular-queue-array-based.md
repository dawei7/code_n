# Formal Mathematical Specification: Circular Queue (Array Based)

## 1. Definitions and Notation

Let $K \in \mathbb{Z}^+$ be the fixed capacity of the circular queue. We define the state of the queue as a tuple $\mathcal{S} = (A, h, t, n)$, where:

*   $A = [a_0, a_1, \dots, a_{K-1}]$ is a sequence of elements where $a_i \in \mathcal{D} \cup \{\perp\}$, and $\mathcal{D}$ is the domain of data elements. $\perp$ denotes an uninitialized or logically empty slot.
*   $h \in \{0, 1, \dots, K-1\}$ is the index of the front element (head).
*   $t \in \{0, 1, \dots, K-1\}$ is the index of the most recently inserted element (tail).
*   $n \in \{0, 1, \dots, K\}$ is the current number of elements stored in the queue.

The state space $\mathcal{S}$ is defined by the Cartesian product $\mathcal{D}^K \times \mathbb{Z}_K \times \mathbb{Z}_K \times \{0, \dots, K\}$.

## 2. Algebraic Characterization

The circular queue is governed by the following transition functions and invariants. We define the modulo operator as $x \pmod K$.

### State Transitions
Given an operation, the state $\mathcal{S}_i = (A_i, h_i, t_i, n_i)$ evolves to $\mathcal{S}_{i+1}$ as follows:

1.  **`enQueue(v)`**: If $n_i < K$:
    *   $t_{i+1} = (t_i + 1) \pmod K$
    *   $A_{i+1}[t_{i+1}] = v$
    *   $n_{i+1} = n_i + 1$
    *   $h_{i+1} = h_i$ (if $n_i = 0$, $h_{i+1} = t_{i+1}$)

2.  **`deQueue()`**: If $n_i > 0$:
    *   $h_{i+1} = (h_i + 1) \pmod K$
    *   $n_{i+1} = n_i - 1$
    *   $t_{i+1} = t_i$

### Invariants
The correctness of the structure is maintained by the following invariants:
*   **Size Constraint:** $0 \le n \le K$.
*   **Empty Condition:** The queue is empty if and only if $n = 0$.
*   **Full Condition:** The queue is full if and only if $n = K$.
*   **Tail-Head Relationship:** If $n > 0$, the index of the tail is related to the head by:
    $t = (h + n - 1) \pmod K$.

## 3. Complexity Analysis

### Time Complexity
Let $T(op)$ be the time complexity of any operation $op \in \{\text{enQueue, deQueue, Front, Rear, isEmpty, isFull}\}$.

Each operation consists of a constant number of arithmetic operations (addition, modulo) and memory access operations (array indexing). Specifically, for any operation:
$$T(op) = \Theta(1)$$
Since the modulo operator $x \pmod K$ is implemented in hardware as a bitwise operation or a single division instruction, the execution time is independent of the capacity $K$ or the number of elements $n$. Thus, the amortized and worst-case time complexity is $O(1)$.

### Space Complexity
The space complexity is determined by the storage required for the array $A$ and the auxiliary variables $(h, t, n)$.

*   **Auxiliary Space:** The variables $h, t, n$ require $O(1)$ space.
*   **Total Space:** The array $A$ requires $K$ slots of size $|\mathcal{D}|$. 
$$S(K) = \text{sizeof}(A) + \text{sizeof}(h, t, n) = K \cdot |\mathcal{D}| + O(1)$$
Asymptotically, the space complexity is $O(K)$. This is optimal for a fixed-capacity buffer as it achieves the theoretical lower bound for storing $K$ elements.