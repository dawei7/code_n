# Guided Example: First Bad Version

We trace the step-by-step binary search bisection on a monotonic boolean predicate array (`isBadVersion`), integer overflow-safe midpoint calculation ($L + \lfloor (R - L) / 2 \rfloor$), and boundary convergence on representative version verification instances:

- **Input:** $n = 5, \quad \text{bad} = 4$
- **Required output:** $4$ (Version evaluations: $[1: \text{False}, 2: \text{False}, 3: \text{False}, 4: \text{True}, 5: \text{True}]$; first bad version is $4$)
- **Immediate First Version Bad:** $n = 1, \quad \text{bad} = 1 \implies 1$ (Single version base case)
- **Large 32-Bit Bound:** $n = 2^{31} - 1, \quad \text{bad} = 2^{31} - 1$ (Exposes $(L + R) // 2$ 32-bit integer overflow; requires $L + (R - L) // 2$)
- **Terminal Version Bad:** $n = 5, \quad \text{bad} = 5 \implies 5$

This instance demonstrates binary search on implicit monotonic boolean predicates ($[\text{False}, \dots, \text{False}, \text{True}, \dots, \text{True}]$), proves why `R = M` is required when `isBadVersion(M)` is True rather than `R = M - 1`, explains the integer overflow mitigation, and bounds total API calls strictly to $\lceil \log_2 n \rceil$ in $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given $n = 5$ product versions labeled $1 \dots 5$, and a designated first bad version $\text{bad} = 4$:
Find the earliest version that fails the quality check using minimal calls to `isBadVersion(version)`.

```text
Version:          1      2      3      4      5
isBadVersion:   False  False  False   True   True
                                       ^
                               First Bad Version
```

### The Monotonic Boolean Predicate
Because every version after a bad version is also bad:
The sequence of API return values across $1 \dots n$ is strictly monotonic:
$$
[\underbrace{\text{False}, \text{False}, \dots, \text{False}}_{\text{Good versions}}, \; \underbrace{\mathbf{\text{True}}, \text{True}, \dots, \text{True}}_{\text{Bad versions}}]
$$
- A linear scan calling `isBadVersion(1)`, `isBadVersion(2)`, $\dots$ takes $O(N)$ API calls. For $n = 2 \times 10^9$, this causes Time Limit Exceeded.
- Binary search inspects the midpoint, discarding half the search space at each step, locating the transition point in only $\approx 31$ API calls.

---

## 2. Conceptual Foundation & Invariants

### Binary Search Predicate Protocol
Initialize the search interval to the full range of versions:
$$
L = 1, \quad R = n
$$
While $L < R$:
1. **Overflow-Safe Midpoint:**
   In languages with 32-bit signed integers, $(L + R) // 2$ overflows when $L + R \ge 2^{31}$.
   We write:
   $$
   M = L + \lfloor (R - L) / 2 \rfloor
   $$
2. **Predicate Evaluation:**
   - **Case 1: `isBadVersion(M) == True`**
     Version $M$ is bad.
     Could $M$ be the *first* bad version? Yes!
     Could the first bad version be to the left of $M$? Yes!
     Could any version to the right of $M$ be the first bad version? No (they are all later bad versions).
     Therefore, we keep $M$ inside the candidate interval:
     $$
     R \leftarrow M
     $$
   - **Case 2: `isBadVersion(M) == False`**
     Version $M$ is good.
     Neither $M$ nor any version $\le M$ can be the first bad version.
     The first bad version must be strictly to the right:
     $$
     L \leftarrow M + 1
     $$

When $L == R$, the search interval has contracted to a single element: the first bad version.

> **Invariant.** The first bad version always lies within the inclusive range $[L, R]$. All versions $< L$ are provably good, and all versions $\ge R$ known to be bad include at least one bad version.

---

## 3. Step-by-Step Worked Execution

We trace the binary search on $n = 5$ with $\text{bad} = 4$:
Initial interval: $L = 1, \quad R = 5$.

---

### Step 1: First Bisection ($L = 1, R = 5$)
- Compute midpoint:
  $$
  M = 1 + \lfloor (5 - 1) / 2 \rfloor = 1 + 2 = \mathbf{3}
  $$
- Query API:
  $$
  \text{isBadVersion}(3) \implies \mathbf{\text{False}}
  $$
- Deduction: Versions $1, 2, 3$ are good. The first bad version must be $\ge 4$.
- Update left bound:
  $$
  L \leftarrow M + 1 = 3 + 1 = \mathbf{4}
  $$
- New search interval: $[4, 5]$.

---

### Step 2: Second Bisection ($L = 4, R = 5$)
- Compute midpoint:
  $$
  M = 4 + \lfloor (5 - 4) / 2 \rfloor = 4 + 0 = \mathbf{4}
  $$
- Query API:
  $$
  \text{isBadVersion}(4) \implies \mathbf{\text{True}}
  $$
- Deduction: Version 4 is bad. The first bad version is either 4 or earlier. It cannot be 5.
- Update right bound:
  $$
  R \leftarrow M = \mathbf{4}
  $$
- New search interval: $[4, 4]$.

---

### Step 3: Termination ($L = 4, R = 4$)
- Interval condition $L < R$ is False ($4 < 4$ is False).
- Both pointers converge on $L = R = 4$.
- First bad version is $\mathbf{4}$.

Total API calls: **2**.

---

## 4. Complete Execution Trace

```text
n = 5, bad = 4
L = 1, R = 5

Iteration 1:
  M = 1 + (5 - 1) // 2 = 3
  isBadVersion(3) -> False
  L = M + 1 = 4 -> Range: [4, 5]

Iteration 2:
  M = 4 + (5 - 4) // 2 = 4
  isBadVersion(4) -> True
  R = M = 4 -> Range: [4, 4]

L == R == 4 -> Stop
Result: 4
```

| Iteration | Search Interval $[L, R]$ | Midpoint $M$ | API Call `isBadVersion(M)` | Outcome | Next Interval $[L, R]$ |
|:---:|:---:|:---:|:---:|:---|:---:|
| **1** | $[1, 5]$ | 3 | $\text{isBadVersion}(3)$ | **False** (Good) | $[4, 5]$ |
| **2** | $[4, 5]$ | 4 | $\text{isBadVersion}(4)$ | **True** (Bad) | **$[4, 4]$** |
| **End** | $[4, 4]$ | - | - | $L == R$ Convergence | **$\mathbf{4}$ (First Bad Version)** |

---

## 5. Algorithmic Correctness

**Soundness.** When `isBadVersion(M)` is False, no version $x \le M$ can be bad, so discarding $[L, M]$ is strictly sound. When `isBadVersion(M)` is True, version $M$ is known to be bad, so setting $R = M$ keeps the earliest known bad version in the search interval while discarding $[M + 1, R]$, which cannot contain the *first* bad version.

**Completeness.** In each iteration where $L < R$, the interval strictly shrinks:
- If `isBadVersion(M)` is False, $L = M + 1 > M \ge L$, so the lower bound increases.
- If `isBadVersion(M)` is True, $R = M$. Because $M = L + \lfloor (R - L) / 2 \rfloor < R$ whenever $L < R$, the upper bound strictly decreases.
The algorithm cannot loop infinitely and must terminate at $L == R$.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Midpoint:** Writing `(L + R) // 2` causes integer overflow in C++, Java, and other languages when $L + R > 2^{31} - 1$. The formula `L + (R - L) // 2` guarantees intermediate values never exceed $n$.
- **Setting $R = M - 1$ on True:** If $M$ is itself the first bad version, setting $R = M - 1$ would eliminate the correct answer from the search range! Because $M$ could be the answer, you must set $R = M$.
- **Termination Loop Condition:** Using `while L <= R` with `R = M` creates an infinite loop when $L == R$. Using `while L < R` ensures clean termination when $L == R$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Each iteration performs exactly one API query and halves the remaining candidate interval size. The total number of queries is bounded by $\lceil \log_2 n \rceil \le 31$ for any 32-bit integer $n$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. Only scalar pointers ($L, R, M$) are maintained.