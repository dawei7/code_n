# Guided Example: Reverse Words in a String

We trace the step-by-step whitespace-normalized word extraction and two-pointer character array reversal on representative string instances:

- **Input:** $s = \text{"  hello world  "}$
- **Required output:** $\text{"world hello"}$
- **Multiple Spaces Instance:** $s = \text{"a good   example"} \implies \text{"example good a"}$

This instance demonstrates stripping irregular leading, trailing, and repeated inter-word spaces, contrasting token-deque accumulation with the classical in-place three-step reversal algorithm (reverse entire string, then reverse each individual word), and achieving $O(N)$ linear runtime.

---

## 1. Instance & Teaching Goal

Given a string with irregular spacing:
$$
s = \text{"  hello world  "}
$$
Reverse the order of words and format the output so that words are separated by exactly one space, with no leading or trailing whitespace:
$$
\text{Output} = \text{"world hello"}
$$

The challenge contains two distinct requirements:
1. **Word Order Inversion:** The sequence of words $[\text{"hello"}, \text{"world"}]$ must be inverted to $[\text{"world"}, \text{"hello"}]$.
2. **Whitespace Normalization:** Redundant leading, trailing, and multiple consecutive inter-word spaces must be collapsed into a single space separator.

While higher-level split methods (`" ".join(reversed(s.split()))`) solve this concisely in $O(N)$ space, understanding low-level pointer manipulation reveals the classic $O(1)$ space follow-up:
1. Trim multiple spaces into single spaces.
2. Reverse the entire character buffer: $\text{"world hello"}^R = \text{"olleh dlrow"}$.
3. Reverse each individual word in-place: $\text{"hello"}$ and $\text{"world"}$.

The two families of solutions differ in what they allocate rather than in what they compute, so their tradeoffs are worth placing side by side before tracing either one:

| Approach | What it actually does | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Split on whitespace, then join the reversed tokens | Uses the language's whitespace-aware split to produce tokens and joins them backwards | $O(N)$ | $O(N)$ for the token list and result | Shortest to write and normalizes runs for free, but it hides the scanning logic and still allocates the full token list |
| Two-pointer extraction, as traced in Section 3 | Advances a skip pointer over spaces and a word pointer to the boundary, collecting slices | $O(N)$ | $O(N)$ for the collected words and result | Explicit and portable, and it never depends on the language's split semantics; it still copies each word into a token |
| Three-step reversal of one mutable buffer | Compacts spaces, reverses the whole buffer, then reverses every word inside it | $O(N)$ | $O(1)$ beyond the buffer itself | The only $O(1)$-auxiliary variant, but it needs a mutable character array, so it is unavailable on an immutable Python `str` without an explicit conversion |

---

## 2. Conceptual Foundation & Invariants

### Method 1: Two-Pointer Word Scanning Protocol
Let $N = |s|$.
Maintain pointer $i = 0$ and a list of words `words = []`.

While $i < N$:
1. **Skip Whitespace:**
   Advance $i$ while $i < N$ and $s[i] == \text{' '}$.
   If $i == N$: break.
2. **Identify Word Boundary:**
   Set $j = i$.
   Advance $j$ while $j < N$ and $s[j] \ne \text{' '}$.
3. **Extract Word:**
   Append token $s[i : j]$ to `words`.
   Set $i = j$.

Assemble final string:
$$
\text{result} = \text{" "}.\text{join}(\text{reversed}(\text{words}))
$$

### Method 2: The In-Place 3-Step Reversal Theorem
For languages with mutable character buffers (e.g. C++ or Java `char[]`):
1. **Space Normalization:** Two pointers compact characters, collapsing runs of spaces into single delimiters.
2. **Global Buffer Reversal:**
   $$
   \text{reverse}(A, \, 0, \, |A|-1)
   $$
   This puts words into reversed relative order, but inverts the spelling of each individual word.
3. **Local Word Reversal:**
   For each word delimited by space:
   $$
   \text{reverse}(A, \, \text{word\_start}, \, \text{word\_end})
   $$
   Restores each word to correct forward spelling.

> **Invariant.** After token extraction, `words` contains only non-empty strings of alphanumeric characters in their original left-to-right order, with all arbitrary space runs discarded.

---

## 3. Step-by-Step Worked Execution

We trace the two-pointer scan on $s = \text{"  hello world  "}$ ($N = 15$):

### Step 1: Skip Leading Spaces
- $i = 0$: $s[0] == \text{' '}$. Advance $i \to 1$.
- $i = 1$: $s[1] == \text{' '}$. Advance $i \to 2$.
- $i = 2$: $s[2] == \text{'h'} \ne \text{' '}$. Word 1 starts!

---

### Step 2: Extract First Word (`"hello"`)
- Set $j = i = 2$.
- Advance $j$ through letters $\text{'h'}, \text{'e'}, \text{'l'}, \text{'l'}, \text{'o'}$:
  - $j$ advances from $2 \to 7$.
  - At $j = 7$: $s[7] == \text{' '}$. Word boundary reached!
- Extract slice: $s[2:7] = \mathbf{\text{"hello"}}$.
- Append: `words = ["hello"]`.
- Update: $i = j = 7$.

---

### Step 3: Skip Inter-Word Space
- $i = 7$: $s[7] == \text{' '}$. Advance $i \to 8$.
- $i = 8$: $s[8] == \text{'w'} \ne \text{' '}$. Word 2 starts!

---

### Step 4: Extract Second Word (`"world"`)
- Set $j = i = 8$.
- Advance $j$ through letters $\text{'w'}, \text{'o'}, \text{'r'}, \text{'l'}, \text{'d'}$:
  - $j$ advances from $8 \to 13$.
  - At $j = 13$: $s[13] == \text{' '}$. Word boundary reached!
