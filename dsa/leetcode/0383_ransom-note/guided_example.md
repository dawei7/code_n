# Guided Example: Ransom Note

We trace the step-by-step multiset frequency inventory counting (`Counter(magazine)`), character-by-character consumption (`cnt[c] -= 1`), inventory exhaustion detection (`cnt[c] < 0`), and feasibility verification on representative string instances:

- **Input:** $ransomNote = \text{"aa"}, \quad magazine = \text{"aab"}$
- **Required output:** `true`
  - Initial magazine inventory: `{'a': 2, 'b': 1}`
  - Step 1: Process first `'a'` from note $\implies cnt[\text{'a'}] = 2 - 1 = 1 \ge 0$ (Valid)
  - Step 2: Process second `'a'` from note $\implies cnt[\text{'a'}] = 1 - 1 = 0 \ge 0$ (Valid)
  - All requested letters successfully supplied from magazine $\implies$ Return `true`
- **Shortage Counterexample:** $ransomNote = \text{"aa"}, magazine = \text{"ab"}$
  - Initial inventory: `{'a': 1, 'b': 1}`
  - Step 1: Process first `'a'` $\implies cnt[\text{'a'}] = 0$
  - Step 2: Process second `'a'` $\implies cnt[\text{'a'}] = -1 < 0 \implies$ Immediate return `false`
- **Character Mismatch:** $ransomNote = \text{"a"}, magazine = \text{"b"} \implies cnt[\text{'a'}] = 0 - 1 = -1 < 0 \implies \text{false}$

This instance demonstrates multiset frequency counting and inventory consumption, mathematically proves why character order is irrelevant in anagram/sub-multiset problems, and achieves $O(M + N)$ linear time and $O(|\Sigma|) = O(1)$ space complexity.

---

## 1. Instance & Teaching Goal

Given two strings $ransomNote = \text{"aa"}$ ($N = 2$) and $magazine = \text{"aab"}$ ($M = 3$):
Determine whether $ransomNote$ can be constructed by cutting out letters from $magazine$.
Each letter in $magazine$ can only be used once in $ransomNote$:

```text
Magazine Inventory: 'a': 2 copies, 'b': 1 copy
Ransom Note Demand: 'a': 2 copies

Matching:
  Note[0] = 'a' -> Consumes 1 'a' from Magazine -> 1 'a' remaining
  Note[1] = 'a' -> Consumes 1 'a' from Magazine -> 0 'a' remaining

All demanded letters satisfied! Output: true
```

### The Sub-Multiset Principle
A note can be formed from a magazine if and only if the multiset of characters in the note is a **sub-multiset** of the magazine:
$$
\text{count}(c, \; ransomNote) \le \text{count}(c, \; magazine) \quad \text{for all } c \in \Sigma
$$
Spatial position and ordering are completely immaterial. A frequency hash table or array of size $26$ captures all necessary information.

---

## 2. Conceptual Foundation & Invariants

### 1. Inventory Hash Table (`cnt`):
Build character frequency map of the magazine:
$$
cnt = \text{Counter}(magazine)
$$

### 2. Sequential Consumption:
For each character $c \in ransomNote$:
1. Decrement inventory:
   $$
   cnt[c] \leftarrow cnt[c] - 1
   $$
2. **Deficit Check:** If $cnt[c] < 0$:
   Magazine lacked sufficient copies of letter $c$. Return **`False`** immediately.

### 3. Termination:
If the loop finishes without deficits, return **`True`**.

> **Invariant.** After processing prefix $ransomNote[0 \dots k]$, $cnt[c]$ accurately stores the surplus copies of character $c$ remaining in the magazine. If $cnt[c] < 0$, the note cannot be constructed.

---

## 3. Step-by-Step Worked Execution

We trace $ransomNote = \text{"aa"}, magazine = \text{"aab"}$:

---

### Step 1: Build Magazine Inventory
Count letters in $magazine = \text{"aab"}$:
- Count of `'a'`: $2$
- Count of `'b'`: $1$
Inventory state:
$$
cnt = \{\text{'a'}: 2, \; \text{'b'}: 1\}
$$

---

### Step 2: Process Note Index 0 ($c = \text{'a'}$)
- Read character: `'a'`.
- Decrement inventory:
  $$
  cnt[\text{'a'}] \leftarrow 2 - 1 = \mathbf{1}
  $$
