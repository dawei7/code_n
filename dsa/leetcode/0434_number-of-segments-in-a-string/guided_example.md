# Guided Example: Number of Segments in a String

We trace the step-by-step whitespace boundary transition detection, leading-character segment anchor counting ($s[i] \ne \text{' '} \land (i = 0 \lor s[i-1] = \text{' '})$), whitespace cluster handling, and non-allocating single-pass counting on representative text inputs:

- **Input:** $s = \text{"Hello, my name is John"}$
- **Required output:** `5`
  - Segment transitions:
    - Index 0 ($i = 0$): $s[0] = \text{'H'} \ne \text{' '}$ (Initial boundary) $\implies$ **Segment 1 begins** (`"Hello,"`)
    - Indices 1–5: `'e'`, `'l'`, `'l'`, `'o'`, `','` $\implies$ Continuation of Segment 1
    - Index 6: `' '` $\implies$ Whitespace separator
    - Index 7: $s[7] = \text{'m'} \ne \text{' '}$ with $s[6] = \text{' '}$ $\implies$ **Segment 2 begins** (`"my"`)
    - Index 8: `'y'` $\implies$ Continuation
    - Index 9: `' '` $\implies$ Whitespace separator
    - Index 10: $s[10] = \text{'n'} \ne \text{' '}$ with $s[9] = \text{' '}$ $\implies$ **Segment 3 begins** (`"name"`)
    - Indices 11–13: `'a'`, `'m'`, `'e'` $\implies$ Continuation
    - Index 14: `' '` $\implies$ Whitespace separator
    - Index 15: $s[15] = \text{'i'} \ne \text{' '}$ with $s[14] = \text{' '}$ $\implies$ **Segment 4 begins** (`"is"`)
    - Index 16: `'s'` $\implies$ Continuation
    - Index 17: `' '` $\implies$ Whitespace separator
    - Index 18: $s[18] = \text{'J'} \ne \text{' '}$ with $s[17] = \text{' '}$ $\implies$ **Segment 5 begins** (`"John"`)
    - Indices 19–21: `'o'`, `'h'`, `'n'` $\implies$ Continuation
  - Total segments detected: $\mathbf{5}$
- **Consecutive Whitespace Instance:** $s = \text{"   "} \implies 0$ non-space segment heads $\implies \mathbf{0}$
- **Punctuation Characters:** $s = \text{"a, b"} \implies \text{"a,"}$ and $\text{"b"}$ $\implies \mathbf{2}$ (all non-space characters form segments)

This instance demonstrates in-place state transition counting, mathematically proves why counting segment heads avoids allocating intermediate string lists, and achieves $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"Hello, my name is John"}$:
A **segment** is defined as a contiguous sequence of non-space characters.
Return the number of segments in $s$.

```text
Input String:
  "Hello, my name is John"
   ^^^^^^  ^^ ^^^^ ^^ ^^^^
     1     2   3   4   5

Total Segments: 5
```

### The Segment Head Anchor
Instead of splitting the entire string into an allocated array of substrings ($O(N)$ extra memory):
A contiguous segment can be uniquely identified by its **initial character** (segment head).
A character at index $i$ is the beginning of a new segment if and only if:
1. $s[i]$ is not a whitespace character: $s[i] \ne \text{' '}$.
2. It either starts at the beginning of the string ($i = 0$) or immediately follows a whitespace character ($s[i - 1] == \text{' '}$).

$$
\text{IsSegmentHead}(i) = (s[i] \ne \text{' '}) \land (i == 0 \lor s[i - 1] == \text{' '})
$$

---

## 2. Conceptual Foundation & Invariants

### 1. In-Place Boundary Predicate:
By counting indices $i$ satisfying $\text{IsSegmentHead}(i)$, every segment is counted exactly once:
- **Soundness:** Any contiguous block of non-space characters has exactly one index that is either at index 0 or preceded by a space.
- **Completeness:** No trailing, leading, or multiple consecutive spaces can trigger the condition.

### 2. State Machine Model:
Alternatively, consider a 2-state automaton with states $\{\text{IN\_SPACE}, \text{IN\_WORD}\}$:
- Transition from $\text{IN\_SPACE} \to \text{IN\_WORD}$: Increment segment counter.
- Transition from $\text{IN\_WORD} \to \text{IN\_SPACE}$: Reset word state.
- Both models run in $O(1)$ auxiliary memory.

> **Bijection Invariant.** There is a strict 1-to-1 bijection between the set of maximal contiguous non-space substrings in $s$ and the set of indices $i$ where $\text{IsSegmentHead}(i)$ is true.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"Hello, my name is John"}$ ($N = 22$):

