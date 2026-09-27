# Guided Example: Remove Duplicate Letters

We trace the step-by-step last-occurrence index precomputation, monotonic stack greedy relaxation, `seen` membership guarding, and lexicographically smallest unique subsequence extraction on representative string instances:

- **Input:** $s = \text{"bcabc"}$
- **Required output:** `"abc"` (Every character appears once; `"abc"` is strictly smaller lexicographically than `"bca"`, `"cab"`, or `"bac"`)
- **Complex Multi-Character Instance:** $s = \text{"cbacdcbc"} \implies \text{"acdb"}$
  - At $s[2] = \text{'a'}$, both `'c'` and `'b'` on stack are greater than `'a'` and appear later in the string, popping both to place `'a'` at the front
  - At $s[4] = \text{'d'}$, `'d'` is added
  - At $s[5] = \text{'c'}$, `'c'` is added
  - At $s[6] = \text{'b'}$, `'b'` is added
  - Remaining `'c'` at index 7 is skipped as already present
- **Already Sorted Unique Characters:** $s = \text{"abc"} \implies \text{"abc"}$
- **Identical Repeated Characters:** $s = \text{"aaaa"} \implies \text{"a"}$
- **Decreasing Sequence Without Duplicates:** $s = \text{"cba"} \implies \text{"cba"}$ (No future occurrences exist to justify popping)

This instance demonstrates monotonic stack greedy optimization with future availability guarantees, proves why popping $stk[-1] > c$ is valid if and only if $last\_pos[stk[-1]] > i$, details the necessity of the `seen` filter, and executes in strictly $O(N)$ linear time and $O(|\Sigma|) = O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given string $s = \text{"bcabc"}$:
Remove duplicate letters so that:
1. Every character appears **exactly once**.
2. The resulting string is **lexicographically smallest** among all possible valid subsequences.

```text
Input: "b  c  a  b  c"
Indices:0  1  2  3  4

All unique permutations formed as subsequences:
- "bca" (using indices 0, 1, 2)
- "bac" (using indices 0, 2, 4)
- "cab" (using indices 1, 2, 3)
- "abc" (using indices 2, 3, 4) -> Lexicographically FIRST!

Output: "abc"
```

### The Monotonic Stack Invariant
To minimize the result lexicographically, we want smaller characters as early (left) as possible:
- If current character $c$ is smaller than top of stack ($c < stk[-1]$), we want to pop $stk[-1]$ to place $c$ first.
- **The Safety Rule:** We can ONLY pop $stk[-1]$ if $stk[-1]$ **appears again later in the string** ($last\_pos[stk[-1]] > i$).
- If $stk[-1]$ does not appear again later, popping it would permanently delete that character from the sequence, violating the requirement that every distinct character appear once!

---

## 2. Conceptual Foundation & Invariants

### 1. Last Occurrence Lookup
Scan $s$ to record the final index where each character appears:
$$
last\_pos[c] = \max \{ j \mid s[j] == c \}
$$
For $s = \text{"bcabc"}$:
- $'a'$ last index: $2$
- $'b'$ last index: $3$
- $'c'$ last index: $4$

### 2. Stack and Membership Set State
- `stk = []`: Monotonic-like stack storing the chosen prefix.
- `seen = set()`: Characters currently present in `stk`.

### 3. Processing Character $c$ at Index $i$:
1. **Duplicate Check:**
   If $c \in seen$, skip immediately (`continue`).
   *(Keeping the earlier occurrence already placed in the stack is optimal).*
2. **Greedy Stack Relaxation:**
   While `stk` is non-empty, and $stk[-1] > c$, and $last\_pos[stk[-1]] > i$:
   - $popped = stk.\text{pop}()$
   - $seen.\text{remove}(popped)$
3. **Insert Current Character:**
   - $stk.\text{append}(c)$
   - $seen.\text{add}(c)$

> **Invariant.** At every index $i$, `stk` contains the lexicographically smallest valid subsequence of distinct characters chosen from prefix $s[0..i]$ that can be completed into a full sequence using remaining characters.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $s = \text{"bcabc"}$ ($N = 5$):
$last\_pos = \{\text{'a'}: 2, \; \text{'b'}: 3, \; \text{'c'}: 4\}$.
Initialize `stk = []`, `seen = set()`.

---

### Step 1: Index $0$, $c = \text{'b'}$
- `'b'` not in `seen`.
- Stack is empty $\implies$ no relaxation.
- Push `'b'`: `stk = ['b']`, `seen = {'b'}`.

---

### Step 2: Index $1$, $c = \text{'c'}$
- `'c'` not in `seen`.
- Top of stack is `'b'`. Check $stk[-1] > c \iff \text{'b'} > \text{'c'}$ (**False**).
- Push `'c'`: `stk = ['b', 'c']`, `seen = {'b', 'c'}`.

---

