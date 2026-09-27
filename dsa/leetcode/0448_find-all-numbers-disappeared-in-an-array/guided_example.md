# Guided Example: Find All Numbers Disappeared in an Array

We trace the step-by-step in-place index sign-negation marking ($nums[|x| - 1] \leftarrow -|nums[|x| - 1]|$), presence flag encoding, unvisited positive-index identification ($nums[i] > 0 \implies i + 1$), and missing number extraction on representative integer arrays:

- **Input:** $nums = [4, 3, 2, 7, 8, 2, 3, 1]$
- **Required output:** `[5, 6]`
  - Array length: $n = 8$, values in range $[1, 8]$
  - Ideal complete set: $\{1, 2, 3, 4, 5, 6, 7, 8\}$
- **In-place sign-negation execution trace:**
  - Presence encoding rule: Encountering value $v$ marks index $v - 1$ negative.
  - **Pass 1: Negate target indices based on observed values:**
    - Value $4 \implies$ Mark index $3$: $nums[3] = 7 \to \mathbf{-7}$
    - Value $3 \implies$ Mark index $2$: $nums[2] = 2 \to \mathbf{-2}$
    - Value $2 \implies$ Mark index $1$: $nums[1] = 3 \to \mathbf{-3}$
    - Value $|-7| = 7 \implies$ Mark index $6$: $nums[6] = 3 \to \mathbf{-3}$
    - Value $8 \implies$ Mark index $7$: $nums[7] = 1 \to \mathbf{-1}$
    - Value $2 \implies$ Index $1$ already negative ($-3$). Unchanged.
    - Value $|-3| = 3 \implies$ Index $2$ already negative ($-2$). Unchanged.
    - Value $|-1| = 1 \implies$ Mark index $0$: $nums[0] = 4 \to \mathbf{-4}$
  - Array state after Pass 1:
    $$
    nums = [\mathbf{-4}, \; \mathbf{-3}, \; \mathbf{-2}, \; \mathbf{-7}, \; \mathbf{8}, \; \mathbf{2}, \; \mathbf{-3}, \; \mathbf{-1}]
    $$
  - **Pass 2: Scan for indices that remain positive:**
    - Index 0: $-4 < 0$ (Value 1 was present)
    - Index 1: $-3 < 0$ (Value 2 was present)
    - Index 2: $-2 < 0$ (Value 3 was present)
    - Index 3: $-7 < 0$ (Value 4 was present)
    - **Index 4: $8 > 0$** $\implies$ Value $4 + 1 = \mathbf{5}$ is **absent**!
    - **Index 5: $2 > 0$** $\implies$ Value $5 + 1 = \mathbf{6}$ is **absent**!
    - Index 6: $-3 < 0$ (Value 7 was present)
    - Index 7: $-1 < 0$ (Value 8 was present)
  - Missing integers: `[5, 6]`
- **Single Missing Value:** $nums = [1, 1] \implies$ Index 0 negated, Index 1 remains positive $\implies \mathbf{[2]}$
- **Complete Permutation:** $nums = [1, 2, 3] \implies$ All indices negated $\implies \mathbf{[]}$

This instance demonstrates in-place bitwise/sign state multiplexing, mathematically proves how index-addressing achieves $O(1)$ auxiliary space without memory reallocation, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array $nums = [4, 3, 2, 7, 8, 2, 3, 1]$ of $n = 8$ integers where each integer is in the range $[1, n]$:
Some elements appear twice and others appear once.
Find all the integers in the range $[1, n]$ that **do not appear** in $nums$.
Solve this in **$O(N)$ time** and **$O(1)$ extra space**.

```text
Expected Elements: 1, 2, 3, 4, 5, 6, 7, 8
Observed Elements: 1, 2, 3, 4,       7, 8  (with duplicates 2 and 3)

Missing Numbers:   5, 6
```

### The In-Place Multiplexing Technique
A standard boolean array `visited[1 .. n]` solves the problem in $O(N)$ time, but uses $O(N)$ auxiliary memory.
Because $1 \le nums[i] \le n$:
- Every valid number $x$ corresponds to a unique 0-indexed position: $x - 1$.
- We can store two pieces of information in each cell:
  1. The **original magnitude**: $|nums[i]|$ preserves the initial value.
  2. The **visitation status**: The arithmetic sign (positive vs. negative) indicates whether the integer $i + 1$ was ever seen in the input.

---

## 2. Conceptual Foundation & Invariants

### 1. In-Place Sign Encoding:
For each element $x$ in $nums$:
- Compute the home index corresponding to its absolute value:
  $$
  idx = |x| - 1
  $$
- Mark index $idx$ as visited by making its value strictly negative:
  $$
  nums[idx] \leftarrow -|nums[idx]|
  $$
- If index $idx$ was already negative, it remains negative (idempotent operation).
- Using absolute values $|x|$ ensures that reading a previously negated cell still recovers the true original value.

### 2. Output Identification:
After marking all elements:
- If integer $k \in [1, n]$ was present at least once in the input, cell $nums[k - 1]$ was negated and is $< 0$.
- If integer $k$ was absent from the input, cell $nums[k - 1]$ was never targeted and remains $> 0$.
- Therefore, scanning the array and collecting all $i + 1$ where $nums[i] > 0$ produces the exact list of missing numbers.

> **Encoding Invariant.** Cell $nums[i] < 0$ if and only if the integer $i + 1$ appeared at least once in the original input array.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [4, 3, 2, 7, 8, 2, 3, 1]$ ($n = 8$):

---

### Pass 1: Sign Inversion Walk

