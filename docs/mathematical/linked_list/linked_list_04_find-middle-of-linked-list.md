# Formal Mathematical Specification: Find Middle of Linked List

## 1. Definitions and Notation

Let $L$ be a singly linked list defined as a tuple $(V, E, h)$, where:
*   $V = \{v_0, v_1, \dots, v_{n-1}\}$ is the set of $n$ nodes in the list.
*   $E \subset V \times V$ is the set of directed edges such that $(v_i, v_{i+1}) \in E$ for all $0 \le i < n-1$, representing the `next` pointer.
*   $h \in V$ is the head node, $v_0$.
*   The length of the list is $|V| = n$.

We define a successor function $f: V \to V \cup \{\text{null}\}$ such that $f(v_i) = v_{i+1}$ for $i < n-1$, and $f(v_{n-1}) = \text{null}$. We define the $k$-th iteration of the successor function as $f^k(v)$, where $f^0(v) = v$ and $f^k(v) = f(f^{k-1}(v))$.

The objective is to find the node $v_m$ such that:
$$m = \left\lfloor \frac{n}{2} \right\rfloor$$
where the index $m$ corresponds to the second middle node in even-length lists.

## 2. Algebraic Characterization

The algorithm employs two pointers, $s$ (slow) and $f$ (fast), representing elements in $V$. Let $s_k$ and $f_k$ denote the positions of the pointers after $k$ iterations.

**Initialization:**
$s_0 = h$
$f_0 = h$

**State Transitions:**
For each iteration $k \ge 0$:
$$s_{k+1} = f(s_k)$$
$$f_{k+1} = f(f(f_k))$$

**Termination Condition:**
The algorithm terminates at the smallest integer $k$ such that $f_k = \text{null}$ or $f(f_k) = \text{null}$.

**Correctness Invariant:**
At any iteration $k$, the position of the slow pointer is $s_k = f^k(h)$, and the fast pointer is $f_k = f^{2k}(h)$. 
The loop terminates when $2k \ge n-1$. Specifically:
1. If $n$ is odd, $n = 2m + 1$. The loop terminates when $2k = 2m$, i.e., $k = m$. Thus, $s_m = f^m(h)$, which is the node at index $m = \lfloor n/2 \rfloor$.
2. If $n$ is even, $n = 2m$. The loop terminates when $2k = n-2$ (if $f(f_k) = \text{null}$), meaning $k = m-1$. However, the condition $f(f_k) = \text{null}$ implies $f_k$ is the second-to-last node. The next step $s_{k+1}$ moves the slow pointer to $f^m(h)$, which is the node at index $m = n/2$.

Thus, the algorithm correctly identifies $v_{\lfloor n/2 \rfloor}$ for all $n \in \mathbb{N}$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of iterations $k$ required to reach the termination condition. 
As established, the loop terminates when $f_k$ reaches the end of the list. Since $f_k = f^{2k}(h)$, the loop terminates when $2k \approx n$. 
The total number of operations $T(n)$ is proportional to the number of steps taken by the fast pointer:
$$T(n) = \sum_{k=0}^{\lfloor n/2 \rfloor} c = c \cdot \left( \frac{n}{2} + 1 \right)$$
where $c$ is the constant time required for pointer updates.
Therefore, $T(n) \in \Theta(n)$.

### Space Complexity
The algorithm maintains exactly two pointers, $s$ and $f$, regardless of the input size $n$. 
Let $S(n)$ be the auxiliary space complexity:
$$S(n) = \text{size}(s) + \text{size}(f) = O(1) + O(1) = O(1)$$
Since no additional data structures (such as arrays or recursion stacks) are utilized that scale with $n$, the space complexity is strictly $O(1)$.