### Step 3: Index $2$, $c = \text{'a'}$
- `'a'` not in `seen`.
- **Relaxation Round 1:**
  - Top is `'c'`.
  - Is $stk[-1] > c$? $\text{'c'} > \text{'a'}$ (**True**).
  - Does `'c'` appear later? $last\_pos[\text{'c'}] = 4 > 2$ (**True!**).
  - Pop `'c'`!
  - `seen.remove('c')` $\implies stk = [\text{'b'}], seen = \{\text{'b'}\}$.
- **Relaxation Round 2:**
  - Top is `'b'`.
  - Is $stk[-1] > c$? $\text{'b'} > \text{'a'}$ (**True**).
  - Does `'b'` appear later? $last\_pos[\text{'b'}] = 3 > 2$ (**True!**).
  - Pop `'b'`!
  - `seen.remove('b')` $\implies stk = [], seen = \emptyset$.
- Stack is now empty.
- Push `'a'`: `stk = ['a']`, `seen = {'a'}`.

---

### Step 4: Index $3$, $c = \text{'b'}$
- `'b'` not in `seen`.
- Top is `'a'`. Is $\text{'a'} > \text{'b'}$? **False**.
- Push `'b'`: `stk = ['a', 'b']`, `seen = {'a', 'b'}`.

---

### Step 5: Index $4$, $c = \text{'c'}$
- `'c'` not in `seen`.
- Top is `'b'`. Is $\text{'b'} > \text{'c'}$? **False**.
- Push `'c'`: `stk = ['a', 'b', 'c']`, `seen = {'a', 'b', 'c'}`.

---

### End of String
Join stack:
$$
\mathbf{\text{"abc"}}
$$

---

## 4. Complete Execution Trace

```text
s = "bcabc", last_pos = {'a': 2, 'b': 3, 'c': 4}

i=0, c='b': push 'b'                -> stk = ['b']
i=1, c='c': 'c' > 'b', push 'c'     -> stk = ['b', 'c']
i=2, c='a':
  'a' < 'c' and last['c']=4 > 2     -> pop 'c'
  'a' < 'b' and last['b']=3 > 2     -> pop 'b'
  push 'a'                          -> stk = ['a']
i=3, c='b': 'b' > 'a', push 'b'     -> stk = ['a', 'b']
i=4, c='c': 'c' > 'b', push 'c'     -> stk = ['a', 'b', 'c']

Final Result: "abc"
```

| Index $i$ | Char $c$ | In `seen`? | Stack Top Before | $stk[-1] > c$? | $last\_pos[top] > i$? | Action Taken | Stack After Step | `seen` Set |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | `'b'` | No | Empty | - | - | Push `'b'` | `['b']` | `{'b'}` |
| 1 | `'c'` | No | `'b'` | No | - | Push `'c'` | `['b', 'c']` | `{'b', 'c'}` |
| **2** | **`'a'`** | **No** | **`'c'`** | **Yes** | **Yes ($4 > 2$)** | **Pop `'c'`** | `['b']` | `{'b'}` |
| | | | **`'b'`** | **Yes** | **Yes ($3 > 2$)** | **Pop `'b'`, Push `'a'`** | **`['a']`** | **`{'a'}`** |
| 3 | `'b'` | No | `'a'` | No | - | Push `'b'` | `['a', 'b']` | `{'a', 'b'}` |
| 4 | `'c'` | No | `'b'` | No | - | Push `'c'` | **`['a', 'b', 'c']`** | **`{'a', 'b', 'c'}`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every character in `stk` is distinct because candidates already in `seen` are bypassed. A character is popped only if an identical character occurs later in the string, ensuring that every required distinct character is retained in the final sequence. By prioritizing smaller characters whenever future copies allow, the sequence is lexicographically minimized.

**Completeness.** Every character index in $s$ is processed. The condition $last\_pos[top] > i$ guarantees that the last occurrence of any character is never popped. Thus, every unique character present in $s$ appears exactly once in the final result.

---

## 6. Traps This Instance Exposes

- **Popping the Last Occurrence:** If $last\_pos[top] == i$, that character never appears again. Popping it would permanently remove that letter from the string, making the result invalid.
- **Skipping Already Seen Characters:** If $c$ is already in `seen`, skipping it is mandatory. Re-inserting it would create duplicate characters, and popping existing smaller characters would worsen the lexicographical order.
- **Synchronizing Stack and Seen:** When popping from `stk`, the popped character must be deleted from `seen`. Failing to do so prevents the character from being re-added when its later occurrence arrives.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$.
  - Computing `last_pos` takes $O(N)$ time.
  - In the main loop, each character is pushed to `stk` at most once and popped at most once ($O(1)$ amortized operations per character).
  - Set lookups and alphabet size are bounded by $|\Sigma| = 26$. Total time is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(|\Sigma|) = O(1)$ auxiliary memory (at most 26 characters stored in `stk` and `seen`).
