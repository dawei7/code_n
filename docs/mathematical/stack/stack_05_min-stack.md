# Formal Mathematical Specification: Min Stack

## 1. Definitions and Notation

Let $\mathcal{V} \subseteq \mathbb{Z}$ be the domain of values that can be stored in the stack. We define the state of the Min Stack as a sequence of pairs $S = \langle (v_1, m_1), (v_2, m_2), \dots, (v_k, m_k) \rangle$, where $k \in \mathbb{N}_0$ denotes the current number of elements in the stack.

- **State Space:** The state space $\mathcal{S}$ is defined as the set of all finite sequences of pairs in $\mathcal{V} \times \mathcal{V}$.
- **Main Stack ($M$):** A projection onto the first component, $M = \langle v_1, v_2, \dots, v_k \rangle$, representing the LIFO order of elements.
- **Min Stack ($N$):** A projection onto the second component, $N = \langle m_1, m_2, \dots, m_k \rangle$, where $m_i$ represents the minimum value in the prefix of the main stack up to index $i$.
- **Operations:**
    - $\text{push}: \mathcal{S} \times \mathcal{V} \to \mathcal{S}$
    - $\text{pop}: \mathcal{S} \to \mathcal{S}$
    - $\text{top}: \mathcal{S} \to \mathcal{V}$
    - $\text{getMin}: \mathcal{S} \to \mathcal{V}$

## 2. Algebraic Characterization

The correctness of the Min Stack is governed by the inductive definition of the minimum value at each depth $k$.

**Base Case:**
For an empty stack $S_0 = \langle \rangle$, the operations are undefined (or return an error).

**Inductive Step:**
Given a stack $S_k = \langle (v_1, m_1), \dots, (v_k, m_k) \rangle$:

1. **Push Operation:** For a value $x \in \mathcal{V}$, the new state $S_{k+1}$ is:
   $$S_{k+1} = S_k \oplus (x, m_{k+1}) \quad \text{where} \quad m_{k+1} = \min(x, m_k)$$
   (With $m_0 = \infty$ for the initial state).

2. **Pop Operation:** The state $S_{k-1}$ is obtained by the truncation of the sequence:
   $$S_{k-1} = \langle (v_1, m_1), \dots, (v_{k-1}, m_{k-1}) \rangle$$

3. **Top Operation:**
   $$\text{top}(S_k) = v_k$$

4. **GetMin Operation:**
   $$\text{getMin}(S_k) = m_k$$

**Invariant:**
For all $i \in \{1, \dots, k\}$, the value $m_i$ satisfies:
$$m_i = \min_{1 \le j \le i} \{v_j\}$$
This invariant is maintained by the definition of $m_{k+1} = \min(v_{k+1}, m_k)$, which effectively propagates the global minimum of the prefix $\{v_1, \dots, v_{k+1}\}$ to the top of the auxiliary stack.

## 3. Complexity Analysis

### Time Complexity
Let $T_{op}$ be the time complexity of an operation.
- **Push:** The operation involves a comparison $\min(x, m_k)$ and an append to two sequences. Since these are $O(1)$ operations in a dynamic array (amortized), $T_{\text{push}} = O(1)$.
- **Pop:** The operation involves a removal from the end of two sequences. $T_{\text{pop}} = O(1)$.
- **Top/GetMin:** These operations involve a single index access to the end of the sequence (e.g., $S[k]$). Thus, $T_{\text{top}} = O(1)$ and $T_{\text{getMin}} = O(1)$.

Since all operations are independent of the total number of elements $n$ currently in the stack, the total time complexity for a sequence of $m$ operations is $O(m)$.

### Space Complexity
The space complexity is determined by the storage of the sequences $M$ and $N$.
- **Total Space:** We store $k$ pairs of integers. The space required is $S(k) = 2k \cdot \text{sizeof}(\text{int})$.
- **Asymptotic Space:** As $k$ grows to $n$ (the maximum number of elements pushed), the space complexity is $O(n)$.
- **Auxiliary Space:** The algorithm requires $O(n)$ auxiliary space to maintain the `min_stack` alongside the `main_stack`. Even if optimized to a single stack of tuples, the space remains $\Theta(n)$ to preserve the history of minimums required for $O(1)$ rollback.