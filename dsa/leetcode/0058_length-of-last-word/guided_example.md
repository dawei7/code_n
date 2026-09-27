# Guided Example: Length of Last Word

We trace the step-by-step backward two-phase scanning algorithm on a representative string containing multiple spaces:

- **Input:** $s = \text{"   fly me   to   the moon  "}$
- **Required output:** $4$

This instance demonstrates searching backwards from string end ($N - 1$), trimming trailing whitespace without string allocation, counting contiguous alphabetical characters until the preceding space delimiter, and stopping early in $O(K)$ time where $K$ is the suffix length.

---

## 1. Instance & Teaching Goal

Given a string $s$ consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

For $s = \text{"   fly me   to   the moon  "}$:
- The string contains leading spaces, multiple inter-word spaces, and trailing spaces.
- The last word is $\text{"moon"}$, which has length $4$.

A naive approach splits the string by whitespace (`s.split()`), allocating an array of all words and taking $O(N)$ extra space. The optimal approach starts at index $N - 1$ and scans backwards:
1. First, skip all trailing spaces.
2. Second, count non-space characters until encountering a space or the start of the string.

This avoids parsing preceding words and requires strictly $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Backward Two-Phase Scan
Let $N = |s|$. We initialize pointer $i = N - 1$ and counter $\text{length} = 0$:

1. **Phase 1 (Skip Trailing Spaces):**
   While $i \ge 0$ and $s[i] == \text{' '}$:
   $$
   i \leftarrow i - 1
   $$
   *(When this loop halts, $i$ points to the final letter of the last word).*

2. **Phase 2 (Measure Last Word):**
   While $i \ge 0$ and $s[i] \ne \text{' '}$:
   $$
   \text{length} \leftarrow \text{length} + 1
   $$
   $$
   i \leftarrow i - 1
   $$
   *(When this loop halts, $i$ points to the space immediately preceding the last word, or $i = -1$ if the word began the string).*

> **Invariant.** Throughout Phase 2, `length` strictly counts the number of letters from the end of the last word backwards to the current pointer position.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"   fly me   to   the moon  "}$ ($N = 27$, indices $0 \dots 26$):

### Phase 1: Skip Trailing Whitespace
- Start at $i = 26$.
- $i = 26$: $s[26] == \text{' '}$. Decrement $i \to 25$.
- $i = 25$: $s[25] == \text{' '}$. Decrement $i \to 24$.
- $i = 24$: $s[24] == \text{'n'} \ne \text{' '}$.
- Phase 1 terminates with $i = 24$.

---

### Phase 2: Accumulate Length of Last Word
- $i = 24$: $s[24] = \text{'n'}$. $\text{length} \leftarrow 0 + 1 = 1$. Decrement $i \to 23$.
- $i = 23$: $s[23] = \text{'o'}$. $\text{length} \leftarrow 1 + 1 = 2$. Decrement $i \to 22$.
- $i = 22$: $s[22] = \text{'o'}$. $\text{length} \leftarrow 2 + 1 = 3$. Decrement $i \to 21$.
- $i = 21$: $s[21] = \text{'m'}$. $\text{length} \leftarrow 3 + 1 = 4$. Decrement $i \to 20$.
- $i = 20$: $s[20] == \text{' '}$. Non-word delimiter detected!
- Phase 2 terminates.

Emitted output: $\text{length} = 4$.

---

## 4. Complete Execution Trace

| Step | Pointer Index $i$ | Character $s[i]$ | Active Phase | Phase Condition Met? | Word Length Counter |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 26 | `' '` | Phase 1 (Trim spaces) | Yes ($s[i] == \text{' '}$) | 0 |
| 2 | 25 | `' '` | Phase 1 (Trim spaces) | Yes ($s[i] == \text{' '}$) | 0 |
| 3 | 24 | `'n'` | Phase 1 End $\to$ Phase 2 | No $\implies$ Start word count | **1** |
| 4 | 23 | `'o'` | Phase 2 (Word counting) | Yes ($s[i] \ne \text{' '}$) | **2** |
| 5 | 22 | `'o'` | Phase 2 (Word counting) | Yes ($s[i] \ne \text{' '}$) | **3** |
| 6 | 21 | `'m'` | Phase 2 (Word counting) | Yes ($s[i] \ne \text{' '}$) | **4** |
| 7 | 20 | `' '` | Phase 2 End | No ($s[i] == \text{' '}$) | **4 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** The problem guarantees that at least one word exists in $s$. Phase 1 skips only trailing non-word spaces. Phase 2 counts characters continuously until hitting the first word delimiter (space). The accumulated count is provably the exact character count of the final word.

