# Guided Example: Find the Duplicate Number

We trace the step-by-step value-range binary search bisection, cumulative pigeonhole counting predicate ($C(x) = \sum [v \le x] > x$), and cycle-detection duality on representative input arrays without array mutation:

- **Input:** $\text{nums} = [1, 3, 4, 2, 2]$
- **Required output:** $2$ ($2$ appears twice; all other values appear once in range $[1, 4]$)
- **Repeated Multiple Times:** $\text{nums} = [3, 1, 3, 4, 2] \implies 3$
- **Minimal Pair Base Case:** $\text{nums} = [1, 1] \implies 1$
- **Duplicate at Boundary:** $\text{nums} = [1, 2, 3, 4, 4] \implies 4$

This instance demonstrates binary search on the answer domain $[1, n]$ constrained by the Pigeonhole Principle, explains why no array mutation or auxiliary hash set is needed, contrasts the $O(N \log N)$ counting predicate with Floyd's $O(N)$ Tortoise-and-Hare cycle detection, and operates in strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an array of $n + 1$ integers $\text{nums} = [1, 3, 4, 2, 2]$ where every value lies in $[1, n]$ ($n = 4$):
Find the **duplicate number** under the strict constraints:
1. You **must not modify** the array (read-only).
2. You must use only **$O(1)$ auxiliary memory**.
3. Runtime must be better than $O(N^2)$.

```text
Array: [1, 3, 4, 2, 2] (length 5, values in [1, 4])
Pigeonhole Principle: 5 items placed into 4 boxes -> at least one box has >= 2 items.
Duplicate value: 2
```

### Why Hash Sets and In-Place Swapping are Disallowed
- Storing seen numbers in a Hash Set takes $O(N)$ extra space (violates constraint 2).
- Sorting or sign-marking (`nums[abs(x)] = -nums[abs(x)]`) modifies the array (violates constraint 1).
- We can search the **value range** $[1, n]$ using **binary search** with a counting predicate:
  For a candidate value $x$, count how many elements in `nums` are $\le x$.

---

## 2. Conceptual Foundation & Invariants

### The Pigeonhole Counting Predicate
Let $C(x)$ be the number of elements in `nums` that are $\le x$:
$$
C(x) = \sum_{v \in \text{nums}} \mathbb{I}(v \le x)
$$
Consider the monotonic predicate $f(x) \equiv (C(x) > x)$:
- If the duplicate value $d > x$:
  All numbers in the range $[1, x]$ can appear at most once. Therefore, at most $x$ elements in `nums` can be $\le x$.
  $$
  C(x) \le x \implies f(x) = \mathbf{\text{False}}
  $$
- If the duplicate value $d \le x$:
  The duplicate value $d$ (which appears $\ge 2$ times) lies inside the prefix $[1, x]$. By the Pigeonhole Principle, the count of elements $\le x$ must strictly exceed $x$:
  $$
  C(x) > x \implies f(x) = \mathbf{\text{True}}
  $$

The predicate sequence over $x \in [1, n]$ is monotonically non-decreasing:
$$
[\underbrace{\text{False}, \dots, \text{False}}_{x < d}, \; \underbrace{\mathbf{\text{True}}, \dots, \text{True}}_{x \ge d}]
$$
The duplicate number $d$ is the **first candidate $x$ where $f(x) == \text{True}$**!

> **Invariant.** The duplicate number $d$ always lies in the active search range $[L, R]$. For any $x < L$, $C(x) \le x$; for any $x \ge R$, $C(x) > x$.

---

## 3. Step-by-Step Worked Execution

We trace the binary search on $\text{nums} = [1, 3, 4, 2, 2]$:
Array length $5 \implies n = 4$.
Search range for value $x$: $L = 1, \quad R = 4$.

---

### Step 1: Evaluate Midpoint $M = 2$ ($L = 1, R = 4$)
- Midpoint value:
  $$
  M = 1 + \lfloor (4 - 1) / 2 \rfloor = \mathbf{2}
  $$
- Scan array to compute $C(2)$:
  - $1 \le 2$ (Count $= 1$)
  - $3 \not\le 2$
  - $4 \not\le 2$
  - $2 \le 2$ (Count $= 2$)
  - $2 \le 2$ (Count $= 3$)
  $$
  C(2) = 3
  $$
- Evaluate predicate:
  $$
  C(2) > 2 \iff 3 > 2 \quad (\mathbf{\text{True}})
  $$
- Deduction: There are 3 numbers $\le 2$ in an interval of capacity 2. By pigeonhole, the duplicate must be $\le 2$!
- Update search range:
  $$
  R \leftarrow M = \mathbf{2}
  $$
