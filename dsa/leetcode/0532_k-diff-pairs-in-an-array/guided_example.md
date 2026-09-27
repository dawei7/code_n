# Guided Example: K-diff Pairs in an Array

We trace the step-by-step canonical pair identification ($|u - v| = k \iff (u, u+k)$), hash-set complement matching ($x - k \in vis \lor x + k \in vis$), canonical smaller-element registration ($ans.add(\min(u, v))$), zero-difference duplicate handling ($k = 0$), and unique pair count evaluation on representative integer sequences:

- **Input:** $nums = [3, 1, 4, 1, 5], \quad k = 2$
- **Required output:** `2`
  - Pair conditions:
    1. Elements at distinct indices: $i \ne j$.
    2. Absolute difference: $|nums[i] - nums[j]| == k = 2$.
    3. Distinct pairs: Pairs $(a, b)$ and $(b, a)$ represent the **same** pair; only count unique value sets $\{a, b\}$.
- **Canonical Hash Set Representation:**
  - Every pair of difference $k$ can be uniquely represented by its smaller element $u$:
    $$
    \{u, \; u + k\} \iff \text{Canonical representation: } u
    $$
  - Track:
    - $vis$: Set of numbers encountered so far.
    - $ans$: Set of smaller elements $u$ corresponding to verified valid pairs $\{u, u+k\}$.
- **Single-pass element-by-element execution trace:**
  - Initialize: $vis = \emptyset, \; ans = \emptyset$.
  - **Index 0 ($x = 3$):**
    - Check complements:
      - $x - k = 3 - 2 = 1 \in vis$? No.
      - $x + k = 3 + 2 = 5 \in vis$? No.
    - Add to seen: $vis \leftarrow \{3\}$.
    - State: $vis = \{3\}, \; ans = \emptyset$.
  - **Index 1 ($x = 1$):**
    - Check complements:
      - $x - k = 1 - 2 = -1 \in vis$? No.
      - $x + k = 1 + 2 = 3 \in vis$? **Yes!** ($3$ was seen earlier).
    - Found pair $\{1, 3\}$. Smaller element is $1$:
      $$
      ans.add(1) \implies ans = \{1\}
      $$
    - Add to seen: $vis \leftarrow \{1, 3\}$.
  - **Index 2 ($x = 4$):**
    - Check complements:
      - $4 - 2 = 2 \in vis$? No.
      - $4 + 2 = 6 \in vis$? No.
    - Add to seen: $vis \leftarrow \{1, 3, 4\}$.
  - **Index 3 ($x = 1$, Duplicate Value):**
    - Check complements:
      - $1 - 2 = -1 \in vis$? No.
      - $1 + 2 = 3 \in vis$? **Yes!**
    - Pair $\{1, 3\}$ formed again:
      $$
      ans.add(1) \implies ans = \{1\}
      $$
      *(Set automatically deduplicates the pair!)*
    - Add to seen: $vis$ remains $\{1, 3, 4\}$.
  - **Index 4 ($x = 5$):**
    - Check complements:
      - $x - k = 5 - 2 = 3 \in vis$? **Yes!** ($3$ was seen earlier).
      - Smaller element is $3$:
        $$
        ans.add(3) \implies ans = \{1, 3\}
      $$
      - $x + k = 5 + 2 = 7 \in vis$? No.
    - Add to seen: $vis \leftarrow \{1, 3, 4, 5\}$.
  - Array completed.
  - Final unique pairs: $\{1\} \to (1, 3)$ and $\{3\} \to (3, 5)$.
  - Total count: $|ans| = \mathbf{2}$.
- **Zero Difference Instance ($k = 0, nums = [1, 3, 1, 5, 4]$):**
  - First $1$: $vis = \{1\}$.
  - Second $1$: $1 - 0 = 1 \in vis \implies ans.add(1) \implies$ pair $(1, 1)$ counted $\implies \mathbf{1}$.
- **Adjacent Sequence Instance ($k = 1, nums = [1, 2, 3, 4, 5]$):**
  - Forms pairs $(1, 2), (2, 3), (3, 4), (4, 5) \implies \mathbf{4}$.

This instance demonstrates hash-set symmetric complement search with canonical min-element projection, mathematically proves why canonical set insertion prevents duplicate pair inflation, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [3, 1, 4, 1, 5]$ and an integer $k = 2$:
Return the number of **unique** $k$-diff pairs $(nums[i], nums[j])$ such that:
$$
i \ne j \quad \text{and} \quad |nums[i] - nums[j]| == k
$$

```text
Array: [ 3,  1,  4,  1,  5 ],  k = 2

Target Differences:
  |3 - 1| = 2  -> Pair (1, 3)
  |5 - 3| = 2  -> Pair (3, 5)

Duplicates handled:
  Array has two 1's, but pair (1, 3) must only be counted ONCE!

Unique Pairs = 2: (1, 3) and (3, 5)
```

### The Canonical Smaller-Element Projection
- A pair $\{u, v\}$ with $|u - v| = k$ can be written uniquely in ordered form as:
  $$
  (\min(u, v), \; \min(u, v) + k)
  $$
- Therefore, each unique pair is uniquely identified by its smaller element:
  $$
  \text{Canonical Key} = \min(u, v)
  $$
