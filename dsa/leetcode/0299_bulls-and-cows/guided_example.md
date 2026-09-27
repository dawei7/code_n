# Guided Example: Bulls and Cows

We trace the step-by-step positional match detection (Bulls `A`), mismatched digit frequency multiset aggregation, minimum occurrence intersection for non-positional matches (Cows `B`), and formatted string generation on representative game instances:

- **Input:** $\text{secret} = \text{"1807"}, \quad \text{guess} = \text{"7810"}$
- **Required output:** `"1A3B"`
  - Bull: Digit `'8'` at index 1 matches in both value and position ($1\text{A}$)
  - Cows: Digits `'0'`, `'1'`, and `'7'` appear in both strings but at different positions ($3\text{B}$)
- **Duplicate Digit Multiplicity:** $\text{secret} = \text{"1123"}, \quad \text{guess} = \text{"0111"} \implies \text{"1A1B"}$ (One bull at index 1; among remaining digits, digit `'1'` has 1 copy in secret and 2 in guess $\implies \min(1, 2) = 1$ cow)
- **Zero Matches Base Case:** $\text{secret} = \text{"1111"}, \quad \text{guess} = \text{"2222"} \implies \text{"0A0B"}$
- **All Bulls Perfect Match:** $\text{secret} = \text{"1234"}, \quad \text{guess} = \text{"1234"} \implies \text{"4A0B"}$

This instance demonstrates two-pass frequency multiset intersection, explains why bulls must be removed prior to counting cows to prevent double-counting positional matches, proves why the cow count for each digit equals the minimum of its unmatched frequencies ($\min(cnt_1[c], cnt_2[c])$), and operates in strictly $O(N)$ linear time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given two equal-length numerical strings:
$$
\text{secret} = \text{"1807"}, \quad \text{guess} = \text{"7810"}
$$
Determine the hint in the format `"xAyB"`:
- `x` (Bulls): Number of digits that match in **both value and exact position**.
- `y` (Cows): Number of digits that match in **value only** (located in the wrong position).

```text
Index:     0   1   2   3
Secret:    1   8   0   7
Guess:     7   8   1   0
           |   |   |   |
Status:   Diff Same Diff Diff
           |   |   |   |
          Cow  Bull Cow Cow

Total Bulls = 1 ('8' at index 1)
Total Cows  = 3 ('0', '1', '7' present at mismatched indices)
Output: "1A3B"
```

### The Priority Invariant: Bulls Exclude Cows
A digit matched as a bull **cannot** be reused as a cow.
If `secret = "1123"` and `guess = "0111"`:
- Index 1 matches: `secret[1] == guess[1] == '1'`. This is locked as a Bull.
- This consumed occurrence of `'1'` is removed from both strings.
- Remaining secret digits: `{'1': 1, '2': 1, '3': 1}`.
- Remaining guess digits: `{'0': 1, '1': 2}`.
- For digit `'1'`: Secret has 1 available, Guess has 2.
  Number of cows formed is $\min(1, 2) = \mathbf{1}$.

---

## 2. Conceptual Foundation & Invariants

### Dual-Counter Frequency Protocol
Let $x$ represent bulls and $y$ represent cows.
1. **Pass 1: Detect Bulls & Count Mismatches:**
   Iterate through aligned pairs $(a, b) \in \text{zip}(\text{secret}, \text{guess})$:
   - If $a == b$:
     $$
     x \leftarrow x + 1 \quad (\text{Bull detected})
     $$
   - Else ($a \ne b$):
     Increment independent mismatch frequency counters:
     $$
     cnt_1[a] \leftarrow cnt_1[a] + 1 \quad (\text{Unmatched in secret})
     $$
     $$
     cnt_2[b] \leftarrow cnt_2[b] + 1 \quad (\text{Unmatched in guess})
     $$
