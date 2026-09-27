# Guided Example: Partition Labels

We trace the step-by-step character last-occurrence mapping ($last[c]$), sliding window right-boundary expansion ($mx = \max(mx, last[c])$), boundary closure condition ($i == mx$), greedy maximum partition segmentation, partition length recording ($i - j + 1$), and string decomposition on representative character sequences:

- **Input:** $s = \text{"ababcbacadefegdehijhklij"}$
- **Required output:**
  $$
  [9, 7, 8]
  $$
  - Partitioning criteria:
    - Partition string $s$ into the **maximum number of substrings** such that each character appears in **at most one substring**.
    - If character `'a'` appears in a part, all occurrences of `'a'` throughout the entire string must reside in that exact same part.
    - Objective: Return the list of sizes of these parts in order.
    - For $s = \text{"ababcbacadefegdehijhklij"}$ (length 24):
      - Part 1: `"ababcbaca"` (length 9). Characters `'a'`, `'b'`, `'c'` never appear again in the remainder of the string.
      - Part 2: `"defegde"` (length 7). Characters `'d'`, `'e'`, `'f'`, `'g'` never appear again.
      - Part 3: `"hijhklij"` (length 8). Characters `'h'`, `'i'`, `'j'`, `'k'`, `'l'` are fully self-contained.
      - Result: $[9, 7, 8]$.
- **Last Occurrence & Greedy Horizon Invariant:**
  - **The Necessary Interval Span:**
    - Any character $c$ must be fully contained within a single partition.
    - If a partition begins at or before the first occurrence of $c$, it **must extend at least** to the last occurrence of $c$:
      $$
      \text{partition\_end} \ge last[c]
      $$
  - **Greedy Horizon Expansion ($mx$):**
    - As we scan left to right from index $i$:
      - Whenever we encounter character $s[i]$, we stretch the current partition horizon:
        $$
        mx \leftarrow \max(mx, \; last[s[i]])
        $$
    - **Cut Condition:**
      - If the scan index reaches the horizon ($i == mx$):
        - Every character observed in the current window $[j, i]$ has its final occurrence at or before $i$.
        - None of these characters appear anywhere in $s[i + 1 \dots n - 1]$!
        - It is safe to cut the partition at index $i$, achieving the minimal valid block length and maximizing the total count of partitions.
        - Record length: $i - j + 1$, and start the next partition at $j \leftarrow i + 1$.
