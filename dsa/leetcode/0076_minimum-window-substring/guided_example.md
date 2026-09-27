# Guided Example: Minimum Window Substring

We trace the step-by-step two-pointer sliding window expansion and contraction algorithm on a representative string instance:

- **Input:** $s = \text{"ADOBECODEBANC"}$, $t = \text{"ABC"}$
- **Required output:** $\text{"BANC"}$

This instance demonstrates frequency map matching across distinct characters, expanding right pointer $R$ to acquire feasibility, contracting left pointer $L$ to minimize window span, tracking surplus characters, and updating the global minimum window in $O(|s| + |t|)$ time.

---

## 1. Instance & Teaching Goal

Given two strings $s$ (length $13$) and $t$ (length $3$), return the minimum window substring of $s$ such that every character in $t$ (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

For $s = \text{"ADOBECODEBANC"}$ and $t = \text{"ABC"}$:
- The required frequency multiset is $\{'A': 1, 'B': 1, 'C': 1\}$.
- Candidate valid windows:
  - `"ADOBEC"` (indices $[0, 5]$, length 6)
  - `"CODEBA"` (indices $[5, 10]$, length 6)
  - `"BANC"` (indices $[9, 12]$, length 4)
The minimum valid window is $\text{"BANC"}$ of length 4.

A brute-force search checking all $O(|s|^2)$ substrings takes $O(|s|^3)$ time. The optimal sliding window maintains character frequencies and a match counter `formed`, adjusting pointers $L$ and $R$ monotonically so each pointer visits each character at most once ($O(|s|)$ time).

---

## 2. Conceptual Foundation & Invariants

### 2-Pointer Dynamic Feasibility Protocol
1. **Target Dictionary:**
   Build frequency map $\text{need}$ of $t$, and let $\text{required} = |\text{need}|$ be the number of unique characters that must meet their target frequency.
2. **Window State Tracker:**
   Maintain $\text{window}$ frequency map, and scalar integer $\text{formed} = 0$, tracking how many distinct characters currently meet or exceed their count in $\text{need}$.
3. **Expansion Phase (Advance $R$):**
   Add $s[R]$ to $\text{window}$.
   If $s[R] \in \text{need}$ and $\text{window}[s[R]] == \text{need}[s[R]]$:
   $$
   \text{formed} \leftarrow \text{formed} + 1
   $$
4. **Contraction Phase (Advance $L$ while $\text{formed} == \text{required}$):**
   The window $[L, R]$ is currently valid:
   - If $R - L + 1 < \text{min\_len}$, update minimum window:
     $$
     \text{min\_len} \leftarrow R - L + 1, \quad \text{best\_window} \leftarrow [L, R]
     $$
   - Remove $s[L]$ from $\text{window}$:
     If $s[L] \in \text{need}$ and $\text{window}[s[L]] < \text{need}[s[L]]$:
     $$
     \text{formed} \leftarrow \text{formed} - 1
     $$
   - Advance left boundary: $L \leftarrow L + 1$.

> **Invariant.** While $\text{formed} == \text{required}$, the active window $[L, R]$ contains all characters of $t$. Once $\text{formed} < \text{required}$, window validity is lost and $R$ must advance.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"ADOBECODEBANC"}$ with $t = \text{"ABC"}$ ($\text{required} = 3$):

### Phase 1: Expand to First Valid Window ($R = 0 \to 5$)
- $R = 0$ (`'A'`): $\text{window}[\text{'A'}] = 1 \implies \text{formed} = 1$.
- $R = 1$ (`'D'`): non-target character.
- $R = 2$ (`'O'`): non-target character.
- $R = 3$ (`'B'`): $\text{window}[\text{'B'}] = 1 \implies \text{formed} = 2$.
- $R = 4$ (`'E'`): non-target character.
- $R = 5$ (`'C'`): $\text{window}[\text{'C'}] = 1 \implies \text{formed} = 3 == \text{required}$!
- **First Valid Window:** $[0, 5]$ (`"ADOBEC"`), $\text{length} = 6$.
  - Attempt contraction: remove $s[0]$ (`'A'`).
  - $\text{window}[\text{'A'}]$ drops to $0 < 1 \implies \text{formed} \leftarrow 2$.
  - $L \leftarrow 1$. Window invalid; resume expansion.

---

### Phase 2: Expand to Second Match ($R = 6 \to 10$)
- $R = 6 \dots 9$: Read `'O', 'D', 'E', 'B'`.
  - At $R = 9$ (`'B'`), $\text{window}[\text{'B'}] = 2$ (surplus 'B').