- Storing this key in a `set` automatically prevents multiple pairs with the same values from inflating the total count.

---

## 2. Conceptual Foundation & Invariants

### 1. Complement Detection with Sets:
Maintain two sets:
- $vis$: numbers seen so far.
- $ans$: smaller elements of verified valid pairs.
For each element $x \in nums$:
1. If $x - k \in vis$:
   A previous element $u = x - k$ exists such that $x - u = k$.
   The smaller element is $x - k \implies ans.add(x - k)$.
2. If $x + k \in vis$:
   A previous element $v = x + k$ exists such that $v - x = k$.
   The smaller element is $x \implies ans.add(x)$.
3. Add $x$ to $vis$: $vis.add(x)$.

### 2. Handling $k = 0$:
When $k = 0$, a pair requires two distinct indices with the same value ($nums[i] == nums[j]$).
- When the first copy of $x$ appears, $x - 0 \notin vis$. $vis.add(x)$.
- When the second copy of $x$ appears, $x - 0 = x \in vis \implies ans.add(x)$.
- Any further duplicates simply re-insert $x$ into set $ans$ without increasing its length.

> **Canonical Representation Invariant.** Registering only the smaller element of each matched pair into a set guarantees that order variations $(a, b)$ vs $(b, a)$ and duplicate input values map to a single entry.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [3, 1, 4, 1, 5], k = 2$:

---

### Step 1: Initialize
- $ans = \emptyset, \; vis = \emptyset$.

---

### Step 2: Traverse Numbers

1. **$x = 3$:**
   - $3 - 2 = 1 \notin vis$
   - $3 + 2 = 5 \notin vis$
   - $vis \leftarrow \{3\}$.

2. **$x = 1$:**
   - $1 - 2 = -1 \notin vis$
   - $1 + 2 = 3 \in vis$ (**Match!** Pair $(1, 3)$)
   - $ans.add(1) \implies ans = \{1\}$.
   - $vis \leftarrow \{1, 3\}$.

3. **$x = 4$:**
   - $4 - 2 = 2 \notin vis$
   - $4 + 2 = 6 \notin vis$
   - $vis \leftarrow \{1, 3, 4\}$.

4. **$x = 1$ (Second 1):**
   - $1 - 2 = -1 \notin vis$
   - $1 + 2 = 3 \in vis$ (**Match!** Pair $(1, 3)$)
   - $ans.add(1) \implies ans = \{1\}$ (no-op).
   - $vis \leftarrow \{1, 3, 4\}$.

5. **$x = 5$:**
   - $5 - 2 = 3 \in vis$ (**Match!** Pair $(3, 5)$)
   - $ans.add(3) \implies ans = \{1, 3\}$.
   - $5 + 2 = 7 \notin vis$
   - $vis \leftarrow \{1, 3, 4, 5\}$.

---

### Step 3: Count Unique Pairs
$$
|ans| = |\{1, 3\}| = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Element $x$ | Lower Complement $x - k$ | In $vis$? | Upper Complement $x + k$ | In $vis$? | Key Added to $ans$ | Set $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $3$ | $1$ | No | $5$ | No | None | $\emptyset$ |
| $1$ | $-1$ | No | **$3$** | **Yes** | $1$ | $\{1\}$ |
| $4$ | $2$ | No | $6$ | No | None | $\{1\}$ |
| $1$ | $-1$ | No | **$3$** | **Yes** | $1$ (Deduplicated) | $\{1\}$ |
| $5$ | **$3$** | **Yes** | $7$ | No | $3$ | **$\{1, 3\}$** |
| **Result** | — | — | — | — | — | **Count: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$ with No Duplicates ($[1, 2, 3], k = 0$):** No number appears twice $\implies ans = \emptyset \implies \mathbf{0}$.
- **$k = 0$ with Duplicates ($[1, 1, 1, 1], k = 0$):** $1$ is added once to $ans \implies \mathbf{1}$.
- **Negative $k$ ($k < 0$):** Distance $|u - v|$ is non-negative; $k < 0$ is impossible $\implies \mathbf{0}$.
- **All Pairs Valid ($[1, 2, 3], k = 1$):** $(1, 2)$ and $(2, 3) \implies \mathbf{2}$.

---

## 6. Traps & Common Anti-Patterns

- **Checking Pairs with $O(N^2)$ Nested Loops:** Nested loops run into TLE for $N = 10^4$ and require complex deduplication logic. Hash sets run in $O(N)$ linear time.
- **Double-Counting by Adding Both $(x, y)$ and $(y, x)$:** Storing tuples without sorting causes both $(1, 3)$ and $(3, 1)$ to enter the set, falsely doubling the count to 4. Storing only the smaller element guarantees unique keys.
- **Failing on $k = 0$ by Adding $x$ to $vis$ First:** If you add $x$ to $vis$ *before* checking $x - k \in vis$, then when $k = 0$, $x - 0 = x \in vis$ is always true on the very first occurrence! You must check $vis$ *before* inserting $x$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single pass iterates through the $N$ integers.
  - Set membership tests and insertions take $O(1)$ amortized time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store sets $vis$ and $ans$.
