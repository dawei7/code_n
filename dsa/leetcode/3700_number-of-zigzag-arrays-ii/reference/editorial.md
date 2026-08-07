### Approach: Dynamic Programming + Matrix Exponentiation

#### Intuition

This problem is the hard version of [「3699. Number of Zigzag Arrays I」](https://leetcode.com/problems/number-of-zigzag-arrays-i/). It is recommended to first understand the dynamic programming solution to the prerequisite problem, as well as the basic idea of matrix exponentiation.

Compared to the previous problem, the range of the lower and upper bounds, $l$ and $r$, is significantly smaller, while the array length can be as large as $10^9$. As a result, it is no longer feasible to perform transitions by iterating through all positions.

Let us revisit the dynamic programming transition. In the previous problem, prefix sums were used to optimize individual state transitions. This reveals that each state can be expressed as a linear combination of the components of the previous state, which means the transition can be represented using a state transition matrix. Repeatedly multiplying the initial state by this transition matrix yields the final state. Once the transition is expressed in matrix form, the transition matrix must be square, and repeated transitions correspond to taking powers of that matrix. We can therefore apply fast matrix exponentiation, reducing the outer time complexity from $O(n)$ to $O(\log n)$.

Next, let us construct the state vector and transition matrix.

Let $m = r - l + 1$ denote the size of the value range. As in the previous problem, we maintain two state vectors of length $m$: $\textit{dp}_0$ and $\textit{dp}_1$.
- $\textit{dp}_0$ represents states where the last two elements form a strictly decreasing pair.
- $\textit{dp}_1$ represents states where the last two elements form a strictly increasing pair.

Each state vector has its own transition matrix. Let:
- $A$ be the transition matrix from $\textit{dp}_0$ to $\textit{dp}_1$.
- $B$ be the transition matrix from $\textit{dp}_1$ to $\textit{dp}_0$.

The transitions can then be written as

$$\begin{aligned}
\textit{dp}_0[i] = \textit{dp}_1[i-1] \cdot B \\
\textit{dp}_1[i] = \textit{dp}_0[i-1] \cdot A
\end{aligned}$$

Using block matrices, we can merge the two state vectors into a single state vector of length $2m$:
$[\textit{dp}\text{\_0}[i],, \textit{dp}\text{\_1}[i]]$
This yields the unified transition equation

$\begin{bmatrix} \textit{dp}\text{\_0}[i] \& \textit{dp}\text{\_1}[i] \end{bmatrix} = \begin{bmatrix} \textit{dp}_0[i-1] \& \textit{dp}_1[i-1] \end{bmatrix} \cdot \begin{bmatrix} O \& A \\ B \& O \end{bmatrix}$

Among them, the large square matrix $U = \begin{bmatrix} O \& A \\ B \& O \end{bmatrix}$ is the merged state transition matrix, of size $(2 \cdot m) \times (2 \cdot m)$, where $O$ is the $m \times m$ zero matrix. The block anti-diagonal structure arises because the two state vectors transition into each other alternately: $\textit{dp}_0$ depends only on the previous $\textit{dp}_1$, and vice versa.

The remaining task is to construct matrices $A$ and $B$.

Both matrices are of size $m\times m$.

- **Matrix $A$ (transition from $\textit{dp}_0$ to $\textit{dp}_1$)**
  Let $i$ and $j$ denote row and column indices, respectively (1-indexed). When computing $\textit{dp}_0 \cdot A$, the $j$-th component of the new state is obtained by taking the dot product of $\textit{dp}_0$ with the $j$-th column of $A$.
  To transition into $\textit{dp}_1$, the new element must be strictly greater than the previous element. Therefore, we need to sum all previous states whose values are smaller than $j$. Consequently, in the $j$-th column of $A$, rows $1$ through $j-1$ contain $1$, while all other entries are $0$.
  Thus, $A$ is a strictly upper triangular matrix whose entries above the main diagonal are all $1$.

- **Matrix $B$ (transition from $\textit{dp}_1$ to $\textit{dp}_0$)**
  Similarly, transitioning into $\textit{dp}_0$ requires the new element to be strictly smaller than the previous element. Therefore, in the $j$-th column of $B$, rows $j+1$ through $m$ contain $1$, while all other entries are $0$.
  Thus, $B$ is a strictly lower triangular matrix whose entries below the main diagonal are all $1$.

For an intuitive understanding, take $m = 3$ as an example. Then matrices $A$ and $B$ are respectively:

$A = \begin{bmatrix} 0 \& 1 \& 1 \\ 0 \& 0 \& 1 \\ 0 \& 0 \& 0 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \& 0 \& 0 \\ 1 \& 0 \& 0 \\ 1 \& 1 \& 0 \end{bmatrix}$

Assemble them into a complete $6 \times 6$ state transition matrix $U$ according to the rules of block matrices, as follows:

$$U = \left[
\begin{array}{ccc:ccc}
0 \& 0 \& 0 \& 0 \& 1 \& 1 \\
0 \& 0 \& 0 \& 0 \& 0 \& 1 \\
0 \& 0 \& 0 \& 0 \& 0 \& 0 \\
\hdashline
0 \& 0 \& 0 \& 0 \& 0 \& 0 \\
1 \& 0 \& 0 \& 0 \& 0 \& 0 \\
1 \& 1 \& 0 \& 0 \& 0 \& 0
\end{array}
\right]$$

Suppose the length of the target zigzag array is $n$, then the final state is $\textit{dp}[n-1]$, and the solution process is as follows:

$\textit{dp}[n-1] = \textit{dp}[0] \cdot U^{n-1}$

We initialize $\textit{dp}[0]$ as a vector whose components are all $1$, compute $U^{n-1}$ using fast matrix exponentiation, and then sum all components of the resulting state vector to obtain the answer.

The matrix exponentiation procedure is identical to ordinary binary exponentiation, except that integer multiplication is replaced by matrix multiplication. One implementation detail is worth noting: instead of starting with an identity matrix, we can directly use $\textit{dp}[0]$ as the accumulator during exponentiation. Since $\textit{dp}[0]$ is a $1\times 2m$ vector, every multiplication still produces a $1\times 2m$ vector, reducing the cost of several intermediate matrix multiplications.

#### Implementation

```python
class Solution:
    MOD = 1_000_000_007

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]
                if r == 0:
                    continue
                for j in range(m):
                    res[i][j] = (res[i][j] + r * b[k][j]) % self.MOD
        return res

    def powMul(self, base, exp, res):
        while exp > 0:
            if exp & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            exp >>= 1
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = self.powMul(u, n - 1, dp)
        ans = 0
        for i in range(size):
            ans = (ans + dp[0][i]) % self.MOD

        return ans
```

#### Complexity Analysis

Let $m$ be the size of the interval, i.e., $m = r - l + 1$.

- Time complexity: $O(m^3 \log n)$.

  Constructing the transition matrix requires $O(m^2)$ time. Each matrix multiplication takes $O(m^3)$ time, and fast matrix exponentiation performs $O(\log n)$ such multiplications. Therefore, the total time complexity is $O(m^3 \log n)$. The final summation of the state vector requires $O(m)$ time, which does not affect the overall complexity.

- Space complexity: $O(m^2)$.

  The transition matrix requires $O(m^2)$ space. The state vector requires $O(m)$ space, and the temporary matrices used during multiplication require an additional $O(m^2)$ space. Therefore, the overall space complexity is $O(m^2)$.

---