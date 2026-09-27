# Guided Example: Longest Substring with At Most K Distinct Characters

We trace the step-by-step non-shrinking sliding window mechanism, hash map character frequency counting (`cnt`), single-step left boundary shifting (`l += 1`), and final maximum window size extraction (`len(s) - l`) on representative string instances:

- **Input:** $s = \text{"eceba"}, \quad k = 2$
- **Required output:** $3$
  - Distinct valid substrings:
    - `"e"` (length 1, 1 distinct)
    - `"ec"` (length 2, 2 distinct)
    - `"ece"` (length 3, 2 distinct: `{'e', 'c'}`) — MAXIMUM VALID WINDOW!
    - `"eceb"` (length 4, 3 distinct: `{'e', 'c', 'b'}`) — Violates $k = 2$
  - Non-shrinking window maintains maximum span of 3 through indices 3 and 4
  - Final length: $5 - 2 = \mathbf{3}$
- **All Identical Characters:** $s = \text{"aaaaa"}, k = 1 \implies 5$ (entire string has 1 distinct character)
- **Zero Distinct Limit:** $k = 0 \implies 0$
- **Large $k$ Exceeding Alphabet:** $s = \text{"abc"}, k = 5 \implies 3$ ($k \ge \text{len}(s)$ allows entire string)

This instance demonstrates the non-shrinking sliding window technique, mathematically proves why advancing the left boundary by at most 1 per iteration preserves the historical maximum window length, contrasts $O(N)$ single-pass execution against $O(N^2)$ brute-force substring generation, and analyzes $O(K)$ frequency map space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"eceba"}$ ($N = 5$) and an integer $k = 2$:
Find the length of the longest contiguous substring that contains at most $k$ distinct characters:

```text
String: "eceba", k = 2

Substrings containing <= 2 distinct characters:
[0..0] "e"     -> {'e'} (1 distinct) -> len = 1
[0..1] "ec"    -> {'e', 'c'} (2 distinct) -> len = 2
[0..2] "ece"   -> {'e', 'c'} (2 distinct) -> len = 3 (MAXIMUM!)
[1..2] "ce"    -> {'c', 'e'} (2 distinct) -> len = 2
[2..3] "eb"    -> {'e', 'b'} (2 distinct) -> len = 2
[3..4] "ba"    -> {'b', 'a'} (2 distinct) -> len = 2

Maximum Substring Length: 3
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Non-Shrinking Window Pattern
In standard sliding windows, whenever the condition is violated, a `while` loop shrinks the window back to a valid state.
However, because we only seek the **maximum** length achieved, shrinking the window below our current maximum is unnecessary!
- When valid ($\text{len}(cnt) \le k$), the window expands ($R$ advances, $L$ stays fixed).
- When invalid ($\text{len}(cnt) > k$), the window does not shrink; it **slides** forward by 1 unit ($R$ advances, $L$ advances by 1).
- At all times, the window size $R - L + 1$ represents the running maximum valid length encountered so far.
- After $R$ reaches the end of the string, the final maximum length is simply $\text{len}(s) - L$!

### 2. Frequency Map Operations:
For each character $c \in s$:
1. $cnt[c] \mathrel{+}= 1$
2. If $\text{len}(cnt) > k$:
   - Decrement count of outgoing character: $cnt[s[l]] \mathrel{-}= 1$
   - If $cnt[s[l]] == 0$: delete $s[l]$ from $cnt$
   - $l \mathrel{+}= 1$

> **Invariant.** The distance $r - l + 1$ never decreases. If a valid window of size $W$ was found, $r - l + 1$ will remain at least $W$ for all subsequent iterations.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"eceba"}$ with $k = 2$:
Initialized: $l = 0, cnt = \{\}$.

---

### Step 1: $r = 0, c = \text{'e'}$
- Add $c$: $cnt[\text{'e'}] = 1$.
- Distinct count: $\text{len}(cnt) = 1 \le 2$.
- Condition holds. Left pointer stays at $l = 0$.
- Current window: $s[0 \dots 0] = \text{"e"}$, length $= 1$.

---

### Step 2: $r = 1, c = \text{'c'}$
- Add $c$: $cnt[\text{'c'}] = 1$.
- Distinct count: $\text{len}(cnt) = 2 \le 2$.
- Condition holds. Left pointer stays at $l = 0$.
- Current window: $s[0 \dots 1] = \text{"ec"}$, length $= 2$.

---

### Step 3: $r = 2, c = \text{'e'}$
- Add $c$: $cnt[\text{'e'}] = 2$.
- Distinct count: $\text{len}(cnt) = 2 \le 2$ (Characters: `{'e', 'c'}`).
- Condition holds. Left pointer stays at $l = 0$.
- Current window: $s[0 \dots 2] = \text{"ece"}$, length $= \mathbf{3}$!

---

### Step 4: $r = 3, c = \text{'b'}$
- Add $c$: $cnt[\text{'b'}] = 1$.
- Map state: $\{\text{'e'}: 2, \; \text{'c'}: 1, \; \text{'b'}: 1\}$.
- Distinct count: $\text{len}(cnt) = 3 > 2$ (**Violation!**).
- **Shift Window Left Boundary:**
  - Evict outgoing character $s[l] = s[0] = \text{'e'}$:
    $cnt[\text{'e'}] \leftarrow 2 - 1 = 1$.
  - Advance left pointer: $l \leftarrow 0 + 1 = \mathbf{1}$.
- Window slides without shrinking: length remains $3 - 1 + 1 = 3$.

---

### Step 5: $r = 4, c = \text{'a'}$
- Add $c$: $cnt[\text{'a'}] = 1$.
- Map state: $\{\text{'e'}: 1, \; \text{'c'}: 1, \; \text{'b'}: 1, \; \text{'a'}: 1\}$.
- Distinct count: $\text{len}(cnt) = 4 > 2$ (**Violation!**).
- **Shift Window Left Boundary:**
  - Evict outgoing character $s[l] = s[1] = \text{'c'}$:
    $cnt[\text{'c'}] \leftarrow 1 - 1 = 0 \implies$ delete `'c'` from $cnt$.
  - Advance left pointer: $l \leftarrow 1 + 1 = \mathbf{2}$.
- Window slides without shrinking: length remains $4 - 2 + 1 = 3$.

---

### Step 6: Final Maximum Calculation
String traversal complete ($N = 5$).
$$
\text{Result} = \text{len}(s) - l = 5 - 2 = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
s = "eceba", k = 2
l = 0, cnt = {}

r=0, c='e': cnt={'e':1}         len=1 <= 2 -> l=0 (window len = 1)
r=1, c='c': cnt={'e':1, 'c':1}  len=2 <= 2 -> l=0 (window len = 2)
r=2, c='e': cnt={'e':2, 'c':1}  len=2 <= 2 -> l=0 (window len = 3: "ece")
r=3, c='b': cnt={'e':2,'c':1,'b':1} len=3 > 2 -> shift s[0]='e': cnt['e']=1, l=1 (len = 3)
r=4, c='a': cnt={'e':1,'c':1,'b':1,'a':1} len=4 > 2 -> shift s[1]='c': del 'c', l=2 (len = 3)

Final: len(s) - l = 5 - 2 = 3
```

