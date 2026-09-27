# Guided Example: Longest Repeating Character Replacement

We trace the step-by-step sliding window expansion, dominant character frequency tracking, replacement budget check ($W - mx \le k$), non-shrinking window shifting, and maximum subsegment extraction on representative string instances:

- **Input:** $s = \text{"AABABBA"}, \quad k = 1$
- **Required output:** `4`
  - Step 1 ($r = 0, c = \text{'A'}$):
    - Window $[0, 0]$: $cnt = \{A: 1\}$, dominant frequency $mx = 1$
    - Replacements needed: $W - mx = 1 - 1 = 0 \le k$ (Valid) $\implies l = 0$
  - Step 2 ($r = 1, c = \text{'A'}$):
    - Window $[0, 1]$: $cnt = \{A: 2\}$, $mx = 2$
    - Replacements: $2 - 2 = 0 \le k$ (Valid) $\implies l = 0$
  - Step 3 ($r = 2, c = \text{'B'}$):
    - Window $[0, 2]$: $cnt = \{A: 2, B: 1\}$, $mx = 2$
    - Replacements: $3 - 2 = 1 \le k$ (Valid) $\implies l = 0$
  - Step 4 ($r = 3, c = \text{'A'}$):
    - Window $[0, 3]$: $cnt = \{A: 3, B: 1\}$, $mx = 3$
    - Replacements: $4 - 3 = 1 \le k$ (Valid) $\implies l = 0$ (Length 4 reached!)
  - Step 5 ($r = 4, c = \text{'B'}$):
    - Window $[0, 4]$: $cnt = \{A: 3, B: 2\}$, $mx = 3$
    - Replacements: $5 - 3 = 2 > k$ (Invalid!)
    - Shift window: drop $s[0]$ (`'A'`), $cnt[A] \leftarrow 2$, advance $l \leftarrow 1$ (Window $[1, 4]$)
  - Step 6 ($r = 5, c = \text{'B'}$):
    - Window $[1, 5]$: $cnt = \{A: 2, B: 3\}$, $mx = 3$
    - Replacements: $5 - 3 = 2 > k$ (Invalid!)
    - Shift window: drop $s[1]$ (`'A'`), $cnt[A] \leftarrow 1$, advance $l \leftarrow 2$ (Window $[2, 5]$)
  - Step 7 ($r = 6, c = \text{'A'}$):
    - Window $[2, 6]$: $cnt = \{A: 2, B: 3\}$, $mx = 3$
    - Replacements: $5 - 3 = 2 > k$ (Invalid!)
    - Shift window: drop $s[2]$ (`'B'`), $cnt[B] \leftarrow 2$, advance $l \leftarrow 3$ (Window $[3, 6]$)
  - Terminal result:
    $$
    |s| - l = 7 - 3 = \mathbf{4}
    $$
    (e.g. Substring `"AABA"` with 1 replacement becomes `"AAAA"`, or `"BABB"` becomes `"BBBB"`)
- **Full Replacement Budget:** $s = \text{"ABAB"}, k = 2 \implies$ replace both $'B'$s with $'A'$ $\implies \mathbf{4}$
- **Zero Budget ($k = 0$):** $s = \text{"AAAB"} \implies$ longest contiguous block of identical characters $\implies \mathbf{3}$

This instance demonstrates the non-shrinking sliding window technique, mathematically proves why maintaining the historical maximum frequency $mx$ without decrements preserves optimality, and derives $O(N)$ runtime and $O(|\Sigma|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"AABABBA"}$ and an integer $k = 1$:
You can choose any character of the string and change it to any other uppercase English character at most $k$ times.
Find the length of the **longest substring** containing the same letter you can get after performing at most $k$ operations:

```text
String:   A  A  B  A  B  B  A
Indices:  0  1  2  3  4  5  6

Valid Candidate Windows (k = 1):
  Indices [0 .. 3]: "AABA" -> Replace 'B' at 2 with 'A' -> "AAAA" (Length 4)
  Indices [2 .. 5]: "BABB" -> Replace 'A' at 3 with 'B' -> "BBBB" (Length 4)

Maximum Repeating Substring Length: 4
```

### The Feasibility Criterion for a Window
For any window $s[l \dots r]$ of length $W = r - l + 1$:
Let $mx$ be the frequency of the **most frequent character** within that window.
The number of other characters in the window that must be replaced to make all characters identical is:
$$
\text{Replacements Needed} = W - mx
$$
The window is valid if and only if:
$$
W - mx \le k \iff (r - l + 1) - mx \le k
$$

---

## 2. Conceptual Foundation & Invariants

