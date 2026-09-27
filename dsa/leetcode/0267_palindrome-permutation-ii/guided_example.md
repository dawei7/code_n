# Guided Example: Palindrome Permutation II

We trace the step-by-step parity feasibility gating, center character extraction, half-string multiset permutation backtracking, and symmetric mirror reflection on representative string instances:

- **Input:** $s = \text{"aabb"}$
- **Required output:** `["abba", "baab"]` (The two unique palindromic permutations of the multiset $\{a: 2, b: 2\}$)
- **Feasibility Rejection:** $s = \text{"abc"} \implies []$ (Three characters with odd frequency $1$; budget is at most 1)
- **Odd Length Valid Instance:** $s = \text{"aab"} \implies \text{["aba"]}$ (Center is `'b'`, half string is `'a'`)
- **Uniform Character Instance:** $s = \text{"aaaa"} \implies \text{["aaaa"]}$ (Single unique permutation)

This instance demonstrates combinatorial symmetry reduction, explains why generating only the left half-string reduces search complexity from $O(N!)$ to $O((N/2)!)$, formalizes the duplicate-skipping backtracking rule on sorted elements, and mirrors the prefix around the center to construct valid palindromes without any wasteful rejection filtering.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"aabb"}$, generate all **unique palindromic permutations**:
```text
All 4! = 24 permutations of "aabb" contain only 2 unique palindromes:
"abba"
"baab"
Output: ["abba", "baab"]
```

### The $N!$ vs $(N/2)!$ Dimensionality Reduction
- Generating all $N!$ permutations and filtering palindromes afterwards tests $24$ strings for $N = 4$, and $3.6 \times 10^6$ strings for $N = 10$, nearly all of which are non-palindromic.
- A palindrome is completely determined by its **left half** and its **center character**:
  $$
  \text{Palindrome} = \text{Left Half} + \text{Center} + \text{reverse}(\text{Left Half})
  $$
- Therefore, we only need to:
  1. Verify whether a palindrome is possible (at most one odd frequency).
  2. Extract the center character (if length is odd).
  3. Form the half-multiset containing half of each character's count.
  4. Generate all **unique permutations of the half-multiset** and mirror each one!

---

## 2. Conceptual Foundation & Invariants

### 1. Parity Feasibility Check
Count character frequencies using a map:
- If more than 1 character has an odd count:
  $$
  \text{odd\_count} > 1 \implies \text{return } []
  $$
- If exactly 1 character $c_{\text{odd}}$ has an odd count:
  Reserve one copy for the center: $\text{mid} = c_{\text{odd}}$.
  Reduce its count: $\text{freq}[c_{\text{odd}}] \leftarrow \text{freq}[c_{\text{odd}}] - 1$.
- If all counts are even: $\text{mid} = \text{""}$.

