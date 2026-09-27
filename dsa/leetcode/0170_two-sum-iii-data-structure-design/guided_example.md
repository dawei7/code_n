# Guided Example: Two Sum III - Data structure design

We trace the step-by-step state evolution of frequency map stream ingestion (`add`) and distinct complement query evaluation (`find`) on representative multi-operation instances:

- **Input Operations:** `["TwoSum", "add", "add", "add", "find", "find"]`
- **Arguments:** `[[], [1], [3], [5], [4], [7]]`
- **Required outputs:** `[null, null, null, null, true, false]` ($1 + 3 = 4 \implies \text{true}$; no pair sums to $7 \implies \text{false}$)
- **Duplicate Self-Pair Instance:** After $\text{add}(3)$, $\text{find}(6) \implies \text{true}$ (Requires frequency $\text{freq}[3] \ge 2$)

This instance demonstrates designing streaming complement lookups with asymmetric workloads, analyzes the frequency map trade-off ($O(1)$ add vs $O(U)$ find), enforces multiplicity gating when $y = \text{target} - x == x$, and achieves optimal space and time guarantees.

---

## 1. Instance & Teaching Goal

Design a data structure supporting continuous streaming additions and pair-sum existence queries:
1. `add(1)`: stores $1$.
2. `add(3)`: stores $3$.
3. `add(5)`: stores $5$.
4. `find(4)`: $1 + 3 = 4 \implies$ returns `true`.
5. `find(7)`: no two distinct stored elements sum to $7 \implies$ returns `false`.

Two design paradigms exist for this problem:
1. **Precompute All Pair Sums on `add`:**
   Querying `find` is $O(1)$, but adding an element takes $O(N)$ time and storing all pairs requires $O(N^2)$ space.
2. **Frequency Map on `add`, Complement Search on `find` (Optimal):**
   Adding an element increments a hash map counter in $O(1)$ time.
   Finding a target iterates over the $U$ distinct keys in the map, testing whether $y = \text{target} - x$ exists in $O(1)$ lookup time:
   - If $y \ne x$: requires $y \in \text{freq}$.
   - If $y == x$: requires $\text{freq}[x] \ge 2$ (cannot reuse the same single element twice).
This achieves strictly $O(1)$ add time, $O(U)$ find time, and $O(U) \le O(N)$ linear space.

---

## 2. Conceptual Foundation & Invariants

### Hash-Map Multiplicity Protocol
Initialize internal dictionary: `self.freq = defaultdict(int)`.

#### Method 1: `add(number)` ($O(1)$ Time)
Increment frequency count:
$$
\text{self.freq}[\text{number}] \leftarrow \text{self.freq}[\text{number}] + 1
$$

#### Method 2: `find(value)` ($O(U)$ Time)
For each unique key $x \in \text{self.freq}$:
Compute required complement:
$$
y = \text{value} - x
$$
1. **Case A: Distinct Complement ($x \ne y$):**
   If $y \in \text{self.freq}$:
   $$
   \text{return True}
   $$
2. **Case B: Identical Complement ($x == y$):**
   Using $x$ twice requires that at least two distinct copies were added:
   $$
   \text{if } \text{self.freq}[x] \ge 2: \quad \text{return True}
   $$

If no key yields a valid complement, return `False`.

> **Invariant.** `self.freq[x]` exactly reflects the total number of times integer $x$ was added. A target value is achievable if and only if two elements with indices $i \ne j$ satisfy $x_i + x_j = \text{value}$.

---

## 3. Step-by-Step Worked Execution

We trace the operations:

### Step 1: `TwoSum()`
- `freq = {}`.
- Output: `null`.

---

### Step 2: `add(1)`
- `freq[1] += 1` $\implies$ `freq = {1: 1}`.
- Output: `null`.

---

### Step 3: `add(3)`
- `freq[3] += 1` $\implies$ `freq = {1: 1, 3: 1}`.
- Output: `null`.

---

### Step 4: `add(5)`
- `freq[5] += 1` $\implies$ `freq = {1: 1, 3: 1, 5: 1}`.
- Output: `null`.

---

### Step 5: `find(4)`
Iterate over keys in `freq`:
- **Key $x = 1$:**
  - Complement: $y = 4 - 1 = 3$.
  - Check: $y \ne x$ ($3 \ne 1$).
  - Is $3 \in \text{freq}$? Yes (`freq[3] = 1`).
  - Valid pair $(1, 3)$ found!