2. **Pass 2: Compute Cows via Multiset Intersection:**
   For each distinct digit $c$ present in $cnt_1$:
   The number of valid non-positional pairings for digit $c$ is strictly bounded by the occurrences available in both strings:
   $$
   y = \sum_{c \in cnt_1} \min(cnt_1[c], \; cnt_2[c])
   $$
3. **Format Result:** Return formatted string `f"{x}A{y}B"`.

> **Invariant.** Every character index is either classified as a bull (if values match identically at that index) or routed into frequency pools $cnt_1$ and $cnt_2$. No digit can be counted as both a bull and a cow.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{secret} = \text{"1807"}$ and $\text{guess} = \text{"7810"}$ ($N = 4$):
Initialize $x = 0$, $cnt_1 = \{\}$, $cnt_2 = \{\}$.

---

### Step 1: Sequential Pair Inspection

- **Index 0 ($a = \text{'1'}, \; b = \text{'7'}):$**
  $a \ne b$ ($1 \ne 7$).
  $cnt_1[\text{'1'}] \mathrel{+}= 1 \implies cnt_1 = \{\text{'1'}: 1\}$.
  $cnt_2[\text{'7'}] \mathrel{+}= 1 \implies cnt_2 = \{\text{'7'}: 1\}$.
  $x = 0$.

- **Index 1 ($a = \text{'8'}, \; b = \text{'8'}):$**
  $a == b$ ($8 == 8$).
  Bull detected!
  $x \leftarrow 0 + 1 = \mathbf{1}$.
  *(Neither counter is updated; digit 8 at index 1 is consumed)*.

- **Index 2 ($a = \text{'0'}, \; b = \text{'1'}):$**
  $a \ne b$ ($0 \ne 1$).
  $cnt_1[\text{'0'}] \mathrel{+}= 1 \implies cnt_1 = \{\text{'1'}: 1, \text{'0'}: 1\}$.
  $cnt_2[\text{'1'}] \mathrel{+}= 1 \implies cnt_2 = \{\text{'7'}: 1, \text{'1'}: 1\}$.
  $x = 1$.

- **Index 3 ($a = \text{'7'}, \; b = \text{'0'}):$**
  $a \ne b$ ($7 \ne 0$).
  $cnt_1[\text{'7'}] \mathrel{+}= 1 \implies cnt_1 = \{\text{'1'}: 1, \text{'0'}: 1, \text{'7'}: 1\}$.
  $cnt_2[\text{'0'}] \mathrel{+}= 1 \implies cnt_2 = \{\text{'7'}: 1, \text{'1'}: 1, \text{'0'}: 1\}$.
  $x = 1$.

End of Pass 1:
- Total Bulls $x = \mathbf{1}$.
- Unmatched Secret Counts: $cnt_1 = \{\text{'0'}: 1, \; \text{'1'}: 1, \; \text{'7'}: 1\}$.
- Unmatched Guess Counts: $cnt_2 = \{\text{'0'}: 1, \; \text{'1'}: 1, \; \text{'7'}: 1\}$.

---

### Step 2: Compute Cows Summation
Evaluate $\min(cnt_1[c], cnt_2[c])$ across all keys in $cnt_1$:
- For digit `'0'`: $\min(cnt_1[\text{'0'}], cnt_2[\text{'0'}]) = \min(1, 1) = \mathbf{1}$.
- For digit `'1'`: $\min(cnt_1[\text{'1'}], cnt_2[\text{'1'}]) = \min(1, 1) = \mathbf{1}$.
- For digit `'7'`: $\min(cnt_1[\text{'7'}], cnt_2[\text{'7'}]) = \min(1, 1) = \mathbf{1}$.

Total cows:
$$
y = 1 + 1 + 1 = \mathbf{3}
$$

---

### Step 3: Format Final Result
$$
\text{Result} = f"{x}\text{A}{y}\text{B}" = \mathbf{\text{"1A3B"}}
$$

---

## 4. Complete Execution Trace

