# Guided Example: Missing Ranges

We trace the step-by-step adjacent interval gap detection with virtual boundary sentinels on representative integer ranges:

- **Input:** $\text{nums} = [0, 1, 3, 50, 75]$, $\text{lower} = 0$, $\text{upper} = 99$
- **Required output:** `[[2, 2], [4, 49], [51, 74], [76, 99]]`
- **Empty Array Instance:** $\text{nums} = []$, $\text{lower} = 1$, $\text{upper} = 1 \implies [[1, 1]]$
- **Complete Coverage Instance:** $\text{nums} = [-1]$, $\text{lower} = -1$, $\text{upper} = -1 \implies []$

This instance demonstrates sentinel augmentation ($[\text{lower} - 1] + \text{nums} + [\text{upper} + 1]$) to unify leading, internal, and trailing gap processing, explains the gap condition ($v - u > 1 \implies [u + 1, v - 1]$), and operates in $O(N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a sorted unique array of integers $\text{nums} = [0, 1, 3, 50, 75]$ and a target closed interval $[\text{lower}, \text{upper}] = [0, 99]$:
Find all contiguous ranges of missing numbers $[a, b]$ that cover every missing integer without including any element present in $\text{nums}$.

In this instance:
- Before 0: $0 == \text{lower}$ (no leading gap).
- Between 1 and 3: 2 is missing $\implies [2, 2]$.
- Between 3 and 50: numbers $4 \dots 49$ are missing $\implies [4, 49]$.
- Between 50 and 75: numbers $51 \dots 74$ are missing $\implies [51, 74]$.
- After 75 up to 99: numbers $76 \dots 99$ are missing $\implies [76, 99]$.
Emitted output: `[[2, 2], [4, 49], [51, 74], [76, 99]]`.

A naive check tests every integer from `lower` to `upper`, taking $O(\text{upper} - \text{lower})$ time (which can be $2 \times 10^9$ operations).
Because `nums` is sorted and unique, missing elements occur solely as the difference gaps between consecutive array elements.
Using virtual sentinel bounds $\text{lower} - 1$ and $\text{upper} + 1$, every missing segment $[u + 1, v - 1]$ is discovered in a single pass over adjacent pairs in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### The Sentinel Pairwise Gap Theorem
Imagine augmenting `nums` with virtual sentinels at both ends:
$$
A = [\text{lower} - 1, \, \text{nums}[0], \, \text{nums}[1], \, \dots, \, \text{nums}[k-1], \, \text{upper} + 1]
$$
For every adjacent pair $(u, v)$ in $A$:
- If $v - u == 1$:
  Numbers are strictly consecutive; no integers are missing between $u$ and $v$.
- If $v - u > 1$:
  At least one integer is missing. The maximal contiguous missing range is:
  $$
  [u + 1, \, v - 1]
  $$

#### Unified Edge Case Resolution
1. **Leading Gap:** When $u = \text{lower} - 1$ and $v = \text{nums}[0]$, if $\text{nums}[0] > \text{lower}$, the gap is $[(\text{lower} - 1) + 1, \text{nums}[0] - 1] = [\text{lower}, \text{nums}[0] - 1]$.
2. **Trailing Gap:** When $u = \text{nums}[-1]$ and $v = \text{upper} + 1$, if $\text{nums}[-1] < \text{upper}$, the gap is $[\text{nums}[-1] + 1, (\text{upper} + 1) - 1] = [\text{nums}[-1] + 1, \text{upper}]$.
3. **Empty Array:** When $\text{nums} = []$, the only pair is $(\text{lower} - 1, \text{upper} + 1)$. The gap condition $(\text{upper} + 1) - (\text{lower} - 1) > 1$ yields $[\text{lower}, \text{upper}]$.

> **Invariant.** For every pair of consecutive elements $(u, v)$ in the augmented sequence, the interval $[u+1, v-1]$ contains only missing integers and is disjoint from `nums`.

---

## 3. Step-by-Step Worked Execution

We trace the augmented array for $\text{nums} = [0, 1, 3, 50, 75]$, $\text{lower} = 0, \text{upper} = 99$:
Augmented sequence:
$$
A = [\mathbf{-1}, \, 0, \, 1, \, 3, \, 50, \, 75, \, \mathbf{100}]
$$

---

### Pair 1: $u = -1, \, v = 0$
- Gap size: $v - u = 0 - (-1) = 1$.
- $1 \ngtr 1$: Consecutive. No missing values.

---

### Pair 2: $u = 0, \, v = 1$
- Gap size: $v - u = 1 - 0 = 1$.
- $1 \ngtr 1$: Consecutive. No missing values.

---

### Pair 3: $u = 1, \, v = 3$
- Gap size: $v - u = 3 - 1 = 2 > 1$.
- Emit range:
  $$
  [u + 1, \, v - 1] = [1 + 1, \, 3 - 1] = \mathbf{[2, 2]}
  $$

---

### Pair 4: $u = 3, \, v = 50$
- Gap size: $v - u = 50 - 3 = 47 > 1$.
- Emit range:
  $$
  [u + 1, \, v - 1] = [3 + 1, \, 50 - 1] = \mathbf{[4, 49]}
  $$

---

### Pair 5: $u = 50, \, v = 75$
- Gap size: $v - u = 75 - 50 = 25 > 1$.
- Emit range:
  $$
  [u + 1, \, v - 1] = [50 + 1, \, 75 - 1] = \mathbf{[51, 74]}
  $$

---

### Pair 6: $u = 75, \, v = 100$
- Gap size: $v - u = 100 - 75 = 25 > 1$.
- Emit range:
  $$
  [u + 1, \, v - 1] = [75 + 1, \, 100 - 1] = \mathbf{[76, 99]}
  $$

All pairs processed.
Final result: `[[2, 2], [4, 49], [51, 74], [76, 99]]`.

---

## 4. Complete Execution Trace

```text
Augmented Sequence: [-1] -> [0] -> [1] -> [3] -> [50] -> [75] -> [100]
Gaps Evaluated:
  (-1, 0):  diff = 1  -> none
  (0, 1):   diff = 1  -> none
  (1, 3):   diff = 2  -> missing [2, 2]
  (3, 50):  diff = 47 -> missing [4, 49]
  (50, 75): diff = 25 -> missing [51, 74]
  (75, 100):diff = 25 -> missing [76, 99]
```

| Pair Index | Previous $u$ | Next $v$ | Difference $(v - u)$ | Condition $(v - u > 1)$ | Missing Range Formula $[u+1, v-1]$ | Appended Range |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | -1 | 0 | 1 | False | - | - |
| 2 | 0 | 1 | 1 | False | - | - |
| **3** | **1** | **3** | **2** | **True** | **$[1+1, 3-1]$** | **`[2, 2]`** |
| **4** | **3** | **50** | **47** | **True** | **$[3+1, 50-1]$** | **`[4, 49]`** |
| **5** | **50** | **75** | **25** | **True** | **$[50+1, 75-1]$** | **`[51, 74]`** |
| **6** | **75** | **100** | **25** | **True** | **$[75+1, 100-1]$** | **`[76, 99]`** |

### Every Authored Instance in One Ledger

The third column pair is the same identity in every row and a useful cross-check on the emitted ranges: the number of integers covered by the emitted ranges always equals $(\text{upper} - \text{lower} + 1) - \lvert \text{nums} \rvert$, the size of the bounded domain minus the values that are present.

| Authored instance | `nums` | $[\text{lower}, \text{upper}]$ | Adjacent pairs evaluated | Ranges emitted | Missing integers covered | Integers a domain scan would test |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| Several gaps | `[0, 1, 3, 50, 75]` | $[0, 99]$ | 6 | 4 | 95 | 100 |
| Sole bounded value present | `[-1]` | $[-1, -1]$ | 2 | 0 | 0 | 1 |
| Empty input, one bounded value | `[]` | $[1, 1]$ | 1 | 1 | 1 | 1 |
| Missing values touch both boundaries | `[2, 3]` | $[0, 5]$ | 3 | 2 | 4 | 6 |
| Ranges crossing zero | `[-3, -1, 2]` | $[-4, 3]$ | 4 | 4 | 5 | 8 |
| Empty input, full domain | `[]` | $[-10^9, 10^9]$ | 1 | 1 | 2000000001 | 2000000001 |
| 100 consecutive present values | `-50` through `49` | $[-50, 49]$ | 101 | 0 | 0 | 100 |
| Extreme endpoints present | `[-1000000000, 1000000000]` | $[-10^9, 10^9]$ | 3 | 1 | 1999999999 | 2000000001 |

---

## 5. Algorithmic Correctness

**Soundness.** For any adjacent pair $(u, v)$ in the augmented sequence, all integers between $u$ and $v$ are strictly greater than $u$ and strictly less than $v$. Since `nums` contains no elements between $u$ and $v$, the interval $[u+1, v-1]$ is completely disjoint from `nums` and contained within $[\text{lower}, \text{upper}]$.

**Completeness.** Since the augmented sequence starts at $\text{lower} - 1$ and ends at $\text{upper} + 1$, every integer in $[\text{lower}, \text{upper}]$ lies either in `nums` or in between some adjacent pair $(u, v)$. Hence, no missing numbers can be omitted.

---

## 6. Traps This Instance Exposes

- **32-Bit Integer Overflow with Sentinels:** In languages with fixed-width 32-bit signed integers (like C++ or Java), if $\text{lower} = -2^{31}$ or $\text{upper} = 2^{31} - 1$, computing $\text{lower} - 1$ or $\text{upper} + 1$ can overflow! Using 64-bit integers (`long long`) or tracking previous bound with `prev = lower` avoids arithmetic overflow.
- **Singleton Missing Ranges:** When only one number is missing (e.g. between 1 and 3, missing 2), the schema requires returning `[2, 2]`, not a scalar `2` or string `"2"`.
- **Empty Array Handling:** When `nums` is empty, the entire interval $[\text{lower}, \text{upper}]$ is missing, which the sentinel pair $(\text{lower}-1, \text{upper}+1)$ correctly evaluates to `[[lower, upper]]`.

Each positional case below is decided by the same comparison, so the table is really a checklist of which pair each authored instance contributes:

| Positional case | Authored instance | Pair $(u, v)$ that decides it | $v - u$ | Emitted range |
|:---|:---|:---|:---:|:---|
| Leading gap, array starts above `lower` | `nums = [2, 3]`, $[0, 5]$ | $(-1, 2)$: the lower sentinel against $\text{nums}[0]$ | 3 | `[0, 1]` |
| Leading position already covered | `nums = [0, 1, 3, 50, 75]`, $[0, 99]$ | $(-1, 0)$ | 1 | none, because `nums[0]` equals `lower` |
| Singleton interior gap | the same sample instance | $(1, 3)$ | 2 | `[2, 2]` |
| Trailing gap, array ends below `upper` | the same sample instance | $(75, 100)$ with $100 = \text{upper} + 1$ | 25 | `[76, 99]` |
| Trailing position already covered | `nums = [-1]`, $[-1, -1]$ | $(-1, 0)$ | 1 | none, because `nums[-1]` equals `upper` |
| Both ends missing | `nums = [2, 3]`, $[0, 5]$ | $(-1, 2)$ and $(3, 6)$ | 3 and 3 | `[0, 1]`, then `[4, 5]` |
| Empty array with one bounded value | `nums = []`, $[1, 1]$ | $(0, 2)$: two sentinels and no interior element | 2 | `[1, 1]` |
| Empty array across the whole domain | `nums = []`, $[-10^9, 10^9]$ | $(-1000000001, 1000000001)$ | 2000000002 | `[-1000000000, 1000000000]` |
| Interior gap spanning almost the whole domain | `nums = [-1000000000, 1000000000]`, same bounds | $(-10^9, 10^9)$ | 2000000000 | `[-999999999, 999999999]` |

---

## 7. Complexity Derivation

The comparison table makes the cost difference concrete: the pairwise method inspects one pair per present value, while the domain-driven methods pay for every integer in $[\text{lower}, \text{upper}]$, which the two extreme instances push past two billion.

| Candidate method | Mechanism | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Test every integer in the domain | walk `lower` through `upper` and check each value against `nums` | $O(\text{upper} - \text{lower} + 1)$ time | the full-domain instances would perform 2,000,000,001 tests, and a linear membership search multiplies that by $N$ |
| Set membership over the domain | build a set of `nums`, then walk the domain and group consecutive absences | $O(\text{upper} - \text{lower} + 1)$ time, $O(N)$ space | the cost is still driven by the domain rather than by the input; the two empty-array instances gain nothing from the set |
| Literal sentinel insertion | prepend $\text{lower} - 1$ and append $\text{upper} + 1$ to a copy of `nums`, then walk consecutive pairs | $O(N)$ time, $O(N)$ auxiliary space | correct, but the copy is avoidable: treating both sentinels as boundary comparisons is what keeps the auxiliary space constant |
| Running cursor of the next expected value | keep `expect`, emit `[expect, v - 1]` whenever a present value exceeds it, then set `expect = v + 1` | $O(N)$ time, $O(1)$ space | the final check `expect <= upper` is required after the loop; without it every trailing range disappears, and setting `expect = v` instead of `v + 1` re-emits values that are present |
| Sentinel arithmetic in fixed-width 32-bit integers | compute $\text{lower} - 1$ and $\text{upper} + 1$ as ordinary machine integers | $O(N)$ time | overflows at the domain ends: at $\text{upper} = 2^{31} - 1$ the upper sentinel wraps to a negative value, so the trailing comparison fabricates a range |

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. We iterate over $N + 1$ adjacent pairs, performing $O(1)$ arithmetic operations per pair.
- **Auxiliary Space Complexity:** $O(1)$ constant memory (excluding the output list), requiring only two pointers $u$ and $v$.
