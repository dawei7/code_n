# Guided Example: Longest Substring with At Most Two Distinct Characters

We trace the step-by-step sliding window expansion, character frequency hash map tracking, and left boundary contraction on representative string instances:

- **Input:** $s = \text{"eceba"}$
- **Required output:** $3$ (Substring `"ece"` of length 3 contains 2 distinct characters: `'e'` and `'c'`)
- **Longer Plateau Instance:** $s = \text{"ccaabbb"} \implies 5$ (Substring `"aabbb"` contains distinct characters `'a'` and `'b'`)

This instance demonstrates two-pointer sliding window mechanics, managing a frequency dictionary with zero-count key deletion, contracting the left pointer $L$ when distinct character count exceeds 2, and achieving optimal $O(N)$ linear time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"eceba"}$, find the length of the longest substring that contains **at most two distinct characters**:
- Substrings of $s$:
  - `"ece"` (length 3, distinct characters: $\{\text{'e'}, \text{'c'}\}$) $\implies$ **Valid**.
  - `"eceb"` (length 4, distinct characters: $\{\text{'e'}, \text{'c'}, \text{'b'}\}$) $\implies$ Invalid ($3 > 2$).
  - `"ceba"` (length 4, distinct characters: $\{\text{'c'}, \text{'e'}, \text{'b'}, \text{'a'}\}$) $\implies$ Invalid ($4 > 2$).
  - `"ba"` (length 2, distinct characters: $\{\text{'b'}, \text{'a'}\}$) $\implies$ Valid.
The maximum valid length is $3$.

A brute-force search inspects all $\binom{N}{2}$ substrings, taking $O(N^2)$ time.
A dynamic sliding window $[L, R]$ expands $R$ to absorb new characters while keeping a hash map of character counts.
Whenever the number of unique keys in the hash map exceeds 2, we advance $L$ to evict characters until at least one distinct character's count drops to zero and its key is deleted.
Because both $L$ and $R$ only move forward, every character is processed at most twice, resulting in strictly $O(N)$ linear runtime.

---

## 2. Conceptual Foundation & Invariants

### Sliding Window Frequency Protocol
Maintain:
- $L = 0$: start index of the current candidate window.
- `counts = defaultdict(int)`: hash map tracking counts of characters currently inside $[L, R]$.
- $\text{max\_len} = 0$: maximum valid window length observed.

For each index $R$ from $0$ to $|s| - 1$:
1. **Window Expansion:**
   Incorporate $s[R]$ into the window:
   $$
   \text{counts}[s[R]] \leftarrow \text{counts}[s[R]] + 1
   $$
2. **Window Contraction on Infeasibility:**
   While the number of unique characters in the window exceeds 2:
   $$
   |\text{counts}| > 2
   $$
   - Decrement the count of character at left pointer:
     $$
     \text{counts}[s[L]] \leftarrow \text{counts}[s[L]] - 1
     $$
   - If count reaches zero, **delete the key from the dictionary**:
     $$
     \text{if } \text{counts}[s[L]] == 0: \quad \text{del } \text{counts}[s[L]]
     $$
   - Advance left pointer:
     $$
     L \leftarrow L + 1
     $$
3. **Record Valid Window Length:**
   $$
   \text{max\_len} \leftarrow \max(\text{max\_len}, \, R - L + 1)
   $$

> **Invariant.** At the end of every outer iteration $R$, the window $[L, R]$ contains at most two distinct characters, representing the longest valid substring ending at index $R$.

---

## 3. Step-by-Step Worked Execution

We trace the sliding window on $s = \text{"eceba"}$ ($N = 5$):

### Step 1: $R = 0, \, s[0] = \text{'e'}$
- `counts['e'] = 1`. Unique keys: $\{\text{'e'}\} \implies 1 \le 2$.
- Window $[0, 0]$: `"e"`.
- Length: $0 - 0 + 1 = 1$.
- $\text{max\_len} = \max(0, 1) = \mathbf{1}$.

---

### Step 2: $R = 1, \, s[1] = \text{'c'}$
- `counts['c'] = 1`. Unique keys: $\{\text{'e'}: 1, \text{'c'}: 1\} \implies 2 \le 2$.
- Window $[0, 1]$: `"ec"`.
- Length: $1 - 0 + 1 = 2$.
- $\text{max\_len} = \max(1, 2) = \mathbf{2}$.

---

### Step 3: $R = 2, \, s[2] = \text{'e'}$
- `counts['e'] = 2`. Unique keys: $\{\text{'e'}: 2, \text{'c'}: 1\} \implies 2 \le 2$.
- Window $[0, 2]$: `"ece"`.
- Length: $2 - 0 + 1 = 3$.
- $\text{max\_len} = \max(2, 3) = \mathbf{3}$.

---