```text
secret = "1807", guess = "7810"

i = 0: '1' != '7' -> cnt1['1']+=1, cnt2['7']+=1
i = 1: '8' == '8' -> Bull! x = 1
i = 2: '0' != '1' -> cnt1['0']+=1, cnt2['1']+=1
i = 3: '7' != '0' -> cnt1['7']+=1, cnt2['0']+=1

Bulls x = 1
Cows y = min(1, 1) [0] + min(1, 1) [1] + min(1, 1) [7] = 1 + 1 + 1 = 3

Result: "1A3B"
```

| Index $i$ | $\text{secret}[i]$ | $\text{guess}[i]$ | Classification | Action Taken | Bulls $x$ | $cnt_1$ (Secret) | $cnt_2$ (Guess) |
|:---:|:---:|:---:|:---:|:---|:---:|:---|:---|
| 0 | `'1'` | `'7'` | Mismatch | Increment $cnt_1[\text{'1'}], cnt_2[\text{'7'}]$ | 0 | `{'1': 1}` | `{'7': 1}` |
| **1** | **`'8'`** | **`'8'`** | **Bull** | **$x \leftarrow x + 1$** | **1** | `{'1': 1}` | `{'7': 1}` |
| 2 | `'0'` | `'1'` | Mismatch | Increment $cnt_1[\text{'0'}], cnt_2[\text{'1'}]$ | 1 | `{'1': 1, '0': 1}` | `{'7': 1, '1': 1}` |
| 3 | `'7'` | `'0'` | Mismatch | Increment $cnt_1[\text{'7'}], cnt_2[\text{'0'}]$ | 1 | `{'1': 1, '0': 1, '7': 1}` | `{'7': 1, '1': 1, '0': 1}` |
| **Cows** | - | - | - | $\sum \min(cnt_1, cnt_2)$ | **$1\text{A}$** | - | **$3\text{B}$** |

---

### Duplicate Trace Contrast (`secret = "1123", guess = "0111"`)
- Index 1 matches `'1' == '1'` $\implies x = 1$ (Bull).
- Mismatches:
  - $cnt_1$: `{'1': 1, '2': 1, '3': 1}`
  - $cnt_2$: `{'0': 1, '1': 2}`
- Cow evaluation for `'1'`: $\min(cnt_1[\text{'1'}], cnt_2[\text{'1'}]) = \min(1, 2) = \mathbf{1}$.
- Result: `"1A1B"`.

---

## 5. Algorithmic Correctness

**Soundness.** Every index where $\text{secret}[i] == \text{guess}[i]$ is counted as a bull and withheld from frequency tables, satisfying the rule that bulls take precedence over cows. For any digit $d$, the number of cows formed cannot exceed the number of available unmatched copies in either string, making $\min(cnt_1[d], cnt_2[d])$ both sound and exact.

**Completeness.** Every character index in both strings is processed. Because digits are independent, summing the minimum counts over all distinct digits exhaustively computes all possible non-positional pairings without omission.

---

## 6. Traps This Instance Exposes

- **Counting Bulls as Cows:** If frequency counts are built from the full strings without first removing bulls, positions where digits matched identically would be double-counted as cows.
- **Set Intersection vs Multiset Frequencies:** Using sets (`set(secret) & set(guess)`) discards digit multiplicities. If `secret` has two `'1'`s and `guess` has three `'1'`s, set intersection yields count 1, ignoring the second valid pair. Frequency counting via `Counter` preserves exact multiplicities.
- **Fixed Alphabet Size Optimization:** Digits consist only of characters `'0'` through `'9'`. Frequency tables have at most 10 keys, bounding the second pass to at most 10 operations regardless of string length.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `secret` and `guess`. The initial loop iterates $N$ times with $O(1)$ operations per character. The second loop iterates over at most 10 distinct digits ($O(1)$ work). Total time is strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory. The counters store frequencies for at most 10 decimal digits (`'0'` through `'9'`), which is constant size independent of $N$.
