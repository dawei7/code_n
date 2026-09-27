# Guided Example: Flatten Nested List Iterator

We trace the step-by-step recursive flattening decomposition (`dfs`), linear integer buffer generation (`nums`), pointer cursor progression (`i`), and lazy iterator contract methods (`hasNext()`, `next()`) on representative nested list instances:

- **Input:** `nestedList = [[1, 1], 2, [1, 1]]`
- **Required output:** `[1, 1, 2, 1, 1]`
  - Flattening process:
    - First element `[1, 1]`: nested list containing two integers $\implies 1, 1$
    - Second element $2$: single scalar integer $\implies 2$
    - Third element `[1, 1]`: nested list containing two integers $\implies 1, 1$
  - Flattened internal sequence: `[1, 1, 2, 1, 1]`
  - Iterator operations:
    - `hasNext() -> True`, `next() -> 1`
    - `hasNext() -> True`, `next() -> 1`
    - `hasNext() -> True`, `next() -> 2`
    - `hasNext() -> True`, `next() -> 1`
    - `hasNext() -> True`, `next() -> 1`
    - `hasNext() -> False`
- **Arbitrary Depth Nesting:** `nestedList = [1, [4, [6]]] \implies [1, 4, 6]`
- **Empty Nested Lists:** `nestedList = [[], [[]]] \implies []` (zero elements yielded, `hasNext()` returns `False` immediately)

This instance demonstrates iterator design for arbitrarily nested recursive structures, contrasts eager flattening with lazy stack unpacking, validates the two-phase iterator contract (`hasNext()` idempotence and `next()` cursor advance), and analyzes $O(N)$ initialization time and $O(1)$ amortized call complexity.

---

## 1. Instance & Teaching Goal

Given an arbitrarily nested list of integers:
$$
\text{nestedList} = [[1, 1], \; 2, \; [1, 1]]
$$
Design an iterator that sequentially yields each integer in depth-first order:
- `hasNext()`: Returns `true` if more integers remain; `false` otherwise.
- `next()`: Returns the next integer in the sequence and advances the internal cursor.

```text
Nested Structure:
[
  [1, 1],  <-- list with two ints: 1, 1
  2,       <-- scalar int: 2
  [1, 1]   <-- list with two ints: 1, 1
]

Sequential Unrolled Stream:
1 -> 1 -> 2 -> 1 -> 1 -> EOF
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Pre-Flattening Invariant
During initialization `__init__(nestedList)`:
A recursive traversal `dfs(ls)` recursively unpacks all elements:
- If `x.isInteger()`: append scalar `x.getInteger()` to `self.nums`.
- Else: recurse into `dfs(x.getList())`.
Initialize cursor `self.i = -1`.

### 2. Iterator Query Contracts:
- **`hasNext()`:**
  Tests whether a subsequent element exists without advancing the cursor:
  $$
  self.i + 1 < \text{len}(self.nums)
  $$
  *Idempotent: Calling `hasNext()` multiple times consecutively does not alter internal state.*
- **`next()`:**
  Advances cursor and retrieves the element:
  $$
  self.i \leftarrow self.i + 1
  $$
  $$
  \text{return } self.nums[self.i]
  $$

> **Invariant.** At any moment, `self.nums[0 \dots self.i]` contains all integers already consumed, and `self.nums[self.i + 1]` is the next candidate integer.

---

## 3. Step-by-Step Worked Execution

We trace the iterator on `nestedList = [[1, 1], 2, [1, 1]]`:

---

### Step 1: Constructor Initialization (`__init__`)
- Start with `self.nums = []`. Call `dfs(nestedList)`:
  1. Inspect element 0 (`[1, 1]`): Not an integer $\implies$ call `dfs([1, 1])`:
     - Inspect child 0 ($1$): is an integer $\implies$ append $1$.
     - Inspect child 1 ($1$): is an integer $\implies$ append $1$.
     - Child returns. `nums = [1, 1]`.
  2. Inspect element 1 ($2$): is an integer $\implies$ append $2$.
     - `nums = [1, 1, 2]`.
  3. Inspect element 2 (`[1, 1]`): Not an integer $\implies$ call `dfs([1, 1])`:
     - Inspect child 0 ($1$): append $1$.
     - Inspect child 1 ($1$): append $1$.
     - `nums = [1, 1, 2, 1, 1]`.
- Set initial cursor: `self.i = -1`.
- Total elements buffered: $M = 5$.

---

### Step 2: Stream Consumption Cycle
1. **Invocation 1:**
   - `hasNext()`: $-1 + 1 < 5 \implies 0 < 5$ (**True**).
   - `next()`: $self.i \leftarrow 0$, returns $nums[0] = \mathbf{1}$.
2. **Invocation 2:**
   - `hasNext()`: $0 + 1 < 5 \implies 1 < 5$ (**True**).
   - `next()`: $self.i \leftarrow 1$, returns $nums[1] = \mathbf{1}$.
3. **Invocation 3:**
   - `hasNext()`: $1 + 1 < 5 \implies 2 < 5$ (**True**).
   - `next()`: $self.i \leftarrow 2$, returns $nums[2] = \mathbf{2}$.
4. **Invocation 4:**
   - `hasNext()`: $2 + 1 < 5 \implies 3 < 5$ (**True**).
   - `next()`: $self.i \leftarrow 3$, returns $nums[3] = \mathbf{1}$.
5. **Invocation 5:**
   - `hasNext()`: $3 + 1 < 5 \implies 4 < 5$ (**True**).
   - `next()`: $self.i \leftarrow 4$, returns $nums[4] = \mathbf{1}$.
6. **Invocation 6:**
   - `hasNext()`: $4 + 1 < 5 \implies 5 < 5$ (**False**).
   - Loop exits cleanly!

---

## 4. Complete Execution Trace

```text
Constructor:
dfs([[1, 1], 2, [1, 1]]) -> self.nums = [1, 1, 2, 1, 1], self.i = -1

