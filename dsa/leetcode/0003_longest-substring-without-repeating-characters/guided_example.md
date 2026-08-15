# Guided Example: Longest Substring Without Repeating Characters

We will determine the maximum length of a contiguous substring containing no duplicate characters:

- **Input:** $s = \text{"abba"}$
- **Required output:** $2$ (corresponding to substrings `"ab"` and `"ba"`)

While `"abcabcbb"` is a common introductory sample, `"abba"` is the definitive diagnostic instance for sliding window design. It tests whether the window's left boundary can accidentally jump backwards when an ancient duplicate outside the active window is encountered.

---

## 1. Instance & Teaching Goal

A substring is contiguous: $s[L \dots R]$. To find the maximum length without checking all $O(N^2)$ candidate pairs $(L, R)$, we expand a window by moving the right boundary $R$ from left to right while dynamically adjusting the left boundary $L$.

When $s[R]$ was previously observed at index $j$:

$$
L_{\text{next}} = \max(L_{\text{current}}, j + 1)
$$

The taking of the maximum is the critical safeguard: if the previous occurrence $j$ occurred before the current window start ($j < L$), it is already outside the active window and must be ignored.

---

## 2. Conceptual Foundation & Invariants

We maintain:
1. Two pointer boundaries: $L$ (left window start) and $R$ (current scan index).
2. A lookup table $M$ recording the most recent index where each character appeared: $M[\text{char}] = \text{index}$.
3. An integer $\text{max\_len}$ tracking $\max(R - L + 1)$.

| Index | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Character | `a` | `b` | `b` | `a` |

> **Invariant.** At every step $R$, the substring $s[L \dots R]$ contains no duplicate characters, and $M$ records the latest index of every observed character in $s[0 \dots R-1]$.

---

## 3. Step-by-Step Worked Execution

### Step 1: $R = 0$, Character `s[0] = 'a'`

- **Lookup:** `'a'` is not in $M$.
- **Left boundary:** $L$ remains $0$.
- **Window:** $s[0 \dots 0] = \text{"a"}$, length $= 0 - 0 + 1 = 1$.
- **State update:** Record $M[\text{'a'}] = 0$. Update $\text{max\_len} = \max(0, 1) = 1$.

| Parameter | State |
|---|---|
| Window $[L, R]$ | $[0, 0] \implies \text{"a"}$ |
| Map $M$ | $\{\text{'a'} \mapsto 0\}$ |
| Window Length | $1$ |
| Global Maximum | $1$ |

---

### Step 2: $R = 1$, Character `s[1] = 'b'`

- **Lookup:** `'b'` is not in $M$.
- **Left boundary:** $L$ remains $0$.
- **Window:** $s[0 \dots 1] = \text{"ab"}$, length $= 1 - 0 + 1 = 2$.
- **State update:** Record $M[\text{'b'}] = 1$. Update $\text{max\_len} = \max(1, 2) = 2$.

| Parameter | State |
|---|---|
| Window $[L, R]$ | $[0, 1] \implies \text{"ab"}$ |
| Map $M$ | $\{\text{'a'} \mapsto 0, \text{'b'} \mapsto 1\}$ |
| Window Length | $2$ |
| Global Maximum | $2$ |

---

### Step 3: $R = 2$, Duplicate Character `s[2] = 'b'`

- **Lookup:** `'b'` is found in $M$ at index $j = 1$.
- **Boundary update:** Since $j = 1 \ge L = 0$, the duplicate lies inside the active window. Move $L = j + 1 = 1 + 1 = 2$.
- **Window:** $s[2 \dots 2] = \text{"b"}$, length $= 2 - 2 + 1 = 1$.
- **State update:** Update $M[\text{'b'}] = 2$. $\text{max\_len} = \max(2, 1) = 2$.

| Parameter | State |
|---|---|
| Window $[L, R]$ | $[2, 2] \implies \text{"b"}$ |
| Map $M$ | $\{\text{'a'} \mapsto 0, \text{'b'} \mapsto 2\}$ |
| Window Length | $1$ |
| Global Maximum | $2$ |

---

### Step 4: $R = 3$, Old Character `s[3] = 'a'` (The Critical Trap)

- **Lookup:** `'a'` is found in $M$ at index $j = 0$.
- **Boundary update:** Compare $j = 0$ with current $L = 2$.
  - Notice $j < L$ ($0 < 2$). The previous `'a'` is already excluded from our current window.
  - Applying $L = \max(L, j + 1) = \max(2, 0 + 1) = 2$.
- **Window:** $s[2 \dots 3] = \text{"ba"}$, length $= 3 - 2 + 1 = 2$.
- **State update:** Update $M[\text{'a'}] = 3$. $\text{max\_len} = \max(2, 2) = 2$.

| Parameter | State |
|---|---|
| Window $[L, R]$ | $[2, 3] \implies \text{"ba"}$ |
| Map $M$ | $\{\text{'a'} \mapsto 3, \text{'b'} \mapsto 2\}$ |
| Window Length | $2$ |
| Global Maximum | $2$ |

---

## 4. Complete Execution Trace

| Step | $R$ | Char | Last Index $j$ | Action on $L$ | Valid Window | Current Length | $\text{max\_len}$ |
|---|---|---|---|---|---|---|---|
| 1 | 0 | `a` | none | $L = 0$ | `"a"` | 1 | 1 |
| 2 | 1 | `b` | none | $L = 0$ | `"ab"` | 2 | 2 |
| 3 | 2 | `b` | 1 ($1 \ge 0$) | $L = 1 + 1 = 2$ | `"b"` | 1 | 2 |
| 4 | 3 | `a` | 0 ($0 < 2$) | $L = \max(2, 1) = 2$ | `"ba"` | 2 | 2 |

Final answer is $\text{max\_len} = 2$.

---

## 5. Algorithmic Correctness

**Soundness.** Every considered window $s[L \dots R]$ is guaranteed to have distinct characters because whenever a character is repeated at index $j \ge L$, the left boundary is strictly shifted past $j$.

**Completeness.** Any longer non-repeating substring must start at some index $L^*$ and end at $R^*$. As $R$ sweeps across every index $0 \dots N-1$, the algorithm maintains the leftmost valid boundary for each $R$, ensuring the maximal window ending at each position is evaluated.

---

## 6. Traps This Instance Exposes

- **The Backward-Jump Bug:** Setting $L = M[c] + 1$ without $\max(L, \dots)$ causes $L$ to jump backwards from $2$ to $1$ on step 4, falsely expanding the window to $s[1 \dots 3] = \text{"bba"}$ and accepting the duplicate `'b'`.
- **Character Set Assumptions:** Strings may contain spaces, digits, and symbols; indexing by fixed 26-character arrays fails. A general hash map or 128/256-ASCII direct array is required.
- **Empty and Single-Character Strings:** $s = \text{""}$ must return $0$, and single-character strings must return $1$ without index errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ because the right pointer $R$ advances exactly once per character, and left pointer adjustments and map lookups take $O(1)$ expected time.
- **Auxiliary Space Complexity:** $O(\min(N, |\Sigma|))$ where $|\Sigma|$ is the alphabet size (at most 128 for ASCII or 256 for extended ASCII), bounded by the unique characters stored in the map.