### Step 4: $R = 3, \, s[3] = \text{'b'}$
- `counts['b'] = 1`.
- Unique keys: $\{\text{'e'}: 2, \text{'c'}: 1, \text{'b'}: 1\} \implies 3 > 2$ (**Violation!**).
- **Contract Left Boundary $L$:**
  - $L = 0, s[0] = \text{'e'}$: `counts['e'] = 2 - 1 = 1`. Advance $L \to 1$.
    Still 3 keys: $\{\text{'e'}: 1, \text{'c'}: 1, \text{'b'}: 1\}$.
  - $L = 1, s[1] = \text{'c'}$: `counts['c'] = 1 - 1 = 0`.
    Count reached zero $\implies$ **Delete `'c'`**!
    Remaining keys: $\{\text{'e'}: 1, \text{'b'}: 1\} \implies 2$ keys. Feasibility restored!
    Advance $L \to 2$.
- Window $[2, 3]$: `"eb"`.
- Length: $3 - 2 + 1 = 2$.
- $\text{max\_len} = \max(3, 2) = \mathbf{3}$.

---

### Step 5: $R = 4, \, s[4] = \text{'a'}$
- `counts['a'] = 1`.
- Unique keys: $\{\text{'e'}: 1, \text{'b'}: 1, \text{'a'}: 1\} \implies 3 > 2$ (**Violation!**).
- **Contract Left Boundary $L$:**
  - $L = 2, s[2] = \text{'e'}$: `counts['e'] = 1 - 1 = 0`.
    Count reached zero $\implies$ **Delete `'e'`**!
    Remaining keys: $\{\text{'b'}: 1, \text{'a'}: 1\} \implies 2$ keys. Feasibility restored!
    Advance $L \to 3$.
- Window $[3, 4]$: `"ba"`.
- Length: $4 - 3 + 1 = 2$.
- $\text{max\_len} = \max(3, 2) = \mathbf{3}$.

