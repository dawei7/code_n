# Belfry Maths - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Permutations of a distinct set of letters are generated starting from alphabetical order by swapping adjacent elements using the Plain Changes (bell-ringing) method.
Find the number of swaps needed to reach the word `NOWPICKBELFRYMATHS` (18 distinct letters).
Given:
- `CBA` requires 3 swaps.
- `BELFRY` requires 59 swaps.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Step-by-Step Swap Simulation
- For 18 letters, there are $18! \approx 6.4 \times 10^{15}$ permutations.
- Simulating swaps one by one until reaching the target would take years.

---

## 3. Core Intuition & Mathematical Structure

### The Steinhaus–Johnson–Trotter Gray Code
The bell-ringing procedure is isomorphic to the classic **Steinhaus–Johnson–Trotter (SJT) permutation algorithm**:
- Elements $\{1, \dots, n-1\}$ are recursively ordered.
- The largest element $n$ sweeps across the $n$ possible insertion slots:
  - If the sub-rank $I_{n-1}$ is even, $n$ sweeps **leftwards** from position $n-1$ down to $0$.
  - If the sub-rank $I_{n-1}$ is odd, $n$ sweeps **rightwards** from position $0$ up to $n-1$.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Recursive Ranking Formula
Let $p$ be the 0-indexed position of the largest element $n$ in the permutation $\pi$.
Let $I_{n-1}$ be the rank of the sub-permutation $\pi \setminus \{n\}$.
The number of steps $k$ taken by element $n$ within its current sweep is:
$$k = \begin{cases} (n - 1) - p & \text{if } I_{n-1} \equiv 0 \pmod 2 \\ p & \text{if } I_{n-1} \equiv 1 \pmod 2 \end{cases}$$

The total 0-indexed rank of $\pi$ is:
$$I_n = n \cdot I_{n-1} + k$$
with base case $I_1 = 0$.

Because the initial permutation has rank 0, the number of swaps to reach the target is precisely $I_n$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for `BELFRY`:
- Sorted: `B, E, F, L, R, Y` $\to$ values $1, 2, 3, 4, 5, 6$.
- Target: `[1, 2, 3, 4, 5, 6]` $\to$ `BELFRY` = `[1, 2, 3, 4, 5, 6]`?
  - Letters in `BELFRY`: `B=1, E=2, L=4, F=3, R=5, Y=6` $\to$ `[1, 2, 4, 3, 5, 6]`?
  - Tracing through sizes $n = 1 \dots 6$:
    - $n=1$: `[1]`, rank $0$.
    - $n=2$: `[1, 2]`, rank $0$.
    - $n=3$: `[1, 2, 3]`, rank $0$.
    - $n=4$: `[1, 2, 4, 3]`, rank $1$.
    - $n=5$: `[1, 2, 4, 3, 5]`, rank $5$.
    - $n=6$: `[1, 2, 4, 3, 5, 6]` has $6$ at index $5$, sub-rank $5$ (odd) $\implies k = 5$.
    - $I_6 = 6(9) + 5 = \mathbf{59}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Alphabet Normalization** | Map target letters to $\{1, \dots, n\}$ in alphabetical order | $\mathcal{O}(n \log n)$ |
| **Stage 2** | **Recursive Rank** | Locate position of $n$, recurse on $n-1$, apply parity sweep rule | $\mathcal{O}(n^2)$ |
| **Stage 3** | **Output Index** | Return $I_n$ | $\mathcal{O}(1)$ in pure Python ($< 0.001\text{ s}$) |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(n^2) \approx 0.001\text{ s}$ | Instantaneous execution |
| **Space Complexity** | $\mathcal{O}(n) \le 1\text{ KB}$ | Recursion stack of depth $n = 18$ |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Sweep Parity Reversal**: Correctly alternating the direction of element $n$'s trajectory based on $I_{n-1} \bmod 2$ guarantees the exact isomorphism with Plain Changes.
2. **Arbitrary BigInt Arithmetic**: Python natively manages 64-bit integer values without precision overflow.
