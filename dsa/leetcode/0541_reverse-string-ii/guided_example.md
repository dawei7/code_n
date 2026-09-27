# Guided Example: Reverse String II

We trace the step-by-step block-stride partitioning ($step = 2k$), prefix window reversal ($[i, i+k]$), suffix window preservation ($[i+k, i+2k]$), boundary tail clamping ($\min(i+k, n)$), and in-place character manipulation on representative strings:

- **Input:** $s = \text{"abcdefg"}, \quad k = 2$
- **Required output:** `"bacdfeg"`
  - Block period: $2k = 2 \times 2 = \mathbf{4}$ characters.
  - Window rule:
    - In every block of length $2k$, reverse the **first $k$** characters.
    - Leave the **next $k$** characters in their original order.
    - If fewer than $k$ characters remain at the end, reverse all of them.
    - If between $k$ and $2k$ characters remain, reverse the first $k$ characters and leave the rest untouched.
- **Stepping Loop execution trace:**
  - Convert string to character sequence:
    $$
    cs = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'d'}, \text{'e'}, \text{'f'}, \text{'g'}] \quad (n = 7)
    $$
  - Stride by $2k = 4$: loop indices $i \in \{0, 4\}$.
  - **Block 1 ($i = 0$):**
    - Span: characters from index $0$ to $3$ (`['a', 'b', 'c', 'd']`).
    - Sub-segment to reverse:
      $$
      [i, \; i + k] = [0, \; 2] \implies [\text{'a'}, \text{'b'}]
      $$
    - Invert sub-segment:
      $$
      [\text{'a'}, \text{'b'}] \to [\mathbf{\text{'b'}}, \mathbf{\text{'a'}}]
      $$
    - Untouched sub-segment:
      $$
      [2, \; 4] \implies [\text{'c'}, \text{'d'}] \quad \text{(Preserved)}
      $$
    - Array state:
      $$
      cs = [\mathbf{\text{'b'}}, \mathbf{\text{'a'}}, \text{'c'}, \text{'d'}, \text{'e'}, \text{'f'}, \text{'g'}]
      $$
  - **Block 2 ($i = 4$):**
    - Span: characters from index $4$ to end ($n = 7$).
    - Remaining characters: $7 - 4 = 3$ characters (`['e', 'f', 'g']`).
    - Since $3 \ge k (2)$, reverse the first $k = 2$ characters:
      $$
      [i, \; i + k] = [4, \; 6] \implies [\text{'e'}, \text{'f'}]
      $$
    - Invert sub-segment:
      $$
      [\text{'e'}, \text{'f'}] \to [\mathbf{\text{'f'}}, \mathbf{\text{'e'}}]
      $$
    - Untouched tail:
      $$
      [6, \; 7] \implies [\text{'g'}] \quad \text{(Preserved)}
      $$
    - Array state:
      $$
      cs = [\text{'b'}, \text{'a'}, \text{'c'}, \text{'d'}, \mathbf{\text{'f'}}, \mathbf{\text{'e'}}, \text{'g'}]
      $$
  - Stride exhausted ($i = 8 \ge 7$).
  - Reassemble string:
    $$
    \mathbf{\text{"bacdfeg"}}
    $$
- **Exact Single Block Instance ($s = \text{"abcd"}, k = 2$):**
  - Block $i = 0$: reverses `"ab"` $\to$ `"ba"`, leaves `"cd"` $\implies \mathbf{\text{"bacd"}}$.
- **Short Tail Fewer Than $k$ ($s = \text{"abcdefg"}, k = 8$):**
  - Entire string has $7 < 8$ characters $\implies$ reverse all $7$ characters $\implies \mathbf{\text{"gfedcba"}}$.
- **$k = 1$ Identity Instance:**
  - Reverses segments of length 1 $\implies$ no-op, returns original string.

This instance demonstrates periodic modular slicing and interval reflection, mathematically proves why advancing by $2k$ decouples independent reversal windows, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"abcdefg"}$ and an integer $k = 2$:
Reverse the first $k$ characters for every $2k$ characters counting from the start.
- If fewer than $k$ characters remain, reverse all of them.
- If between $k$ and $2k$ characters remain, reverse the first $k$ and leave the rest unchanged.

```text
Full String:  a  b  c  d  e  f  g   (Length = 7, k = 2)

Blocks of 2k = 4:
  Block 0 (0..3): [a  b]  c  d   -> Reverse [a, b] -> [b, a, c, d]
  Block 1 (4..6): [e  f]  g       -> Reverse [e, f] -> [f, e, g]

Result: "bacdfeg"
```

### Stride Decoupling
- By looping with step size $2k$:
  $$
  i = 0, \ 2k, \ 4k, \ 6k, \ \dots
  $$
