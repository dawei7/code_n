# Guided Example: Design Compressed String Iterator

We trace the step-by-step run-length token serialization (`[char, count]`), multi-digit integer parsing ($x \leftarrow x \cdot 10 + d$), active token index tracking ($p$), decrement-and-advance lazy character streaming (`next()`), exhaustion predicate verification (`hasNext()`), and empty fallback space emission (`' '`) on representative compressed strings:

- **Input:**
  - Compressed string: `"L1e2t1C1o1d1e1"`
  - Operation sequence:
    ```text
    StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1")
    iterator.next()     // returns 'L'
    iterator.next()     // returns 'e'
    iterator.next()     // returns 'e'
    iterator.next()     // returns 't'
    iterator.next()     // returns 'C'
    iterator.next()     // returns 'o'
    iterator.hasNext()  // returns true
    iterator.next()     // returns 'd'
    iterator.hasNext()  // returns true
    ```
- **Required outputs:**
  - `'L'`, `'e'`, `'e'`, `'t'`, `'C'`, `'o'`, `true`, `'d'`, `true`
  - Uncompressed reference string: `"LeetCode"`
  - Behavior contract:
    - `next()`: Yields the next character in sequence. If all characters have been consumed, returns a single space `' '`.
    - `hasNext()`: Returns `true` if unread characters remain; `false` otherwise.
- **Run-Length Token Architecture:**
  - Decompressing the entire string into memory up front can cause Out-Of-Memory (OOM) errors if a count is huge (e.g. `"a1000000000"`).
  - Instead, the iterator operates **lazily** over parsed run-length tokens:
    $$
    d = [[c_1, k_1], \; [c_2, k_2], \; \dots, \; [c_m, k_m]]
    $$
  - Pointer $p$: Points to the active token currently being consumed ($p \in [0, m - 1]$).
  - Token state: `[char, remaining_count]`.
  - When `next()` is called:
    - Decrement `remaining_count` by $1$.
    - When `remaining_count` hits $0$, advance pointer $p \leftarrow p + 1$.
- **Step-by-Step Construction & Streaming Trace:**
  - **Phase 1: Parse Compressed String into Tokens:**
    - Input: `"L1e2t1C1o1d1e1"`.
    - Token 0: character `'L'`, digits `"1"` $\implies ['L', 1]$
    - Token 1: character `'e'`, digits `"2"` $\implies ['e', 2]$
    - Token 2: character `'t'`, digits `"1"` $\implies ['t', 1]$
    - Token 3: character `'C'`, digits `"1"` $\implies ['C', 1]$
    - Token 4: character `'o'`, digits `"1"` $\implies ['o', 1]$
    - Token 5: character `'d'`, digits `"1"` $\implies ['d', 1]$
    - Token 6: character `'e'`, digits `"1"` $\implies ['e', 1]$
    - Initial token list:
      $$
      d = [[\text{'L'}, 1], \; [\text{'e'}, 2], \; [\text{'t'}, 1], \; [\text{'C'}, 1], \; [\text{'o'}, 1], \; [\text{'d'}, 1], \; [\text{'e'}, 1]]
      $$
    - Active pointer: $p = 0$.
  - **Phase 2: Step-by-Step Iterator Calls:**
    - **Call 1: `next()`:**
      - $p = 0$: Current token is `['L', 1]`.
      - Character to return: `'L'`.
      - Decrement count: $1 - 1 = 0$.
      - Count reached 0 $\implies$ Advance pointer: $p \leftarrow 1$.
      - Returns: **`'L'`**.
    - **Call 2: `next()`:**
      - $p = 1$: Current token is `['e', 2]`.
      - Character to return: `'e'`.
      - Decrement count: $2 - 1 = \mathbf{1}$.
      - Count is $1 > 0 \implies$ Pointer stays at $p = 1$.
      - Returns: **`'e'`**.
    - **Call 3: `next()`:**
      - $p = 1$: Current token is `['e', 1]`.
      - Character to return: `'e'`.
      - Decrement count: $1 - 1 = 0$.
      - Count reached 0 $\implies$ Advance pointer: $p \leftarrow 2$.
      - Returns: **`'e'`**.
    - **Call 4: `next()`:**
      - $p = 2$: Current token is `['t', 1]`.
      - Returns: **`'t'`**, advances $p \leftarrow 3$.
    - **Call 5: `next()`:**
      - $p = 3$: Current token is `['C', 1]`.
      - Returns: **`'C'`**, advances $p \leftarrow 4$.
    - **Call 6: `next()`:**
      - $p = 4$: Current token is `['o', 1]`.
      - Returns: **`'o'`**, advances $p \leftarrow 5$.
    - **Call 7: `hasNext()`:**
      - Check condition: $p = 5 < \text{len}(d) = 7$ and $d[5][1] = 1 > 0$.
      - Tokens 5 (`'d'`) and 6 (`'e'`) remain unconsumed.
      - Returns: **`true`**.
    - **Call 8: `next()`:**
      - $p = 5$: Current token is `['d', 1]`.
      - Returns: **`'d'`**, advances $p \leftarrow 6$.
    - **Call 9: `hasNext()`:**
      - $p = 6 < 7$ and $d[6][1] = 1 > 0$.
      - Token 6 (`'e'`) remains unconsumed.
      - Returns: **`true`**.
- **Post-Exhaustion Space Return Instance:**
  - After consuming the final `'e'` from token 6, $p$ advances to $7 == \text{len}(d)$.
  - `hasNext()` returns `false`.
  - Any subsequent call to `next()` returns `' '` (single space character).