### 1. The Non-Shrinking Window Invariant:
We want to find the **maximum** valid window length $W^*$.
- As the right pointer $r$ expands from $0$ to $N-1$, the window grows whenever a new record or valid state is found.
- If incorporating $s[r]$ causes the current window to become invalid ($W - mx > k$):
  - We do not shrink the window back to length $W - 1$.
  - Instead, we simply **slide** the window forward by incrementing $l \leftarrow l + 1$, maintaining the window size achieved so far.
  - A smaller window can never beat our best recorded length, so shrinking is unnecessary.
- The window only expands when a larger valid state is discovered.
- At the end of the scan, the maximum window size is strictly $N - l$.

### 2. The Monotonicity of $mx$:
Does $mx$ need to be decremented when $l$ advances?
**No!**
- If the true maximum frequency in the contracted window is smaller than the historical $mx$, this smaller frequency cannot help us find a window strictly *larger* than what we have already seen.
- Only a new character that creates a frequency *strictly greater* than the historical $mx$ can enable the window to grow further.
- Therefore, $mx$ only needs to be updated monotonically: $mx \leftarrow \max(mx, cnt[s[r]])$.

> **Invariant.** At every step, the window size $r - l + 1$ is non-decreasing, and the final difference $N - l$ equals the length of the longest valid window.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"AABABBA"}$ with $k = 1$:
Initialize $l = 0, mx = 0, cnt = \{\}$.

---

### Step 1: $r = 0, s[0] = \text{'A'}$
- Increment: $cnt[\text{'A'}] = 1$.
- Dominant frequency: $mx = \max(0, 1) = \mathbf{1}$.
- Window length: $W = 0 - 0 + 1 = 1$.
- Test: $W - mx = 1 - 1 = 0 \le k (1)$ (**Valid**).
- State: $l = 0$, Window $[0, 0]$ (`"A"`).

---

### Step 2: $r = 1, s[1] = \text{'A'}$
- Increment: $cnt[\text{'A'}] = 2$.
- Dominant frequency: $mx = \max(1, 2) = \mathbf{2}$.
- Window length: $W = 1 - 0 + 1 = 2$.
- Test: $W - mx = 2 - 2 = 0 \le 1$ (**Valid**).
- State: $l = 0$, Window $[0, 1]$ (`"AA"`).

---

### Step 3: $r = 2, s[2] = \text{'B'}$
- Increment: $cnt[\text{'B'}] = 1$.
- Dominant frequency: $mx = \max(2, 1) = \mathbf{2}$.
- Window length: $W = 2 - 0 + 1 = 3$.
- Test: $W - mx = 3 - 2 = 1 \le 1$ (**Valid**).
- State: $l = 0$, Window $[0, 2]$ (`"AAB"`).

---

### Step 4: $r = 3, s[3] = \text{'A'}$
- Increment: $cnt[\text{'A'}] = 3$.
- Dominant frequency: $mx = \max(2, 3) = \mathbf{3}$.
- Window length: $W = 3 - 0 + 1 = 4$.
- Test: $W - mx = 4 - 3 = 1 \le 1$ (**Valid**).
- State: $l = 0$, Window $[0, 3]$ (`"AABA"`). Length 4 reached!

---

### Step 5: $r = 4, s[4] = \text{'B'}$
- Increment: $cnt[\text{'B'}] = 2$.
- Dominant frequency: $mx = \max(3, 2) = \mathbf{3}$.
- Window length: $W = 4 - 0 + 1 = 5$.
- Test: $W - mx = 5 - 3 = 2 > k (1)$ (**Invalid!** Needs 2 replacements).
- Action: Slide window by advancing left pointer:
  $$
  cnt[s[l]] = cnt[s[0]] = cnt[\text{'A'}] \leftarrow 3 - 1 = 2
  $$
  $$
  l \leftarrow 0 + 1 = \mathbf{1}
  $$
- State: $l = 1$, Window $[1, 4]$ (`"ABAB"`), length remains 4.

---

### Step 6: $r = 5, s[5] = \text{'B'}$
- Increment: $cnt[\text{'B'}] = 3$.
- Dominant frequency: $mx = \max(3, 3) = \mathbf{3}$.
- Window length: $W = 5 - 1 + 1 = 5$.
- Test: $W - mx = 5 - 3 = 2 > 1$ (**Invalid!**).
- Action: Slide window:
  $$
  cnt[s[1]] = cnt[\text{'A'}] \leftarrow 2 - 1 = 1
  $$
  $$
  l \leftarrow 1 + 1 = \mathbf{2}
  $$
