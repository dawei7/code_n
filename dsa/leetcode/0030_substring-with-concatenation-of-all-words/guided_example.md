# Guided Example: Substring with Concatenation of All Words

We trace the step-by-step multi-offset sliding window on a representative concatenated string instance:

- **Input:** $s = \text{"barfoothefoobarman"}$, $\text{words} = [\text{"foo"}, \text{"bar"}]$
- **Required output:** $[0, 9]$

This instance demonstrates word chunking, parallel sliding window passes over $W$ distinct remainder offsets, hash-map frequency counting, window contraction upon over-allocation, and clearing window state upon encountering invalid non-dictionary words.

---

## 1. Instance & Teaching Goal

Given a string $s$ of length $N = 18$ and an array $\text{words}$ of $M = 2$ words, where each word has uniform length $W = 3$:
- Total concatenation length is $L_{\text{total}} = M \cdot W = 2 \cdot 3 = 6$.
- Target word multiset:
  $$
  \text{target\_counts} = \{ \text{"bar"}: 1, \, \text{"foo"}: 1 \}
  $$

A naive sliding window re-evaluates all $M$ words at every single character index $i \in [0, N - L_{\text{total}}]$, requiring $O(N \cdot M \cdot W)$ time.

The optimal algorithm recognizes that each word has length $W$. We partition the search into $W$ independent sliding window tracks (starting at offsets $0, 1, \dots, W-1$). Within each track, the window steps forward by chunks of $W$ characters, achieving an amortized $O(N)$ runtime.

---

## 2. Conceptual Foundation & Invariants

### Multi-Offset Chunking
Because words have fixed length $W = 3$, any contiguous valid concatenation aligned with words must fall into one of $W$ residue classes modulo $W$:
- **Offset 0:** Tokens at indices $[0, 3, 6, 9, 12, 15] \implies \text{"bar"}, \text{"foo"}, \text{"the"}, \text{"foo"}, \text{"bar"}, \text{"man"}$
- **Offset 1:** Tokens at indices $[1, 4, 7, 10, 13] \implies \text{"arf"}, \text{"oot"}, \text{"hef"}, \text{"oob"}, \text{"arm"}$
- **Offset 2:** Tokens at indices $[2, 5, 8, 11, 14] \implies \text{"rfo"}, \text{"oth"}, \text{"efo"}, \text{"oba"}, \text{"rma"}$

### Window State within an Offset Track
Within each offset track, we maintain two pointer indices $L$ and $R$ advancing in steps of $W$:
1. Read word $w = s[R \dots R+W-1]$:
   - **Case 1 (Invalid Word):** If $w \notin \text{target\_counts}$, all windows spanning across $R$ are invalid. Reset frequency table, and shift $L \leftarrow R + W$.
   - **Case 2 (Valid Word):** Increment $\text{current\_counts}[w]$.
     - If $\text{current\_counts}[w] > \text{target\_counts}[w]$ (excess duplicate), advance $L$ by $W$, decrementing counts until the frequency of $w$ is restored to valid limits.
2. **Match Detection:** When the active window $[L, R + W - 1]$ contains exactly $M$ valid words, record $L$ as a valid start index, then shift $L$ forward by $W$ to search for subsequent matches.

> **Invariant.** For any active window $[L, R]$, every token inside the window is present in $\text{words}$ with count $\le \text{target\_counts}$. A match occurs if and only if the window length equals $M \cdot W$.

---

## 3. Step-by-Step Worked Execution

We trace Offset Track $0$ ($L = 0, R = 0$) on $s = \text{"barfoothefoobarman"}$:

### Chunk 1 ($R = 0$): Token $\text{"bar"}$
- Slice: $s[0 \dots 3] = \text{"bar"}$.
- Check: $\text{"bar"} \in \text{target\_counts}$ (allowed count: 1).
- Add to window: $\text{current\_counts}[\text{"bar"}] = 1$.
- Window words: $1 < M=2$.
- Advance: $R \leftarrow 3$.

---

### Chunk 2 ($R = 3$): Token $\text{"foo"}$
- Slice: $s[3 \dots 6] = \text{"foo"}$.
- Check: $\text{"foo"} \in \text{target\_counts}$ (allowed count: 1).
- Add to window: $\text{current\_counts}[\text{"foo"}] = 1$.
- Window words: $2 == M=2$.
- Window span: $[0 \dots 5] = \text{"barfoo"}$.
- **Match Confirmed!** Record index $L = 0$.
- Slide window: Decrement $\text{"bar"}$, advance $L \leftarrow 3$.
- Advance: $R \leftarrow 6$.

