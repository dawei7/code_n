# Guided Example: Flatten 2D Vector

We trace the step-by-step two-coordinate cursor management, lazy empty-row skipping, and idempotent `hasNext` validation on representative 2D vector instances:

- **Input:**
  - Initialization: $\text{vec} = [[1, 2], [3], [4]]$
  - Calls: `next()`, `next()`, `next()`, `hasNext()`, `hasNext()`, `next()`, `hasNext()`
- **Required output:**
  - Sequence of returns: `1, 2, 3, true, true, 4, false`
- **Interleaved Empty Rows Instance:** $\text{vec} = [[], [1, 2], [], [], [3], []]$ (Multiple contiguous empty rows skipped transparently)
- **All Empty Rows Instance:** $\text{vec} = [[], [], []] \implies \text{hasNext}() = \text{false}$ immediately
- **Single Element Instance:** $\text{vec} = [[42]] \implies \text{next}() = 42, \, \text{hasNext}() = \text{false}$

This instance demonstrates lazy evaluation patterns for composite data iterators, proves amortized $O(1)$ time complexity for cursor advances across empty sub-arrays, maintains idempotence across repeated `hasNext` inquiries, and enforces strictly $O(1)$ auxiliary memory without copying or pre-flattening the underlying matrix.

---

## 1. Instance & Teaching Goal

We implement the `Vector2D` streaming iterator:
```text
Vector2D iterator = new Vector2D([[1, 2], [3], [4]]);
iterator.next();    // returns 1
iterator.next();    // returns 2
iterator.next();    // returns 3
iterator.hasNext(); // returns true (idempotent, doesn't advance)
iterator.hasNext(); // returns true
iterator.next();    // returns 4
iterator.hasNext(); // returns false
```

### Pre-Flattening vs Lazy Streaming
- **Pre-flattening:** Unrolling all rows into a 1D array in the constructor takes $O(N)$ time and $O(N)$ auxiliary space upfront. If the client only iterates the first 5 elements of a million-element dataset, pre-flattening wastes massive memory and time.
- **Lazy Two-Pointer Cursor:** Store only two integer variables:
  - `row`: Current row index in `vec`.
  - `col`: Current column index in `vec[row]`.
  A helper function `advance_to_next()` skips empty rows on demand. This achieves **$O(1)$ auxiliary space** and **amortized $O(1)$ time per operation**.

The four designs below are the realistic candidates; the last column is the concrete reason each rejected design fails or costs more on this instance:

| Design | What it stores | Memory for $\text{vec} = [[1, 2], [3], [4]]$ | Per-call behaviour | Failure mode, or why it is rejected |
|:---|:---|:---|:---|:---|
| Pre-flattening in the constructor | a complete copy of all $N$ values | $4$ copied integers | $O(1)$ per call, after an $O(N)$ setup | reading only the first value of a huge input already pays for every value |
| A live iterator per row | the outer iterator plus one inner iterator per row | $3$ row iterators plus the outer one | $O(1)$ amortized, but each step unwraps two levels | memory still grows with the row count $R$ |
| Two scalar coordinates with an `if` normalization step | `row` and `col` only | $2$ integers | at most one row advance per call | cannot cross a run of empty rows: from `(0, 0)` on `vec = [[], [], [1, 2]]` it settles on row $1$, whose length is $0$, so the following read is out of bounds |
| Two scalar coordinates with a `while` normalization loop (the method used) | `row` and `col` only | $2$ integers | amortized $O(1)$, with the empty prefix crossed inside a single call | none; this is the design traced below |

---

## 2. Conceptual Foundation & Invariants

### The Cursor Invariant
At any point, `(row, col)` points to the next unread element, or `row == len(vec)` if the entire vector is exhausted.