| Step $r$ | Character $c$ | Frequency Map $cnt$ | Distinct Count $\text{len}(cnt)$ | Exceeds $k = 2$? | Left Action | Updated $l$ | Active Window Length $r - l + 1$ |
|:---:|:---:|:---|:---:|:---:|:---|:---:|:---:|
| 0 | `'e'` | `{'e': 1}` | 1 | No | None | 0 | 1 |
| 1 | `'c'` | `{'e': 1, 'c': 1}` | 2 | No | None | 0 | 2 |
| **2** | **'e'** | **`{'e': 2, 'c': 1}`** | **2** | **No** | **None** | **0** | **3 (Peak Window)** |
| 3 | `'b'` | `{'e': 1, 'c': 1, 'b': 1}` | 3 | Yes | Decrement `'e'` | 1 | 3 |
| 4 | `'a'` | `{'e': 1, 'b': 1, 'a': 1}` | 3 | Yes | Delete `'c'` | 2 | 3 |
| **Exit** | - | - | - | - | **$\text{len}(s) - l = 5 - 2$** | - | **$\mathbf{3}$ (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** Whenever $\text{len}(cnt) \le k$, the current window $s[l \dots r]$ is a valid substring with at most $k$ distinct characters. When $\text{len}(cnt) > k$, shifting $l$ by 1 prevents the window length from expanding further. Thus, the window length can only grow when a strictly larger valid substring is encountered.

**Completeness.** Since the window never shrinks below its maximum attained valid length, and advances through the entire string character by character, the final value of $\text{len}(s) - l$ exactly equals the length of the longest valid substring in $s$.

---

## 6. Traps This Instance Exposes

- **Deleting Keys with Zero Count:** In Python's `Counter`, setting `cnt[x] -= 1` when `cnt[x] == 1` leaves `cnt[x] == 0`. The key remains in the dictionary, causing `len(cnt)` to incorrectly report that the character is still present! Explicitly executing `del cnt[s[l]]` when count reaches 0 is required.
- **$k = 0$ Edge Case:** If $k = 0$, no valid substring can contain any characters. The output must be $0$.
- **Window Size Invariance:** A common mistake is using `while len(cnt) > k:`, which shrinks the window. Both approaches yield $O(N)$ time, but the non-shrinking `if` variation eliminates inner-loop overhead.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. The right pointer advances $N$ times, and the left pointer advances at most $N$ times. Each dictionary insertion, deletion, and lookup executes in $O(1)$ expected time.
- **Auxiliary Space Complexity:** $O(K)$, where $K = \min(k + 1, |\Sigma|)$ is the maximum number of distinct characters stored in the frequency map at any time.