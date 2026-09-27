# Guided Example: Next Greater Element III

We trace the step-by-step next lexicographical permutation algorithm (Narayana Pandita method), right-to-left pivot discovery ($cs[i] < cs[i+1]$), minimal strictly-greater successor selection ($cs[j] > cs[i]$), prefix swap, descending suffix reversal ($cs[i+1:][::-1]$), and 32-bit signed integer overflow bound validation ($ans \le 2^{31} - 1$) on representative integers:

- **Input:** $n = 230241$
- **Required output:** `230412`
  - Problem objective: Rearrange the exact decimal digits of $n$ to form the **smallest integer strictly greater than $n$**.
  - Constraints: If digits are strictly descending (no greater permutation exists), or if the answer exceeds the 32-bit signed integer maximum ($2^{31} - 1 = 2{,}147{,}483{,}647$), return `-1`.
- **Next Permutation Digit Execution Trace:**
  - Convert $n$ into a mutable array of decimal character digits:
    $$
    cs = [\text{'2'}, \text{'3'}, \text{'0'}, \text{'2'}, \text{'4'}, \text{'1'}] \quad (\text{length } 6)
    $$
  - **Step 1: Find the Pivot Index $i$ (First Decrease from the Right):**
    - Inspect adjacent digit pairs moving leftwards:
      - $cs[4] = \text{'4'}, \; cs[5] = \text{'1'} \implies 4 \ge 1$ (Descending)
      - $cs[3] = \text{'2'}, \; cs[4] = \text{'4'} \implies 2 < 4$ (**Ascent found!**)
    - Pivot index located at:
      $$
      i = \mathbf{3} \quad (cs[3] = \text{'2'})
      $$
    - *(The suffix $cs[4 \dots 5] = \text{"41"}$ is already in maximum descending order; to make the number larger, we must change digit $cs[3]$)*.
  - **Step 2: Find the Smallest Greater Successor $j$ in the Suffix:**
    - Scan the suffix from right to left ($j = 5 \to 4$) to find the first digit strictly greater than $cs[i] = \text{'2'}$:
      - At $j = 5$: $cs[5] = \text{'1'} \ngtr \text{'2'}$.
      - At $j = 4$: $cs[4] = \text{'4'} > \text{'2'}$.
    - Successor index:
      $$
      j = \mathbf{4} \quad (cs[4] = \text{'4'})
      $$
  - **Step 3: Swap Pivot and Successor:**
    - Swap $cs[i]$ and $cs[j]$ ($cs[3] \leftrightarrow cs[4]$):
      $$
      cs[3] \leftarrow \text{'4'}, \quad cs[4] \leftarrow \text{'2'}
      $$
    - Intermediate array:
      $$
      cs = [\text{'2'}, \text{'3'}, \text{'0'}, \mathbf{\text{'4'}}, \mathbf{\text{'2'}}, \text{'1'}]
      $$
  - **Step 4: Reverse the Suffix to Minimize its Value:**
    - The suffix starting at index $i + 1 = 4$ is currently $cs[4 \dots 5] = [\text{'2'}, \text{'1'}]$ (still in descending order).
    - To make the total number as small as possible, reverse this suffix into ascending order:
      $$
      [\text{'2'}, \text{'1'}] \to [\mathbf{\text{'1'}}, \mathbf{\text{'2'}}]
      $$
    - Resulting digit array:
      $$
      cs = [\text{'2'}, \text{'3'}, \text{'0'}, \text{'4'}, \mathbf{\text{'1'}}, \mathbf{\text{'2'}}]
      $$
  - **Step 5: Parse and Check 32-Bit Integer Bound:**
    - Numerical value:
      $$
      ans = \mathbf{230412}
      $$
    - 32-bit limit check:
      $$
      230412 \le 2^{31} - 1 = 2{,}147{,}483{,}647 \implies \mathbf{Valid!}
      $$
    - Final answer: **`230412`**.
- **Descending Digits Instance ($n = 21$):**
  - Digits `['2', '1']`. Scanner $i$ moves past index 0 without finding any increase ($i = -1$).
  - No greater permutation exists $\implies \mathbf{-1}$.
- **Simple Two-Digit Swap ($n = 12$):**
  - $i = 0, j = 1 \implies$ swap 1 and 2 $\implies \mathbf{21}$.
- **32-Bit Overflow Disqualification ($n = 1{,}999{,}999{,}999$):**
  - Permuting digits yields a number $> 2^{31} - 1 \implies \mathbf{-1}$.

This instance demonstrates in-place lexicographical permutation advancement, mathematically proves why suffix reversal minimizes the successor configuration, and derives $O(D)$ runtime and $O(D)$ space bounds (where $D \le 10$ is the number of decimal digits).

---

## 1. Instance & Teaching Goal

Given a positive 32-bit integer $n$:
Find the **smallest integer** that can be formed using the exact same digits as $n$ and is strictly greater than $n$.
If no such number exists, or if it exceeds the 32-bit signed integer limit ($2^{31} - 1$), return `-1`.

```text
Input: n = 230241

Digits: [ 2,  3,  0,  2,  4,  1 ]
                      ^
          Pivot i = 3 (first decrease from right: 2 < 4)

Find smallest digit in suffix [4, 1] greater than 2:
  Digit 4 (at index 4)

Swap pivot and successor:
  [ 2,  3,  0,  4,  2,  1 ]

Reverse suffix [2, 1] -> [1, 2]:
  [ 2,  3,  0,  4,  1,  2 ]

Result: 230412
```