---

### Step 1: Scan Word 1 (`"Hello,"`)
- $i = 0, s[0] = \text{'H'}$: Non-space, $i = 0 \implies \mathbf{ans \leftarrow 1}$.
- $i = 1 \dots 5$: Non-space, but preceded by non-space $\implies$ Contiguous continuation.
- $i = 6, s[6] = \text{' '}$: Space character. Ignored.

---

### Step 2: Scan Word 2 (`"my"`)
- $i = 7, s[7] = \text{'m'}$: Non-space, $s[6] == \text{' '} \implies \mathbf{ans \leftarrow 2}$.
- $i = 8, s[8] = \text{'y'}$: Non-space, preceded by $'m'$.
- $i = 9, s[9] = \text{' '}$: Space character.

---

### Step 3: Scan Word 3 (`"name"`)
- $i = 10, s[10] = \text{'n'}$: Non-space, $s[9] == \text{' '} \implies \mathbf{ans \leftarrow 3}$.
- $i = 11 \dots 13$: Non-space continuation.
- $i = 14, s[14] = \text{' '}$: Space character.

---

### Step 4: Scan Word 4 (`"is"`)
- $i = 15, s[15] = \text{'i'}$: Non-space, $s[14] == \text{' '} \implies \mathbf{ans \leftarrow 4}$.
- $i = 16, s[16] = \text{'s'}$: Non-space continuation.
- $i = 17, s[17] = \text{' '}$: Space character.

---

### Step 5: Scan Word 5 (`"John"`)
- $i = 18, s[18] = \text{'J'}$: Non-space, $s[17] == \text{' '} \implies \mathbf{ans \leftarrow 5}$.
- $i = 19 \dots 21$: Non-space continuation.
- End of string reached.

---

### Final Result:
Total segment count: **`5`**.

---

## 4. Complete Execution Trace

| Index Range | Substring Segment | Character Type | Preceded by Space? | Segment Head Triggered? | Cumulative Segments |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[0 \dots 5]$ | `"Hello,"` | Non-space | Yes ($i = 0$) | **Yes (at $i = 0$)** | **$1$** |
| $[6]$ | `' '` | Whitespace | — | No | $1$ |
| $[7 \dots 8]$ | `"my"` | Non-space | Yes ($s[6] = \text{' '}$) | **Yes (at $i = 7$)** | **$2$** |
| $[9]$ | `' '` | Whitespace | — | No | $2$ |
| $[10 \dots 13]$ | `"name"` | Non-space | Yes ($s[9] = \text{' '}$) | **Yes (at $i = 10$)** | **$3$** |
| $[14]$ | `' '` | Whitespace | — | No | $3$ |
| $[15 \dots 16]$ | `"is"` | Non-space | Yes ($s[14] = \text{' '}$) | **Yes (at $i = 15$)** | **$4$** |
| $[17]$ | `' '` | Whitespace | — | No | $4$ |
| $[18 \dots 21]$ | `"John"` | Non-space | Yes ($s[17] = \text{' '}$) | **Yes (at $i = 18$)** | **$5$** |

---

## 5. Boundary Cases & Failure Modes

- **Empty String ($s = \text{""}$):** Loop does not execute $\implies 0$.
- **All Spaces ($s = \text{"     "}):$** $s[i] == \text{' '}$ for all $i \implies 0$.
- **Leading and Trailing Spaces ($s = \text{"  abc  def  "}):$** Head condition triggers only at index of `'a'` and `'d'`. Correctly counts $2$.
- **Single Character ($s = \text{"x"}):$** Non-space at $i = 0 \implies 1$.
- **Punctuation Without Spaces ($s = \text{"foo,bar"}):$** Punctuation characters are non-spaces. Count is $1$ (a single continuous segment).

---

## 6. Traps & Common Anti-Patterns

- **Assuming Only Letters Form Segments:** Characters such as commas, exclamation points, and digits are non-space characters and part of segments. Checking `c.isalpha()` causes incorrect segment fragmentations.
- **Counting Every Space as a Word Separator:** If multiple spaces appear between words (`"hello   world"`), counting spaces yields 3 separators instead of 2 words. Only state transitions from space to non-space represent words.
- **Materializing Full Substring Arrays:** Using `s.split()` in languages with heavy string memory footprints allocates $O(N)$ extra memory for new string objects. In-place index traversal uses $O(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The string is scanned once from left to right in $N$ steps.
  - Character comparisons take $O(1)$ time per index.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. Requires only integer index and count registers.
