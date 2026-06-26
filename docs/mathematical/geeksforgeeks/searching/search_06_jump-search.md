# Formal Mathematical Specification: Jump Search (Block Search)

## 1. Definitions and Notation

Let $A = (a_0, a_1, \dots, a_{n-1})$ be a sequence of elements drawn from a totally ordered set $(\mathcal{X}, \le)$, such that for all $i, j \in \{0, \dots, n-1\}$, if $i < j$, then $a_i \le a_j$. 
Let $x \in \mathcal{X}$ be the target value. 
We define the search space as the index set $\mathcal{I} = \{0, 1, \dots, n-1\}$.

The algorithm utilizes a jump parameter $m \in \mathbb{Z}^+$, where $m = \lfloor \sqrt{n} \rfloor$.
We define the set of jump indices as $\mathcal{J} = \{k \cdot m \mid k \in \mathbb{N}_0, k \cdot m < n\} \cup \{n-1\}$.

The output is a function $f: \mathcal{X} \times \mathcal{I}^n \to \mathcal{I} \cup \{-1\}$ defined as:
$$f(x, A) = \begin{cases} i & \text{if } a_i = x \\ -1 & \text{if } \forall i \in \mathcal{I}, a_i \neq x \end{cases}$$

## 2. Algebraic Characterization

The algorithm partitions $\mathcal{I}$ into a sequence of blocks $B_k = \{i \in \mathbb{Z} \mid (k-1)m \le i < \min(km, n)\}$ for $k = 1, 2, \dots, \lceil n/m \rceil$.

### Loop Invariant
Let $p_k$ denote the value of the variable `prev` at the start of the $k$-th iteration of the jump phase. The invariant maintained is:
1. If $x \in A$, then there exists some $k$ such that $x \in \{a_i \mid p_k \le i < \min(p_k + m, n)\}$.
2. For all $j < p_k$, $a_j < x$.

### Termination Condition
The jump phase terminates at the smallest index $k^*$ such that $a_{\min(k^*m, n)-1} \ge x$ or $k^*m \ge n$. 
The search space is then restricted to the interval $[p_{k^*}, \min(p_{k^*} + m, n))$. The correctness of the subsequent linear search is guaranteed by the monotonicity of $A$: since $a_{p_{k^*-1}} < x$ and $a_{\min(k^*m, n)-1} \ge x$, the Intermediate Value Theorem for discrete ordered sets implies that if $x$ exists, it must reside within the identified block.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two distinct phases: the jump phase and the linear search phase.

1. **Jump Phase:** The number of jumps is $N_J = \lceil n/m \rceil$. In each jump, we perform a constant number of comparisons. Thus, the time complexity is $O(n/m)$.
2. **Linear Search Phase:** In the worst case, the target is at the end of the block, requiring $N_L = m - 1$ comparisons.

The total time complexity $T(n)$ is given by:
$$T(n) = O\left(\frac{n}{m} + m\right)$$
To minimize $T(n)$, we differentiate with respect to $m$:
$$\frac{d}{dm} \left( \frac{n}{m} + m \right) = -\frac{n}{m^2} + 1$$
Setting the derivative to zero yields $m^2 = n$, or $m = \sqrt{n}$. Substituting $m = \sqrt{n}$ into the complexity expression:
$$T(n) = O\left(\frac{n}{\sqrt{n}} + \sqrt{n}\right) = O(\sqrt{n} + \sqrt{n}) = O(\sqrt{n})$$
Thus, the worst-case time complexity is $\Theta(\sqrt{n})$.

### Space Complexity
The algorithm maintains a fixed number of scalar variables: `step`, `prev`, and `index`. These variables occupy $O(1)$ space. As no auxiliary data structures proportional to the input size $n$ are allocated, the total auxiliary space complexity is:
$$S(n) = O(1)$$