### Normalization Protocol: `advance_to_next()`
Before any read or availability check, normalize the pointer:
While `row < len(vec)` and `col >= len(vec[row])`:
$$
\text{row} \leftarrow \text{row} + 1
$$
$$
\text{col} \leftarrow 0
$$
*(Notice: If a row is empty, $\text{len}(\text{vec}[\text{row}]) = 0$. Since $\text{col} = 0 \ge 0$, the condition is immediately met and the empty row is skipped instantly!)*

### API Methods:
1. **`hasNext()`:**
   - Call `advance_to_next()`.
   - Return $\text{row} < \text{len}(\text{vec})$.
   *(Calling `hasNext()` multiple times is strictly idempotent: it never consumes an element)*.
2. **`next()`:**
   - Call `advance_to_next()`.
   - Read value: $\text{val} = \text{vec}[\text{row}][\text{col}]$.
   - Increment: $\text{col} \leftarrow \text{col} + 1$.
   - Return $\text{val}$.

> **Invariant.** `advance_to_next()` ensures that whenever `row < len(vec)`, $\text{vec}[\text{row}][\text{col}]$ is guaranteed to be a valid existing integer.

---

## 3. Step-by-Step Worked Execution

We trace $\text{vec} = [[1, 2], [3], [4]]$:
Initial state: $\text{row} = 0, \quad \text{col} = 0$.

---

### Step 1: `next()`
- Call `advance_to_next()`: $\text{row} = 0 < 3, \, \text{col} = 0 < \text{len}(\text{vec}[0]) = 2$. Valid.
- Read $\text{vec}[0][0] = \mathbf{1}$.
- Increment: $\text{col} \leftarrow 0 + 1 = 1$.
- State: $\text{row} = 0, \, \text{col} = 1$.
- **Returns 1.**

---

### Step 2: `next()`
- Call `advance_to_next()`: $\text{row} = 0, \, \text{col} = 1 < 2$. Valid.
- Read $\text{vec}[0][1] = \mathbf{2}$.
- Increment: $\text{col} \leftarrow 1 + 1 = 2$.
- State: $\text{row} = 0, \, \text{col} = 2$.
- **Returns 2.**

---

### Step 3: `next()`
- Call `advance_to_next()`:
  - $\text{row} = 0 < 3$, but $\text{col} = 2 \ge \text{len}(\text{vec}[0]) = 2$.
  - Row 0 exhausted! Advance: $\text{row} \leftarrow 1, \, \text{col} \leftarrow 0$.
  - Now $\text{row} = 1 < 3$, $\text{col} = 0 < \text{len}(\text{vec}[1]) = 1$. Stop normalization.
- Read $\text{vec}[1][0] = \mathbf{3}$.
- Increment: $\text{col} \leftarrow 0 + 1 = 1$.
- State: $\text{row} = 1, \, \text{col} = 1$.
- **Returns 3.**

---

### Step 4: `hasNext()`
- Call `advance_to_next()`:
  - $\text{row} = 1 < 3, \, \text{col} = 1 \ge \text{len}(\text{vec}[1]) = 1$.
  - Row 1 exhausted! Advance: $\text{row} \leftarrow 2, \, \text{col} \leftarrow 0$.
  - Check row 2: $\text{col} = 0 < \text{len}(\text{vec}[2]) = 1$. Valid.
- Availability check: $\text{row} = 2 < 3 \implies \mathbf{\text{True}}$.
- Cursor state remains $\text{row} = 2, \, \text{col} = 0$.
- **Returns `true`.**

---

### Step 5: `hasNext()` (Repeated Verification)
- Call `advance_to_next()`:
  - $\text{row} = 2 < 3, \, \text{col} = 0 < 1$. Loop does not run.
- Availability check: $\text{row} = 2 < 3 \implies \mathbf{\text{True}}$.
- State unchanged: $\text{row} = 2, \, \text{col} = 0$.
- **Returns `true`.**

---

### Step 6: `next()`
- Call `advance_to_next()`: already normalized.
- Read $\text{vec}[2][0] = \mathbf{4}$.
- Increment: $\text{col} \leftarrow 0 + 1 = 1$.
- State: $\text{row} = 2, \, \text{col} = 1$.
- **Returns 4.**

