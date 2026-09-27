# Guided Example: Count Words Obtained After Adding a Letter

We trace the step-by-step execution of the bitmask character set encoding and reverse single-letter deletion approach on a representative problem instance:

- **Start Words (`startWords`):** `["ant", "act", "tack"]`
- **Target Words (`targetWords`):** `["tack", "act", "acti"]`
- **Expected Output:** `2`

This instance illustrates how anagram permutation invariance reduces strings to 26-bit binary masks, demonstrating why testing backward single-bit deletions from each target word against a precomputed set of start masks evaluates reachability in linear time.

---

## 1. Problem Overview & Representative Instance

We are given two string arrays: `startWords` and `targetWords`. Each string consists exclusively of distinct lowercase English letters. In one operation, we can choose any word from `startWords`, append any lowercase letter not already present in the word, and rearrange its letters in any arbitrary order.

We must count how many strings in `targetWords` can be formed using this operation from some string in `startWords`. Each start word may be reused indefinitely.

In our representative instance:
- `startWords`: `"ant"` ($\{a, n, t\}$), `"act"` ($\{a, c, t\}$), `"tack"` ($\{a, c, k, t\}$)
- `targetWords`:
  1. `"tack"` ($\{a, c, k, t\}$): Removing `'k'` leaves $\{a, c, t\}$, which matches start word `"act"`. Appending `'k'` to `"act"` and rearranging produces `"tack"`. (Valid)
  2. `"act"` ($\{a, c, t\}$): A start word must have length $3 - 1 = 2$. No 2-letter word exists in `startWords`. (Invalid)
  3. `"acti"` ($\{a, c, t, i\}$): Removing `'i'` leaves $\{a, c, t\}$, matching `"act"`. Appending `'i'` and rearranging produces `"acti"`. (Valid)
Total valid target words: $2$.

---

## 2. Mathematical & Algorithmic Principles

### Anagram Invariance via 26-Bit Bitmasks
Because the problem permits arbitrary letter rearrangement and every word contains distinct characters, any word $w$ is completely determined by its set of constituent characters. We map each word to a 26-bit integer:

$$\text{mask}(w) = \sum_{c \in w} 2^{\text{ord}(c) - \text{ord}('a')}$$

Bit $k$ is $1$ if the $k$-th letter of the alphabet is present in $w$, and $0$ otherwise. Anagrams have identical bitmasks.

### Backward Deletion Duality
A start word $s$ can form target word $t$ if and only if:
1. $|t| = |s| + 1$
2. $\text{mask}(s) \subset \text{mask}(t)$ with exactly one bit difference.

Instead of generating up to $26$ expanded masks for every start word, we invert the perspective:
1. Store all start word masks in a hash set $\mathcal{S}$.
2. For each target word $t$, compute its bitmask $M = \text{mask}(t)$.
3. For each character $c \in t$, evaluate the candidate predecessor mask obtained by deleting bit $c$:

$$M' = M \oplus 2^{\text{ord}(c) - \text{ord}('a')}$$

4. If $M' \in \mathcal{S}$, target $t$ can be produced. Increment the valid target count and immediately break to prevent duplicate counts for the same target word.

| Metric | Role in Evaluation | Representation |
|---|---|---|
| Start Mask Set $\mathcal{S}$ | Hash set of valid base word bit patterns | Hash set of 26-bit integers |
| Target Mask $M$ | Complete bit pattern of candidate target word | 26-bit integer |
| Single-Bit Deletion $M'$ | Sub-pattern with one letter removed | $M \oplus (1 \ll \text{shift})$ |
| Verification Criterion | Membership in $\mathcal{S}$ | $M' \in \mathcal{S} \implies \text{obtainable}$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Phase 1: Precomputing Start Word Mask Set $\mathcal{S}$
Convert each start word into its bitmask representation:
- `"ant"`: letters $\{a, n, t\} \implies \text{bits } \{0, 13, 19\} \implies M_1$.
- `"act"`: letters $\{a, c, t\} \implies \text{bits } \{0, 2, 19\} \implies M_2$.
- `"tack"`: letters $\{a, c, k, t\} \implies \text{bits } \{0, 2, 10, 19\} \implies M_3$.
Hash set $\mathcal{S} = \{M_1, M_2, M_3\}$.
Running valid target counter: $\text{count} = 0$.

