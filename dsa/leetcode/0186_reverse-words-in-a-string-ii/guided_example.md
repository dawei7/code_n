# Guided Example: Reverse Words in a String II

We trace the step-by-step two-pass in-place array reversal and word-boundary un-reversal on representative character array instances:

- **Input:** $s = [\text{'t'}, \text{'h'}, \text{'e'}, \text{' '}, \text{'s'}, \text{'k'}, \text{'y'}, \text{' '}, \text{'i'}, \text{'s'}, \text{' '}, \text{'b'}, \text{'l'}, \text{'u'}, \text{'e'}]$
- **Required output:** $[\text{'b'}, \text{'l'}, \text{'u'}, \text{'e'}, \text{' '}, \text{'i'}, \text{'s'}, \text{' '}, \text{'s'}, \text{'k'}, \text{'y'}, \text{' '}, \text{'t'}, \text{'h'}, \text{'e'}]$
- **Two-Word Instance:** $s = [\text{'a'}, \text{' '}, \text{'b'}] \implies [\text{'b'}, \text{' '}, \text{'a'}]$
- **Single Word Instance:** $s = [\text{'w'}, \text{'o'}, \text{'r'}, \text{'d'}] \implies [\text{'w'}, \text{'o'}, \text{'r'}, \text{'d'}]$ (Double reversal returns word unchanged)

