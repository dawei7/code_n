# Guided Example: Remove K Digits

We trace the step-by-step monotonic increasing digit stack (`stk[-1] > c \implies stk.pop()`), high-significance greedy priority, trailing excess deletion slice (`stk[:remain]`), leading zero stripping (`.lstrip('0')`), and zero fallback on representative integer strings:

- **Input:** $num = \text{"1432219"}, \quad k = 3$
- **Required output:** `"1219"`
  - Target length: $remain = \text{len}(num) - k = 7 - 3 = 4$
  - Step-by-step stack evolution:
    - $c = \text{'1'}: stk = [\text{'1'}]$
    - $c = \text{'4'}: stk = [\text{'1'}, \text{'4'}]$
    - $c = \text{'3'}: 4 > 3 \implies$ Pop `'4'`, $k \leftarrow 2$; push `'3'` $\implies stk = [\text{'1'}, \text{'3'}]$
    - $c = \text{'2'}: 3 > 2 \implies$ Pop `'3'`, $k \leftarrow 1$; push `'2'` $\implies stk = [\text{'1'}, \text{'2'}]$
    - $c = \text{'2'}: 2 \not> 2 \implies$ Push `'2'` $\implies stk = [\text{'1'}, \text{'2'}, \text{'2'}]$
    - $c = \text{'1'}: 2 > 1 \implies$ Pop `'2'`, $k \leftarrow 0$; push `'1'` $\implies stk = [\text{'1'}, \text{'2'}, \text{'1'}]$
    - $c = \text{'9'}: k = 0 \implies$ Push `'9'` $\implies stk = [\text{'1'}, \text{'2'}, \text{'1'}, \text{'9'}]$
  - Take first $remain = 4$ digits: `"1219"`
  - Strip leading zeros: $\mathbf{\text{"1219"}}$
- **Leading Zero Removal:** $num = \text{"10200"}, k = 1 \implies$ pops `'1'`, remaining `"0200"` strips to $\mathbf{\text{"200"}}$
- **Total Elimination:** $num = \text{"10"}, k = 2 \implies$ all digits removed $\implies \mathbf{\text{"0"}}$
- **Monotonically Increasing Input:** $num = \text{"12345"}, k = 2 \implies$ zero pops, truncated from tail: $\mathbf{\text{"123"}}$

This instance demonstrates monotonic stack greedy optimization, mathematically proves why eliminating peaks from left to right yields the lexicographically smallest magnitude, and derives $O(N)$ linear runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a non-negative integer string $num = \text{"1432219"}$ and an integer $k = 3$:
Return the **smallest possible integer** after removing exactly $k$ digits from $num$:

```text
Original: 1 4 3 2 2 1 9   (Length 7, k = 3 deletions -> Output Length 4)
Peaks:      ^ ^     ^
            4 3     2

Greedy Deletion Process:
1. '4' > '3' -> delete '4' -> "132219" (k=2 left)
2. '3' > '2' -> delete '3' -> "12219"  (k=1 left)
3. '2' > '1' -> delete '2' -> "1219"   (k=0 left)

Smallest Result: "1219"
```

### The High-Significance Greedy Theorem
In a base-10 positional numeral system:
$$
V = \sum_{j=0}^{M-1} d_j \cdot 10^{M - 1 - j}
$$
The value is dominated by the leftmost digits. Given two equal-length numbers, whichever differs first with a smaller digit is strictly smaller, regardless of all subsequent digits (e.g. $1299 < 1300$).
Therefore, whenever an earlier digit $d_i$ is strictly greater than the following digit $d_{i+1}$, removing $d_i$ replaces a larger digit at a higher place value with a smaller digit, which is always optimal.

---

## 2. Conceptual Foundation & Invariants

### 1. Monotonic Stack State:
- `stk = []`: Stores digits of the optimal candidate prefix in non-decreasing order.
- `remain = len(num) - k`: Exact length of the final string before zero-stripping.