### The Invariant of Lexicographical Permutations
- Any descending sequence of digits (e.g. $4, 3, 1$) is in its **absolute maximum possible configuration**; it cannot be made larger without altering an earlier digit.
- To produce the *next smallest* larger permutation:
  1. We must locate the rightmost position $i$ that can be made larger ($cs[i] < cs[i+1]$).
  2. We swap $cs[i]$ with the smallest possible digit in the suffix that is strictly greater than $cs[i]$ (ensuring the new digit at $i$ is as small as possible while still increasing the overall value).
  3. We sort the remaining suffix in ascending order (by reversing it) to ensure the suffix contributes the minimum possible value.

---

## 2. Conceptual Foundation & Invariants

### 1. The Algorithm:
1. Scan $i$ from $n - 2$ down to $0$:
   Find the first index where $cs[i] < cs[i + 1]$.
   If $i < 0$, the digits are already in maximal descending order $\implies$ return $-1$.
2. Scan $j$ from $n - 1$ down to $i + 1$:
   Find the first index where $cs[j] > cs[i]$.
3. Swap $cs[i]$ and $cs[j]$.
4. Reverse the suffix $cs[i + 1 : n]$.
5. Parse integer $ans = \text{int}(\text{"".join}(cs))$.
6. If $ans > 2^{31} - 1$, return $-1$; else return $ans$.

> **Minimality Invariant.** Choosing the smallest possible successor for $cs[i]$ and flipping the suffix from descending to ascending order guarantees that no intermediate valid permutation exists between $n$ and $ans$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 230241$:

---

### Step 1: Find Pivot $i$
- $cs = ['2', '3', '0', '2', '4', '1']$
- $cs[4] \ge cs[5]$ ($4 \ge 1$)
- $cs[3] < cs[4]$ ($2 < 4$) $\implies i = \mathbf{3}$.

---

### Step 2: Find Successor $j$
Scan from right end ($j = 5$ down):
- $cs[5] = \text{'1'} \ngtr \text{'2'}$
- $cs[4] = \text{'4'} > \text{'2'} \implies j = \mathbf{4}$.

---

### Step 3: Swap $cs[3]$ and $cs[4]$
- Swap `'2'` and `'4'`:
  $$
  cs = ['2', '3', '0', \mathbf{\text{'4'}}, \mathbf{\text{'2'}}, '1']
  $$

---

### Step 4: Reverse Suffix $cs[4:]$
- Suffix is `['2', '1']`.
- Reversed: `['1', '2']`.
- Array becomes:
  $$
  cs = ['2', '3', '0', '4', \mathbf{\text{'1'}}, \mathbf{\text{'2'}}]
  $$

---

### Step 5: Convert and Verify Bounds
- Parsed value: $230412$.
- Bound: $230412 \le 2147483647$.
- Return:
  $$
  \mathbf{230412}
  $$

---

## 4. Complete Execution Trace

| Step | Array State $cs$ | Target Pointers | Comparison / Action | Next State |
|:---:|:---:|:---:|:---:|:---:|
| **Init** | `['2', '3', '0', '2', '4', '1']` | $i = 4 \to 3$ | $cs[3] < cs[4]$ ($2 < 4$) | $i = 3$ |
| **Successor** | `['2', '3', '0', '2', '4', '1']` | $j = 5 \to 4$ | $cs[4] > cs[3]$ ($4 > 2$) | $j = 4$ |
| **Swap** | `['2', '3', '0', '4', '2', '1']` | $i = 3, j = 4$ | Swap $cs[3]$ and $cs[4]$ | Digits swapped |
| **Reverse** | `['2', '3', '0', '4', '1', '2']` | Slice $cs[4:]$ | Reverse `['2', '1']` to `['1', '2']` | Suffix ascending |
| **Validate** | $230412$ | Limit Check | $230412 \le 2^{31} - 1$ | **Valid: `230412`** |

---

## 5. Boundary Cases & Failure Modes

- **Strictly Descending ($21$ or $98765$):** $i$ falls below 0 without finding an ascent $\implies \mathbf{-1}$.
- **All Digits Identical ($1111$):** Digits are equal $\implies i < 0 \implies \mathbf{-1}$.
- **32-Bit Overflow ($2147483647$):** Valid next permutation exceeds $2^{31} - 1 \implies \mathbf{-1}$.
- **Two Digits ($12 \to 21$):** Single swap and empty suffix $\implies \mathbf{21}$.

---

## 6. Traps & Common Anti-Patterns

- **Searching from Left to Right:** Modifying higher-order digits earlier increases the number far more than necessary. The pivot must be found from the **rightmost** possible position.
- **Forgetting the Suffix Reversal:** Swapping $cs[i]$ and $cs[j]$ leaves the suffix in descending order. Forgetting to reverse the suffix produces an unnecessarily large number instead of the *smallest* larger one.
- **Ignoring 32-Bit Integer Limit:** In Python, integers have arbitrary precision and do not automatically overflow. Explicitly checking `ans > 2**31 - 1` is strictly required by the contract.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - An integer $n \le 2^{31} - 1$ has at most $D = 10$ decimal digits.
  - Scanning for $i$ takes at most $D$ steps.
  - Scanning for $j$ takes at most $D$ steps.
  - Reversing the suffix takes at most $D/2$ steps.
  - Total Time: $\mathcal{O}(D)$ operations, where $D \le 10$. Completes in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(D)$ space to store the list of digit characters ($D \le 10$).
