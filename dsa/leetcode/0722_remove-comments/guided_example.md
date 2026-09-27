# Guided Example: Remove Comments

We trace the step-by-step lexical state machine scanning, line-comment truncation (`//`), multi-line block-comment open/close delimitation (`/*` and `*/`), inter-line buffer accumulation ($t$), cross-line code concatenation, and non-empty line emission on representative source code text buffers:

- **Input:**
  $$
  source = [
    \text{"a/* comment"},
    \text{"continued */b"}
  ]
  $$
- **Required output:** `["ab"]`
  - Lexical parsing specifications:
    - C++ comments come in two forms:
      1. **Line Comment (`//`):** Ignores all characters from `//` to the end of the current line.
      2. **Block Comment (`/*` to `*/`):** Ignores all characters between `/*` and the first subsequent `*/`. Can span multiple lines.
    - Multi-line block comment concatenation:
      - If a block comment starts on one line and terminates on a subsequent line, any code preceding `/*` and any code succeeding `*/` are concatenated into a **single unified line**.
    - Empty line suppression:
      - If an entire line becomes empty after removing comments, it is omitted from the output.
    - For the input:
      - Line 1 has code `'a'` followed by `/*`.
      - Line 2 has `*/` followed by code `'b'`.
      - The comment block spans from line 1 to line 2.
      - The surviving characters `'a'` and `'b'` fuse into `"ab"`.
- **Lexical State Machine & Buffer Invariant:**
  - **State Variable:**
    - `block_comment`: boolean flag indicating whether the scanner is currently inside a block comment.
    - Crucial Invariant: `block_comment` **persists across lines**, whereas line comments terminate at the end of each string.
  - **The Character Accumulator ($t$):**
    - `t` collects surviving code characters for the currently active output line.
    - If a line finishes while `block_comment == true`, the accumulator $t$ is **not flushed**; it waits to collect any trailing code after the comment closes on a later line.
  - **Token Matching Priority (when not in block comment):**
    1. If $s[i \dots i+1] == \text{"/*"}$:
       - Enter block comment: `block_comment = true`. Advance $i$ past the 2-character token ($i \leftarrow i + 1$).
    2. Else if $s[i \dots i+1] == \text{"//"}$:
       - Line comment encountered: truncate and discard the rest of the line immediately (`break`).
    3. Otherwise:
       - Regular source code character: append $s[i]$ to buffer $t$.
  - **Closing Token Matching (when in block comment):**
    - Scan for $s[i \dots i+1] == \text{"*/"}$:
      - Exit block comment: `block_comment = false`. Advance $i$ past the 2-character token.
  - **Line Flush Condition:**
    - At the end of each input line:
      - If `not block_comment and t`:
        - Flush buffer to output: $ans.\text{append}(\text{string}(t))$.
        - Clear buffer $t$.
- **Step-by-Step Worked Execution Trace on $[\text{"a/* comment"}, \; \text{"continued */b"}]$:**
  - Initial state:
    $$
    ans = [], \quad t = [], \quad block\_comment = \text{false}
    $$
  - **Line 0 ($s = \text{"a/* comment"}$, length 12):**
    - $i = 0$ ($s[0] = \text{'a'}$):
      - `block_comment` is false.
      - Two-character lookahead $s[0 \dots 1] = \text{"a/"} \ne \text{"/*"}$ and $\ne \text{"//"}$.
      - Regular code: $t.\text{append}(\text{'a'}) \implies t = [\text{'a'}]$.
      - Advance: $i \leftarrow 1$.
    - $i = 1$ ($s[1 \dots 2] = \text{"/*"}$):
      - Matches opening delimiter `"/*"`!
      - Activate block comment state:
        $$
        block\_comment \leftarrow \mathbf{true}
        $$
      - Skip delimiter: $i \leftarrow 1 + 1 = \mathbf{2}$.
      - Loop increment advances: $i \leftarrow 3$.
    - $i = 3 \dots 11$:
      - In block comment. No `"*/"` encountered.
    - End of Line 0 reached:
      - Test flush condition: `not block_comment and t`.
      - Since $block\_comment == \mathbf{true}$, line is **not flushed**!
      - Buffer $t = [\text{'a'}]$ is retained across lines.
  - **Line 1 ($s = \text{"continued */b"}$, length 14):**
    - Initial state: $block\_comment = \text{true}, \; t = [\text{'a'}]$.
    - $i = 0 \dots 9$ (text `"continued "`):
      - Inside block comment. Ignored.
    - $i = 10$ ($s[10 \dots 11] = \text{"*/"}$):
      - Matches closing delimiter `"*/"`!
      - Deactivate block comment state:
        $$
        block\_comment \leftarrow \mathbf{false}
        $$
      - Skip delimiter: $i \leftarrow 10 + 1 = \mathbf{11}$.
      - Loop increment advances: $i \leftarrow 12$.
    - $i = 12$ ($s[12] = \text{'b'}$):
      - `block_comment` is false!
      - Regular code:
        $$
        t.\text{append}(\text{'b'}) \implies t = [\text{'a'}, \; \text{'b'}]
        $$
      - Advance: $i \leftarrow 13$.
    - End of Line 1 reached:
      - Test flush condition: $block\_comment == \text{false} \land t \ne [] \implies \mathbf{Flush!}$
      - Combine characters: $\text{join}([\text{'a'}, \text{'b'}]) = \mathbf{\text{"ab"}}$.
      - Append to output:
        $$
        ans \leftarrow [\mathbf{\text{"ab"}}]
        $$
      - Clear buffer $t \leftarrow []$.
  - **Step 3: Execution Complete:**
    $$
    ans = [\mathbf{\text{"ab"}}]
    $$