- State: $l = 2$, Window $[2, 5]$ (`"BABB"`), length remains 4.

---

### Step 7: $r = 6, s[6] = \text{'A'}$
- Increment: $cnt[\text{'A'}] = 2$.
- Dominant frequency: $mx = \max(3, 2) = \mathbf{3}$.
- Window length: $W = 6 - 2 + 1 = 5$.
- Test: $W - mx = 5 - 3 = 2 > 1$ (**Invalid!**).
- Action: Slide window:
  $$
  cnt[s[2]] = cnt[\text{'B'}] \leftarrow 3 - 1 = 2
  $$
  $$
  l \leftarrow 2 + 1 = \mathbf{3}
  $$
- State: $l = 3$, Window $[3, 6]$ (`"ABBA"`), length remains 4.

---

### Termination:
Loop over $r$ completes. Maximum window length:
$$
\text{Max Length} = |s| - l = 7 - 3 = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Right $r$ | Char $s[r]$ | Frequency Map $cnt$ | Dominant $mx$ | Window $[l, r]$ | Length $W$ | Budget Test $W - mx \le 1$ | Left Shift $l$ | Effective Window Size |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | `'A'` | `{A: 1}` | $1$ | $[0, 0]$ (`"A"`) | $1$ | $0 \le 1$ (Pass) | $0$ | $1$ |
| **1** | `'A'` | `{A: 2}` | $2$ | $[0, 1]$ (`"AA"`) | $2$ | $0 \le 1$ (Pass) | $0$ | $2$ |
| **2** | `'B'` | `{A: 2, B: 1}` | $2$ | $[0, 2]$ (`"AAB"`) | $3$ | $1 \le 1$ (Pass) | $0$ | $3$ |
| **3** | `'A'` | `{A: 3, B: 1}` | $3$ | $[0, 3]$ (`"AABA"`) | $4$ | $1 \le 1$ (Pass) | $0$ | **$4$** |
| **4** | `'B'` | `{A: 2, B: 2}` | $3$ | $[1, 4]$ (`"ABAB"`) | $5 \to 4$ | $2 > 1$ (**Slide**) | $0 \to \mathbf{1}$ | $4$ |
| **5** | `'B'` | `{A: 1, B: 3}` | $3$ | $[2, 5]$ (`"BABB"`) | $5 \to 4$ | $2 > 1$ (**Slide**) | $1 \to \mathbf{2}$ | $4$ |
| **6** | `'A'` | `{A: 2, B: 2}` | $3$ | $[3, 6]$ (`"ABBA"`) | $5 \to 4$ | $2 > 1$ (**Slide**) | $2 \to \mathbf{3}$ | $4$ |
| **End** | — | — | — | — | — | — | $l = 3$ | **Result: $7 - 3 = \mathbf{4}$** |

---

## 5. Boundary Cases & Failure Modes

- **Budget Exceeds String Length ($k \ge |s|$):** Can replace all characters to match any chosen letter. Output is $|s|$.
- **Zero Replacement Budget ($k = 0$):** $W - mx \le 0 \implies W = mx$, requiring all characters in the window to be identical. Correctly finds the longest contiguous run of equal characters.
- **Single Distinct Character ($s = \text{"AAAAA"}, k = 2$):** $mx = W$ throughout. Output is $5$.
- **All Unique Characters ($s = \text{"ABCDE"}, k = 1$):** $mx = 1$. Maximum window length is $1 + 1 = 2$.

---

## 6. Traps & Common Anti-Patterns

- **Rescanning the Alphabet to Recalculate $mx$:** Recomputing $\max(cnt.values())$ by scanning all 26 uppercase letters upon every left pointer advance is unnecessary. Since a smaller $mx$ cannot expand the window, keeping $mx$ non-decreasing preserves the optimal window size with zero extra work.
- **Shrinking the Window with a `while` Loop:** Using `while (r - l + 1) - mx > k: l += 1` shrinks the window when it becomes invalid. While functionally correct, it performs redundant left advances. A simple `if` condition slides the window without ever reducing its size.
- **Quadratic Substring Enumeration ($O(N^2)$):** Checking all $O(N^2)$ pairs $(l, r)$ exceeds time limits for $|s| = 10^5$. Linear two-pointer sliding window runs in under 15 ms.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The right pointer $r$ advances from $0$ to $N - 1$ in $N$ steps.
  - The left pointer $l$ advances at most once per right step, totaling at most $N$ increments.
  - Dictionary updates and comparisons take $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|) = \mathcal{O}(1)$. The frequency map stores at most 26 uppercase English letters.