- Deficit check: $cnt[\text{'a'}] = 1 \ge 0$ (Sufficient).
- Remaining inventory: `{'a': 1, 'b': 1}`.

---

### Step 3: Process Note Index 1 ($c = \text{'a'}$)
- Read character: `'a'`.
- Decrement inventory:
  $$
  cnt[\text{'a'}] \leftarrow 1 - 1 = \mathbf{0}
  $$
- Deficit check: $cnt[\text{'a'}] = 0 \ge 0$ (Exactly exhausted, but valid).
- Remaining inventory: `{'a': 0, 'b': 1}`.

---

### Step 4: Final Acceptance
All characters in $ransomNote$ processed without violation.
Return:
$$
\mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

```text
ransomNote = "aa", magazine = "aab"
Inventory cnt = {'a': 2, 'b': 1}

Char 0 ('a'): cnt['a'] = 2 - 1 = 1 >= 0 -> OK
Char 1 ('a'): cnt['a'] = 1 - 1 = 0 >= 0 -> OK

All characters satisfied -> Return True
```

| Step | Current Note Char | Magazine Supply Before | Action | Magazine Supply After | Deficit Status ($cnt[c] < 0$?) | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | - | - | Count $magazine$ | `{'a': 2, 'b': 1}` | None | In Progress |
| 1 | `'a'` | $2$ | $cnt[\text{'a'}] \mathrel{-}= 1$ | $1$ | No ($1 \ge 0$) | In Progress |
| **2** | **'a'** | **$1$** | **$cnt[\text{'a'}] \mathrel{-}= 1$** | **$0$** | **No ($0 \ge 0$)** | **`true` (Complete)** |

---

### Comparison: Deficit Failure Trace ($ransomNote = \text{"aa"}, magazine = \text{"ab"}$)

```text
ransomNote = "aa", magazine = "ab"
Inventory cnt = {'a': 1, 'b': 1}

Char 0 ('a'): cnt['a'] = 1 - 1 = 0 >= 0 -> OK
Char 1 ('a'): cnt['a'] = 0 - 1 = -1 < 0 -> DEFICIT DETECTED! -> Return False
```

| Step | Note Char | Supply Before | Decrement | Supply After | Deficit Condition | Immediate Exit |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `'a'` | $1$ | $1 - 1$ | $0$ | No | In Progress |
| **2** | **'a'** | **$0$** | **$0 - 1$** | **$-1$** | **Yes ($-1 < 0$)** | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because each decrement $cnt[c] \mathrel{-}= 1$ corresponds to consuming one physical letter from the magazine, if $cnt[c]$ drops below $0$, the note requires strictly more copies of $c$ than the magazine contains. Since letters are indivisible and cannot be reused, construction is impossible, making the early exit `False` sound.

**Completeness.** If the loop terminates without any count dropping below $0$, then for every distinct character $c$, the total demand $\text{count}(c, ransomNote)$ was at most the initial supply $\text{count}(c, magazine)$. Every requested letter is accounted for, guaranteeing a valid construction.

---

## 6. Traps This Instance Exposes

- **Length Precheck Optimization:** If $\text{len}(ransomNote) > \text{len}(magazine)$, the note is guaranteed to be unconstructible. Returning `False` immediately avoids building the frequency map.
- **Fixed Array vs Hash Map:** Because inputs consist solely of lowercase English letters (`'a'`–`'z'`), a fixed-size integer array of length 26 (`int[26]`) avoids hashing overhead and guarantees strict $O(1)$ space.
- **One-Way Sub-Multiset vs Anagram:** In anagram problems, the multisets must be identical ($\text{count}_{note} == \text{count}_{mag}$). Here, the magazine may contain excess unused letters (e.g. `'b'` in `"aab"`).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + N)$, where $M = \text{len}(magazine)$ and $N = \text{len}(ransomNote)$.
  - Counting magazine characters takes $O(M)$ time.
  - Scanning note characters takes at most $O(N)$ time.
  - Total runtime is strictly linear $O(M + N)$.
- **Auxiliary Space Complexity:** $O(|\Sigma|) = O(1)$, where $|\Sigma| \le 26$ is the English lowercase alphabet size, bounding the dictionary memory.
