# Guided Example: Design Bitset

We analyze and execute the lazy global inversion Bitset data structure on a representative sequence of operations, demonstrating how a parity flag and running population counter achieve constant-time array-wide bit flips and queries.

- **Input Operations:** `["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]`
- **Arguments:** `[[5], [3], [1], [], [], [0], [], [], [0], [], []]`
- **Output:** `[null, null, null, null, false, null, null, true, null, 2, "01010"]`

This instance illustrates lazy global parity toggling, localized write translation, running population tracking, and deferred string reconstruction.

---

## 1. Problem Overview & Representative Instance

A `Bitset` of fixed length `size` maintains a sequence of binary digits initialized to zero. The data structure must support:
- `fix(idx)`: Sets the bit at index `idx` to $1$. Idempotent if already $1$.
- `unfix(idx)`: Sets the bit at index `idx` to $0$. Idempotent if already $0$.
- `flip()`: Inverts every bit in the bitset ($0 \leftrightarrow 1$).
- `all()`: Returns `true` if every bit is $1$, else `false`.
- `one()`: Returns `true` if at least one bit is $1$, else `false`.
- `count()`: Returns the total count of $1$ bits.
- `toString()`: Returns the binary string of all bits in index order.

With $\text{size} \le 10^5$ and up to $10^5$ calls, modifying every bit during `flip()` would cost $O(\text{size})$ per call ($10^{10}$ operations), causing Time Limit Exceeded. A valid design must execute `flip()`, `fix()`, `unfix()`, and all query methods in $O(1)$ time.

In our representative instance:
- `size = 5`.
- Operations include consecutive individual sets, two global flips, conditional unsets, and boundary query calls.
- The final state must accurately emit $2$ ones with string `"01010"`.

---

## 2. Mathematical & Algorithmic Principles

### Dual-State Parity Invariance (Lazy Inversion)

Instead of updating every cell of an array during `flip()`, we decouple the **physical stored bit** from the **logical observed bit** using a single boolean inversion flag `flipped`:
$$\text{logical\_bit}(idx) = \text{physical\_bit}[idx] \oplus \text{flipped}$$

Where $\oplus$ is the XOR operator:
- When $\text{flipped} = 0$: $\text{logical} = \text{physical}$.
- When $\text{flipped} = 1$: $\text{logical} = 1 - \text{physical}$.

### Constant-Time Method Implementations

1. **`flip()` in $O(1)$:**
   Toggling the global state:
   $$\text{flipped} \leftarrow 1 - \text{flipped}$$
   $$\text{ones\_count} \leftarrow \text{size} - \text{ones\_count}$$
   Every bit in the collection is inverted logically in $O(1)$ time without touching a single array element.
2. **`fix(idx)` in $O(1)$:**
   We require $\text{logical\_bit}(idx) = 1$.
   - Check current logical value: $v = \text{physical\_bit}[idx] \oplus \text{flipped}$.
   - If $v = 0$:
     Set physical storage to $\text{physical\_bit}[idx] = 1 \oplus \text{flipped}$.
     Increment $\text{ones\_count} \leftarrow \text{ones\_count} + 1$.
   - If $v = 1$: Do nothing (idempotent).
3. **`unfix(idx)` in $O(1)$:**
   We require $\text{logical\_bit}(idx) = 0$.
   - Check current logical value: $v = \text{physical\_bit}[idx] \oplus \text{flipped}$.
   - If $v = 1$:
     Set physical storage to $\text{physical\_bit}[idx] = 0 \oplus \text{flipped}$.
     Decrement $\text{ones\_count} \leftarrow \text{ones\_count} - 1$.
   - If $v = 0$: Do nothing (idempotent).
4. **Queries in $O(1)$:**
   - `all()`: evaluates $\text{ones\_count} == \text{size}$.
   - `one()`: evaluates $\text{ones\_count} > 0$.
   - `count()`: evaluates $\text{ones\_count}$.
5. **`toString()` in $O(\text{size})$:**
   Because `toString()` is called at most $5$ times across the entire lifetime, constructing the string by iterating through each index $i$ and emitting $\text{physical\_bit}[i] \oplus \text{flipped}$ runs in $O(\text{size})$ time, well within the time budget.