---

### Chunk 3 ($R = 6$): Token $\text{"the"}$
- Slice: $s[6 \dots 9] = \text{"the"}$.
- Check: $\text{"the"} \notin \text{target\_counts}$ (invalid word!).
- Action: Clear $\text{current\_counts} = \{\}$.
- Reset: $L \leftarrow 9$.
- Advance: $R \leftarrow 9$.

---

### Chunk 4 ($R = 9$): Token $\text{"foo"}$
- Slice: $s[9 \dots 12] = \text{"foo"}$.
- Check: $\text{"foo"} \in \text{target\_counts}$.
- Add to window: $\text{current\_counts}[\text{"foo"}] = 1$.
- Window words: $1 < M=2$.
- Advance: $R \leftarrow 12$.

---

### Chunk 5 ($R = 12$): Token $\text{"bar"}$
- Slice: $s[12 \dots 15] = \text{"bar"}$.
- Check: $\text{"bar"} \in \text{target\_counts}$.
- Add to window: $\text{current\_counts}[\text{"bar"}] = 1$.
- Window words: $2 == M=2$.
- Window span: $[9 \dots 14] = \text{"foobar"}$.
- **Match Confirmed!** Record index $L = 9$.
- Slide window: Decrement $\text{"foo"}$, advance $L \leftarrow 12$.
- Advance: $R \leftarrow 15$.

---

### Chunk 6 ($R = 15$): Token $\text{"man"}$
- Slice: $s[15 \dots 18] = \text{"man"}$.
- Check: $\text{"man"} \notin \text{target\_counts}$ (invalid word!).
- Reset: Clear window. $R$ reaches string end.

### Summary of Offsets 1 & 2
- Offset 1: Scans $\text{"arf"}, \text{"oot"}, \dots$ — none match the dictionary; yields no valid matches.
- Offset 2: Scans $\text{"rfo"}, \text{"oth"}, \dots$ — none match the dictionary; yields no valid matches.

Final emitted matches: $[0, 9]$.

---

## 4. Complete Execution Trace (Offset 0)

| Step | Window $[L, R]$ | Extracted Word $w$ | Target Limit | Current Count | Window Words Count | Action Taken | Confirmed Match? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | $[0, 0]$ | `"bar"` | 1 | 1 | 1 | Expand window; $R \leftarrow 3$ | - |
| 2 | $[0, 3]$ | `"foo"` | 1 | 1 | 2 | Full match; contract $L \leftarrow 3$ | **Index 0** |
| 3 | $[3, 6]$ | `"the"` | 0 | 0 | 0 | Invalid token; reset $L \leftarrow 9$ | - |
| 4 | $[9, 9]$ | `"foo"` | 1 | 1 | 1 | Expand window; $R \leftarrow 12$ | - |
| 5 | $[9, 12]$ | `"bar"` | 1 | 1 | 2 | Full match; contract $L \leftarrow 12$ | **Index 9** |
| 6 | $[12, 15]$ | `"man"` | 0 | 0 | 0 | Invalid token; reset $L \leftarrow 18$ | - |

### Residue-Class Coverage Table for All Three Offsets

Every candidate start $i$ lies in exactly one residue class modulo $W = 3$, and a start is a match only if both of its aligned tokens are dictionary words. The legal starts here are $i \in [0, N - L] = [0, 12]$.

| Offset $r$ | Candidate Starts $i \equiv r \pmod 3$, $i \le 12$ | Tokens at Each Aligned Start | Tokens Present in $\text{words}$ | Matches Emitted |
|:---:|:---|:---|:---|:---|
| 0 | 0, 3, 6, 9, 12 | `"bar"`, `"foo"`, `"the"`, `"foo"`, `"bar"` | `"bar"` and `"foo"` only | $0$ and $9$ |
| 1 | 1, 4, 7, 10 | `"arf"`, `"oot"`, `"hef"`, `"oob"` | none | none |
| 2 | 2, 5, 8, 11 | `"rfo"`, `"oth"`, `"efo"`, `"oba"` | none | none |

The offset-0 row explains why the matches are exactly $0$ and $9$: start $3$ opens on the valid token `"foo"` but is followed by `"the"`, start $6$ begins on `"the"`, and start $12$ is followed by `"man"`. Both aligned tokens of a candidate must belong to $\text{words}$, so one valid token is never enough. The other two residue classes contribute nothing, yet each still has to be scanned, because the residue class of a valid start is not known in advance.