- Each block begins at index $i$.
- The prefix to reverse is simply the slice:
  $$
  [i, \; \min(i + k, n)]
  $$
- Python slice bounds automatically clamp to $n$ if $i + k > n$, naturally handling the tail cases with zero special conditional branches!

---

## 2. Conceptual Foundation & Invariants

### 1. In-Place Array Reversal:
- Convert string $s$ into a mutable array of characters $cs$.
- For each step $i \in [0, |cs|)$ with step $2k$:
  $$
  cs[i : i + k] \leftarrow \text{reversed}(cs[i : i + k])
  $$
- Rejoin characters: `"".join(cs)`.

### 2. Tail Rules Unified:
1. If $n - i < k$:
   The slice $[i : i + k]$ spans from $i$ to $n$, reversing all remaining characters.
2. If $k \le n - i < 2k$:
   The slice $[i : i + k]$ reverses exactly the first $k$ characters; the remaining characters up to $n$ are untouched.
3. If $n - i \ge 2k$:
   The slice reverses the first $k$ characters; the next $k$ characters are skipped by the $+2k$ loop step.

> **Periodic Invariant.** Stepping by $2k$ ensures that each reversal operation is non-overlapping and strictly localized to the interval $[i, i+k)$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abcdefg"}$ ($n = 7, k = 2$):

---

### Step 1: Initialize
- $cs = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'d'}, \text{'e'}, \text{'f'}, \text{'g'}]$
- Stride: $2k = 4$.

---

### Step 2: First Block ($i = 0$)
- Slice to reverse: $[0 : 2] = [\text{'a'}, \text{'b'}]$.
- Reversed: $[\text{'b'}, \text{'a'}]$.
- Array state:
  $$
  [\mathbf{\text{'b'}}, \mathbf{\text{'a'}}, \text{'c'}, \text{'d'}, \text{'e'}, \text{'f'}, \text{'g'}]
  $$

---

### Step 3: Second Block ($i = 4$)
- Slice to reverse: $[4 : 6] = [\text{'e'}, \text{'f'}]$.
- Reversed: $[\text{'f'}, \text{'e'}]$.
- Array state:
  $$
  [\text{'b'}, \text{'a'}, \text{'c'}, \text{'d'}, \mathbf{\text{'f'}}, \mathbf{\text{'e'}}, \text{'g'}]
  $$

---

### Step 4: Advance Stride
- $i \leftarrow 4 + 4 = 8 \ge 7$. Loop finishes.

---

### Step 5: String Reconstruction
$$
\mathbf{\text{"bacdfeg"}}
$$

---

## 4. Complete Execution Trace

| Block Index $i$ | Block Span | Target Slice $[i : i+k]$ | Substring Reversed | Untouched Suffix | Cumulative Result |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $[0, 3]$ | $[0, 2]$ | `"ab" \to \text{"ba"}` | `"cd"` | `"bacdefg"` |
| **$4$** | $[4, 6]$ | $[4, 6]$ | `"ef" \to \text{"fe"}` | `"g"` | **`"bacdfeg"`** |
| **Done** | — | — | — | — | **`"bacdfeg"`** |

---

## 5. Boundary Cases & Failure Modes

- **$k \ge n$:** The entire string has length $\le k \implies$ entire string is reversed (e.g. `"abcdefg"`, $k=8 \implies$ `"gfedcba"`).
- **$k = 1$:** Every block of 2 reverses 1 character $\implies$ no character changes position $\implies$ identical string.
- **Exact Multiple of $2k$ ($n = 4, k = 2$):** Exactly one block $\implies$ `"bacd"`.
- **Exact Multiple of $2k$ Plus $k$ ($n = 6, k = 2$):** Block 0 reverses $[0, 2]$, block 4 reverses $[4, 6]$, tail has 0 elements.

---

## 6. Traps & Common Anti-Patterns

- **Multiple `if-else` Case Splits:** Writing separate logic for $remaining < k$, $k \le remaining < 2k$, etc., introduces off-by-one errors. A single loop with step $2k$ and slice $[i : i + k]$ handles all cases automatically.
- **Iterating Character-by-Character with State Flags:** Maintaining alternating boolean flags and temporary buffers complicates an operation that is inherently block-based.
- **Repeated String Concatenation in Loop:** Building strings using `s += ...` takes $O(N^2)$ due to immutable string reallocations. Converting to a list and joining at the end runs in linear $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Converting the string to a list takes $O(N)$ time.
  - Slicing and reversing $k$ characters every $2k$ elements visits each character at most once: $O(N)$.
  - Joining characters back into a string takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the mutable character list $cs$.
