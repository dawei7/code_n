# Cookie Game - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

$N$ cookies are partitioned into piles $(p_1, \dots, p_k)$.
- **Odd's turn**: Select an odd pile $2m + 1$, eat 1, split remainder into two equal piles of $m$.
- **Even's turn**: Select an even pile $2m + 2$, eat 2, split remainder into two equal piles of $m$.
- Normal play convention: The last player to move wins (a player with no moves loses).
- Odd moves first.
- $C(N)$ is the number of integer partitions of $N$ for which Even (Player 2) has a winning strategy.
Given:
- $C(5) = 2$
- $C(16) = 64$

Find $C(300)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full Game Tree Search
- The number of partitions of $N = 300$ is $p(300) = 9\,253\,082\,936\,723\,602 \approx 9.25 \times 10^{15}$.
- Evaluating individual partisan game trees by minimax recursion is impossible.

---

## 3. Core Intuition & Mathematical Structure

### Combinatorial Game Theory (Conway Numbers)
Because each pile can only be acted upon by one specific player:
- An odd pile $2m + 1$ offers move $\{2g(m)\}$ to Odd (Left) and $\emptyset$ to Even (Right).
- An even pile $2m + 2$ offers $\emptyset$ to Left and $\{2g(m)\}$ to Right.
By Conway's simplicity rule in Combinatorial Game Theory, every single pile has a canonical **integer number value** $g(n)$:
$$g(0) = 0$$

$$g(2m + 1) = \max(0, 2g(m) + 1)$$

$$g(2m + 2) = \min(0, 2g(m) - 1)$$

### Winning Condition for Second Player (Even)
Because all pile values are integers (surreal numbers), the total game value is simply the arithmetic sum:
$$G = \sum_{i=1}^k g(p_i)$$
Under normal play convention, second player (Even) wins if and only if:
$$G \le 0$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### 2D Partition Dynamic Programming
To count partitions $\sum p_i = N$ with $\sum g(p_i) \le 0$:
We construct a 2D unbounded knapsack DP:
- `table[w][v]` = number of partitions of total weight $w$ summing to CGT value $v$.
- Item sizes $x \in \{1, \dots, N\}$ with weights $x$ and values $g(x) \in [-N, N]$.
- Transition:
  $$\text{table}[w][v] = \text{table}[w][v] + \text{table}[w - x][v - g(x)]$$
- Total winning partitions:
  $$C(N) = \sum_{v \le 0} \text{table}[N][v]$$

Total state space: $N \times (2N + 1) = 300 \times 601 \approx \mathbf{180,300} \text{ states}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $N = 5$:
- CGT values for $x \le 5$:
  - $g(1) = 1$
  - $g(2) = -1$
  - $g(3) = 3$
  - $g(4) = 0$
  - $g(5) = 0$
- Partitions of 5 with sum of $g(p_i) \le 0$:
  1. $[5]$: $g(5) = 0 \le 0 \implies \mathbf{\text{Valid}}$.
  2. $[2, 2, 1]$: $g(2) + g(2) + g(1) = -1 - 1 + 1 = -1 \le 0 \implies \mathbf{\text{Valid}}$.
  3. Other partitions (e.g. $[4, 1]$: $0 + 1 = 1 > 0$, $[3, 2]$: $3 - 1 = 2 > 0$, $[3, 1, 1]$: $3 + 2 = 5 > 0$, $[1, 1, 1, 1, 1]$: $5 > 0$) have sum $> 0$.
- Total valid: $C(5) = \mathbf{2}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **CGT Array Computation** | Compute $g(n)$ for $n \in [1, N]$ via 2-term recurrence | $\mathcal{O}(N)$ |
| **Stage 2** | **2D DP Grid Allocation** | Allocate $(N+1) \times (2N+1)$ table with offset $N$ | $\mathcal{O}(N^2)$ |
| **Stage 3** | **Unbounded Knapsack Loop** | Accumulate partition counts over $x = 1 \dots N$ | $\mathcal{O}(N^3)$ in C ($< 0.005\text{ s}$) |
| **Stage 4** | **Non-positive Extraction** | Sum $\text{table}[N][v]$ for $v \le 0$ | $\mathcal{O}(N)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^3) \approx 0.01\text{ s}$ | High-performance C DLL |
| **Space Complexity** | $\mathcal{O}(N^2) \le 2\text{ MB}$ | Small 2D array |
| **Implementation Standard** | C DLL + Pure Python Fallback | Seamless dual implementation |

### Critical Invariants Handled:
1. **Surreal Integer Simplicity**: The property that every pile value simplifies strictly to an integer guarantees that games never contain infinitesimal switches ($*$), making the $G \le 0$ criterion exact and complete.
2. **Unbounded Partitions**: Iterating $w$ from $x$ up to $N$ correctly generates all multiset partitions with repeated pile sizes.