This instance demonstrates in-place sentence word reversal without string allocations, proves why composing a global reversal with intra-word local reversals inverts word order while restoring character order, and operates in strictly $O(N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a mutable array of characters:
$$
s = [\text{'t'}, \text{'h'}, \text{'e'}, \text{' '}, \text{'s'}, \text{'k'}, \text{'y'}, \text{' '}, \text{'i'}, \text{'s'}, \text{' '}, \text{'b'}, \text{'l'}, \text{'u'}, \text{'e'}]
$$
Reverse the order of words in-place such that $s$ becomes:
$$
s = [\text{'b'}, \text{'l'}, \text{'u'}, \text{'e'}, \text{' '}, \text{'i'}, \text{'s'}, \text{' '}, \text{'s'}, \text{'k'}, \text{'y'}, \text{' '}, \text{'t'}, \text{'h'}, \text{'e'}]
$$
The problem explicitly requires in-place modification with strictly $O(1)$ extra space.

### The Double-Reversal Principle
In standard string manipulation, reversing the entire array reverses both the sequence of words **and** the characters inside each word:
$$
\text{"the sky is blue"} \xrightarrow{\text{reverse all}} \text{"eulb si yks eht"}
$$
Notice:
- The words are now in the correct global positions (`"blue"` is first, `"the"` is last).
- However, each individual word is reversed internally (`"blue"` is spelled `"eulb"`).
If we now reverse each individual word locally:
$$
\text{"eulb"} \to \text{"blue"}, \quad \text{"si"} \to \text{"is"}, \quad \text{"yks"} \to \text{"sky"}, \quad \text{"eht"} \to \text{"the"}
$$
The words retain their reversed positions while their internal characters return to original left-to-right spelling!

---

## 2. Conceptual Foundation & Invariants

### In-Place Two-Pointer Reversal Protocol
Define a helper function $\text{reverse}(L, R)$ that swaps characters from both ends inward until pointers meet:
```python
def reverse(L, R):
    while L < R:
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1
```

### Execution Pipeline:
1. **Pass 1: Reverse Entire Array ($0 \dots N - 1$):**
   $$
   \text{reverse}(0, N - 1)
   $$
2. **Pass 2: Reverse Each Word:**
   Maintain word boundary pointer $\text{start} = 0$.
   Iterate $\text{end}$ from $0$ to $N$:
   - If $\text{end} == N$ or $s[\text{end}] == \text{' '}$:
     The current word spans $[ \text{start}, \, \text{end} - 1 ]$.
     $$
     \text{reverse}(\text{start}, \, \text{end} - 1)
     $$
     $$
     \text{start} \leftarrow \text{end} + 1
     $$

> **Invariant.** After Pass 1, word positions are fully inverted, but words are mirrored internally. After Pass 2, each individual word is un-mirrored, restoring genuine English word order.

---

## 3. Step-by-Step Worked Execution

We trace $s = [\text{'t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'}]$ ($N = 15$):

### Pass 1: Global Array Reversal
Call $\text{reverse}(0, 14)$:
- Swapping $(0, 14)$: `'t'` $\leftrightarrow$ `'e'`
- Swapping $(1, 13)$: `'h'` $\leftrightarrow$ `'u'`
- Swapping $(2, 12)$: `'e'` $\leftrightarrow$ `'l'`
- Swapping $(3, 11)$: `' '` $\leftrightarrow$ `'b'`
- Swapping $(4, 10)$: `'s'` $\leftrightarrow$ `' '`
- Swapping $(5, 9)$: `'k'` $\leftrightarrow$ `'s'`
- Swapping $(6, 8)$: `'y'` $\leftrightarrow$ `'i'`
- Index $7$ (`' '`) remains at center.

Result after Pass 1:
$$
s = [\text{'e','u','l','b',' ','s','i',' ','y','k','s',' ','e','h','t'}]
$$
*(Notice: word positions are blue, is, sky, the, but characters are mirrored!)*

---

### Pass 2: Un-reverse Individual Words

#### Word 1: Indices $[0, 3]$ (`"eulb"`)
- Detected space at index $4$.
- Call $\text{reverse}(0, 3)$:
  - Swap $(0, 3)$: `'e'` $\leftrightarrow$ `'b'`
  - Swap $(1, 2)$: `'u'` $\leftrightarrow$ `'l'`
  - Becomes: `"blue"`.
- Next word start: $\text{start} = 4 + 1 = 5$.

#### Word 2: Indices $[5, 6]$ (`"si"`)
- Detected space at index $7$.
- Call $\text{reverse}(5, 6)$:
  - Swap $(5, 6)$: `'s'` $\leftrightarrow$ `'i'`
  - Becomes: `"is"`.
- Next word start: $\text{start} = 7 + 1 = 8$.

#### Word 3: Indices $[8, 10]$ (`"yks"`)
- Detected space at index $11$.
- Call $\text{reverse}(8, 10)$:
  - Swap $(8, 10)$: `'y'` $\leftrightarrow$ `'s'`
  - Index $9$ (`'k'`) stays in place.
  - Becomes: `"sky"`.
- Next word start: $\text{start} = 11 + 1 = 12$.

#### Word 4: Indices $[12, 14]$ (`"eht"`)
- Detected end of array at $\text{end} = 15$.
- Call $\text{reverse}(12, 14)$:
  - Swap $(12, 14)$: `'e'` $\leftrightarrow$ `'t'`
  - Index $13$ (`'h'`) stays in place.
  - Becomes: `"the"`.

Final in-place state of $s$:
$$
[\text{'b','l','u','e',' ','i','s',' ','s','k','y',' ','t','h','e'}]
$$

---

## 4. Complete Execution Trace

```text
Initial Array:
"the sky is blue"

Pass 1 (Reverse All):
"eulb si yks eht"

Pass 2 (Reverse Words):
  reverse(0, 3):   "eulb" -> "blue"   --> "blue si yks eht"
  reverse(5, 6):   "si"   -> "is"     --> "blue is yks eht"
  reverse(8, 10):  "yks"  -> "sky"    --> "blue is sky eht"
  reverse(12, 14): "eht"  -> "the"    --> "blue is sky the"

Result: "blue is sky the"
```

| Pass | Target Range $[L, R]$ | Substring Before | Action Taken | Substring After | Full Array State |
|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | $[0, 14]$ | `"the sky is blue"` | Global Reversal | `"eulb si yks eht"` | `"eulb si yks eht"` |
| 2a | $[0, 3]$ | `"eulb"` | Word Reversal | `"blue"` | `"blue si yks eht"` |
| 2b | $[5, 6]$ | `"si"` | Word Reversal | `"is"` | `"blue is yks eht"` |
| 2c | $[8, 10]$ | `"yks"` | Word Reversal | `"sky"` | `"blue is sky eht"` |
| **2d** | **$[12, 14]$** | **`"eht"`** | **Word Reversal** | **`"the"`** | **`"blue is sky the"` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let the sentence be composed of $k$ words $W_1, W_2, \dots, W_k$. Reversing the whole array transforms the sequence into $W_k^R, \dots, W_2^R, W_1^R$, where $W^R$ denotes the reverse of word $W$. Reversing each word locally applies the identity $(W^R)^R = W$, restoring the spelling while preserving the inverted order $W_k, \dots, W_1$.

**Completeness.** Since words are strictly single-space delimited and there are no leading or trailing spaces, every non-space interval is parsed and un-reversed. The trailing word is handled at $\text{end} = N$.

---

## 6. Traps This Instance Exposes

- **Missing the Final Word:** Because the last word is terminated by the end of the array rather than a space character, failing to check `end == N` leaves the final word backwards.
- **Using External Memory:** Calling `s = " ".join(s.split()[::-1])` allocates a new string and list of tokens, violating the $O(1)$ extra memory requirement.
- **Single Word Array:** If $s = [\text{'a'}, \text{'b'}, \text{'c'}]$, Pass 1 produces `cba`, and Pass 2 un-reverses it back to `abc`, returning the correct unchanged single word.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of array $s$. Pass 1 performs $\lfloor N / 2 \rfloor$ swaps. Pass 2 touches each character exactly once during word reversals. Total operations are strictly bounded by $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant memory, operating purely in-place on $s$.
