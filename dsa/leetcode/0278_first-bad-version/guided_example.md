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

### Mirror Trace: When the True Branch Fires Repeatedly

The worked instance above reaches `isBadVersion(M) == False` once and
`isBadVersion(M) == True` once, so it never shows what happens when the boundary
sits near the low end. Take $n = 10$ with $\text{bad} = 2$: the first three
midpoints all land on bad versions, so the right bound absorbs the work and the
*left* pointer moves only on the final probe. Both branches must therefore keep
the interval valid; neither branch is the rare case.

| Step | Interval before $[L, R]$ | Midpoint $M$ | `isBadVersion(M)` | Half rejected by the answer | Interval after $[L, R]$ | Versions still alive |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | $[1, 10]$ | $5$ | $\text{True}$ | $[6, 10]$: all bad, but each is later than $M$ | $[1, 5]$ | 5 |
| 2 | $[1, 5]$ | $3$ | $\text{True}$ | $[4, 5]$: both strictly later than $M$ | $[1, 3]$ | 3 |
| 3 | $[1, 3]$ | $2$ | $\text{True}$ | $[3, 3]$: strictly later than $M$ | $[1, 2]$ | 2 |
| 4 | $[1, 2]$ | $1$ | $\text{False}$ | $[1, 1]$: version 1 is good, so it cannot be the first bad one | $[2, 2]$ | 1 |
| End | $[2, 2]$ | — | — | $L == R$ convergence, no further probe needed | $[2, 2]$ | **answer $2$** |

Reading the last two rows together shows why the two update rules are not
symmetric. A $\text{True}$ answer keeps $M$ inside the interval because $M$ is
itself a legitimate answer, so the right bound becomes $M$ rather than $M - 1$.
A $\text{False}$ answer proves $M$ is good, so the left bound may safely jump
past it to $M + 1$. Here the interval shrinks $10 \to 5 \to 3 \to 2 \to 1$ in
four probes, which is exactly the halving the complexity analysis predicts.

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

### Boundary Census: Where the Probe Count Peaks

The instance above is deliberately mild. The table below records the probe count
for every interesting shape of the input, including the two extremes of the
$2^{31} - 1$ ceiling. Every row was obtained by running the same two rules, so
the counts are facts about the method rather than estimates.

| Instance | $n$ | $\text{bad}$ | Probes used | Final interval reached | Returned | Why this row matters |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Only version is bad | 1 | 1 | 0 | $[1, 1]$ initially | 1 | The loop body never runs: $L = R = 1$ before any probe, so the answer is known without asking |
| Bad at the far end | 5 | 5 | 2 | $[5, 5]$ | 5 | Both probes return $\text{False}$; only $L$ ever moves, and the last good version is one below the answer |
| Bad in the middle | 5 | 4 | 2 | $[4, 4]$ | 4 | The traced instance: one $\text{False}$ then one $\text{True}$ |
| Boundary near the low end | 10 | 2 | 4 | $[2, 2]$ | 2 | Three $\text{True}$ answers in a row, exercising the halving on the right bound |
| Boundary at the far end | 100 | 100 | 6 | $[100, 100]$ | 100 | Every probe is $\text{False}$, so the search behaves like a plain halving climb |
| 32-bit ceiling, answer last | $2^{31} - 1$ | $2^{31} - 1$ | 30 | $[2^{31} - 1, 2^{31} - 1]$ | 2147483647 | Midpoint arithmetic reaches $L + R > 2^{31} - 1$, which is where $(L + R) // 2$ overflows |
| 32-bit ceiling, answer first | $2^{31} - 1$ | 1 | 31 | $[1, 1]$ | 1 | The true worst case: $\lceil \log_2 n \rceil = 31$ probes, and the very first sum $L + R = 2^{31}$ already exceeds the signed 32-bit maximum |

Two conclusions follow. The worst case is *not* the largest $\text{bad}$: moving
the boundary to 1 costs one extra probe because every answer is $\text{True}$ and
the interval must be halved from the top down. And no row exceeds 31 probes, so a
hard call limit of $3n$ or even 31 is met with room to spare.

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

### Strategy Comparison on the $n = 10, \text{bad} = 2$ Instance

Each row below is a complete, self-contained way to attack the problem. Only the
second one survives all three hazards at once: the call budget, the discarded
answer, and termination.

| Strategy | Probes on this instance | Result it returns | Auxiliary space | Failure mode |
|:---|:---:|:---:|:---:|:---|
| Linear scan from version 1 | 2 | 2 | $O(1)$ | Correct here only because the boundary is early; with $\text{bad} = n$ it needs $n$ probes, and $n$ can reach $2^{31} - 1$ |
| Bisection with $R \leftarrow M$ on $\text{True}$ (this lesson) | 4 | 2 | $O(1)$ | None: $\lceil \log_2 n \rceil \le 31$ probes, the answer is never discarded, and $L < R$ guarantees progress |
| Bisection with $R \leftarrow M - 1$ on $\text{True}$ | 2 | **1** | $O(1)$ | Wrong answer: the probe at $M = 2$ is $\text{True}$, yet $R$ becomes 1, so the interval collapses to $[1, 1]$ and the real boundary 2 is gone |
| Bisection with loop condition $L \le R$ and $R \leftarrow M$ | never terminates | — | $O(1)$ | Infinite loop: once $L == R$ the probe repeats the same midpoint and re-assigns the same bound forever |
| Ternary split (two interior probes per level) | 6 | 2 | $O(1)$ | No benefit: a boolean predicate carries one bit per probe, so one probe per halving is already optimal and the second probe per level only adds calls |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Each iteration performs exactly one API query and halves the remaining candidate interval size. The total number of queries is bounded by $\lceil \log_2 n \rceil \le 31$ for any 32-bit integer $n$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. Only scalar pointers ($L, R, M$) are maintained.