### Phase 2: Evaluating Target Word 1: `"tack"`
- Character set: $\{a, c, k, t\}$ (Length $4$).
- Mask $M_{\text{tack}}$ has bits $\{0, 2, 10, 19\}$.
- Test single-character deletions:
  - Delete `'a'`: mask with $\{c, k, t\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'c'`: mask with $\{a, k, t\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'k'`: mask with $\{a, c, t\}$. This equals $M_2$ (corresponding to `"act"`)!
- Match found! Target `"tack"` is obtainable from `"act"`.
- Update: $\text{count} \leftarrow 0 + 1 = 1$. Break to next target.

### Phase 3: Evaluating Target Word 2: `"act"`
- Character set: $\{a, c, t\}$ (Length $3$).
- Mask $M_{\text{act}}$ has bits $\{0, 2, 19\}$.
- Test single-character deletions:
  - Delete `'a'`: mask with $\{c, t\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'c'`: mask with $\{a, t\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'t'`: mask with $\{a, c\}$. Check $\mathcal{S} \implies$ Not found.
- All deletions exhausted without finding a matching predecessor in $\mathcal{S}$.
- Target `"act"` is unobtainable. Count remains $1$.

### Phase 4: Evaluating Target Word 3: `"acti"`
- Character set: $\{a, c, t, i\}$ (Length $4$).
- Mask $M_{\text{acti}}$ has bits $\{0, 2, 8, 19\}$.
- Test single-character deletions:
  - Delete `'a'`: mask with $\{c, i, t\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'c'`: mask with $\{a, i, t\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'t'`: mask with $\{a, c, i\}$. Check $\mathcal{S} \implies$ Not found.
  - Delete `'i'`: mask with $\{a, c, t\}$. This equals $M_2$ (corresponding to `"act"`)!
- Match found! Target `"acti"` is obtainable from `"act"`.
- Update: $\text{count} \leftarrow 1 + 1 = 2$. Break.

Total valid target words: $2$.

---

## 4. Comprehensive State Trace

The evaluation metrics across all target words are tabulated below:

| Target Word | Letters Present | Target Length | Deleted Letter Tested | Remaining Character Set | Predecessor in $\mathcal{S}$? | Target Obtainable? | Cumulative Count |
|---|---|---|---|---|---|---|---|
| `"tack"` | $\{a, c, k, t\}$ | $4$ | `'a'` | $\{c, k, t\}$ | No | — | $0$ |
| `"tack"` | $\{a, c, k, t\}$ | $4$ | `'c'` | $\{a, k, t\}$ | No | — | $0$ |
| `"tack"` | $\{a, c, k, t\}$ | $4$ | `'k'` | $\{a, c, t\}$ | Yes (`"act"`) | Yes | $1$ |
| `"act"` | $\{a, c, t\}$ | $3$ | `'a'`, `'c'`, `'t'` | $\{c, t\}$, $\{a, t\}$, $\{a, c\}$ | No for all | No | $1$ |
| `"acti"` | $\{a, c, t, i\}$ | $4$ | `'a'`, `'c'`, `'t'` | $\{c, i, t\}$, etc. | No | — | $1$ |
| `"acti"` | $\{a, c, t, i\}$ | $4$ | `'i'` | $\{a, c, t\}$ | Yes (`"act"`) | Yes | $2$ |

Total count of obtainable target words: $2$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** If a single-character deletion $M \oplus 2^{\text{shift}}$ exists in $\mathcal{S}$, there exists some start word $s$ whose character set is identical to $t \setminus \{c\}$. Appending character $c$ (which was absent from $s$) produces a multiset of letters identical to $t$. Because any permutation of characters is permitted by the operation, $s$ can be transformed into $t$.

**Completeness.** Any valid transformation consists of taking some start word $s$ and appending exactly one missing character $c^*$ to form $t$. Therefore, the character set of $s$ must be $t \setminus \{c^*\}$. Because the algorithm tests removing every character $c \in t$, the exact added character $c^*$ is guaranteed to be tested. Its corresponding predecessor mask will be found in $\mathcal{S}$, ensuring no obtainable target word is missed.

---

## 6. Edge Cases & Anti-Patterns

- **Identical Word in Both Arrays:** A word present in both `startWords` and `targetWords` (like `"act"`) cannot be obtained from itself without adding a letter; the predecessor must have length $|t| - 1$.
- **Multiple Valid Predecessors:** If deleting either of two different letters matches different start words, the early `break` ensures the target word is counted only once.
- **Duplicate Words in Targets:** If identical target words appear multiple times in `targetWords`, each instance is counted toward the total independently.
- **Anti-Pattern — Expanding All Start Words:** Generating all 26 expansions for every start word and inserting them into a set takes $\mathcal{O}(26 \cdot |S|)$ memory and time. Backward deletion from targets requires only $\mathcal{O}(|S|)$ storage for start words and performs at most $26$ lookups per target.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L_{\text{start}} + L_{\text{target}})$, where $L_{\text{start}}$ is the total character length of all words in `startWords` and $L_{\text{target}}$ is the total character length of all words in `targetWords`. Building the start set takes $\mathcal{O}(L_{\text{start}})$. For each target word of length $m \le 26$, testing all $m$ deletions takes $\mathcal{O}(m)$ operations with expected $\mathcal{O}(1)$ hash lookups.
- **Auxiliary Space Complexity:** $\mathcal{O}(|S|)$, where $|S|$ is the number of words in `startWords`, to store the 26-bit integer masks in hash set $\mathcal{S}$.
