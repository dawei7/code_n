# Guided Example: Search in Rotated Sorted Array

We trace the step-by-step rotated binary search on a representative circular sorted array instance:

- **Input:** $\text{nums} = [4, 5, 6, 7, 0, 1, 2]$, $\text{target} = 0$
- **Required output:** $4$

This instance demonstrates identifying which half of the bisected array is normally sorted, testing target range containment within the sorted half, eliminating the contradictory half, and converging on the target in $O(\log N)$ time.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of $N = 7$ distinct elements sorted in ascending order and then rotated at an unknown pivot, and a target value $\text{target} = 0$:
$$
[4, 5, 6, 7, 0, 1, 2]
$$

We must return the index of $\text{target}$ in $O(\log N)$ time, or $-1$ if it does not exist in the array.

A linear scan takes $O(N)$ time. Because the array was originally sorted before rotation, bisecting the array at midpoint $M$ guarantees that at least one of the two halves $[L, M]$ or $[M, R]$ is strictly sorted in monotonic ascending order. By testing whether $\text{target}$ falls inside the known bounds of the sorted half, we deterministically eliminate half of the remaining elements at each step.

### Why classifying the sorted half beats the alternatives

| Candidate method | How it would process $[4, 5, 6, 7, 0, 1, 2]$ for $\text{target} = 0$ | Probes on $N = 7$ | Tradeoff or failure mode |
|:---|:---|:---:|:---|
| Linear scan | Inspect indices $0, 1, 2, 3, 4$ in order until the value $0$ appears at index $4$ | $5$ | Correct but ignores the rotation structure entirely; $O(N)$ time violates the required logarithmic bound |
| Locate the seam, then bisect | Probe for the descent pair $(7, 0)$ to recover the pivot index $4$, then binary-search the sorted segment that contains $0$ | Two full logarithmic passes | Still $O(\log N)$, but it spends two searches and needs an extra branch for an array that was never rotated |
| Classify the sorted half at every probe | Compare $\text{nums}[L]$ with $\text{nums}[M]$, then test whether $0$ lies inside that sorted range | $3$ | Single loop, no pivot bookkeeping; sound only because the half-sorted invariant holds for every interval |

---

## 2. Conceptual Foundation & Invariants

### The Half-Sorted Invariant
For any search interval $[L, R]$ with midpoint $M = \lfloor (L + R) / 2 \rfloor$:
- If $\text{nums}[M] == \text{target}$, we have found the target and return $M$.
- Otherwise, we determine which half is sorted:
  1. **Left Half Sorted ($\text{nums}[L] \le \text{nums}[M]$):**
     - Elements in $[L, M]$ are monotonically increasing without a rotation seam.
     - If $\text{nums}[L] \le \text{target} < \text{nums}[M]$, the target must be in the left half $\implies R \leftarrow M - 1$.
     - Otherwise, the target cannot be in the left half $\implies L \leftarrow M + 1$.
  2. **Right Half Sorted ($\text{nums}[L] > \text{nums}[M]$, which implies $\text{nums}[M] \le \text{nums}[R]$):**
     - Elements in $[M, R]$ are monotonically increasing.
     - If $\text{nums}[M] < \text{target} \le \text{nums}[R]$, the target must be in the right half $\implies L \leftarrow M + 1$.
     - Otherwise, the target cannot be in the right half $\implies R \leftarrow M - 1$.

> **Invariant.** If $\text{target}$ is present in $\text{nums}$, it is guaranteed to lie within the active search interval $[L, R]$.

---

## 3. Step-by-Step Worked Execution

We search for $\text{target} = 0$ in $\text{nums} = [4, 5, 6, 7, 0, 1, 2]$:

### Iteration 1: $L = 0, R = 6$
- Midpoint: $M = \lfloor (0 + 6) / 2 \rfloor = 3$.
- Midpoint value: $\text{nums}[3] = 7$.
- Target check: $\text{nums}[3] = 7 \ne 0$.
- **Determine Sorted Half:**
  - Left boundary $\text{nums}[0] = 4 \le \text{nums}[3] = 7$.
  - **Left half $[0 \dots 3] = [4, 5, 6, 7]$ is strictly sorted.**
- **Range Containment Test:**
  - Does $\text{target} = 0$ satisfy $\text{nums}[0] \le \text{target} < \text{nums}[3]$ ($4 \le 0 < 7$)? **No ($0 < 4$).**
- **Decision:** Eliminate left half $[0 \dots 3]$. Target must reside in the right half.
- Update: $L \leftarrow M + 1 = 4$.
- Active interval becomes $[4, 6]$.

---

### Iteration 2: $L = 4, R = 6$
- Midpoint: $M = \lfloor (4 + 6) / 2 \rfloor = 5$.
- Midpoint value: $\text{nums}[5] = 1$.
- Target check: $\text{nums}[5] = 1 \ne 0$.
- **Determine Sorted Half:**
  - Left boundary $\text{nums}[4] = 0 \le \text{nums}[5] = 1$.
  - **Left half $[4 \dots 5] = [0, 1]$ is strictly sorted.**
- **Range Containment Test:**
  - Does $\text{target} = 0$ satisfy $\text{nums}[4] \le \text{target} < \text{nums}[5]$ ($0 \le 0 < 1$)? **Yes!**