---

### Step 7: `hasNext()`
- Call `advance_to_next()`:
  - $\text{row} = 2 < 3, \, \text{col} = 1 \ge \text{len}(\text{vec}[2]) = 1$.
  - Row 2 exhausted! Advance: $\text{row} \leftarrow 3, \, \text{col} \leftarrow 0$.
  - Loop condition: $\text{row} = 3 < 3$ is False.
- Availability check: $\text{row} < \text{len}(\text{vec}) \implies 3 < 3$ (**False**).
- State: $\text{row} = 3, \, \text{col} = 0$.
- **Returns `false`.**

---

## 4. Complete Execution Trace

```text
vec = [[1, 2], [3], [4]]

Call 1: next()    -> row=0, col=0 -> val=1 -> col becomes 1 -> return 1
Call 2: next()    -> row=0, col=1 -> val=2 -> col becomes 2 -> return 2
Call 3: next()    -> col=2 >= 2 -> row=1, col=0 -> val=3 -> col becomes 1 -> return 3
Call 4: hasNext() -> col=1 >= 1 -> row=2, col=0 -> row < 3 -> return True
Call 5: hasNext() -> row=2, col=0 already valid -> return True
Call 6: next()    -> row=2, col=0 -> val=4 -> col becomes 1 -> return 4
Call 7: hasNext() -> col=1 >= 1 -> row=3, col=0 -> row == 3 -> return False

Sequence: [1, 2, 3, True, True, 4, False]
```

| Step | Method Call | $\text{advance\_to\_next}()$ Action | Active Coordinate $(\text{row}, \text{col})$ | Value Returned | Invariant Status |
|:---:|:---:|:---|:---:|:---:|:---:|
| **1** | `next()` | None (Already in row 0) | $(0, 0)$ | **1** | Points to 2 |
| **2** | `next()` | None (Still in row 0) | $(0, 1)$ | **2** | Row 0 consumed |
| **3** | `next()` | Advance row: $0 \to 1, \, \text{col} \to 0$ | $(1, 0)$ | **3** | Row 1 consumed |
| **4** | `hasNext()` | Advance row: $1 \to 2, \, \text{col} \to 0$ | $(2, 0)$ | **`true`** | Ready at 4 |
| **5** | `hasNext()` | No change (Idempotent) | $(2, 0)$ | **`true`** | Ready at 4 |
| **6** | `next()` | None (Already positioned) | $(2, 0)$ | **4** | Row 2 consumed |
| **7** | `hasNext()` | Advance row: $2 \to 3$ (Exhausted) | $(3, 0)$ | **`false`** | Iterator finished |

---

## 5. Algorithmic Correctness

**Soundness.** `next()` only reads values at coordinates where $\text{row} < \text{len}(\text{vec})$ and $\text{col} < \text{len}(\text{vec}[\text{row}])$, strictly respecting row and column bounds. Elements are yielded in row-major left-to-right order.

**Completeness.** Every element in every non-empty row is visited exactly once before the cursor advances. Empty rows are skipped by the normalization loop without incrementing any element counter or skipping valid data.

---

## 6. Traps This Instance Exposes

- **Contiguous Empty Rows:** Inputs like `[[], [], [1], [], []]` contain sequences of multiple empty rows. The normalization check must be a `while` loop, not an `if` statement, to skip past consecutive empty lists.
- **Idempotence Violation:** If `hasNext()` modified iterator position or consumed elements, calling `hasNext()` twice would skip elements. `advance_to_next()` only positions the cursor at the next valid element without consuming it.
- **Calling `next()` Without `hasNext()`:** Some clients call `next()` directly without checking `hasNext()`. Placing `advance_to_next()` inside both `next()` and `hasNext()` guarantees safety regardless of caller order.

### Boundary instances of the same protocol