- $R = 10$ (`'A'`): $\text{window}[\text{'A'}] = 1 \implies \text{formed} = 3$!
- Window $[1, 10]$ (`"DOBECODEBA"`), $\text{length} = 10$.
- **Contraction Loop:**
  - $L = 1$ (`'D'`): discard irrelevant $\to L = 2$.
  - $L = 2$ (`'O'`): discard irrelevant $\to L = 3$.
  - $L = 3$ (`'B'`): $\text{window}[\text{'B'}]$ drops from $2 \to 1 \ge 1$. $\text{formed}$ remains $3$!
    - Window $[4, 10]$ (`"ECODEBA"`), $\text{length} = 7$.
  - $L = 4$ (`'E'`): discard irrelevant $\to L = 5$.
    - Window $[5, 10]$ (`"CODEBA"`), $\text{length} = 6$.
  - $L = 5$ (`'C'`): $\text{window}[\text{'C'}]$ drops to $0 < 1 \implies \text{formed} \leftarrow 2$.
  - $L \leftarrow 6$. Window invalid; resume expansion.

---

### Phase 3: Expand to Optimal Match ($R = 11 \to 12$)
- $R = 11$ (`'N'`): non-target character.
- $R = 12$ (`'C'`): $\text{window}[\text{'C'}] = 1 \implies \text{formed} = 3$!
- Window $[6, 12]$ (`"ODEBANC"`), $\text{length} = 7$.
- **Contraction Loop:**
  - $L = 6$ (`'O'`): discard $\to L = 7$.
  - $L = 7$ (`'D'`): discard $\to L = 8$.
  - $L = 8$ (`'E'`): discard $\to L = 9$.
  - Window $[9, 12]$ is $\text{"BANC"}$, $\text{length} = 4$.
    - $4 < 6 \implies$ **New Global Minimum Window Recorded!**
  - $L = 9$ (`'B'`): $\text{window}[\text{'B'}]$ drops to $0 < 1 \implies \text{formed} \leftarrow 2$.
  - $L \leftarrow 10$. Window invalid.
- $R = 13 == |s|$. Search terminates.

Final minimal substring: $\text{"BANC"}$.

---

### Window Frequency State at Decisive Events

The `formed` counter only tells us how many target letters are satisfied. The underlying counts show *why* it moves, and how a surplus letter keeps a window feasible while a target letter is being evicted.

| Event | Window $[L, R]$ and its content | `'A'` | `'B'` | `'C'` | Non-target letters inside | `formed` |
|:---|:---|:---:|:---:|:---:|:---|:---:|
| $R = 5$ acquires the first `'C'` | `[0, 5]` = `"ADOBEC"` | 1 | 1 | 1 | `'D'`, `'O'`, `'E'` | 3 |
| Evict $s[0]$ = `'A'` | `[1, 5]` = `"DOBEC"` | 0 | 1 | 1 | `'D'`, `'O'`, `'E'` | 2 |
| $R = 9$ acquires a second `'B'` | `[1, 9]` = `"DOBECODEB"` | 0 | 2 | 1 | `'D'`, `'O'`, `'E'`, `'O'`, `'D'`, `'E'` | 2 |
| $R = 10$ acquires a fresh `'A'` | `[1, 10]` = `"DOBECODEBA"` | 1 | 2 | 1 | `'D'`, `'O'`, `'E'`, `'O'`, `'D'`, `'E'` | 3 |
| Evict $s[1], s[2]$ = `'D'`, `'O'` | `[3, 10]` = `"BECODEBA"` | 1 | 2 | 1 | `'E'`, `'C'`, `'O'`, `'D'`, `'E'` | 3 |
| Evict $s[3]$ = surplus `'B'` | `[4, 10]` = `"ECODEBA"` | 1 | 1 | 1 | `'E'`, `'C'`, `'O'`, `'D'`, `'E'` | 3 |
| Evict $s[4]$ = `'E'` | `[5, 10]` = `"CODEBA"` | 1 | 1 | 1 | `'C'`, `'O'`, `'D'`, `'E'` | 3 |
| Evict $s[5]$ = `'C'` | `[6, 10]` = `"ODEBA"` | 1 | 1 | 0 | `'O'`, `'D'`, `'E'` | 2 |
| $R = 12$ acquires a new `'C'` | `[6, 12]` = `"ODEBANC"` | 1 | 1 | 1 | `'O'`, `'D'`, `'E'`, `'N'` | 3 |
| Evict $s[6..8]$ = `'O'`, `'D'`, `'E'` | `[9, 12]` = `"BANC"` | 1 | 1 | 1 | `'N'` | 3 |
| Evict $s[9]$ = `'B'` | `[10, 12]` = `"ANC"` | 1 | 0 | 1 | `'N'` | 2 |

