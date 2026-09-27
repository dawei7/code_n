# Guided Example: Unique Substrings in Wraparound String

We trace the step-by-step alphabet cyclic transition check ($(ord(c) - ord(prev)) \pmod{26} == 1$), consecutive run-length expansion ($k$), end-character maximal substring aggregation ($f[c] = \max(f[c], k)$), and disjoint partition summation on representative string instances:

- **Input:** $s = \text{"zab"}$
- **Required output:** `6`
  - The infinite wraparound string is `"abcdefghijklmnopqrstuvwxyz..."` wrapping cyclically from `'z'` to `'a'`.
  - We must count all unique non-empty substrings of $s$ that appear in the wraparound sequence.
  - Substring partition by ending character:
    - Substrings ending with `'z'`: `["z"]` (Length 1)
    - Substrings ending with `'a'`: `["a", "za"]` (Lengths 1 and 2)
    - Substrings ending with `'b'`: `["b", "ab", "zab"]` (Lengths 1, 2, and 3)
    - Total unique substrings: $1 + 2 + 3 = \mathbf{6}$
- **Dynamic programming execution trace:**
  - Let $f[c]$ store the maximum contiguous valid run length ending with character $c$.
  - Initialize: $k = 0, \; f = \{\}$
  - **Step 1 ($i = 0, c = \text{'z'}$):**
    - First character: $k = 1$
    - Update: $f[\text{'z'}] = \max(0, 1) = \mathbf{1}$
  - **Step 2 ($i = 1, c = \text{'a'}$):**
    - Transition test:
      $$
      (ord(\text{'a'}) - ord(\text{'z'})) \pmod{26} = (0 - 25) \pmod{26} = -25 \equiv 1 \pmod{26} \quad (\mathbf{Wrap\ Around!})
      $$
    - Alphabet continues cyclically! Extend run length: $k \leftarrow 1 + 1 = 2$.
    - Run `"za"` ends at `'a'`. It covers $2$ unique substrings: `"a"` and `"za"`.
    - Update: $f[\text{'a'}] = \max(0, 2) = \mathbf{2}$
  - **Step 3 ($i = 2, c = \text{'b'}$):**
    - Transition test:
      $$
      (ord(\text{'b'}) - ord(\text{'a'})) \pmod{26} = (1 - 0) \equiv 1 \pmod{26} \quad (\mathbf{Valid!})
      $$
    - Consecutive sequence extends! $k \leftarrow 2 + 1 = 3$.
    - Run `"zab"` ends at `'b'`. It covers $3$ unique substrings: `"b"`, `"ab"`, and `"zab"`.
    - Update: $f[\text{'b'}] = \max(0, 3) = \mathbf{3}$
  - Sum over all 26 character buckets:
    $$
    \sum f[c] = f[\text{'z'}] + f[\text{'a'}] + f[\text{'b'}] = 1 + 2 + 3 = \mathbf{6}
    $$
- **Broken Run Instance:** $s = \text{"cac"}$
  - Index 0 (`'c'`): $k = 1 \implies f[\text{'c'}] = 1$
  - Index 1 (`'a'`): broken run $\implies k = 1 \implies f[\text{'a'}] = 1$
  - Index 2 (`'c'`): broken run $\implies k = 1 \implies f[\text{'c'}] = \max(1, 1) = 1$
  - Total: $f[\text{'a'}] + f[\text{'c'}] = 1 + 1 = \mathbf{2}$ (`"a"` and `"c"`)
- **Single Character Instance:** $s = \text{"a"} \implies f[\text{'a'}] = 1 \implies \mathbf{1}$

This instance demonstrates end-character equivalence classes for substring counting, mathematically proves why tracking the maximum contiguous run length per ending character completely avoids duplicate substring counting, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"zab"}$:
Consider the infinite cyclic string $base = \text{"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz..."}$.
Count the number of **unique non-empty substrings** of $s$ that are present in $base$.

```text
Wraparound Sequence: ... y -> z -> a -> b -> c ...

Input String s: "zab"
Contiguous Substring Runs:
  - "z":   valid run of length 1 ending at 'z'
  - "za":  valid run of length 2 ending at 'a' (wraps from 'z' to 'a')
  - "zab": valid run of length 3 ending at 'b'

Unique Valid Substrings Generated:
  Ending with 'z': "z"                (1 substring)
  Ending with 'a': "a", "za"          (2 substrings)
  Ending with 'b': "b", "ab", "zab"   (3 substrings)

Total Count: 1 + 2 + 3 = 6
```

### The End-Character Deduplication Principle
A naive approach generating all substrings and storing them in a hash set takes $O(N^2)$ memory and time, which exceeds limits for $|s| = 10^5$.
However, note the structural properties of $base$:
- A substring is valid if and only if every adjacent pair $(c_{i-1}, c_i)$ satisfies:
  $$
  (ord(c_i) - ord(c_{i-1})) \pmod{26} == 1
  $$
- In $base$, any valid substring is **uniquely and completely determined by its ending character and its length**!
  For example, a valid substring of length 3 ending with `'d'` can *only* be `"bcd"`.
- Therefore, if the longest valid run in $s$ that ends with character $c$ has length $L$:
  - It automatically generates valid substrings of length $1, 2, \dots, L$, all ending with $c$.
  - Any shorter valid run ending with $c$ will only generate substrings of length $\le L$, which are already included!
- Thus, the number of unique valid substrings ending with character $c$ is **exactly the maximum run length ending with $c$**.
- Because substrings ending with different characters are disjoint, summing these maximums over all 26 letters yields the exact total unique count with zero duplicate counting!

---

