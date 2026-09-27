# Guided Example: Unique Binary Search Trees

We trace the step-by-step 1D dynamic programming recurrence and closed-form Catalan evaluation on representative tree sizes:

- **Input:** $n = 3$
- **Required output:** $5$
- **Sequence Progression:** $n = 1 \to 1, \; n = 2 \to 2, \; n = 3 \to 5, \; n = 4 \to 14$

This instance demonstrates decomposing the number of structurally unique BSTs into independent left and right subtree counts, establishing the Catalan recurrence $G(n) = \sum_{i=1}^n G(i - 1) \cdot G(n - i)$, evaluating the 1D DP table, and deriving the $O(n)$ mathematical combination formula $C_n = \frac{1}{n+1}\binom{2n}{n}$.

---

## 1. Instance & Teaching Goal

Given an integer $n = 3$, return the number of structurally unique Binary Search Trees (BSTs) which have exactly $n$ nodes of unique values from $1$ to $n$.

Consider picking each value $i \in \{1, 2, 3\}$ as the root:
- **Root $i = 1$:**
  - Left subtree must contain values $< 1$: $\emptyset$ ($0$ nodes) $\implies G(0)$ possibilities.
  - Right subtree must contain values $> 1$: $\{2, 3\}$ ($2$ nodes) $\implies G(2)$ possibilities.
  - Combinations: $G(0) \times G(2) = 1 \times 2 = 2$.
- **Root $i = 2$:**
  - Left subtree: $\{1\}$ ($1$ node) $\implies G(1)$ possibilities.
  - Right subtree: $\{3\}$ ($1$ node) $\implies G(1)$ possibilities.
  - Combinations: $G(1) \times G(1) = 1 \times 1 = 1$.
- **Root $i = 3$:**
  - Left subtree: $\{1, 2\}$ ($2$ nodes) $\implies G(2)$ possibilities.
  - Right subtree: $\emptyset$ ($0$ nodes) $\implies G(0)$ possibilities.
  - Combinations: $G(2) \times G(0) = 2 \times 1 = 2$.

Total unique BSTs for $n = 3$:
$$
G(3) = 2 + 1 + 2 = 5
$$

A naive recursion without memoization repeats subproblem counts exponentially in $O(3^n)$ time.
Dynamic programming builds the array $G[0 \dots n]$ in $O(n^2)$ time, and the direct Catalan multiplicative formula computes the answer in $O(n)$ time with $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### The Catalan DP Recurrence
Let $G(n)$ denote the number of unique BSTs that can be formed with $n$ nodes.
Let $F(i, n)$ denote the number of unique BSTs when $i$ ($1 \le i \le n$) is chosen as the root of an $n$-node tree.

1. **Subtree Factoring:**
   Since BST values to the left must be strictly less than $i$, the left subtree contains $i - 1$ nodes.
   Since BST values to the right must be strictly greater than $i$, the right subtree contains $n - i$ nodes.
   Because the left and right subtree structures can be chosen independently:
   $$
   F(i, n) = G(i - 1) \times G(n - i)
   $$
2. **Total Sum:**
   Summing over all possible choices of the root $i \in [1, n]$:
   $$
   G(n) = \sum_{i=1}^n F(i, n) = \sum_{i=1}^n G(i - 1) \cdot G(n - i)
   $$
3. **Base Cases:**
   - $G(0) = 1$ (an empty tree is a single valid structure).
   - $G(1) = 1$ (a single root node is a single valid structure).

### Closed-Form Combinatorial Formula
The sequence $G(n)$ is identically the $n$-th Catalan number $C_n$:
$$
C_n = \frac{1}{n + 1}\binom{2n}{n} = \prod_{k=2}^n \frac{n + k}{k}
$$

> **Invariant.** For every integer $k \le n$, $G[k]$ stores the exact count of unique BST topologies for $k$ nodes.

---

## 3. Step-by-Step Worked Execution

We trace computing $G[0 \dots 3]$:

### Base Cases
- $G[0] = 1$
- $G[1] = 1$

---

### Step 1: Compute $G[2]$ ($n = 2$)
- $i = 1$ as root: Left $G[0]$, Right $G[1] \implies 1 \times 1 = 1$.
- $i = 2$ as root: Left $G[1]$, Right $G[0] \implies 1 \times 1 = 1$.
- Sum:
  $$
  G[2] = 1 + 1 = 2
  $$

---

### Step 2: Compute $G[3]$ ($n = 3$)
- $i = 1$ as root:
  $$
  G[0] \cdot G[2] = 1 \times 2 = 2
  $$
- $i = 2$ as root:
  $$
  G[1] \cdot G[1] = 1 \times 1 = 1
  $$
- $i = 3$ as root:
  $$
  G[2] \cdot G[0] = 2 \times 1 = 2
  $$
- Sum:
  $$
  G[3] = 2 + 1 + 2 = \mathbf{5}
  $$

---

### Step 3: Compute $G[4]$ ($n = 4$) (Extended Verification)
- $i = 1$: $G[0] \cdot G[3] = 1 \times 5 = 5$.
- $i = 2$: $G[1] \cdot G[2] = 1 \times 2 = 2$.
- $i = 3$: $G[2] \cdot G[1] = 2 \times 1 = 2$.
- $i = 4$: $G[3] \cdot G[0] = 5 \times 1 = 5$.
- Sum:
  $$
  G[4] = 5 + 2 + 2 + 5 = 14
  $$

---

### Step 4: The Same Values from the Multiplicative Closed Form