- New range: $[1, 2]$.

---

### Step 2: Evaluate Midpoint $M = 1$ ($L = 1, R = 2$)
- Midpoint value:
  $$
  M = 1 + \lfloor (2 - 1) / 2 \rfloor = \mathbf{1}
  $$
- Scan array to compute $C(1)$:
  - $1 \le 1$ (Count $= 1$)
  - $3 \not\le 1, \; 4 \not\le 1, \; 2 \not\le 1, \; 2 \not\le 1$
  $$
  C(1) = 1
  $$
- Evaluate predicate:
  $$
  C(1) > 1 \iff 1 > 1 \quad (\mathbf{\text{False}})
  $$
- Deduction: There is only 1 number $\le 1$. The value $1$ cannot be the duplicate. The duplicate must be $> 1$.
- Update search range:
  $$
  L \leftarrow M + 1 = 1 + 1 = \mathbf{2}
  $$
- New range: $[2, 2]$.

---

### Step 3: Termination ($L = R = 2$)
- Range contracted to a single integer: $L == R == 2$.
- The duplicate number is $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
nums = [1, 3, 4, 2, 2], n = 4
L = 1, R = 4

Iteration 1:
  M = 2
  Count elements <= 2: [1, 2, 2] -> C(2) = 3
  3 > 2 is True -> R = 2, Range: [1, 2]

Iteration 2:
  M = 1
  Count elements <= 1: [1] -> C(1) = 1
  1 > 1 is False -> L = 2, Range: [2, 2]

L == R == 2 -> Terminate
Result: 2
```

| Iteration | Value Range $[L, R]$ | Probe $M$ | Array Elements $\le M$ | $C(M)$ | Predicate $C(M) > M$ | Next Range $[L, R]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | $[1, 4]$ | 2 | $\{1, 2, 2\}$ | 3 | **True ($3 > 2$)** | $[1, 2]$ |
| **2** | $[1, 2]$ | 1 | $\{1\}$ | 1 | **False ($1 \not> 1$)** | **$[2, 2]$** |
| **End** | $[2, 2]$ | - | - | - | - | **$\mathbf{2}$ (Duplicate)** |

---

### Dual Perspective: Floyd's Cycle Detection ($O(N)$ Alternative)
Treat the array as a functional graph where node $i$ has directed edge to $\text{nums}[i]$:
- $0 \to \text{nums}[0] = 1$
- $1 \to \text{nums}[1] = 3$
- $3 \to \text{nums}[3] = 2$
- $2 \to \text{nums}[2] = 4$
- $4 \to \text{nums}[4] = 2$
- Directed edges: $0 \to 1 \to 3 \to 2 \to 4 \to 2$.
Node $2$ has in-degree 2 (both node 3 and node 4 point to 2).
The cycle entrance is the duplicate value $2$, detectable using slow/fast pointers in $O(N)$ time and $O(1)$ space.

---

## 5. Algorithmic Correctness

**Soundness.** If $C(x) > x$, by the Pigeonhole Principle, at least one number in the range $[1, x]$ appears multiple times. Because the problem statement guarantees there is only one distinct repeated number, that repeated number must be in $[1, x]$. Conversely, if $C(x) \le x$, the duplicate cannot be in $[1, x]$ and must be strictly greater than $x$.

**Completeness.** In each bisection step, the active search range $[L, R]$ is strictly halved. Because the monotonic predicate transition from False to True exists and corresponds to the duplicate number $d$, binary search convergence on $L == R$ provably isolates $d$.

---

## 6. Traps This Instance Exposes

- **Array Modification Prohibition:** Setting negative signs `nums[abs(x)] = -nums[abs(x)]` or swapping values violates the explicit "do not modify the array" constraint. Value-range binary search reads the array without writing a single bit.
- **Counting Values vs Indices:** Binary search bisects candidate **values** from $1$ to $n$, NOT indices of the array. The length of the array is $n + 1$, but candidate answers are values in $[1, n]$.
- **Multiple Duplicate Occurrences:** If the duplicate appears 3 or 4 times (e.g. $[2, 2, 2, 2, 2]$), $C(x)$ is still $> x$ for all $x \ge 2$ and $\le x$ for $x < 2$. The monotonicity of the predicate is completely invariant to the repetition frequency.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N = n$. The binary search range $[1, n]$ has $\log_2 n$ bisection steps. Each step performs a full linear scan of all $N + 1$ elements to evaluate $C(M)$. Total time is $(N + 1) \log_2 N = O(N \log N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. No hash set or allocated collections are used; only scalar search pointers ($L, R, M, \text{count}$) are maintained.