### 2. Transition Rule for Character $c$:
While $k > 0$ and $stk$ is non-empty and $stk[-1] > c$:
- The digit on top of the stack is a local peak that can be replaced by smaller digit $c$.
- Pop stack:
  $$
  stk.\text{pop}()
  $$
- Decrement available deletions:
  $$
  k \leftarrow k - 1
  $$
Push incoming digit:
$$
stk.\text{append}(c)
$$

### 3. Post-Processing:
1. **Truncation:** If $k > 0$ remains (e.g. for already non-decreasing sequences), the largest digits reside at the tail. Slice $stk[:remain]$.
2. **Leading Zeros:** Remove leading zeros via `.lstrip('0')`.
3. **Empty String Guard:** If the stripped string is empty, return `'0'`.

> **Invariant.** At every step, $stk$ represents the lexicographically smallest subsequence of digits chosen from the processed prefix that can still form a valid candidate of length $remain$.

---

## 3. Step-by-Step Worked Execution

We trace $num = \text{"1432219"}, k = 3$:
Target length: $remain = 7 - 3 = 4$. Initial: $stk = [], k = 3$.

---

### Step 1: Process $c = \text{'1'}$
- Stack empty $\implies stk = [\text{'1'}]$.

---

### Step 2: Process $c = \text{'4'}$
- $stk[-1] = \text{'1'} \le \text{'4'}$. No pops.
- Stack: $stk = [\text{'1'}, \; \text{'4'}]$.

---

### Step 3: Process $c = \text{'3'}$
- Condition: $k = 3 > 0$ and $stk[-1] = \text{'4'} > \text{'3'}$.
- **Pop `'4'`**:
  $$
  stk.\text{pop}() \implies stk = [\text{'1'}], \quad k \leftarrow 3 - 1 = \mathbf{2}
  $$
- Next check: $stk[-1] = \text{'1'} \le \text{'3'}$. Stops popping.
- Append `'3'`:
  $$
  stk = [\text{'1'}, \; \text{'3'}]
  $$

---

### Step 4: Process $c = \text{'2'}$
- Condition: $k = 2 > 0$ and $stk[-1] = \text{'3'} > \text{'2'}$.
- **Pop `'3'`**:
  $$
  stk.\text{pop}() \implies stk = [\text{'1'}], \quad k \leftarrow 2 - 1 = \mathbf{1}
  $$
- Next check: $stk[-1] = \text{'1'} \le \text{'2'}$.
- Append `'2'`:
  $$
  stk = [\text{'1'}, \; \text{'2'}]
  $$

---

### Step 5: Process $c = \text{'2'}$
- Condition: $stk[-1] = \text{'2'} \not> \text{'2'}$. No pops.
- Append `'2'`:
  $$
  stk = [\text{'1'}, \; \text{'2'}, \; \text{'2'}]
  $$

---

### Step 6: Process $c = \text{'1'}$
- Condition: $k = 1 > 0$ and $stk[-1] = \text{'2'} > \text{'1'}$.
- **Pop `'2'`**:
  $$
  stk.\text{pop}() \implies stk = [\text{'1'}, \; \text{'2'}], \quad k \leftarrow 1 - 1 = \mathbf{0}
  $$
- Deletion budget exhausted ($k = 0$). No further pops allowed.
- Append `'1'`:
  $$
  stk = [\text{'1'}, \; \text{'2'}, \; \text{'1'}]
  $$

---

### Step 7: Process $c = \text{'9'}$
- $k = 0 \implies$ No pops.
- Append `'9'`:
  $$
  stk = [\text{'1'}, \; \text{'2'}, \; \text{'1'}, \; \text{'9'}]
  $$

---

### Step 8: Post-Processing & Normalization
- Truncate to $remain = 4$:
  $$
  stk[:4] \implies \text{"1219"}
  $$