Every row below is a separate input to the identical contract; the third column is what a single normalization call actually does, which is what makes each boundary benign or dangerous.

| Instance | Why it is a boundary | First normalization from `(0, 0)` | Values yielded |
|:---|:---|:---|:---|
| `vec = []` | the outer vector is itself empty | the loop guard fails immediately because $\text{row} = 0$ is not $< 0$ | none; `hasNext()` answers `false` at once |
| `vec = [[], [], []]` | three contiguous empty rows and no data at all | $\text{row}$ climbs $0 \to 3$ inside one call | none |
| `vec = [[], [], [1, 2], [], [], [3], []]` | leading pair, middle pair, and a trailing empty row | $\text{row}$ climbs $0 \to 2$ inside one call and lands on the first value | $1, 2, 3$ |
| `vec = [[42]]` | one element, and the read itself exhausts its row | no advance is needed, but after the read $\text{col} = 1$ forces $\text{row}$ from $0$ to $1$ on the next call | $42$, then `false` |
| $199$ empty rows followed by `[42]` | the empty prefix is far longer than the data suffix | one call walks $\text{row}$ through all $199$ empty rows and stops on the row holding $42$ | $42$ |
| `vec = [[-1, 0], [], [0, 1], [-1]]` | signed values with repeated $0$ and repeated $-1$ | no advance is needed for the first row | $-1, 0, 0, 1, -1$, in row-major order, keeping both duplicates |

The third and fifth rows together expose the property that makes the `while` loop mandatory rather than merely tidy: the number of rows crossed in one normalization call is data-dependent, and it can be as large as the entire row count.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Constructor:** $O(1)$ constant time.
  - **`next()` and `hasNext()`:** **Amortized $O(1)$ time**. Across the entire lifetime of the iterator, `row` advances at most $R$ times (where $R$ is the number of rows), and `col` advances at most $N$ times (where $N$ is the total number of integers). Total work for $K$ operations is $O(N + R)$, averaging $O(1)$ per operation.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only two scalar integer variables (`row` and `col`) are stored.

### Cost ledger over a complete lifetime

Both instances are fully consumed below, sheet by sheet, to show where the amortized bound comes from. Here $N$ counts stored integers and $R$ counts rows.

| Quantity | Primary instance `[[1, 2], [3], [4]]` | Interleaved instance `[[], [], [1, 2], [], [], [3], []]` | General bound | Why the bound holds |
|:---|:---:|:---:|:---|:---|
| Values yielded | 4 | 3 | exactly $N$ | every `next()` reads one entry and then moves past it |
| Row advances for the whole lifetime | 3 | 7 | at most $R$ | `row` never decreases, so it can be advanced once per row at most |
| Column increments from `next()` | 4 | 3 | exactly $N$ | only `next()` increments `col`, once per yielded value |
| Column resets to $0$ | 3 | 7 | at most $R$ | a reset accompanies each row advance and nothing else |
| Total cursor movement | 10 | 17 | $O(N + R)$ | the three quantities above are each bounded independently of the call pattern |
| Calls to consume everything | $4$ `next()` plus $5$ `hasNext()` | $3$ `next()` plus $4$ `hasNext()` | $2N + 1$ for a full drain | one `next()` per value, one final `hasNext()` to observe exhaustion |
| Average movement per call | $10 / 9 \approx 1.1$ | $17 / 7 \approx 2.4$ | $O(1)$ | total work grew by $7$ when the row count grew by $4$, not multiplicatively |
| Auxiliary variables held | 2 | 2 | $O(1)$ | the state is `row` and `col` only, independent of $N$ and $R$ |

The fifth row is the amortization argument in one line: the interleaved instance has seven rows but only three values, and its $17$ total movements are still linear in rows plus values, so a caller cannot force repeated re-scanning of the same empty prefix. That is what "amortized $O(1)$" means here, and it is also why the constructor is $O(1)$ rather than $O(N)$.
