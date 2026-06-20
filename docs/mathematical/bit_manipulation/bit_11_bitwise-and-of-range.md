# Formal Mathematical Specification: Bitwise AND of Numbers Range

## 1. Definitions and Notation

Let $\mathbb{Z}_{\ge 0}$ denote the set of non-negative integers. We define the input domain as a pair $(L, R) \in \mathbb{Z}_{\ge 0}^2$ such that $0 \le L \le R \le 2^{31} - 1$. 

Let $b_k(n) \in \{0, 1\}$ denote the $k$-th bit of the binary representation of $n$, such that $n = \sum_{k=0}^{30} b_k(n) \cdot 2^k$. 

The objective is to compute the function $f: \mathbb{Z}_{\ge 0}^2 \to \mathbb{Z}_{\ge 0}$ defined by the bitwise AND operator ($\land$):
$$f(L, R) = \bigwedge_{i=L}^{R} i$$
where the bitwise AND of a set of integers is defined bit-wise:
$$b_k(f(L, R)) = \prod_{i=L}^{R} b_k(i)$$
where the product $\prod$ is taken over the Boolean domain $\{0, 1\}$ (equivalent to the logical AND).

## 2. Algebraic Characterization

**Theorem:** The bitwise AND of the range $[L, R]$ is equal to the value obtained by masking all bits to the right of the most significant bit where $L$ and $R$ differ.

**Proof Sketch:**
Consider the binary representations of $L$ and $R$. Let $k_{max}$ be the largest index such that $b_{k_{max}}(L) \neq b_{k_{max}}(R)$. For any $k > k_{max}$, $b_k(L) = b_k(R) = c_k$. Since $L \le R$, it must be that $b_{k_{max}}(L) = 0$ and $b_{k_{max}}(R) = 1$. 

For any $k \le k_{max}$, there exists at least one integer $x \in [L, R]$ such that $b_k(x) = 0$. Specifically, the range $[L, R]$ contains a transition point where the $k$-th bit flips from $1$ to $0$ or vice versa. Consequently, $\prod_{i=L}^{R} b_k(i) = 0$ for all $k \le k_{max}$.

Thus, the result is:
$$f(L, R) = \sum_{k=k_{max}+1}^{30} c_k \cdot 2^k$$

**Algorithm Invariant:**
Let $(L_t, R_t, s_t)$ be the state at iteration $t$.
1. Initialization: $L_0 = L, R_0 = R, s_0 = 0$.
2. Transition: If $L_t < R_t$, then $L_{t+1} = \lfloor L_t / 2 \rfloor$, $R_{t+1} = \lfloor R_t / 2 \rfloor$, and $s_{t+1} = s_t + 1$.
3. Termination: The loop terminates at $T$ when $L_T = R_T$.
4. Invariant: $f(L, R) = L_T \cdot 2^{s_T}$.

This invariant holds because right-shifting both $L$ and $R$ by $s$ positions is equivalent to dividing by $2^s$. The process effectively truncates the bits that are not common to both $L$ and $R$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a sequence of right-shift operations. The number of iterations $T$ is determined by the position of the most significant bit where $L$ and $R$ differ. 
Since $L, R < 2^{31}$, the maximum number of bits is $W = 31$. The loop condition $L < R$ is satisfied at most $W$ times. 
The work per iteration is $O(1)$ (a bitwise shift and an increment). Thus, the total time complexity is:
$$T(W) = \sum_{t=1}^{T} O(1) = O(W)$$
Given $W$ is a fixed constant (the word size of the architecture), the complexity is $O(1)$.

### Space Complexity
The algorithm maintains a constant number of integer variables: `left`, `right`, and `shift`. 
The memory required is independent of the magnitude of the input $L$ and $R$.
$$S(L, R) = \Theta(1)$$
Thus, the auxiliary space complexity is $O(1)$.