Scan complete. Global maximum valid substring length is $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
String:          e    c    e    b    a
Indices:         0    1    2    3    4
R=0: [L=0, R=0] "e"            len=1, max=1
R=1: [L=0, R=1] "ec"           len=2, max=2
R=2: [L=0, R=2] "ece"          len=3, max=3 (GLOBAL MAX)
R=3: [L=0..2, R=3] "eceb" -> 3 distinct! L moves to 2 -> "eb" len=2, max=3
R=4: [L=2..3, R=4] "eba"  -> 3 distinct! L moves to 3 -> "ba" len=2, max=3
```

| $R$ | Character $s[R]$ | Map Before Shrink | Condition ($\lvert \text{counts} \rvert > 2$) | $L$ Advance Steps | Map After Shrink | Window $[L, R]$ | Window Length | Cumulative $\text{max\_len}$ |
|:---:|:---:|:---|:---:|:---:|:---|:---:|:---:|:---:|
| 0 | `'e'` | `{'e': 1}` | $1 \le 2$ (No) | None ($L=0$) | `{'e': 1}` | $[0, 0]$ (`"e"`) | 1 | 1 |
| 1 | `'c'` | `{'e': 1, 'c': 1}` | $2 \le 2$ (No) | None ($L=0$) | `{'e': 1, 'c': 1}` | $[0, 1]$ (`"ec"`) | 2 | 2 |
| **2** | **`'e'`** | **`{'e': 2, 'c': 1}`** | **$2 \le 2$ (No)** | **None ($L=0$)** | **`{'e': 2, 'c': 1}`** | **$[0, 2]$ (`"ece"`)** | **3** | **3 (Max)** |
| 3 | `'b'` | `{'e': 2, 'c': 1, 'b': 1}` | $3 > 2$ (Yes) | $L: 0 \to 1 \to 2$ (del `'c'`) | `{'e': 1, 'b': 1}` | $[2, 3]$ (`"eb"`) | 2 | 3 |
| 4 | `'a'` | `{'e': 1, 'b': 1, 'a': 1}` | $3 > 2$ (Yes) | $L: 2 \to 3$ (del `'e'`) | `{'b': 1, 'a': 1}` | $[3, 4]$ (`"ba"`) | 2 | **3 (Final)** |

### Boundary Behaviour Across the Authored Instances

The authored inputs exercise every degenerate alphabet size, and each row answers the same question: which part of the loop decides the result?

| Boundary shape | Authored instance | Answer | Why the main loop produces it |
|:---|:---|:---:|:---|
| Single character | `"Z"` | 1 | the only window is $[0, 0]$ with one key, so no contraction is triggered |
| One distinct character | `"zzzz"` | 4 | the map never reaches three keys, the contraction body never executes, and the recorded length grows with $R$ up to $N$ |
| Exactly two distinct characters | `"abababa"` | 7 | alternating characters still occupy only two keys, so the window spans the whole string |
| Case-sensitive alphabet | `"aAab"` | 3 | `'a'` and `'A'` are separate keys, so appending `'b'` creates a third key and forces two evictions; the best window is `"aAa"` |
| Several evictions inside one contraction | `"abacccab"` | 5 | the final `'b'` creates the third key, and `L` must advance four positions before `'c'` leaves the map; the answer is the earlier window `"accca"` |
| Three long runs | 100,000 characters: 33,333 `'a'`, 33,334 `'b'`, 33,333 `'c'` | 66667 | a single contraction evicts the whole `'a'` run, after which the window covers all 66,667 characters of the `'b'` and `'c'` runs |

---

## 5. Algorithmic Correctness

**Soundness.** Every substring $[L, R]$ evaluated when recording `max_len` has $|\text{counts}| \le 2$, strictly adhering to the two-distinct-character restriction.

**Completeness.** For any fixed end position $R$, the length of the valid substring ending at $R$ decreases monotonically as $L$ increases. Thus, the minimum index $L$ such that $[L, R]$ contains at most 2 distinct characters identifies the uniquely longest valid substring ending at $R$. Since all $R \in [0, N-1]$ are considered, the global maximum cannot be missed.

---

## 6. Traps This Instance Exposes

- **Failing to Delete Zero-Count Keys:** In Python dictionaries, setting `counts[ch] = 0` still leaves the key in the dictionary! `len(counts)` would still report 3 unique keys! Explicitly calling `del counts[ch]` is mandatory.
- **Short Input Strings ($|s| \le 2$):** If $s = \text{"ab"}$ or $s = \text{"a"}$, the entire string contains at most 2 distinct characters. Returning $|s|$ directly is valid and handled naturally by the window logic.
- **Plateau Excision:** With $s = \text{"ccaabbb"}$, after adding `'b'`, multiple `'c'` characters must be evicted by advancing $L$ from 0 to 2 before `'c'` is deleted, expanding the subsequent `"aabbb"` to length 5.

The alternative methods below are the ones most often reached for first; each is separated from the traced window by a specific instance:

| Candidate method | Mechanism | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Enumerate every substring | for each start index, extend the end while counting the distinct characters seen | $O(N^2)$ time, $O(1)$ auxiliary space | the largest authored instance has 100,000 characters, so roughly $5.0 \times 10^9$ substrings would be examined |
| Keep counts without deleting zero keys | decrement `counts[s[L]]` but leave the key in the map | intended $O(N)$, but incorrect | `len(counts)` still reports three keys, so feasibility is never restored and `L` is driven past the current right end of the window |
| Demand exactly two distinct characters | contract whenever the window holds anything other than two keys | $O(N)$ | single-character and one-run inputs become unanswerable: `"zzzz"` holds one key yet the correct answer is $4$ |
| Track the window with a set instead of counts | insert each entering character, discard each character that leaves | $O(N)$ | a character that leaves the window may still occur later inside it, so the set under-reports the alphabet and the window grows past the two-character limit |
| Remember only the last position of the two active characters | keep the newest index of each active character and restart the window one step past the earlier of the two when a third appears | $O(N)$ time, $O(1)$ space | competitive, but that restart index is easy to place one step too early or too late, and a late restart silently keeps three characters in the window with no count available to detect it |

---

## 7. Complexity Derivation

Counting the two pointer movements on every authored instance shows the amortization directly: the right pointer advances once per character, the left pointer advances only during a contraction, and the two totals together stay below $2N$:

| Instance | $N$ | Right-side expansions | Left-side evictions | Peak map size | Answer | Window that attains it |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| `"Z"` | 1 | 1 | 0 | 1 | 1 | `"Z"`, $[0, 0]$ |
| `"zzzz"` | 4 | 4 | 0 | 1 | 4 | the whole string, $[0, 3]$ |
| `"abababa"` | 7 | 7 | 0 | 2 | 7 | the whole string, $[0, 6]$ |
| `"eceba"` | 5 | 5 | 3 | 3 | 3 | `"ece"`, $[0, 2]$ |
| `"aAab"` | 4 | 4 | 2 | 3 | 3 | `"aAa"`, $[0, 2]$ |
| `"ccaabbb"` | 7 | 7 | 2 | 3 | 5 | `"aabbb"`, $[2, 6]$ |
| `"abacccab"` | 8 | 8 | 6 | 3 | 5 | `"accca"`, $[2, 6]$ |
| Three-run string | 100000 | 100000 | 33333 | 3 | 66667 | the `'b'` run followed by the `'c'` run, $[33333, 66666]$ |

- **Time Complexity:** $O(N)$, where $N = |s|$. Both $R$ and $L$ advance monotonically from $0$ to $N - 1$. Each character is added once and evicted at most once. Hash map operations take $O(1)$ time since the map contains at most 3 keys at any time.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, since the hash map stores at most 3 distinct character keys regardless of $N$.