- **Multi-Digit Repetition Count (`"a12b1"`):**
  - Digits `'1'` and `'2'` accumulate: $1 \times 10 + 2 = 12$.
  - First token is `['a', 12]`, which yields `'a'` for twelve consecutive `next()` calls before advancing to `'b'`.

This instance demonstrates stateful run-length decompression streaming via pointer-index token consumption, mathematically proves why lazy evaluation achieves $O(1)$ amortized runtime while bounding memory to token count, and derives $O(T)$ construction time and $O(1)$ per-call bounds.

---

## 1. Instance & Teaching Goal

Given a compressed string like `"L1e2t1C1o1d1e1"` representing `"LeetCode"`:
Design an iterator supporting:
- `next()`: Returns the next character, or `' '` if finished.
- `hasNext()`: Returns whether characters remain.

```text
Input: "L1e2t1C1o1d1e1"
Tokens:
  [L: 1] -> yield 'L'
  [e: 2] -> yield 'e', then 'e'
  [t: 1] -> yield 't'
  [C: 1] -> yield 'C'
  [o: 1] -> yield 'o'
  [d: 1] -> yield 'd'
  [e: 1] -> yield 'e'

Output: L -> e -> e -> t -> C -> o -> d -> e -> ' ' (exhausted)
```

### The Invariant of Lazy Expansion
- A compressed string like `"a1000000000"` represents 1 billion characters.
- Expanding the full string into memory will crash with Out Of Memory.
- Instead, store only the **run-length metadata** (character and integer count).
- The iterator decrements the active integer count in $O(1)$ time without materializing any extra characters.

---

## 2. Conceptual Foundation & Invariants

### 1. Token Construction:
Scan the string to parse `(char, integer)` pairs:
- Character $c$ followed by digits parsed via $x = x \cdot 10 + \text{digit}$.
- Stored as `[c, x]` in token array $d$.

### 2. The Iterator Invariant:
- Pointer $p$ always points to the first token that has `remaining_count > 0`.
- `hasNext()` is true if and only if $p < |d|$.
- `next()`:
  - If $p \ge |d|$: return `' '`.
  - Decrement count: $d[p][1] \leftarrow d[p][1] - 1$.
  - If count reaches 0: advance $p \leftarrow p + 1$.
  - Return the character $d[p_{old}][0]$.

> **Zero Inflation Invariant.** The memory footprint remains bounded by the compressed token count $O(T)$ regardless of the decompressed string length $\sum k_i$.

---

## 3. Step-by-Step Worked Execution

We trace `"L1e2"`:

---

### Step 1: Parse Tokens
- Token 0: `['L', 1]`
- Token 1: `['e', 2]`
- $p = 0$.

---

### Step 2: First `next()`
- $p = 0$, char `'L'`, count $1 - 1 = 0$.
- Count is 0 $\implies p \leftarrow 1$.
- Return `'L'`.

---

### Step 3: Second `next()`
- $p = 1$, char `'e'`, count $2 - 1 = 1$.
- Count is $1 > 0 \implies p$ remains 1.
- Return `'e'`.

---

### Step 4: Third `next()`
- $p = 1$, char `'e'`, count $1 - 1 = 0$.
- Count is 0 $\implies p \leftarrow 2$.
- Return `'e'`.

---

### Step 5: `hasNext()` and Fourth `next()`
- $p = 2 == \text{len}(d) \implies hasNext() = \mathbf{False}$.
- `next()` returns `' '`.

---

## 4. Complete Execution Trace

| Call | Active $p$ | Active Token | Remaining Count Before | Action Taken | Remaining Count After | Return Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `next()` | $0$ | `['L', 1]` | $1$ | Decrement, advance $p$ | $0$ | **`'L'`** |
| `next()` | $1$ | `['e', 2]` | $2$ | Decrement, keep $p=1$ | $1$ | **`'e'`** |
| `next()` | $1$ | `['e', 1]` | $1$ | Decrement, advance $p$ | $0$ | **`'e'`** |
| `next()` | $2$ | `['t', 1]` | $1$ | Decrement, advance $p$ | $0$ | **`'t'`** |
| `hasNext()`| $3$ | `['C', 1]` | $1$ | Check $p < 7$ | $1$ | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Multi-Digit Numbers (`"a10b2"`):** Number parser correctly reads $10$.
- **Repeated Calls After Exhaustion:** Safely returns `' '` repeatedly without index-out-of-bounds error.
- **Single Character (`"x1"`):** Handled identically.
- **Large Counts ($10^9$):** Uses 64-bit integer counts in $O(1)$ space.

---

## 6. Traps & Common Anti-Patterns

- **Materializing the Decompressed String:** Building the uncompressed string as a string or list causes Memory Limit Exceeded on large test cases.
- **Assuming Counts Are Single Digits:** Scanning only one character after the letter breaks on counts like `"a12"`. A `while isdigit()` loop is required to parse multi-digit counts.
- **Off-by-One Pointer Advance:** Advancing $p$ before checking count 0 can skip the final repetition of a character.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Constructor: $\mathcal{O}(L)$ where $L$ is the length of the compressed string.
  - `next()`: $\mathcal{O}(1)$ amortized time.
  - `hasNext()`: $\mathcal{O}(1)$ strictly.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(T)$ space to store the $T$ tokens where $T \le L / 2$. Memory is completely independent of total uncompressed character counts.