The combination formula can be evaluated without ever forming a factorial, by chaining the ratio between consecutive Catalan numbers:
$$
\frac{C_k}{C_{k-1}} = \frac{4k - 2}{k + 1}
$$
Starting from $C_0 = 1$ and applying one multiplication and one division per step reproduces every DP entry, and the two columns must agree at every row:

| Step $k$ | Multiplier $\frac{4k - 2}{k + 1}$ | Previous value $C_{k-1}$ | Product | $C_k$ | DP value $G[k]$ |
|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | $\frac{2}{2} = 1$ | $C_0 = 1$ | $1 \times 1$ | 1 | 1 |
| 2 | $\frac{6}{3} = 2$ | $C_1 = 1$ | $1 \times 2$ | 2 | 2 |
| 3 | $\frac{10}{4} = \frac{5}{2}$ | $C_2 = 2$ | $2 \times \frac{5}{2}$ | 5 | 5 |
| 4 | $\frac{14}{5}$ | $C_3 = 5$ | $5 \times \frac{14}{5}$ | 14 | 14 |
| 5 | $\frac{18}{6} = 3$ | $C_4 = 14$ | $14 \times 3$ | 42 | 42 |
| 6 | $\frac{22}{7}$ | $C_5 = 42$ | $42 \times \frac{22}{7}$ | 132 | 132 |

Every row divides exactly, which is the point of this formulation: the factor $\frac{4k-2}{k+1}$ is never an integer on its own, yet it always cancels against the previous Catalan value, so the running product stays integral and no factorial term is ever materialised.

---

## 4. Complete Execution Trace

| Tree Size $n$ | Root Loop $i$ | Left Subtree Nodes ($i - 1$) | Right Subtree Nodes ($n - i$) | Term $G[i-1] \times G[n-i]$ | Running Sum $G[n]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | - | - | - | Base definition | 1 |
| 1 | 1 | 0 | 0 | $G[0] \cdot G[0] = 1 \times 1 = 1$ | 1 |
| 2 | 1 | 0 | 1 | $G[0] \cdot G[1] = 1 \times 1 = 1$ | 1 |
| 2 | 2 | 1 | 0 | $G[1] \cdot G[0] = 1 \times 1 = 1$ | 2 |
| **3** | **1** | 0 | 2 | $G[0] \cdot G[2] = 1 \times 2 = 2$ | 2 |
| **3** | **2** | 1 | 1 | $G[1] \cdot G[1] = 1 \times 1 = 1$ | 3 |
| **3** | **3** | 2 | 0 | $G[2] \cdot G[0] = 2 \times 1 = 2$ | **5 (Result)** |
| 4 | 1, 2, 3, 4 | - | - | $5 + 2 + 2 + 5$ | 14 |

---

## 5. Algorithmic Correctness

**Soundness.** For any root $i \in [1, n]$, the keys placed in the left subtree $\{1, \dots, i-1\}$ are all strictly smaller than $i$, and the keys placed in the right subtree $\{i+1, \dots, n\}$ are all strictly larger than $i$. The number of structural topologies depends only on the **number of nodes**, not their actual values. Multiplying left and right counts computes the exact Cartesian combinations without overlap.

**Completeness.** Every valid BST has a unique root from $1 \dots n$. Because the summation partitions all possible roots into mutually exclusive cases and covers all $i \in [1, n]$, no structural topology is missed.

---

## 6. Traps This Instance Exposes

The boundaries below are all consequences of the recurrence or of the arithmetic used to evaluate it:

| Boundary | Input | Result | Why it behaves that way |
|:---|:---|:---|:---|
| Smallest legal input | $n = 1$ | 1 | The only term is $G[0] \cdot G[0] = 1 \times 1$, so the answer is the single node. |
| Degenerate base case | $n = 3$ with $G[0]$ set to $0$ instead of $1$ | 0 instead of 5 | The two skewed root choices $i = 1$ and $i = 3$ each multiply by $G[0]$, so a zero base case erases $4$ of the $5$ trees. |
| Term symmetry | $n = 4$ | $5 + 2 + 2 + 5 = 14$ | $F(i, n) = G[i-1]\,G[n-i]$ satisfies $F(i, n) = F(n+1-i, n)$, so the root loop is palindromic and the terms pair up around the middle. |
| Constraint ceiling | $n = 19$ | 1767263190 | The largest legal answer is below $2^{31} - 1 = 2147483647$, so a signed 32-bit return type still holds it. |
| Factorial-first evaluation | $n = 19$ | $(2n)! = 38!$ | The intermediate value is about $5.23 \times 10^{44}$, which overflows any 64-bit integer long before the division by $(n+1)!\,n!$ can shrink it back. |

- **Base Case $G[0] = 0$ instead of $1$:** If $G[0]$ is set to $0$, any choice where one child is empty (such as $i = 1$ or $i = n$) would multiply by $0$, incorrectly zeroing out all valid skewed trees. $G[0]$ must be $1$ representing the unique empty tree.
- **Integer Overflow with Closed Form:** While $C_n = \frac{(2n)!}{(n+1)! n!}$, computing $(2n)!$ directly in languages with 32-bit or 64-bit integers overflows quickly. Computing using iterative multiplication $C = C \times \frac{4k - 2}{k + 1}$ or using Python's arbitrary-precision integers avoids overflow.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Dynamic Programming:** $O(n^2)$. Outer loop runs $n$ times; inner loop runs $i$ times, totaling $\sum_{i=1}^n i = \frac{n(n+1)}{2} = O(n^2)$ iterations.
  - **Direct Mathematical Catalan:** $O(n)$ using single-loop combination multiplication.
- **Auxiliary Space Complexity:** $O(n)$ for the 1D DP table, or $O(1)$ for the mathematical closed-form approach.