1. **At $i = 0$:** Value is $4$. Target index: $|4| - 1 = 3$.
   - Negate $nums[3]$: $7 \to \mathbf{-7}$.
   - Array: $[4, 3, 2, \mathbf{-7}, 8, 2, 3, 1]$.
2. **At $i = 1$:** Value is $3$. Target index: $|3| - 1 = 2$.
   - Negate $nums[2]$: $2 \to \mathbf{-2}$.
   - Array: $[4, 3, \mathbf{-2}, -7, 8, 2, 3, 1]$.
3. **At $i = 2$:** Current cell is $-2$. Magnitude is $|-2| = 2$. Target index: $2 - 1 = 1$.
   - Negate $nums[1]$: $3 \to \mathbf{-3}$.
   - Array: $[4, \mathbf{-3}, -2, -7, 8, 2, 3, 1]$.
4. **At $i = 3$:** Current cell is $-7$. Magnitude is $|-7| = 7$. Target index: $7 - 1 = 6$.
   - Negate $nums[6]$: $3 \to \mathbf{-3}$.
   - Array: $[4, -3, -2, -7, 8, 2, \mathbf{-3}, 1]$.
5. **At $i = 4$:** Value is $8$. Target index: $|8| - 1 = 7$.
   - Negate $nums[7]$: $1 \to \mathbf{-1}$.
   - Array: $[4, -3, -2, -7, 8, 2, -3, \mathbf{-1}]$.
6. **At $i = 5$:** Value is $2$. Target index: $|2| - 1 = 1$.
   - Cell $nums[1]$ is already negative ($-3$). Left negative.
7. **At $i = 6$:** Current cell is $-3$. Magnitude is $|-3| = 3$. Target index: $3 - 1 = 2$.
   - Cell $nums[2]$ is already negative ($-2$). Left negative.
8. **At $i = 7$:** Current cell is $-1$. Magnitude is $|-1| = 1$. Target index: $1 - 1 = 0$.
   - Negate $nums[0]$: $4 \to \mathbf{-4}$.
   - Array: $[\mathbf{-4}, -3, -2, -7, 8, 2, -3, -1]$.

---

### Pass 2: Identification of Unmarked Indices

Scan indices $i \in [0, 7]$:
- $i = 0: nums[0] = -4 < 0 \implies$ Number $1$ present.
- $i = 1: nums[1] = -3 < 0 \implies$ Number $2$ present.
- $i = 2: nums[2] = -2 < 0 \implies$ Number $3$ present.
- $i = 3: nums[3] = -7 < 0 \implies$ Number $4$ present.
- $i = 4: nums[4] = \mathbf{8 > 0} \implies$ **Number $4 + 1 = \mathbf{5}$ missing!**
- $i = 5: nums[5] = \mathbf{2 > 0} \implies$ **Number $5 + 1 = \mathbf{6}$ missing!**
- $i = 6: nums[6] = -3 < 0 \implies$ Number $7$ present.
- $i = 7: nums[7] = -1 < 0 \implies$ Number $8$ present.

---

### Final Result:
Disappeared numbers: **`[5, 6]`**.

---

## 4. Complete Execution Trace

| Scanned Element | Target Index $|x| - 1$ | Target Value Before | Target Value After | State Meaning Encoded |
|:---:|:---:|:---:|:---:|:---|
| $4$ | $3$ | $7$ | **$-7$** | Number 4 observed |
| $3$ | $2$ | $2$ | **$-2$** | Number 3 observed |
| $-2$ | $1$ | $3$ | **$-3$** | Number 2 observed |
| $-7$ | $6$ | $3$ | **$-3$** | Number 7 observed |
| $8$ | $7$ | $1$ | **$-1$** | Number 8 observed |
| $2$ | $1$ | $-3$ | $-3$ | Number 2 repeated (no change) |
| $-3$ | $2$ | $-2$ | $-2$ | Number 3 repeated (no change) |
| $-1$ | $0$ | $4$ | **$-4$** | Number 1 observed |
| **Pass 2** | Inspect signs | — | — | **Indices 4 and 5 remain $> 0 \implies [5, 6]$** |

---

## 5. Boundary Cases & Failure Modes

- **No Missing Numbers ($[1, 2, 3]$):** All cells negated. Emits empty list `[]`.
- **All Identical Elements ($[1, 1, 1, 1]$):** Only index 0 negated. Indices 1, 2, 3 remain positive $\implies [2, 3, 4]$.
- **Single Element ($[1]$):** Index 0 negated $\implies []$.
- **Alternating Pairs ($[2, 2, 4, 4]$):** Indices 1 and 3 negated. Indices 0 and 2 remain positive $\implies [1, 3]$.

---

## 6. Traps & Common Anti-Patterns

- **Missing Absolute Value on Lookup:** Forgetting $|nums[i]|$ when reading the current element causes negative array indexing when looking up previously marked cells. Always use $|nums[i]| - 1$.
- **Negating Already-Negative Values with `-=`:** Multiplying by $-1$ or blindly using $-nums[idx]$ turns negative numbers back into positives on duplicate encounters. Using $-|nums[idx]|$ ensures the operation is strictly idempotent.
- **Modifying Length During Scan:** Appending or deleting elements dynamically alters array indices. In-place modification must preserve the fixed $N$-element structure.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Pass 1: Negates indices for each of the $N$ numbers in $O(1)$ operations per number.
  - Pass 2: Scans the $N$ elements to test for positive signs.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, executes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond the returned answer list. No auxiliary hash tables, sets, or boolean vectors are allocated.