- Return $\mathbf{True}$.

---

### Step 6: `find(7)`
Iterate over keys in `freq`:
- **Key $x = 1$:** $y = 7 - 1 = 6 \implies 6 \notin \text{freq}$.
- **Key $x = 3$:** $y = 7 - 3 = 4 \implies 4 \notin \text{freq}$.
- **Key $x = 5$:** $y = 7 - 5 = 2 \implies 2 \notin \text{freq}$.
All keys exhausted without finding a complement.
Return $\mathbf{False}$.

---

### Step 7 (Follow-up): `add(3)` then `find(6)`
- `add(3)`: `freq[3] += 1` $\implies$ `freq = {1: 1, 3: 2, 5: 1}`.
- `find(6)`:
  - Check $x = 3$:
  - Complement: $y = 6 - 3 = 3$.
  - $x == y$ ($3 == 3$) $\implies$ Multiplicity condition evaluated:
    $$
    \text{freq}[3] = 2 \ge 2 \implies \mathbf{True}
    $$
  - Two distinct instances of 3 exist!
- Return $\mathbf{True}$.

---

## 4. Complete Execution Trace

```text
Stream State:
add(1) -> freq: {1: 1}
add(3) -> freq: {1: 1, 3: 1}
add(5) -> freq: {1: 1, 3: 1, 5: 1}

Query find(4):
  x=1: y = 4 - 1 = 3. 3 in freq? YES (distinct) -> Return True

Query find(7):
  x=1: y = 7 - 1 = 6. 6 in freq? NO
  x=3: y = 7 - 3 = 4. 4 in freq? NO
  x=5: y = 7 - 5 = 2. 2 in freq? NO -> Return False
```

| Operation | Input Value | Updated `self.freq` State | Complement Evaluated ($y = \text{val} - x$) | Multiplicity Check | Emitted Result |
|:---:|:---:|:---|:---:|:---:|:---:|
| `TwoSum` | - | `{}` | - | - | `null` |
| `add` | 1 | `{1: 1}` | - | - | `null` |
| `add` | 3 | `{1: 1, 3: 1}` | - | - | `null` |
| `add` | 5 | `{1: 1, 3: 1, 5: 1}` | - | - | `null` |
| **`find`** | **4** | `{1: 1, 3: 1, 5: 1}` | **$x=1 \implies y=3$** | **$3 \ne 1$ (distinct)** | **`true`** |
| **`find`** | **7** | `{1: 1, 3: 1, 5: 1}` | **$y \in \{6, 4, 2\}$** | **None found** | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** If $x \ne y$ and both exist in `freq`, they represent elements added at different steps. If $x == y$, checking $\text{freq}[x] \ge 2$ guarantees that at least two separate calls to `add(x)` were made, satisfying the requirement of two distinct elements.

**Completeness.** Any pair of elements summing to `value` consists of some $x$ and $y = \text{value} - x$. Since the loop iterates over all distinct keys $x$, if a valid pair exists, its smaller member $x$ will be tested and its complement $y$ identified in $O(1)$ hash map lookup.

---

## 6. Traps This Instance Exposes

- **Using a Set Instead of a Frequency Map:** A standard `set` cannot differentiate between receiving a single $3$ versus receiving two $3$s. Calling `find(6)` on `set({1, 3, 5})` would falsely return `True` by pairing $3$ with itself!
- **Precomputing All Pair Sums:** If $N$ numbers are added, there are $\binom{N}{2} \approx N^2 / 2$ pairs. Precomputing all sums takes $O(N^2)$ space and $O(N)$ time per `add`, exceeding memory limits for large streams.
- **Negative Targets and Numbers:** Complement formula $y = \text{value} - x$ works identically for negative numbers and negative targets without modification.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `add(number)`: $O(1)$ amortized time for hash map insertion.
  - `find(value)`: $O(U)$ worst-case time, where $U \le N$ is the number of unique integers currently stored in `freq`. For each unique key, $O(1)$ hash lookup is performed.
- **Auxiliary Space Complexity:** $O(U) \le O(N)$ auxiliary memory to store the frequencies of the $U$ distinct added values.