- Strip leading zeros: `"1219".lstrip('0') \implies \mathbf{\text{"1219"}}`.

---

## 4. Complete Execution Trace

```text
num = "1432219", k = 3, remain = 4

c = '1': push 1                     -> stk = ['1'], k = 3
c = '4': push 4                     -> stk = ['1', '4'], k = 3
c = '3': pop 4 (4 > 3), push 3      -> stk = ['1', '3'], k = 2
c = '2': pop 3 (3 > 2), push 2      -> stk = ['1', '2'], k = 1
c = '2': push 2 (2 <= 2)            -> stk = ['1', '2', '2'], k = 1
c = '1': pop 2 (2 > 1), push 1      -> stk = ['1', '2', '1'], k = 0
c = '9': push 9 (k == 0)            -> stk = ['1', '2', '1', '9'], k = 0

stk[:4] = "1219" -> lstrip('0') -> "1219"
```

| Step | Char $c$ | Remaining $k$ | Stack Top Before | Condition $k > 0 \land top > c$ | Action Taken | Stack After Step |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `'1'` | 3 | - | Stack empty | Append `'1'` | `['1']` |
| 2 | `'4'` | 3 | `'1'` | $1 > 4$ (False) | Append `'4'` | `['1', '4']` |
| 3 | `'3'` | 3 | `'4'` | $4 > 3$ (True) | Pop `'4'`, Append `'3'` | `['1', '3']` |
| 4 | `'2'` | 2 | `'3'` | $3 > 2$ (True) | Pop `'3'`, Append `'2'` | `['1', '2']` |
| 5 | `'2'` | 1 | `'2'` | $2 > 2$ (False) | Append `'2'` | `['1', '2', '2']` |
| **6** | **'1'** | **1** | **'2'** | **$2 > 1$ (True)** | **Pop `'2'`, Append `'1'** | **`['1', '2', '1']`** |
| 7 | `'9'` | 0 | `'1'` | $k = 0$ (False) | Append `'9'` | `['1', '2', '1', '9']` |
| **Norm**| - | 0 | - | - | Slicing & `.lstrip('0')` | **`"1219"` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $A$ and $B$ be two $m$-digit numbers. $A < B$ if and only if at the first index $j$ where they differ, $A[j] < B[j]$. By popping any previous digit whenever $top > c$ and $k > 0$, the algorithm guarantees that the earlier position receives a smaller digit, which mathematically minimizes the overall value. Equal digits are preserved because $A[j] == B[j]$ confers no immediate advantage, and retaining deletion budget for later drops is optimal.

**Completeness.** Each digit is pushed and popped at most once. Slicing $stk[:remain]$ handles cases where remaining digits are monotonically non-decreasing. Stripping leading zeros and defaulting to `'0'` guarantees adherence to integer string formatting specifications.

---

## 6. Traps This Instance Exposes

- **Strict vs Non-Strict Inequality ($top > c$ vs $top \ge c$):** Using `>=` pops identical digits needlessly. For `num = "112", k = 1`, `>=` pops `'1'` to keep `'12'`, whereas keeping `'1'` allows popping `'2'` to yield `'11'`, which is smaller!
- **Unused Deletions ($k > 0$ at End):** For monotonic inputs like `num = "12345", k = 2`, zero pops occur during the loop. The slice `stk[:remain]` correctly drops the largest trailing digits (`"123"`).
- **All Digits Removed:** For `num = "10", k = 2`, all digits are dropped. Slicing yields `""`. Returning `or '0'` ensures `"0"` is returned rather than an empty string.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(num)$.
  - Each character is pushed onto $stk$ exactly once.
  - Each character is popped from $stk$ at most once.
  - Slicing and zero-stripping take $O(N)$ time.
  - Total runtime is strictly linear $O(N)$, running in under 5 ms for $N = 10^5$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space to store characters in the monotonic stack $stk$.
