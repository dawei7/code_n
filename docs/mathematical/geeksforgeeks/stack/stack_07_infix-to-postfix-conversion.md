# Formal Mathematical Specification: Infix to Postfix Conversion

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet consisting of three disjoint sets:
1. $\mathcal{O} = \{+, -, *, /\}$ (the set of binary operators).
2. $\mathcal{P} = \{(, )\}$ (the set of grouping symbols).
3. $\mathcal{A} = \{a, b, c, \dots\}$ (the set of operands).

An infix expression $E$ is a string $E \in (\mathcal{A} \cup \mathcal{O} \cup \mathcal{P})^*$. We define a precedence function $\rho: \mathcal{O} \to \mathbb{Z}^+$ such that:
$$\rho(op) = \begin{cases} 1 & \text{if } op \in \{+, -\} \\ 2 & \text{if } op \in \{*, /\} \end{cases}$$

Let $S$ be a stack, defined as a sequence $S = \langle s_1, s_2, \dots, s_k \rangle$, where $s_k$ is the top element. Let $\Phi$ be the output string (the postfix representation). The algorithm defines a state transition function $f: (\Sigma, S, \Phi) \to (S', \Phi')$.

## 2. Algebraic Characterization

The correctness of the Shunting-Yard algorithm relies on the maintenance of an invariant regarding operator precedence. For any two operators $op_1, op_2 \in \mathcal{O}$ where $op_1$ is currently at the top of the stack and $op_2$ is the incoming operator, the algorithm enforces the following transition:

If $op_2$ is encountered, we pop $op_1$ from $S$ to $\Phi$ if and only if:
$$\rho(op_1) \geq \rho(op_2) \land op_1 \neq '('$$

This ensures that the postfix string $\Phi$ satisfies the property that for any sub-expression, the operator with the highest precedence is applied to its operands before operators of lower precedence, preserving the semantics of the original infix expression $E$.

Formally, let $E = e_1 e_2 \dots e_n$. The algorithm processes each $e_i$ according to the following transition rules:
1. **Operand:** If $e_i \in \mathcal{A}$, then $\Phi_{i} = \Phi_{i-1} \cdot e_i$.
2. **Left Parenthesis:** If $e_i = '(',$ then $S_{i} = S_{i-1} \cdot ('(')$.
3. **Right Parenthesis:** If $e_i = ')',$ then $S_i$ is reduced by popping all $op \in \mathcal{O}$ such that $\rho(op)$ is defined, appending them to $\Phi$ until $S_{top} = '('.$
4. **Operator:** If $e_i \in \mathcal{O}$, let $S_{top}$ be the top of the stack. While $S_{top} \neq '('$ and $\rho(S_{top}) \geq \rho(e_i)$, perform $\Phi \leftarrow \Phi \cdot \text{pop}(S)$. Finally, push $e_i$ onto $S$.

The final postfix expression is $\Phi_n \cdot \text{pop}(S)^k$, where $k = |S|$.

## 3. Complexity Analysis

### Time Complexity
Let $N$ be the length of the input string $E$. We define the total time complexity $T(N)$ as the sum of operations performed on each character $e_i \in E$.

Each character $e_i$ is pushed onto the stack $S$ at most once and popped from the stack at most once. 
- For operands, the operation is $O(1)$.
- For operators, let $k_i$ be the number of operators popped from the stack for a given $e_i$. The total time is:
$$T(N) = \sum_{i=1}^{N} (1 + k_i)$$
Since each operator is pushed exactly once, the total number of pops across the entire execution is bounded by $N$. Thus, $\sum_{i=1}^{N} k_i \leq N$.
Therefore, $T(N) = O(N) + O(N) = O(N)$.

### Space Complexity
The space complexity $S(N)$ is determined by the auxiliary storage required for the stack $S$ and the output string $\Phi$.
- The output string $\Phi$ has length $N$, requiring $O(N)$ space.
- The stack $S$ can contain at most $N$ elements in the worst case (e.g., an expression with nested parentheses or increasing precedence).
- Thus, the total space complexity is:
$$S(N) = \text{Space}(\Phi) + \text{Space}(S) = O(N) + O(N) = O(N)$$
The algorithm is strictly linear in both time and space relative to the input size $N$.