- Extract slice: $s[8:13] = \mathbf{\text{"world"}}$.
- Append: `words = ["hello", "world"]`.
- Update: $i = j = 13$.

---

### Step 5: Skip Trailing Spaces
- $i = 13$: $s[13] == \text{' '}$. Advance $i \to 14$.
- $i = 14$: $s[14] == \text{' '}$. Advance $i \to 15$.
- $i = 15 == N$. End of string reached!

---

### Step 6: Invert Word Order and Join
- Extracted words: `["hello", "world"]`.
- Reverse word list: `["world", "hello"]`.
- Join with single delimiter `" "`:
  $$
  \text{Output} = \mathbf{\text{"world hello"}}
  $$

---

## 4. Complete Execution Trace

```text
Input:       "  hello world  "
Pointers:     ^^-----^-----^^
Skipped:      [0..1] leading spaces
Word 1:       [2..6]  "hello"
Skipped:      [7]     inter-word space
Word 2:       [8..12] "world"
Skipped:      [13..14] trailing spaces

Extracted:    ["hello", "world"]
Reversed:     ["world", "hello"]
Formatted:    "world hello"
```

| Scan Phase | Pointer Interval $[i, j)$ | Characters Evaluated | Action Taken | Current `words` Array |
|:---:|:---:|:---|:---|:---|
| Leading Trim | $[0, 2)$ | `' '`, `' '` | Skip whitespace | `[]` |
| **Word 1** | **$[2, 7)$** | **`"hello"`** | **Capture word** | **`["hello"]`** |
| Inter-Word | $[7, 8)$ | `' '` | Skip whitespace | `["hello"]` |
| **Word 2** | **$[8, 13)$** | **`"world"`** | **Capture word** | **`["hello", "world"]`** |
| Trailing Trim | $[13, 15)$ | `' '`, `' '` | Skip whitespace | `["hello", "world"]` |
| **Final Join** | - | Invert & Join | `reversed(words)` | **`"world hello"`** |

The in-place method reaches the same output through three passes over a single buffer, and the buffer contents after each pass show exactly what each pass is responsible for:

| Pass | Buffer contents afterwards | Word boundaries reversed in this pass | Why the pass is needed |
|:---|:---|:---|:---|
| 1. Normalize whitespace | `hello world` | none | Collapsing the two leading, the one inter-word, and the two trailing spaces to single delimiters makes every later pass a plain scan over one-space separators |
| 2. Reverse the whole buffer | `dlrow olleh` | none | The words now sit in the required order, but the global reversal also spelled every word backwards |
| 3. Reverse each word in place | `world hello` | $[0, 4]$ and $[6, 10]$ | Restoring the spelling inside each word repairs the damage of pass 2 without disturbing the word order that pass 2 established |

The composition of passes 2 and 3 is the whole theorem: reversing the entire buffer and then reversing each of its words is exactly reversing the sequence of words, because each word's characters are reversed twice and therefore return to their original orientation.

---

## 5. Algorithmic Correctness

**Soundness.** A word is captured only when non-space characters are bounded by whitespace or string edges. Reversing the array of words changes their sequence from $[W_0, W_1, \dots, W_{k-1}]$ to $[W_{k-1}, \dots, W_0]$ without modifying individual character spelling within any word. Joining with single spaces guarantees exactly one space delimiter between adjacent words.

**Completeness.** Every index from $0$ to $N-1$ is visited by $i$ or $j$. No word characters can be skipped, and all non-space segments are extracted.

---

## 6. Traps This Instance Exposes

- **Leading / Trailing Whitespace Leakage:** Naively splitting by `" "` (e.g. `s.split(' ')`) creates empty strings `""` for consecutive spaces! Using regex, `s.split()` (without arguments in Python), or explicit character testing filters out all empty tokens.
- **Index Out of Bounds at String End:** In inner while loops, the condition `j < N` must always precede `s[j] != ' '` to prevent IndexError when the final word touches the end of the string.
- **Single Word String:** For $s = \text{"  hello  "}$, only `["hello"]` is extracted, returning `"hello"` with zero delimiter spaces.

Every case in this package is a different combination of leading, trailing, and repeated spaces, and in each one the delimiter count of the answer is pinned to $k - 1$ for $k$ extracted words:

| Case input | Extracted words | Delimiters in the answer | Required output | Why the normalization is correct |
|:---|:---|:---:|:---|:---|
| `"the sky is blue"` | `["the", "sky", "is", "blue"]` | $3$ | `"blue is sky the"` | Nothing needs compaction here; with four words the joined answer carries exactly $4 - 1 = 3$ single spaces |
| `"  hello world  "` | `["hello", "world"]` | $1$ | `"world hello"` | The two-space prefix and the two-space suffix are each consumed by a single skip phase, so neither becomes an empty token |
| `"a good   example"` | `["a", "good", "example"]` | $2$ | `"example good a"` | The three-space run is one skip phase rather than two empty words, so three words still yield exactly two delimiters |
| `"   solitary   "` | `["solitary"]` | $0$ | `"solitary"` | A lone word has no neighbour to separate from: the boundary case that breaks any implementation which unconditionally appends a delimiter after every word |
| `"  a  b   c d  "` | `["a", "b", "c", "d"]` | $3$ | `"d c b a"` | Space runs of length $2$, $3$, and $1$ all normalize to the same single delimiter, so only the word count survives into the output |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. Both pointers $i$ and $j$ advance strictly forward, visiting each character at most twice. Joining the extracted words takes $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$ to store the parsed words and the newly allocated output string.