---

## 5. Algorithmic Correctness

**Soundness.** A substring starting at index $i$ is a valid concatenation if and only if it decomposes into $M$ consecutive words of length $W$ whose multiset matches $\text{target\_counts}$. The sliding window verifies exact token matches and frequencies, guaranteeing zero false positives.

**Completeness.** Any valid starting position $i$ must satisfy $i \equiv k \pmod W$ for some offset $k \in [0, W - 1]$. Since all $W$ offset tracks are independently searched, and the two-pointer window explores every contiguous sequence of valid tokens within each track, all valid start indices are discovered.

---

## 6. Traps This Instance Exposes

- **Overlapping Offset Classes:** Evaluating only offset 0 misses valid concatenations starting at non-multiples of $W$ (e.g. at index 1 or 2). Iterating across all $W$ distinct offsets guarantees complete coverage.
- **Handling Duplicate Words in Dictionary:** If $\text{words} = [\text{"word"}, \text{"good"}, \text{"best"}, \text{"word"}]$, the word $\text{"word"}$ has count 2. Using boolean sets fails; a full frequency counter mapping is required.
- **Excess Word Contraction:** When an existing word appears too many times ($\text{current\_counts}[w] > \text{target\_counts}[w]$), the left pointer $L$ must advance until the redundant copy is expelled from the window, rather than resetting $L$ entirely.

### Boundary Instances and the Window Rule That Resolves Them

| Boundary Scenario | Concrete Input | Expected | Window Rule That Decides It |
|:---|:---|:---|:---|
| Concatenation cannot fit | $s = \text{"abc"}$, $\text{words} = [\text{"ab"}, \text{"cd"}]$ | `[]` | $L = 2 + 2 = 4 > N = 3$, so no start index $i \in [0, N - L]$ exists and the search range is empty. |
| Single word matching at unaligned offsets | $s = \text{"aaaa"}$, $\text{words} = [\text{"aa"}]$ | `[0, 1, 2]` | With $M = 1$ a match needs only one token, so every legal start belongs to a match; the starts fall in both residue classes and each is emitted by its own track. |
| Identical required words | $s = \text{"aaaaaa"}$, $\text{words} = [\text{"aa"}, \text{"aa"}]$ | `[0, 1, 2]` | The target count of `"aa"` is 2, so a window is valid exactly when it holds two copies; the window length is $M \cdot W = 4$ and starts $3$ and beyond would need index $\ge 7$. |
| Excess duplicate must shrink the window | $s = \text{"wordgoodgoodgoodbestword"}$, $\text{words} = [\text{"word"}, \text{"good"}, \text{"best"}, \text{"good"}]$ | `[8]` | The dictionary holds `"good"` twice, so the third consecutive `"good"` makes $\text{current\_counts}[\text{"good"}] = 3 > 2$ and forces $L$ forward until only two copies remain, which is why the sole match begins at $8$. |
| Foreign tokens reset the track | $s = \text{"barxxfoobar"}$, $\text{words} = [\text{"foo"}, \text{"bar"}]$ | `[5]` | The token `"xxf"` at index $3$ is not in $\text{words}$, so that track clears its window state and jumps past it; the match comes from the offset-$2$ track, where `"foo"` at index $5$ is followed by `"bar"` at index $8$, giving the clean run `"foobar"`. |
| Wrong multiplicity everywhere | $s = \text{"wordgoodgoodgoodbestword"}$, $\text{words} = [\text{"word"}, \text{"good"}, \text{"best"}, \text{"word"}]$ | `[]` | Here `"word"` must appear twice inside one window of length $M \cdot W = 16$. The text supplies `"word"` at indices $0$ and $20$, and no window of length $16$ can contain both, so no window holds the required multiset. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot W)$, or $O(N)$ when treating $W$ as a constant. There are $W$ passes. In each pass, the right pointer $R$ moves across at most $N/W$ words, and the left pointer $L$ moves at most $N/W$ words. Dictionary lookups and frequency operations take $O(W)$ string hashing time. Total runtime is $W \cdot (N/W) \cdot O(W) = O(N \cdot W)$.
- **Auxiliary Space Complexity:** $O(M \cdot W)$. The hash map stores at most $M$ unique words from the dictionary.