- **Line Comment with Preceding Whitespace Trace ($source = [\text{"int x = 1; // note"}] $):**
  - Characters `"int x = 1; "` appended to $t$.
  - `"//"` encountered $\implies$ line scanning breaks.
  - Flushes `"int x = 1; "` to output.
- **Empty Line from Whole-Line Comment ($source = [\text{"// comment"}] $):**
  - Line breaks at $i = 0$.
  - Buffer $t$ is empty $\implies$ no line emitted.

This instance demonstrates deterministic finite-state string tokenization and multi-line stream defragmentation, mathematically proves why lexical state persistence across line boundaries resolves inter-line comment splicing, and derives $O(L)$ execution time and $O(L)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given C++ source code lines:
Remove all **line comments (`//`)** and **block comments (`/* ... */`)**.
Concatenate code split across multi-line block comments onto the same line.
Omit lines that become empty.

```text
source:
  "a/* comment"
  "continued */b"

Line 1: 'a' is kept, "/*" starts block comment
Line 2: "*/" ends block comment, 'b' is kept

Surviving characters fuse together: "ab"
Result: [ "ab" ]
```

### The Invariant of the Cross-Line Buffer
- `block_comment` is a state that persists between lines.
- When an active block comment spans across multiple lines, the character buffer $t$ must **not be flushed** at the end of the line.
- $t$ only flushes when a line ends and `block_comment` is false.

---

## 2. Conceptual Foundation & Invariants

### 1. Lexical State Machine:
For each line $s$:
- If `block_comment`:
  $$
  s[i:i+2] == \text{"*/"} \implies block\_comment \leftarrow \mathbf{False}, \quad i \leftarrow i + 1
  $$
- If not `block_comment`:
  $$
  s[i:i+2] == \text{"/*"} \implies block\_comment \leftarrow \mathbf{True}, \quad i \leftarrow i + 1
  $$
  $$
  s[i:i+2] == \text{"//"} \implies \mathbf{break}
  $$
  $$
  \text{else} \implies t.\text{append}(s[i])
  $$

### 2. Line Flush Invariant:
$$
\text{If } \neg block\_comment \land |t| > 0 \implies ans.\text{append}(\text{join}(t)), \quad t.\text{clear}()
$$

> **Chomsky Type-3 Lexical Automaton Invariant.** The grammar of C-style comment stripping forms a regular language recognized by a 2-state deterministic finite automaton $\{ \text{Code}, \text{BlockComment} \}$, whose output transduction preserves token adjacency across newline transitions.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Line 1 (`"a/* comment"`)
- `'a'` appended to $t = [\text{'a'}]$.
- `"/*"` sets `block_comment = True`.
- Line ends with `block_comment == True` $\implies$ do not flush.

---

### Step 2: Line 2 (`"continued */b"`)
- `"continued "` skipped.
- `"*/"` sets `block_comment = False`.
- `'b'` appended to $t = [\text{'a'}, \text{'b'}]$.
- Line ends with `block_comment == False` $\implies$ flush `"ab"`.

---

### Step 3: Output
$$
[\mathbf{\text{"ab"}}]
$$

---

## 4. Complete Execution Trace

| Line Number | Current Token | Active Parser State | Action Taken | Buffer $t$ State | Flushed to Output? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `'a'` | Code | Append character | `['a']` | No |
| $0$ | `"/*"` | Code $\to$ Block | Enter Block Comment | `['a']` | No |
| $0$ | End of Line | Block Comment | Inactive (Block Open) | `['a']` | No |
| $1$ | `"*/"` | Block $\to$ Code | Exit Block Comment | `['a']` | No |
| $1$ | `'b'` | Code | Append character | `['a', 'b']` | No |
| **$1$** | **End of Line** | **Code** | **Flush Line** | **`[]`** | **`"ab"`** |

---

## 5. Boundary Cases & Failure Modes

- **Line Comment Preceded by Spaces (`"  // note"`):** Retains leading spaces `"  "` if spaces are code.
- **Multiple Comments on Same Line (`"a/*1*/b/*2*/c"`):** Concatenates into `"abc"`.
- **Delimiters inside Block Comments:** A `"/*"` inside an existing block comment is ignored; only `"*/"` can close it.
- **No Comments in Source:** Entire source returned identical to input.

---

## 6. Traps & Common Anti-Patterns

- **Flushing $t$ at Every Line End:** Flushing $t$ at the end of every line outputs `["a", "b"]` instead of `"ab"`, failing multi-line block comment concatenation.
- **Overlapping Tokens (`/*/*` or `/*/`):** Advancing $i += 1$ when matching a 2-character delimiter prevents double-counting (e.g. `/*/` is not a closed comment).
- **Line Comments Starting with Single Slash (`/`):** Must verify both characters `s[i:i+2] == "//"`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Scans each character in the source text at most twice (due to 2-character lookahead).
  - Total Time: strictly linear $\mathcal{O}(L)$ where $L$ is total characters across all lines. Completes in $< 2$ ms for $L = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ memory to store the reconstructed code lines.