- **Step-by-Step Worked Execution Trace on $s = \text{"ababcbacadefegdehijhklij"}$:**
  - **Phase 0: Precompute Last Occurrence Table:**
    - `'a'`: index 8
    - `'b'`: index 5
    - `'c'`: index 7
    - `'d'`: index 14
    - `'e'`: index 15
    - `'f'`: index 11
    - `'g'`: index 13
    - `'h'`: index 19
    - `'i'`: index 22
    - `'j'`: index 23
    - `'k'`: index 20
    - `'l'`: index 21
  - **Phase 1: Partition 1 (Indices $0 \dots 8$):**
    - Start pointer: $j = 0$, horizon: $mx = 0$.
    - $i = 0$ (`'a'`): $mx \leftarrow \max(0, last[\text{'a'}]) = \max(0, 8) = \mathbf{8}$.
    - $i = 1$ (`'b'`): $mx \leftarrow \max(8, last[\text{'b'}]) = \max(8, 5) = \mathbf{8}$.
    - $i = 2$ (`'a'`): $mx \leftarrow \max(8, 8) = \mathbf{8}$.
    - $i = 3$ (`'b'`): $mx = \mathbf{8}$.
    - $i = 4$ (`'c'`): $mx \leftarrow \max(8, last[\text{'c'}]) = \max(8, 7) = \mathbf{8}$.
    - $i = 5$ (`'b'`): $mx = \mathbf{8}$.
    - $i = 6$ (`'a'`): $mx = \mathbf{8}$.
    - $i = 7$ (`'c'`): $mx = \mathbf{8}$.
    - $i = 8$ (`'a'`): $mx = \mathbf{8}$.
      - Check cut condition:
        $$
        i == mx \iff 8 == 8 \quad \mathbf{(Cut\ Point\ Reached!)}
        $$
      - Record partition length:
        $$
        \text{length}_1 = 8 - 0 + 1 = \mathbf{9}
        $$
      - Advance start: $j \leftarrow 8 + 1 = \mathbf{9}$.
  - **Phase 2: Partition 2 (Indices $9 \dots 15$):**
    - $i = 9$ (`'d'`): $mx \leftarrow \max(8, last[\text{'d'}]) = \max(8, 14) = \mathbf{14}$.
    - $i = 10$ (`'e'`): $mx \leftarrow \max(14, last[\text{'e'}]) = \max(14, 15) = \mathbf{15}$.
    - $i = 11$ (`'f'`): $mx \leftarrow \max(15, 11) = \mathbf{15}$.
    - $i = 12$ (`'e'`): $mx = \mathbf{15}$.
    - $i = 13$ (`'g'`): $mx \leftarrow \max(15, 13) = \mathbf{15}$.
    - $i = 14$ (`'d'`): $mx = \mathbf{15}$.
    - $i = 15$ (`'e'`): $mx = \mathbf{15}$.
      - Check cut condition:
        $$
        i == mx \iff 15 == 15 \quad \mathbf{(Cut\ Point\ Reached!)}
        $$
      - Record partition length:
        $$
        \text{length}_2 = 15 - 9 + 1 = \mathbf{7}
        $$
      - Advance start: $j \leftarrow 15 + 1 = \mathbf{16}$.
  - **Phase 3: Partition 3 (Indices $16 \dots 23$):**
    - $i = 16$ (`'h'`): $mx \leftarrow \max(15, 19) = \mathbf{19}$.
    - $i = 17$ (`'i'`): $mx \leftarrow \max(19, 22) = \mathbf{22}$.
    - $i = 18$ (`'j'`): $mx \leftarrow \max(22, 23) = \mathbf{23}$.
    - $i = 19 \dots 22$: $mx$ remains $23$.
    - $i = 23$ (`'j'`):
      - Check cut condition:
        $$
        i == mx \iff 23 == 23 \quad \mathbf{(Cut\ Point\ Reached!)}
        $$
      - Record partition length:
        $$
        \text{length}_3 = 23 - 16 + 1 = \mathbf{8}
        $$
  - **Final Output List:**
    $$
    ans = [\mathbf{9}, \; \mathbf{7}, \; \mathbf{8}]
    $$
- **Single Monolithic Partition Trace ($s = \text{"eccbbbbdec"}$):**
  - Character `'e'` appears at index 0 and 8.
  - Character `'c'` appears at index 1 and 9 (end).
  - Horizon $mx$ expands to 9 immediately.
  - No cut is possible until the very last index $i = 9$.
  - Output: `[10]`.
- **All Unique Characters Trace ($s = \text{"abcdef"}$):**
  - For every character, $last[c] == i$.
  - Cuts after every single character $\implies [1, 1, 1, 1, 1, 1]$.

