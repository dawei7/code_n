# Formal Mathematical Specification: Evaluate Reverse Polish Notation

## 1. Definitions and Notation

Let $\Sigma$ be the set of valid tokens, defined as $\Sigma = \mathbb{Z} \cup \mathcal{O}$, where $\mathbb{Z}$ is the set of integers and $\mathcal{O} = \{+, -, *, /\}$ is the set of binary arithmetic operators.

An RPN expression is represented as a sequence $T = (t_1, t_2, \dots, t_N)$, where $t_i \in \Sigma$. The evaluation of $T$ is a mapping $f: \Sigma^N \to \mathbb{Z}$.

We define the state of the algorithm at step $k$ (where $0 \le k \le N$) as a tuple $(\sigma_k, \tau_k)$, where:
*   $\sigma_k \in \mathbb{Z}^*$ is a stack, represented as a finite sequence of integers. We denote the empty stack as $\epsilon$.
*   $\tau_k = (t_{k+1}, \dots, t_N)$ is the remaining suffix of the input sequence.

The division operator $/$ is defined as the truncation-toward-zero function:
$$a / b = \text{sgn}(a/b) \cdot \lfloor |a/b| \rfloor$$
where $a, b \in \mathbb{Z}, b \neq 0$.

## 2. Algebraic Characterization

The algorithm defines a state transition function $\delta: (\mathbb{Z}^*, \Sigma) \to \mathbb{Z}^*$. Given a stack $\sigma$ and a token $t$, the transition is defined as:

1.  **If $t \in \mathbb{Z}$:**
    $$\delta(\sigma, t) = \sigma \cdot [t]$$
    where $\cdot$ denotes the concatenation of the sequence $\sigma$ with the singleton sequence $[t]$.

2.  **If $t \in \mathcal{O}$:**
    Let $\sigma = (\dots, a, b)$. Then:
    $$\delta(\sigma, t) = (\dots, a \circ_t b)$$
    where $\circ_t$ is the binary operation corresponding to $t \in \{+, -, *, /\}$.

**Correctness Invariant:**
Let $S_k$ be the stack after processing $k$ tokens. For any valid RPN expression $T$, the algorithm maintains the invariant that the stack contains the partial results of the expression tree traversal. Specifically, if $T$ represents a tree $E$, then after $N$ steps, the stack $\sigma_N$ contains exactly one element $v \in \mathbb{Z}$, such that $v = \text{eval}(E)$.

The evaluation is governed by the recursive structure of the postfix expression:
$$ \text{eval}(T) = \begin{cases} t_1 & \text{if } N=1 \\ \text{eval}(T_{left}) \circ \text{eval}(T_{right}) & \text{if } t_N \in \mathcal{O} \end{cases} $$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single linear scan of the input sequence $T$. Let $N$ be the number of tokens.
For each token $t_i$:
*   If $t_i \in \mathbb{Z}$, the operation is a stack `push`, which is $O(1)$.
*   If $t_i \in \mathcal{O}$, the operation involves two `pop` operations and one `push` operation, each $O(1)$.

The total time complexity $T(N)$ is given by the summation:
$$T(N) = \sum_{i=1}^{N} c_i$$
where $c_i$ is the constant time cost of the $i$-th operation. Since $c_i = \Theta(1)$ for all $i$, we have:
$$T(N) = \Theta(N)$$

### Space Complexity
The space complexity is determined by the maximum depth of the stack $\sigma$. 
Let $n_i$ be the number of operands and $o_i$ be the number of operators encountered up to step $i$. The stack size $|\sigma_i|$ is given by:
$$|\sigma_i| = n_i - o_i$$
In the worst-case scenario, where all operands appear before all operators (e.g., $T = (z_1, z_2, \dots, z_{N/2}, o_1, o_2, \dots, o_{N/2})$), the stack grows to size $N/2$. 

Since the auxiliary space required for the stack is proportional to the number of elements pushed, the space complexity is:
$$S(N) = O(N)$$
This is optimal, as the stack must store intermediate operands to satisfy the postfix evaluation order.