| Operation | Logical Objective | Physical Update Formula | Population Count Update |
|---|---|---|---|
| `fix(idx)` | Force logical bit to $1$ | $\text{physical}[idx] \leftarrow 1 \oplus \text{flipped}$ | $\text{ones} \leftarrow \text{ones} + 1$ (if changed) |
| `unfix(idx)` | Force logical bit to $0$ | $\text{physical}[idx] \leftarrow 0 \oplus \text{flipped}$ | $\text{ones} \leftarrow \text{ones} - 1$ (if changed) |
| `flip()` | Invert all logical bits | $\text{flipped} \leftarrow 1 - \text{flipped}$ | $\text{ones} \leftarrow \text{size} - \text{ones}$ |
| `count()` | Report active ones | Return $\text{ones}$ | No change |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the representative command sequence for `size = 5`.

```
Initial: physical = [0, 0, 0, 0, 0], flipped = 0, ones = 0
Logical: [0, 0, 0, 0, 0]
```

### Step 1: `fix(3)`
- Current logical at $3$: $0 \oplus 0 = 0$.
- Update physical: $\text{physical}[3] = 1 \oplus 0 = 1$.
- Update count: $\text{ones} = 0 + 1 = 1$.
- Logical state: `[0, 0, 0, 1, 0]`.

### Step 2: `fix(1)`
- Current logical at $1$: $0 \oplus 0 = 0$.
- Update physical: $\text{physical}[1] = 1 \oplus 0 = 1$.
- Update count: $\text{ones} = 1 + 1 = 2$.
- Logical state: `[0, 1, 0, 1, 0]`.

### Step 3: `flip()`
- Toggle parity flag: $\text{flipped} \leftarrow 1$.
- Update count: $\text{ones} = 5 - 2 = 3$.
- Physical state: `[0, 1, 0, 1, 0]`.
- Logical state: `[1, 0, 1, 0, 1]` (evaluated via $\text{physical} \oplus 1$).

### Step 4: `all()`
- Check $\text{ones} == 5 \implies 3 == 5$ is **false**.
- Return: `false`.

### Step 5: `unfix(0)`
- Target: Set logical bit $0$ to $0$.
- Current logical at $0$: $\text{physical}[0] \oplus \text{flipped} = 0 \oplus 1 = 1$.
- Needs change: Yes.
- New physical: $\text{physical}[0] = 0 \oplus 1 = 1$.
- Update count: $\text{ones} = 3 - 1 = 2$.
- Physical state: `[1, 1, 0, 1, 0]`.
- Logical state: `[0, 0, 1, 0, 1]` ($\text{physical} \oplus 1$).

### Step 6: `flip()`
- Toggle parity flag: $\text{flipped} \leftarrow 0$.
- Update count: $\text{ones} = 5 - 2 = 3$.
- Physical state: `[1, 1, 0, 1, 0]`.
- Logical state: `[1, 1, 0, 1, 0]` ($\text{physical} \oplus 0$).

### Step 7: `one()`
- Check $\text{ones} > 0 \implies 3 > 0$ is **true**.
- Return: `true`.

### Step 8: `unfix(0)`
- Target: Set logical bit $0$ to $0$.
- Current logical at $0$: $\text{physical}[0] \oplus \text{flipped} = 1 \oplus 0 = 1$.
- Needs change: Yes.
- New physical: $\text{physical}[0] = 0 \oplus 0 = 0$.
- Update count: $\text{ones} = 3 - 1 = 2$.
- Physical state: `[0, 1, 0, 1, 0]`.
- Logical state: `[0, 1, 0, 1, 0]`.

### Step 9: `count()`
- Return: $\text{ones} = 2$.

### Step 10: `toString()`
- Iterate $i = 0 \dots 4$:
  - $i=0: 0 \oplus 0 = \text{'0'}$
  - $i=1: 1 \oplus 0 = \text{'1'}$
  - $i=2: 0 \oplus 0 = \text{'0'}$
  - $i=3: 1 \oplus 0 = \text{'1'}$
  - $i=4: 0 \oplus 0 = \text{'0'}$
- Result: `"01010"`.

---

## 4. Comprehensive State Trace

The table below catalogs every operation in the sequence, detailing internal state evolution and method outputs:

| Call # | Method Call | Argument | `flipped` Flag | Physical Array | Logical Array State | `ones` Count | Return Value |
|---|---|---|---|---|---|---|---|
| 0 | `Bitset` | `size = 5` | $0$ | `[0, 0, 0, 0, 0]` | `00000` | $0$ | `null` |
| 1 | `fix` | `idx = 3` | $0$ | `[0, 0, 0, 1, 0]` | `00010` | $1$ | `null` |
| 2 | `fix` | `idx = 1` | $0$ | `[0, 1, 0, 1, 0]` | `01010` | $2$ | `null` |
| 3 | `flip` | - | **1** | `[0, 1, 0, 1, 0]` | `10101` | $3$ | `null` |
| 4 | `all` | - | $1$ | `[0, 1, 0, 1, 0]` | `10101` | $3$ | **false** |
| 5 | `unfix` | `idx = 0` | $1$ | `[1, 1, 0, 1, 0]` | `00101` | $2$ | `null` |
| 6 | `flip` | - | **0** | `[1, 1, 0, 1, 0]` | `11010` | $3$ | `null` |
| 7 | `one` | - | $0$ | `[1, 1, 0, 1, 0]` | `11010` | $3$ | **true** |
| 8 | `unfix` | `idx = 0` | $0$ | `[0, 1, 0, 1, 0]` | `01010` | $2$ | `null` |
| 9 | `count` | - | $0$ | `[0, 1, 0, 1, 0]` | `01010` | $2$ | **2** |
| 10 | `toString` | - | $0$ | `[0, 1, 0, 1, 0]` | `01010` | $2$ | **"01010"** |

---

## 5. Algorithmic Correctness & Soundness

### Mathematical Invertibility
The mapping $f(b) = b \oplus \text{flipped}$ is an involution on $\mathbb{F}_2$: applying it twice restores the original value ($f(f(b)) = b \oplus \text{flipped} \oplus \text{flipped} = b$).
- When $\text{flipped}$ toggles, every logical bit inverts simultaneously.
- When an individual bit is modified, setting physical bit to $\text{target} \oplus \text{flipped}$ ensures that when queried via $\text{physical} \oplus \text{flipped}$, the result simplifies to $\text{target} \oplus \text{flipped} \oplus \text{flipped} = \text{target}$.
- Running count $\text{ones}$ tracks the exact number of logical ones, guaranteeing that `all()`, `one()`, and `count()` return strictly accurate answers at all times.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Size 1 Bitset:** `size = 1`. `flip()` inverts the single bit; `all()` and `one()` return identical booleans.
2. **Repeated Idempotent Operations:** Calling `fix(2)` when bit $2$ is already $1$ checks $v = 1$, performs zero writes, and does not increment `ones`.
3. **Flips on Completely Set Bitsets:** If `ones = size`, `flip()` correctly sets `ones = 0`.
4. **Consecutive Flips:** Calling `flip()` twice toggles `flipped` twice, returning the system to its exact initial state with zero overhead.

### Common Anti-Patterns
- **Eager Flipping ($O(\text{size})$ per flip):** Iterating through all $10^5$ elements on each `flip()` takes $10^{10}$ operations across $10^5$ calls, exceeding the 2-second time limit.
- **Bit-by-Bit Counting:** Recomputing `count()` by looping over the array on demand turns an $O(1)$ query into an $O(\text{size})$ operation.
- **Forgetting Parity on Writes:** Writing `physical[idx] = 1` directly during `fix()` while `flipped = 1` sets the logical bit to $1 \oplus 1 = 0$, corrupting the state.

---

## 7. Complexity Analysis

### Time Complexity
- `Bitset(size)`: Initializes an array of size $N$ in $O(N)$ time.
- `fix(idx)`: $O(1)$ time (single array read/write, bitwise XOR, scalar increment).
- `unfix(idx)`: $O(1)$ time (single array read/write, bitwise XOR, scalar decrement).
- `flip()`: $O(1)$ time (scalar negation and subtraction).
- `all()`: $O(1)$ time (integer equality comparison).
- `one()`: $O(1)$ time (integer inequality comparison).
- `count()`: $O(1)$ time (integer return).
- `toString()`: $O(N)$ time (called at most 5 times, total work $O(5N)$).
- Across $Q = 10^5$ operations, total execution time is strictly $O(N + Q)$, running in under $25$ milliseconds.

### Auxiliary Space Complexity
- A single integer or boolean array of length $N = \text{size}$.
- Two scalar tracking variables (`flipped` and `ones`).
- Total auxiliary space complexity is $O(N)$.