This instance demonstrates interval chaining and greedy right-boundary absorption, mathematically proves why cutting at the earliest point satisfying $i = \max_{j \le i} last[s[j]]$ maximizes partition cardinality without constraint violation, and derives $O(N)$ execution time and $O(|\Sigma|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
Partition $s$ into the **maximum number of parts** such that each letter appears in **at most one part**.
Return the sizes of the parts.

```text
s = "ababcbacadefegdehijhklij"

Precompute last index of each character:
  'a' ends at 8, 'b' ends at 5, 'c' ends at 7
  At index 8: all 'a', 'b', 'c' are finished -> CUT! Length = 9

  'd' ends at 14, 'e' ends at 15, 'f' at 11, 'g' at 13
  At index 15: all 'd', 'e', 'f', 'g' finished -> CUT! Length = 7

  'h' to 'l' end by 23
  At index 23: all finished -> CUT! Length = 8

Result: [ 9, 7, 8 ]
```

### The Invariant of the Horizon Catch-Up
- The partition must extend to at least $last[c]$ for every character $c$ seen.
- Tracking $mx = \max(mx, last[c])$ maintains the required horizon.
- The moment the current index $i$ equals $mx$, all characters in the current window are completely contained, making $i$ an optimal cut point.

---

## 2. Conceptual Foundation & Invariants

### 1. Last Occurrence Lookup:
$$
last[c] = \max \{ k \in [0, n - 1] \mid s[k] = c \}
$$

### 2. Horizon Dynamic Update:
$$
mx \leftarrow \max(mx, \; last[s[i]])
$$
$$
\text{if } i == mx \implies ans.\text{append}(i - j + 1), \quad j \leftarrow i + 1
$$

> **Connected Component Interval Invariant.** Each character $c$ defines a span $[first(c), last(c)]$. The problem reduces to finding the connected components of the intersection graph of these intervals, which are precisely delimited by points $i$ satisfying $i = \max_{k \le i} last(s[k])$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"ababcbacadefegdehijhklij"}$:

---

### Step 1: Precompute Last
- `'a': 8`, `'b': 5`, `'c': 7`, `'d': 14`, `'e': 15`, `'h': 19`, `'j': 23`.

---

### Step 2: Part 1 ($0 \dots 8$)
- Starts with `'a'` $\to mx = 8$.
- Scanning $0 \dots 8$: no character exceeds 8.
- At $i = 8 == mx \implies$ cut! Length $8 - 0 + 1 = \mathbf{9}$.

---

### Step 3: Part 2 ($9 \dots 15$)
- Starts at 9, sees `'e'` ending at 15 $\to mx = 15$.
- At $i = 15 == mx \implies$ cut! Length $15 - 9 + 1 = \mathbf{7}$.

---

### Step 4: Part 3 ($16 \dots 23$)
- Starts at 16, sees `'j'` ending at 23 $\to mx = 23$.
- At $i = 23 == mx \implies$ cut! Length $23 - 16 + 1 = \mathbf{8}$.

---

### Step 5: Output
$$
[9, 7, 8]
$$

---

## 4. Complete Execution Trace

| Partition | Start Index $j$ | Characters Ingested | Maximum Horizon $mx$ | Cut Index $i$ ($i == mx$) | Part Size $(i - j + 1)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | `'a'`, `'b'`, `'c'` | $8$ | $8$ | **`9`** |
| $2$ | $9$ | `'d'`, `'e'`, `'f'`, `'g'` | $15$ | $15$ | **`7`** |
| **$3$** | **$16$** | **`'h'`, `'i'`, `'j'`, `'k'`, `'l'`** | **$23$** | **$23$** | **`8`** |

---

## 5. Boundary Cases & Failure Modes

- **All Characters Unique ($"abcdef"$):** Every character cuts immediately $\implies [1, 1, 1, 1, 1, 1]$.
- **Single Character Repeated ($"aaaa"$):** Single cut at end $\implies [4]$.
- **First and Last Same ($"abaca"$):** Entire string is one partition $\implies [5]$.
- **Single Character ($"a"$):** Returns $[1]$.

---

## 6. Traps & Common Anti-Patterns

- **Premature Cuts:** Cutting as soon as a character finishes its last occurrence without checking if other characters inside the partition appear further right. $mx = \max(mx, last[c])$ ensures all enclosed characters are accounted for.
- **Nested Loops ($O(N^2)$):** Scanning forward to find last occurrences repeatedly takes $O(N^2)$. Precomputing $last$ with a single dictionary pass runs in $O(N)$.
- **Forgetting to Advance Start Pointer $j$:** After a cut at $i$, $j$ must become $i + 1$ to measure the length of the next partition accurately.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to compute $last$ indices: $\mathcal{O}(N)$.
  - One pass to find cut points: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 500$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|) \le 26$ space for the $last$ index lookup table.