### 2. Half-Multiset Construction
Populate list `half` with $\text{freq}[c] / 2$ copies of each character:
$$
\text{half} = \sum_{c \in \Sigma} [c] \times (\text{freq}[c] // 2)
$$
For $s = \text{"aabb"}$: `half = ['a', 'b']`, $\text{mid} = \text{""}$.
For $s = \text{"aab"}$: `half = ['a']`, $\text{mid} = \text{"b"}$.

### 3. Backtracking Unique Permutations on `half`
Sort `half` so identical characters are adjacent:
Maintain `used = [False] * len(half)` and current trajectory `curr`:
- If $\text{len}(\text{curr}) == \text{len}(\text{half})$:
  $$
  \text{left} = \text{"".join}(\text{curr})
  $$
  $$
  \text{results}.\text{append}(\text{left} + \text{mid} + \text{reverse}(\text{left}))
  $$
- For index $i$ from $0$ to $\text{len}(\text{half}) - 1$:
  - If `used[i]`: continue.
  - **Duplicate Skip Invariant:**
    If $i > 0$ and $\text{half}[i] == \text{half}[i - 1]$ and not $\text{used}[i - 1]$:
    continue *(Skip duplicate choices at the same tree depth)*.
  - `used[i] = True; curr.append(half[i])`
  - `backtrack(curr)`
  - `curr.pop(); used[i] = False`

> **Invariant.** Every generated half-string is a unique permutation of the half-multiset. Symmetrically mirroring each unique half-string around `mid` produces an exhaustive, mutually disjoint set of valid palindromes.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $s = \text{"aabb"}$:

### Step 1: Frequency and Parity Analysis
- Frequencies: `{'a': 2, 'b': 2}`.
- Parities:
  - `'a'`: $2 \pmod 2 = 0$ (Even).
  - `'b'`: $2 \pmod 2 = 0$ (Even).
- Odd count $= 0 \le 1$. Palindrome is feasible!
- Center character: $\text{mid} = \text{""}$.

---

### Step 2: Build Half-Multiset
- For `'a'`: $2 // 2 = 1$ copy $\implies \text{['a']}$.
- For `'b'`: $2 // 2 = 1$ copy $\implies \text{['b']}$.
- Sorted half array: $\text{half} = [\text{'a'}, \text{'b'}]$.
- Length: $M = 2$.

---

### Step 3: Backtracking Permutations of `['a', 'b']`

#### Depth 0 $\to$ Choose First Character:
- **Branch A: Pick index 0 (`'a'`):**
  - $\text{curr} = [\text{'a'}]$.
  - Mark `used[0] = True`.
  - **Depth 1:**
    - Test index 0: already used.
    - Test index 1 (`'b'`): available.
    - Pick `'b'`: $\text{curr} = [\text{'a'}, \text{'b'}]$.
    - Mark `used[1] = True`.
    - **Depth 2 (Base Case Reached):**
      $\text{len}(\text{curr}) == 2$.
      - Form left half: `"ab"`.
      - Construct palindrome:
        $$
        \text{"ab"} + \text{""} + \text{reverse}(\text{"ab"}) = \text{"ab"} + \text{""} + \text{"ba"} = \mathbf{\text{"abba"}}
        $$
      - Add to results: `["abba"]`.
    - Backtrack: unmark `used[1] = False`, $\text{curr} = [\text{'a'}]$.
  - Backtrack: unmark `used[0] = False`, $\text{curr} = []$.

- **Branch B: Pick index 1 (`'b'`):**
  - $\text{curr} = [\text{'b'}]$.
  - Mark `used[1] = True`.
  - **Depth 1:**
    - Test index 0 (`'a'`): available.
    - Pick `'a'`: $\text{curr} = [\text{'b'}, \text{'a'}]$.
    - Mark `used[0] = True`.
    - **Depth 2 (Base Case Reached):**
      $\text{len}(\text{curr}) == 2$.
      - Form left half: `"ba"`.
      - Construct palindrome:
        $$
        \text{"ba"} + \text{""} + \text{reverse}(\text{"ba"}) = \text{"ba"} + \text{""} + \text{"ab"} = \mathbf{\text{"baab"}}
        $$
      - Add to results: `["abba", "baab"]`.
    - Backtrack: unmark `used[0] = False`, $\text{curr} = [\text{'b'}]$.
  - Backtrack: unmark `used[1] = False`, $\text{curr} = []$.

All branches exhausted.
Collected output:
$$
\mathbf{[\text{"abba"}, \text{"baab"}]}
$$

---

## 4. Complete Execution Trace

```text
s = "aabb"
Counts: {'a': 2, 'b': 2} -> 0 odd counts -> Feasible!
mid = ""
half = ['a', 'b']

backtrack([]):
  Pick 'a': curr = ['a']
    Pick 'b': curr = ['a', 'b'] -> Complete half!
      Palindrome: "ab" + "" + "ba" = "abba"
    Backtrack
  Backtrack
  Pick 'b': curr = ['b']
    Pick 'a': curr = ['b', 'a'] -> Complete half!
      Palindrome: "ba" + "" + "ab" = "baab"
    Backtrack
  Backtrack

Result: ["abba", "baab"]
```

| Decision Step | Chosen Element | Current `curr` | Remaining Available in `half` | Full Left Half | Symmetrically Mirrored Palindrome |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `'a'` | `['a']` | `['b']` | - | - |
| **2** | `'b'` | `['a', 'b']` | None | `"ab"` | **`"abba"`** |
| 3 | Backtrack | `['a']` | `['b']` | - | - |
| 4 | Backtrack | `[]` | `['a', 'b']` | - | - |
| 5 | `'b'` | `['b']` | `['a']` | - | - |
| **6** | `'a'` | `['b', 'a']` | None | `"ba"` | **`"baab"`** |
| **End** | - | - | - | - | **`["abba", "baab"]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted string has the structure $\text{left} + \text{mid} + \text{reverse}(\text{left})$, which is palindromic by construction. The multiset of characters in each output string equals $2 \times \text{half} + \text{mid} = \text{multiset}(s)$, ensuring that every output is a valid permutation of $s$.

**Completeness.** Any palindromic permutation $P$ of $s$ must have the center equal to $\text{mid}$, and its prefix $P[0 \dots \lfloor N/2 \rfloor - 1]$ must be a permutation of the multiset $\text{half}$. Because backtracking with the duplicate-skip rule enumerates all unique permutations of $\text{half}$, every valid palindromic permutation is produced without omission or repetition.

---

## 6. Traps This Instance Exposes

- **Generating Full Permutations and Filtering:** Exploring all $N!$ permutations wastes $O(N! \cdot N)$ time. Permuting only the half-array reduces search depth by half, visiting exactly the number of palindromes that actually exist.
- **Duplicate Suppression at the Source:** Using a hash set to filter duplicates after generation uses unnecessary heap memory. Sorting `half` and skipping equal siblings (`half[i] == half[i-1] and not used[i-1]`) guarantees that duplicate permutations are pruned before they are explored.
- **Center Character Preservation:** In odd-length strings (e.g. `"aab"`), the odd character `'b'` must have one copy removed for $\text{mid}$ before building `half`. If the remaining count of that character is $> 0$ (e.g. for `'a': 3`, one goes to center, and two remain), the remaining two copies must be halved and placed into `half`!

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot P)$, where $N$ is the length of $s$ and $P = \frac{(N/2)!}{k_1! k_2! \dots k_m!}$ is the number of unique palindromic permutations. Generating each permutation of length $N/2$ takes $O(N/2)$ operations, and mirroring it takes $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the recursion call stack and `used` tracking array (excluding the returned list of solutions).