- **Decision:** Eliminate right half $[5 \dots 6]$. Target must reside in the left half.
- Update: $R \leftarrow M - 1 = 4$.
- Active interval becomes $[4, 4]$.

---

### Iteration 3: $L = 4, R = 4$
- Midpoint: $M = \lfloor (4 + 4) / 2 \rfloor = 4$.
- Midpoint value: $\text{nums}[4] = 0$.
- Target check: $\text{nums}[4] == 0 == \text{target}$. **Match found!**
- Output: Return index $4$.

---

## 4. Complete Execution Trace

| Iteration | Left $L$ | Right $R$ | Midpoint $M$ | Value $\text{nums}[M]$ | Sorted Half Identified | Range Containment ($\text{target}=0$) | Search Space Update | Remaining Elements |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 6 | 3 | 7 | Left ($[4, 5, 6, 7]$) | $4 \le 0 < 7$ is False | Search right: $L \leftarrow 4$ | $[0, 1, 2]$ |
| 2 | 4 | 6 | 5 | 1 | Left ($[0, 1]$) | $0 \le 0 < 1$ is **True** | Search left: $R \leftarrow 4$ | $[0]$ |
| 3 | 4 | 4 | 4 | 0 | Singleton ($[0]$) | $\text{nums}[4] == 0$ | **Exact match found** | Index $4$ |

---

## 5. Algorithmic Correctness

**Soundness.** Because the array was rotated from a sorted sequence of unique elements, every division produces at least one subarray with monotonic order. Checking containment within the endpoints $[L, M]$ or $[M, R]$ of a sorted half is necessary and sufficient: if the target falls within that value range, it must be in that subarray; if not, it cannot be in that subarray.

**Completeness.** At each step, either the midpoint matches the target, or the search interval $[L, R]$ shrinks by at least half. If the target exists, it cannot be eliminated from the active window, guaranteeing convergence in $\le \lceil \log_2 N \rceil + 1$ iterations.

---

## 6. Traps This Instance Exposes

- **Inclusive vs Exclusive Range Checks:** When the left half is sorted, the condition must check $\text{nums}[L] \le \text{target} < \text{nums}[M]$ (inclusive of $L$, exclusive of $M$, because $M$ was already checked for equality).
- **Target Not Present:** If $\text{target} = 3$ in $[4, 5, 6, 7, 0, 1, 2]$, the interval contracts until $L > R$, properly exiting the loop and returning $-1$.
- **Pivot at Midpoint:** When the rotation seam lies exactly at $M$, $\text{nums}[L] > \text{nums}[M]$, which naturally classifies the right half $[M, R]$ as the sorted branch, preserving correctness without special cases.

### Boundary conditions traced on the authored instances

| Instance | Input condition | Traced behaviour | Result | Why the result is forced |
|:---|:---|:---|:---:|:---|
| `nums = [1]`, `target = 0` | Interval is already a singleton | $L = R = 0$ before the first probe, so no bisection occurs | $-1$ | The closing equality test on the single surviving index is the only check needed; an exhausted interval can never report a match |
| `nums = [3, 1]`, `target = 1` | Two values, seam between them | $M = 0$ with $\text{nums}[0] = 3$; the left half is the singleton $\{3\}$ and $3 \le 1 < 3$ fails, so $L \leftarrow 1$ | $1$ | A one-element subarray is trivially sorted, so the containment test discards it with no special case |
| `nums = [5, 1, 3]`, `target = 5` | Target sits at index $0$, left of the seam | $M = 1$ with $\text{nums}[1] = 1$, so the right half $[1, 3]$ is sorted; $1 < 5 \le 3$ fails and $R \leftarrow 0$ | $0$ | Failing containment in a sorted half is a proof of absence there, which pins the target to index $0$ |
| `nums = [4, 5, 1, 2, 3]`, `target = 3` | Target sits at the final index | $M = 2$; right half $[1, 2, 3]$ is sorted and $1 < 3 \le 3$ holds, so $L \leftarrow 3$; then $M = 3$ with $\text{nums}[3] = 2$, and $2 \le 3 < 2$ fails, so $L \leftarrow 4$ | $4$ | Each rejection removes a subarray whose sorted endpoints bound the target strictly away from it |
| `nums = [-10000, 0, 10000]`, `target = 10000` | Array is not rotated at all | $M = 1$; left half $[-10000, 0]$ is sorted and $-10000 \le 10000 < 0$ fails, so $L \leftarrow 2$ | $2$ | With no seam the left half is always the sorted branch, and the target either lies inside it or strictly to its right |
| `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 3` | Target is absent | Probes at $M = 3$ ($\text{nums}[3] = 7$, so $L \leftarrow 4$) and $M = 5$ ($\text{nums}[5] = 1$, so $L \leftarrow 6$); the interval collapses to $[6, 6]$ | $-1$ | Absence is never detected early; the interval shrinks to one index and the closing equality test rejects it |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$. Each iteration eliminates at least half of the remaining elements through $O(1)$ comparisons. For $N = 7$, convergence occurs in at most 3 steps.
- **Auxiliary Space Complexity:** $O(1)$. Binary search uses scalar index variables ($L, R, M$) without dynamic allocations.