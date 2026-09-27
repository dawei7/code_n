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

### Query Evaluation, Key by Key

A `find` call is only as good as the keys it inspects, and the two branches of the multiplicity rule are what separate a real pair from a value paired with itself:

| Query | Key $x$ inspected | Complement $y = \text{value} - x$ | Branch taken | Membership / multiplicity evidence | Verdict from this key |
|:---:|:---:|:---:|:---|:---|:---|
| `find(4)` | 1 | 3 | distinct, $y \ne x$ | `freq[3] = 1`, so one stored copy exists | `true` — pair $(1, 3)$ is valid |
| `find(7)` | 1 | 6 | distinct, $y \ne x$ | 6 was never added | continue |
| `find(7)` | 3 | 4 | distinct, $y \ne x$ | 4 was never added | continue |
| `find(7)` | 5 | 2 | distinct, $y \ne x$ | 2 was never added | continue; all keys exhausted, so `false` |
| `find(6)` after a second `add(3)` | 3 | 3 | identical, $x == y$ | `freq[3] = 2`, so two separate `add` calls happened | `true` — the two copies are distinct elements |
| `find(6)` before the second `add(3)` | 3 | 3 | identical, $x == y$ | `freq[3] = 1`, only one copy ever stored | `false` — a single element may not be reused as both addends |

The same key $x = 3$ answers `true` and `false` for the same query value $6$ depending only on the stored multiplicity. That is why the data structure stores counts rather than mere membership.

### Scenario Table: What Kind of Evidence Each Query Needs

| Stored state | Query | Complement situation | Deciding check | Result | Why |
|:---|:---:|:---|:---|:---:|:---|
| `{}` | 0 | no keys to inspect | loop body never runs | `false` | Nothing has been added, so no pair can exist |
| `{0: 1}` | 0 | $x = 0$ gives $y = 0$ | multiplicity: `freq[0] = 1` is below $2$ | `false` | Zero is its own complement, so the same single element would have to serve twice |
| `{0: 2}` | 0 | $x = 0$ gives $y = 0$ | multiplicity: `freq[0] = 2` | `true` | Two separate `add(0)` calls provide two distinct elements |
| `{3: 1}` | 6 | $x = 3$ gives $y = 3$ | multiplicity: `freq[3] = 1` | `false` | The classic double-counting trap: a set-like store would answer `true` here |
| `{3: 2}` | 6 | $x = 3$ gives $y = 3$ | multiplicity: `freq[3] = 2` | `true` | Duplicates are legal addends as long as two copies exist |
| `{-2: 1, 5: 1}` | 3 | $x = -2$ gives $y = 5$ | membership: $5$ present and $5 \ne -2$ | `true` | The complement rule is pure subtraction, so it works unchanged across the sign boundary |
| `{-100000: 1, 100000: 1}` | 0 | $x = -100000$ gives $y = 100000$ | membership: $100000$ present | `true` | The query value may be far smaller than either stored magnitude |
| `{-100000: 2, 100000: 1}` | $-200000$ | $x = -100000$ gives $y = -100000$ | multiplicity: `freq[-100000] = 2` | `true` | A negative target can be met by two copies of the same negative value |
| `{-100000: 2, 100000: 1}` | $2^{31} - 1$ | complements $2147583647$ (for $x = -100000$) and $2147383647$ (for $x = 100000$) are both absent | membership: no key matches | `false` | The stored magnitudes are tiny compared with the query, so the complement of every key misses |

The last two rows also settle a performance question: an unreachable target still forces a scan of all $U$ distinct keys, which is why `find` costs $O(U)$ even when the answer is obviously `false`.

---

## 5. Algorithmic Correctness

**Soundness.** If $x \ne y$ and both exist in `freq`, they represent elements added at different steps. If $x == y$, checking $\text{freq}[x] \ge 2$ guarantees that at least two separate calls to `add(x)` were made, satisfying the requirement of two distinct elements.

**Completeness.** Any pair of elements summing to `value` consists of some $x$ and $y = \text{value} - x$. Since the loop iterates over all distinct keys $x$, if a valid pair exists, its smaller member $x$ will be tested and its complement $y$ identified in $O(1)$ hash map lookup.

---

## 6. Traps This Instance Exposes

- **Using a Set Instead of a Frequency Map:** A standard `set` cannot differentiate between receiving a single $3$ versus receiving two $3$s. Calling `find(6)` on `set({1, 3, 5})` would falsely return `True` by pairing $3$ with itself!
- **Precomputing All Pair Sums:** If $N$ numbers are added, there are $\binom{N}{2} \approx N^2 / 2$ pairs. Precomputing all sums takes $O(N^2)$ space and $O(N)$ time per `add`, exceeding memory limits for large streams.
- **Negative Targets and Numbers:** Complement formula $y = \text{value} - x$ works identically for negative numbers and negative targets without modification.

### Alternative Designs on This Operation Stream

| Design | `add` cost | `find` cost | Space after $N$ adds | What it does on this exact stream |
|:---|:---:|:---:|:---:|:---|
| List of all added values | $O(1)$ | $O(N^{2})$ by scanning all index pairs | $O(N)$ | Answers `find(4)` and `find(7)` correctly but re-derives every pair from scratch on each query |
| Sorted list plus two pointers | $O(N)$ to keep it sorted | $O(N)$ | $O(N)$ | Maintains order unnecessarily; additions dominate the cost even though the queries are rare |
| Set of distinct values | $O(1)$ | $O(U)$ | $O(U)$ | Returns `true` for `find(6)` after a single `add(3)`, silently pairing an element with itself |
| Precomputed set of all pair sums | $O(N)$ per add | $O(1)$ | $O(N^{2})$ | Answers instantly but stores roughly $N^{2}/2$ sums, which is untenable for a long stream |
| Frequency map with complement scan | $O(1)$ | $O(U)$ | $O(U)$ | Answers `find(4)` $\to$ `true`, `find(7)` $\to$ `false`, and correctly distinguishes one `add(3)` from two |
| Frequency map plus a bound on stored values | $O(1)$ | $O(U)$ | $O(U)$ | The value range reaches $\pm 2^{31}$, so a direct-address array indexed by value is infeasible; hashing the keys is what keeps the space linear in distinct inputs |

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `add(number)`: $O(1)$ amortized time for hash map insertion.
  - `find(value)`: $O(U)$ worst-case time, where $U \le N$ is the number of unique integers currently stored in `freq`. For each unique key, $O(1)$ hash lookup is performed.
- **Auxiliary Space Complexity:** $O(U) \le O(N)$ auxiliary memory to store the frequencies of the $U$ distinct added values.
