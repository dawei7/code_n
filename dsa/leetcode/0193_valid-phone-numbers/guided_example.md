# Guided Example: Valid Phone Numbers

We trace the step-by-step regular expression matching, boundary anchoring, and prefix branching on representative phone number candidate files:

- **Input File `file.txt`:**
  ```text
  987-123-4567
  123 456 7890
  (123) 456-7890
  ```
- **Required output:**
  ```text
  987-123-4567
  (123) 456-7890
  ```
- **Invalid Prefix Instance:** `123 456 7890` (Space separator instead of hyphen $\implies$ Disqualified)
- **Sub-String Embedded Instance:** `abc987-123-4567xyz` (Anchors `^` and `$` reject extra surrounding characters)
- **Missing Area Code Space Instance:** `(123)456-7890` (Requires space after closing parenthesis $\implies$ Disqualified)

This instance demonstrates POSIX Extended Regular Expression (ERE) pattern design, proves why start (`^`) and end (`$`) line anchors are essential to prevent partial substring matches, analyzes the two valid prefix grammars, and executes in linear $O(C)$ time across the character stream.

---

## 1. Instance & Teaching Goal

Given a text file `file.txt` containing phone number candidates (one per line):
```text
987-123-4567
123 456 7890
(123) 456-7890
```
Print all lines that conform strictly to either of the two standard North American telephone formats:
1. **Format 1 (Hyphen-delimited):** `xxx-xxx-xxxx`
2. **Format 2 (Parenthesized area code with space):** `(xxx) xxx-xxxx`

Evaluating each candidate:
- `987-123-4567`: Matches Format 1 ($3$ digits, hyphen, $3$ digits, hyphen, $4$ digits). **Valid.**
- `123 456 7890`: Uses spaces instead of hyphens between exchange and subscriber numbers. **Invalid.**
- `(123) 456-7890`: Matches Format 2 (parenthesized area code, single space, $3$ digits, hyphen, $4$ digits). **Valid.**
Output must stream the valid lines in their original order.

---

## 2. Conceptual Foundation & Invariants

### The Unified Extended Regular Expression (ERE)
Both valid formats share an identical suffix:
$$
\text{suffix} = \texttt{[0-9]\{3\}-[0-9]\{4\}}
$$
The formats differ only in their 3-digit area code prefix:
- Option A: `[0-9]{3}-`
- Option B: `\([0-9]{3}\) ` *(note the trailing literal space!)*

Combining with alternation group `(A|B)` and anchoring to line boundaries:
$$
\text{Pattern} = \texttt{\textasciicircum([0-9]\{3\}-|\textbackslash([0-9]\{3\}\textbackslash) )[0-9]\{3\}-[0-9]\{4\}\$}
$$

### Command Implementations:
1. **`grep -E` (Standard Unix Regex Filter):**
   ```bash
   grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
   ```
2. **`awk` Pattern Matcher:**
   ```bash
   awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
   ```
3. **`sed -n` Stream Editor:**
   ```bash
   sed -n -E '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
   ```

### Why Anchors `^` and `$` Are Mandatory
- `^` asserts the match starts at the very beginning of the line.
- `$` asserts the match terminates at the very end of the line.
Without `^` and `$`, a line containing extra characters (e.g. `ext 987-123-4567` or `123-456-78901`) would match as a substring!

> **Invariant.** A line is printed if and only if its entire character sequence from index $0$ to $\text{length}-1$ exactly satisfies the language $\mathcal{L}(\text{Pattern})$.

---

## 3. Step-by-Step Worked Execution

We trace the regex engine across the lines of `file.txt`:

### Line 1: `"987-123-4567"`
1. `^` matches beginning of line.
2. Prefix evaluation:
   - Option A: `[0-9]{3}-` tests `"987-"`. Three digits followed by hyphen $\implies$ **Match!**
3. Suffix evaluation:
   - `[0-9]{3}-` tests `"123-"`. Three digits followed by hyphen $\implies$ Match.
   - `[0-9]{4}` tests `"4567"`. Four digits $\implies$ Match.
4. `$` matches end of line.
- Full line matches pattern!
- Emitted: `987-123-4567`.

---

### Line 2: `"123 456 7890"`
1. `^` matches beginning of line.
2. Prefix evaluation:
   - Option A: `[0-9]{3}-` expects hyphen after 123. Found space `' '` $\implies$ Fail.
   - Option B: `\([0-9]{3}\) ` expects opening parenthesis `'('`. Found `'1'` $\implies$ Fail.
- Neither branch of the prefix group matches.
- Line rejected! Discarded.

---

### Line 3: `"(123) 456-7890"`
1. `^` matches beginning of line.
2. Prefix evaluation:
   - Option A: `[0-9]{3}-` expects digit. Found `'('` $\implies$ Fail.
   - Option B: `\([0-9]{3}\) ` tests `"(123) "`:
     - Literal `'('` $\implies$ Match.
     - Three digits `"123"` $\implies$ Match.
     - Literal `')'` $\implies$ Match.
     - Single space `' '` $\implies$ Match.
     - Option B **Matches!**
3. Suffix evaluation:
   - `[0-9]{3}-` tests `"456-"` $\implies$ Match.
   - `[0-9]{4}` tests `"7890"` $\implies$ Match.
4. `$` matches end of line.
- Full line matches pattern!
- Emitted: `(123) 456-7890`.

---

## 4. Complete Execution Trace

```text
File file.txt:
Line 1: 987-123-4567   -> Matches Option A prefix + suffix -> PRINT
Line 2: 123 456 7890   -> Prefix fails (space instead of -) -> DROP
Line 3: (123) 456-7890 -> Matches Option B prefix + suffix -> PRINT

Output Stream:
987-123-4567
(123) 456-7890
```

| Line Number | Line Content | Prefix Evaluated | Suffix Evaluated | Full Match Status | Action Taken |
|:---:|:---|:---|:---|:---:|:---|
| **1** | **`987-123-4567`** | Option A (`"987-"`) | `"123-4567"` | **Valid** | **Printed** |
| 2 | `123 456 7890` | Neither branch | - | Invalid | Dropped |
| **3** | **`(123) 456-7890`** | Option B (`"(123) "`) | `"456-7890"` | **Valid** | **Printed** |

---

## 5. Algorithmic Correctness

**Soundness.** Every accepted line strictly complies with the ERE specification. The alternation `(A|B)` precisely covers the two allowed representations. Escaping parentheses `\(` and `\)` ensures they are treated as literal characters rather than capture groups.

**Completeness.** Lines are evaluated in a single sequential streaming pass. Any valid phone number line present in `file.txt` is matched and printed.

---

## 6. Traps This Instance Exposes

- **Missing Parenthesis Space:** A candidate like `(123)456-7890` lacks the mandatory space after the closing parenthesis. The pattern requires a literal space after `\)`.
- **Missing Boundary Anchors:** Omitting `^` or `$` causes grep to perform substring matching, erroneously accepting strings like `call 987-123-4567 now` or `987-123-45678`.
- **Unescaped Parentheses in ERE:** In Extended Regular Expressions, unescaped `(` and `)` denote capture groups. Failing to escape them as `\(` and `\)` prevents matching literal parenthesis characters.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$, where $C$ is the total number of characters in `file.txt`. A deterministic finite automaton (DFA) constructed from the regular expression processes each character in $O(1)$ state transitions.
- **Auxiliary Space Complexity:** $O(L)$ where $L$ is the maximum line length (constant buffer space for line streaming).