Call 1: hasNext() -> True  | next() -> nums[0] = 1, i = 0
Call 2: hasNext() -> True  | next() -> nums[1] = 1, i = 1
Call 3: hasNext() -> True  | next() -> nums[2] = 2, i = 2
Call 4: hasNext() -> True  | next() -> nums[3] = 1, i = 3
Call 5: hasNext() -> True  | next() -> nums[4] = 1, i = 4
Call 6: hasNext() -> False | Stream Exhausted

Output Stream: [1, 1, 2, 1, 1]
```

| Operation Step | Method Called | Cursor State Before | Predicate Evaluated | Value Returned | Cursor State After | Stream Emitted |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | `__init__` | - | DFS Flattening | None | $i = -1$ | `[]` |
| 1 | `hasNext()` | $i = -1$ | $-1 + 1 < 5$ | `True` | $i = -1$ | `[]` |
| 2 | `next()` | $i = -1$ | Advance $i \to 0$ | **1** | $i = 0$ | `[1]` |
| 3 | `hasNext()` | $i = 0$ | $0 + 1 < 5$ | `True` | $i = 0$ | `[1]` |
| 4 | `next()` | $i = 0$ | Advance $i \to 1$ | **1** | $i = 1$ | `[1, 1]` |
| 5 | `hasNext()` | $i = 1$ | $1 + 1 < 5$ | `True` | $i = 1$ | `[1, 1]` |
| 6 | `next()` | $i = 1$ | Advance $i \to 2$ | **2** | $i = 2$ | `[1, 1, 2]` |
| 7 | `hasNext()` | $i = 2$ | $2 + 1 < 5$ | `True` | $i = 2$ | `[1, 1, 2]` |
| 8 | `next()` | $i = 2$ | Advance $i \to 3$ | **1** | $i = 3$ | `[1, 1, 2, 1]` |
| 9 | `hasNext()` | $i = 3$ | $3 + 1 < 5$ | `True` | $i = 3$ | `[1, 1, 2, 1]` |
| 10 | `next()` | $i = 3$ | Advance $i \to 4$ | **1** | $i = 4$ | `[1, 1, 2, 1, 1]` |
| 11 | `hasNext()` | $i = 4$ | $4 + 1 < 5$ (False) | `False` | $i = 4$ | `[1, 1, 2, 1, 1]` |

---

## 5. Algorithmic Correctness

**Soundness.** The recursive `dfs` traverses nested lists in exact left-to-right, depth-first pre-order. Every integer encountered in the nested list is appended in its exact sequential appearance order. The cursor variable $i$ starts at $-1$ and is incremented exclusively upon calling `next()`, ensuring each element in `self.nums` is returned exactly once.

**Completeness.** `hasNext()` returns `true` whenever $i + 1 < \text{len}(self.nums)$, guaranteeing that all $M$ extracted integers can be retrieved. Once $i$ reaches the last index, `hasNext()` evaluates to `false`, preventing out-of-bounds access.

---

## 6. Traps This Instance Exposes

- **Empty Sublists Interleaved:** If an empty list `[]` or nested empty list `[[]]` appears between integers (e.g. `[1, [], 2]`), the iterator must not return null or crash. The DFS skips empty lists automatically because their loops run 0 times.
- **Multiple Consecutive `hasNext()` Calls:** An iterator must be idempotent with respect to `hasNext()`. Calling `hasNext()` several times in a row must not advance the cursor.
- **Calling `next()` Without Checking `hasNext()`:** If `next()` is called past the end, `self.nums[self.i]` raises an `IndexError`. Standard iterator contract requires client code to guard with `hasNext()`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization `__init__`: $O(N)$, where $N$ is the total number of nested list objects and integers.
  - `next()`: $O(1)$ constant time index lookup and pointer increment.
  - `hasNext()`: $O(1)$ constant time integer comparison.
- **Auxiliary Space Complexity:** $O(K)$, where $K$ is the total count of integers stored in `self.nums` ($K \le N$).