**Completeness.** Pointer $i$ moves strictly from right to left. It terminates either upon encountering a space after the word or upon reaching index $-1$ (if the last word spans to the beginning of the string).

---

## 6. Traps This Instance Exposes

- **Trailing Spaces Ignored:** A naive forward scan that resets `count = 0` upon seeing a space will output $0$ if the string ends with spaces. Backtracking from the end avoids this entirely.
- **Single Word with No Spaces:** If $s = \text{"hello"}$, Phase 1 executes zero times, and Phase 2 runs until $i = -1$, correctly returning $5$.
- **Library Split Overhead:** Calling `s.split()` scans the entire string, allocates string slices for every word, and creates a Python list, taking $O(N)$ auxiliary memory. The backward two-pointer scan uses $O(1)$ memory.

### Boundary Shapes of the Input

Only the tail matters, so the shapes below differ merely in how much work Phase 1 does before Phase 2 can start counting. Each result is the verified output of the authored case.

| Shape of $s$ | Instance | Phase 1 work | Phase 2 work | Verified result |
|---|---|---|---|---|
| No surrounding spaces | `"Hello World"` | Zero iterations: $s[10] = \text{'d'}$ already ends a word | Counts `World` over indices $10 \dots 6$, then stops at the space at index $5$ | 5 |
| Single spaces throughout | `"luffy is still joyboy"` | Zero iterations | Counts `joyboy` over indices $20 \dots 15$, then stops at the space at index $14$ | 6 |
| Six trailing spaces | `"one two alphabet      "` | Skips indices $21 \dots 16$, stopping on the `t` at index $15$ | Counts `alphabet` over indices $15 \dots 8$, then stops at the space at index $7$ | 8 |
| Leading spaces only | `"    final"` | Zero iterations, because the final character is a letter | Counts `final` over indices $8 \dots 4$, then stops at the space at index $3$ | 5 |
| Single character | `"a"` | Zero iterations | Counts one letter at index $0$; the pointer then reaches $i = -1$ and the loop ends on the boundary guard | 1 |
| Leading, repeated and trailing spaces | $s = \text{"   fly me   to   the moon  "}$ | Skips indices $26$ and $25$, stopping on the `n` at index $24$ | Counts `moon` over indices $24 \dots 21$, then stops at the space at index $20$ | 4 |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ worst case (e.g. if the string consists of one word). On average, it takes $O(K)$ where $K$ is the length of the trailing spaces plus the last word, terminating without reading earlier words.
- **Auxiliary Space Complexity:** $O(1)$. Memory consumption is strictly constant using two integer registers (`i` and `length`).

### Comparison of Candidate Methods

On this instance every method agrees on $4$; they differ in how much of the string they touch and in where the counting state lives.

| Method | Time | Auxiliary space | Tradeoff or failure mode |
|---|---|---|---|
| Backward two-phase scan (this lesson) | $O(K)$ for the trailing spaces plus the last word, $O(N)$ worst case for a single-word string | $O(1)$ | Phase 2 must be guarded by $i \ge 0$: when the last word reaches index $0$, the pointer lands on $-1$ and an unguarded read falls off the string. |
| Split on whitespace and take the final token | $O(N)$ | $O(N)$ | It materialises every word, including the ones the question never asks about, and each token is a fresh string copy. |
| Forward scan accumulating the current word length | $O(N)$ | $O(1)$ | A trailing space run resets the counter to $0$, so the running value must be preserved separately or the final answer becomes $0$ on inputs such as `"one two alphabet      "`. |
| Trim trailing blanks, then scan forward | $O(N)$ | $O(N)$ when the trim copies | Trimming allocates a new string whose length differs from the original, so the "constant memory" claim only holds for a scan that indexes into the original text. |