## 2. Conceptual Foundation & Invariants

### 1. Alphabet Continuity Condition:
Two consecutive characters $s[i-1]$ and $s[i]$ are adjacent in the wraparound alphabet if:
$$
(ord(s[i]) - ord(s[i - 1])) \pmod{26} == 1
$$
- If True: the current consecutive run continues: $k \leftarrow k + 1$.
- If False: the current run breaks: reset $k \leftarrow 1$.

### 2. The Maximal Run Invariant:
Maintain an array $f[0 \dots 25]$:
$$
f[c] = \max(f[c], \; k)
$$
At the end of scanning $s$:
$$
\text{Total Unique Substrings} = \sum_{c = \text{'a'}}^{\text{'z'}} f[c]
$$

> **Disjoint Union Theorem.** Every valid substring belongs to exactly one equivalence class defined by its terminal character. Within the class for character $c$, the set of valid lengths is the contiguous range $\{1, 2, \dots, f[c]\}$, yielding exactly $f[c]$ unique substrings.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"zab"}$ ($N = 3$):
Initialize $f = \{c: 0 \text{ for } c \in \text{'a'} \dots \text{'z'}\}, \; k = 0$.

---

### Step 1: Process $s[0] = \text{'z'}$
- Index $i = 0$: Start of string.
- Set run length: $k = 1$.
- Update terminal character `'z'`:
  $$
  f[\text{'z'}] = \max(0, 1) = \mathbf{1}
  $$

---

### Step 2: Process $s[1] = \text{'a'}$
- Compare with $s[0] = \text{'z'}$:
  $$
  (ord(\text{'a'}) - ord(\text{'z'})) \pmod{26} = (97 - 122) \pmod{26} = -25 \equiv 1 \pmod{26}
  $$
- The wraparound condition holds!
- Extend run length:
  $$
  k \leftarrow 1 + 1 = \mathbf{2}
  $$
- Update terminal character `'a'`:
  $$
  f[\text{'a'}] = \max(0, 2) = \mathbf{2}
  $$
  (Accounted substrings: `"a"` and `"za"`).

---

### Step 3: Process $s[2] = \text{'b'}$
- Compare with $s[1] = \text{'a'}$:
  $$
  (ord(\text{'b'}) - ord(\text{'a'})) \pmod{26} = (98 - 97) = 1 \pmod{26}
  $$
- The alphabetical step holds!
- Extend run length:
  $$
  k \leftarrow 2 + 1 = \mathbf{3}
  $$
- Update terminal character `'b'`:
  $$
  f[\text{'b'}] = \max(0, 3) = \mathbf{3}
  $$
  (Accounted substrings: `"b"`, `"ab"`, `"zab"`).

---

### Step 4: Summation Across All 26 Letters
- $f[\text{'a'}] = 2$
- $f[\text{'b'}] = 3$
- $f[\text{'z'}] = 1$
- All other letters: $0$.
Total:
$$
2 + 3 + 1 = \mathbf{6}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Character $s[i]$ | Previous $s[i-1]$ | Cyclic Step $\Delta \pmod{26}$ | Consecutive Run $k$ | Table Update $f[s[i]]$ | Substrings Captured |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$0$** | `'z'` | None | — | $1$ | $f[\text{'z'}] \leftarrow 1$ | `"z"` |
| **$1$** | `'a'` | `'z'` | $-25 \equiv \mathbf{1}$ | $2$ | $f[\text{'a'}] \leftarrow 2$ | `"a"`, `"za"` |
| **$2$** | `'b'` | `'a'` | $1 \equiv \mathbf{1}$ | $3$ | $f[\text{'b'}] \leftarrow 3$ | `"b"`, `"ab"`, `"zab"` |
| **Sum** | — | — | — | — | $\sum f$ | **Result: $6$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Letter Repeated ($s = \text{"aaaa"}):$**
  - $i=0: k=1, f['a']=1$.
  - $i=1$: $(ord('a') - ord('a')) \pmod{26} = 0 \ne 1$. Run breaks: $k=1$.
  - $f['a'] = \max(1, 1) = 1$. Total count is $\mathbf{1}$ (only `"a"` is unique).
- **Broken Run with Duplicate ($s = \text{"cac"}):$** $f['a']=1, f['c']=1 \implies \mathbf{2}$.
- **Full Alphabet In Order ($s = \text{"abcdefghijklmnopqrstuvwxyz"}):$** $k$ grows from 1 to 26.
  - $f = \{'a': 1, 'b': 2, \dots, 'z': 26\}$.
  - Total: $\frac{26 \times 27}{2} = \mathbf{351}$.

---

## 6. Traps & Common Anti-Patterns

- **Using a Set of Strings ($O(N^2)$ Memory):** Storing all substrings in a hash set causes Out-of-Memory on strings of length $10^5$. Deduplicating by maximum length per ending character reduces storage to 26 integers.
- **Missing the Modulo Wraparound:** Writing `ord(c) - ord(prev) == 1` fails to detect the wrap from `'z'` to `'a'` ($'a' - 'z' = -25$). Using `% 26 == 1` handles both normal transitions and cyclic wraps seamlessly.
- **Overwriting Instead of Maximizing:** Setting $f[c] = k$ instead of $f[c] = \max(f[c], k)$ forgets longer substrings encountered earlier in the string when a shorter instance of the same letter appears later.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single pass iterates through the string of length $N$.
  - Each character performs $O(1)$ arithmetic comparisons and array updates.
  - Summing the 26 table entries takes $O(26) = O(1)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, executes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|) = \mathcal{O}(1)$ space to store the fixed 26-element array $f$.