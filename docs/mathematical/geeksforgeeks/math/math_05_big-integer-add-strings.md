# Formal Mathematical Specification: Add Strings (Big Integer Addition)

## 1. Definitions and Notation

Let $\Sigma = \{'0', '1', \dots, '9'\}$ be the alphabet of decimal digits. A non-negative integer $X$ is represented as a string $S_X \in \Sigma^n$, where $n$ is the length of the string. We define a mapping function $\phi: \Sigma \to \{0, 1, \dots, 9\}$ such that $\phi(d)$ returns the integer value of the character $d$.

The value of the string $S_X = d_{n-1}d_{n-2}\dots d_0$ is given by the positional notation:
$$V(S_X) = \sum_{i=0}^{n-1} \phi(d_i) \cdot 10^i$$

**Inputs:** Two strings $A \in \Sigma^N$ and $B \in \Sigma^M$.
**Output:** A string $R \in \Sigma^L$ such that $V(R) = V(A) + V(B)$.
**State Space:** The algorithm maintains a state tuple $(i, c) \in \mathbb{N}_0 \times \{0, 1\}$, where $i$ represents the current digit position (index) being processed, and $c$ represents the carry-over value from the previous position.

## 2. Algebraic Characterization

The addition process is defined by the propagation of a carry $c_i$ through each decimal position $i$. Let $a_i$ and $b_i$ be the digits at position $i$ for strings $A$ and $B$ respectively, where $a_i = 0$ if $i \ge N$ and $b_i = 0$ if $i \ge M$.

For each position $i \in \{0, 1, \dots, \max(N, M)-1\}$, the sum $s_i$ and the carry $c_{i+1}$ are defined by the following recurrence relations:

1. **Summation:** $s_i = \phi(a_i) + \phi(b_i) + c_i$
2. **Digit Extraction:** $r_i = s_i \pmod{10}$
3. **Carry Propagation:** $c_{i+1} = \lfloor s_i / 10 \rfloor$

**Base Case:** $c_0 = 0$.
**Termination:** The process terminates at index $k = \max(N, M)$ such that $c_k = 0$. If $c_k > 0$, the result string $R$ is extended by the digit $\phi^{-1}(c_k)$.

**Loop Invariant:** At the start of each iteration $i$, the partial sum of the processed suffixes of $A$ and $B$ plus the carry $c_i$ is congruent to the total sum modulo $10^i$. Formally, if $A^{(i)}$ and $B^{(i)}$ are the integers represented by the last $i$ digits of $A$ and $B$:
$$V(A^{(i)}) + V(B^{(i)}) + c_i \cdot 10^i = \sum_{j=0}^{i-1} r_j \cdot 10^j + c_i \cdot 10^i$$

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through the digits of the input strings exactly once. Let $N = |A|$ and $M = |B|$. The number of iterations $T$ is governed by the length of the longer string:
$$T = \max(N, M)$$
In each iteration $i$, the operations performed (integer conversion, addition, modulo, and division) are constant time, $O(1)$. The final reversal and join operations take $O(L)$ time, where $L$ is the length of the result string. Since $L \le \max(N, M) + 1$, the total time complexity is:
$$T(N, M) = \sum_{i=1}^{\max(N, M)} O(1) + O(\max(N, M)) = O(\max(N, M))$$

### Space Complexity
The auxiliary space is dominated by the storage of the result digits before the final string construction. 
1. **Result Array:** We store at most $\max(N, M) + 1$ digits.
2. **Pointers and Carry:** We store a constant number of integer variables ($i, c, s, da, db$), which occupy $O(1)$ space.

Thus, the total space complexity is:
$$S(N, M) = O(\max(N, M) + 1) = O(\max(N, M))$$
This is optimal as we must store the output string of length proportional to the input size.