Two rows carry the decisive lesson. The second `'B'` at index 9 pushes the count from $1$ to $2$, yet `formed` does not move, because a count above the requirement is surplus; that surplus is exactly what lets the contraction loop continue past index 3 later without losing feasibility. Symmetrically, evicting the only `'C'` at index 5 drops the count from $1$ to $0$, which is the first time the loop falls *below* the requirement and forces `formed` down to $2$.

---

## 4. Complete Execution Trace

| Step Event | Active $R$ | Char $s[R]$ | Active $L$ | Current Window String | Formed / Req | Best Window | Best Length |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Expand | 5 | `'C'` | 0 | `"ADOBEC"` | 3 / 3 | `[0, 5]` | 6 |
| Contract | 5 | `'C'` | 1 | `"DOBEC"` | 2 / 3 | `[0, 5]` | 6 |
| Expand | 10 | `'A'` | 1 | `"DOBECODEBA"` | 3 / 3 | `[0, 5]` | 6 |
| Contract | 10 | `'A'` | 3 | `"BECODEBA"` | 3 / 3 | `[0, 5]` | 6 |
| Contract | 10 | `'A'` | 5 | `"CODEBA"` | 3 / 3 | `[5, 10]` | 6 |
| Contract | 10 | `'A'` | 6 | `"ODEBA"` | 2 / 3 | `[0, 5]` | 6 |
| Expand | 12 | `'C'` | 6 | `"ODEBANC"` | 3 / 3 | `[0, 5]` | 6 |
| Contract | 12 | `'C'` | 8 | `"EBANC"` | 3 / 3 | `[0, 5]` | 6 |
| **Contract** | **12** | **`'C'`** | **9** | **`"BANC"`** | **3 / 3** | **`[9, 12]`** | **4 (Min)** |
| Contract | 12 | `'C'` | 10 | `"ANC"` | 2 / 3 | `[9, 12]` | 4 |

---

## 5. Algorithmic Correctness

**Soundness.** A window is considered feasible if and only if $\text{formed} == \text{required}$, meaning every distinct character in $t$ appears with frequency at least as high as in $t$. Contraction only removes characters from the left while preserving feasibility, ensuring every evaluated window is legally valid.

**Completeness.** Any global minimum window must end at some right boundary index $R$. By expanding $R$ incrementally and shrinking $L$ to its absolute minimal feasible width for each $R$, no candidate minimum window can be skipped.

---

## 6. Traps This Instance Exposes

- **Duplicate Characters in $t$:** If $t = \text{"AAB"}$, the window must contain at least two `'A'`s. Using a frequency count rather than a set check is mandatory.
- **Surplus Characters in $s$:** Having more of a character than requested (e.g. two `'B'`s in `"DOBECODEBA"`) is valid. The `formed` counter increments only when the frequency strictly reaches $\text{need}[c]$, and decrements only when falling below $\text{need}[c]$.
- **Filtered S-List Optimization:** For sparse targets in large texts, pre-filtering $s$ into a list of tuples `(index, char)` for characters present in $t$ accelerates the two-pointer scan by skipping irrelevant letters.

---

## 7. Complexity Derivation

### Variant Comparison

| Approach | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---|:---|:---|
| Enumerate every window | For each pair $(L, R)$, rebuild the frequency map of the window and test it | $O(\lvert s \rvert^3)$ | $O(\lvert \Sigma \rvert)$ | Correct but cubic; the count rebuild dominates and nothing is reused between windows |
| Two-pointer window with a `formed` counter (used here) | Grow $R$ until feasible, then shrink $L$ while feasibility survives | $O(\lvert s \rvert + \lvert t \rvert)$ | $O(\lvert \Sigma \rvert)$ | Each character enters and leaves the window once, but the counter must increment only on strict equality with the target count |
| Two-pointer window with a per-step feasibility re-check | Grow and shrink the same way, but re-compare every target count on each evaluation | $O(\lvert s \rvert \cdot \lvert \Sigma_t \rvert)$ | $O(\lvert \Sigma \rvert)$ | Simpler to reason about, yet the repeated verification multiplies the running time by the number of distinct letters in $t$ |
| Prefiltered index list | Compress $s$ to the positions whose letters occur in $t$, then slide over that compressed list | $O(\lvert s \rvert + \lvert t \rvert)$ | $O(\lvert s \rvert)$ | Skips irrelevant letters but stores a filtered index list, and the winning window must be mapped back to original indices |

- **Time Complexity:** $O(|s| + |t|)$. Building the frequency dictionary takes $O(|t|)$ time. Pointers $L$ and $R$ each traverse string $s$ from index $0$ to $|s|$ at most once ($2|s|$ operations).
- **Auxiliary Space Complexity:** $O(|\Sigma|)$, where $|\Sigma|$ is the alphabet size of unique characters in $s$ and $t$ (at most $52$ for ASCII letters).
