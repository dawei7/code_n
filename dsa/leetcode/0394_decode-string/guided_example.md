# Guided Example: Decode String

We trace the step-by-step nested bracket expansion, multi-digit integer accumulation ($num \leftarrow num \times 10 + \text{int}(c)$), dual-stack frame push on `'['` (`s1` for multipliers, `s2` for prefix strings), frame pop-and-multiply reduction on `']'` ($res \leftarrow prev + res \times k$), and arbitrary nesting depth resolution on representative encoded strings:

- **Input:** $s = \text{"3[a2[c]]"}$
- **Required output:** `"accaccacc"`
  - Nested bracket trace:
    - Step 1 ($c = \text{'3'}$): $num = 3$
    - Step 2 ($c = \text{'['}$): Push $3 \to s1$, push `""` $\to s2$; reset $num = 0, res = \text{""}$
    - Step 3 ($c = \text{'a'}$): Append to current level: $res = \text{"a"}$
    - Step 4 ($c = \text{'2'}$): Inner multiplier: $num = 2$
    - Step 5 ($c = \text{'['}$): Push $2 \to s1$, push `"a"` $\to s2$; reset $num = 0, res = \text{""}$
    - Step 6 ($c = \text{'c'}$): Append to inner level: $res = \text{"c"}$
    - Step 7 ($c = \text{']'}$): Close inner frame:
      - $k = 2, prev = \text{"a"} \implies res = \text{"a"} + \text{"c"} \times 2 = \text{"acc"}$
    - Step 8 ($c = \text{']'}$): Close outer frame:
      - $k = 3, prev = \text{""} \implies res = \text{""} + \text{"acc"} \times 3 = \mathbf{\text{"accaccacc"}}$
  - Result: `"accaccacc"`
- **Adjacent Sibling Sequences:** $s = \text{"3[a]2[bc]"} \implies \text{"aaabcbc"}$
- **Trailing / Unbracketed Characters:** $s = \text{"2[abc]3[cd]ef"} \implies \text{"abcabccdcdcdef"}$
- **Multi-Digit Multipliers:** $s = \text{"12[ab]"} \implies num$ parses $1 \to 12$, repeats `"ab"` twelve times

This instance demonstrates stack-based parsing of nested context-free grammars, mathematically proves why separating multiplier and prefix state decouples hierarchical scopes, avoids recursion limits, and achieves $O(|output|)$ time and $O(|output|)$ space.

---

## 1. Instance & Teaching Goal

Given an encoded string $s = \text{"3[a2[c]]"}$ where the encoding rule is `k[encoded_string]`, meaning the `encoded_string` inside the square brackets is repeated exactly $k$ times:
Decode the string to its fully expanded representation:

```text
Grammar Tree Representation:
           Root
             |
           3 * [...]
             |
         "a" + 2 * [...]
                 |
                "c"

Innermost resolution: 2 * "c" -> "cc"
Intermediate segment: "a" + "cc" -> "acc"
Outermost resolution: 3 * "acc" -> "accaccacc"
```

### The Dual-Stack Architecture
Because brackets can be arbitrarily nested (e.g. `3[a2[c]]`), an inner bracket pair must be evaluated and expanded before its enclosing outer repeat count can be applied:
1. `s1`: Stores the multiplier integers $k$ awaiting their closing bracket.
2. `s2`: Stores the prefix strings accumulated before entering the current bracket level.

---

## 2. Conceptual Foundation & Invariants

### 1. State Variables:
- `num`: Non-negative integer holding the multiplier currently being read.
- `res`: String accumulator of the decoded text at the current nesting level.
- `s1 = []`: Stack of integer multipliers.
- `s2 = []`: Stack of prefix strings.

### 2. State Transition Rules for Each Character $c \in s$:
1. **Digit ($c \in \text{'0'}\dots\text{'9'}$):**
   Accumulate multi-digit numbers:
   $$
   num \leftarrow num \times 10 + \text{int}(c)
   $$
2. **Open Bracket (`c == '['`):**
   Enter a new nested scope:
   - Push current multiplier: $s1.\text{append}(num)$.
   - Push accumulated prefix: $s2.\text{append}(res)$.
   - Clear registers for child scope: $num \leftarrow 0, \; res \leftarrow \text{""}$.
3. **Close Bracket (`c == ']'`):**
   Exit the active scope and resolve expansion:
   - Pop multiplier: $k = s1.\text{pop}()$.
   - Pop parent prefix: $prev = s2.\text{pop}()$.
   - Expand and concatenate:
     $$
     res \leftarrow prev + res \times k
     $$
4. **Letter ($c \in \text{'a'}\dots\text{'z'}$):**
   Append directly to the current frame:
   $$
   res \leftarrow res + c
   $$

> **Invariant.** At any moment, `res` contains the fully expanded text of the current nesting level, and `s2` stores the exact prefixes needed to assemble enclosing ancestor frames upon hitting `]`.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"3[a2[c]]"}$:
Initial: $num = 0, res = \text{""}, s1 = [], s2 = []$.

---

### Step 1: Character `'3'`
- Digit $\implies num = 0 \times 10 + 3 = \mathbf{3}$.

---

### Step 2: Character `'['` (Open Outer Frame)
- Save state to stacks:
  $$
  s1.\text{append}(3) \implies s1 = [3]
  $$
  $$
  s2.\text{append}(\text{""}) \implies s2 = [\text{""}]
  $$
- Reset active registers:
  $$
  num = 0, \quad res = \text{""}
  $$

---

### Step 3: Character `'a'`
- Letter $\implies res = \text{""} + \text{'a'} = \mathbf{\text{"a"}}$.

---

### Step 4: Character `'2'`
- Digit $\implies num = 0 \times 10 + 2 = \mathbf{2}$.

---

### Step 5: Character `'['` (Open Inner Frame)
- Save state to stacks:
  $$
  s1.\text{append}(2) \implies s1 = [3, \; 2]
  $$
  $$
  s2.\text{append}(\text{"a"}) \implies s2 = [\text{""}, \; \text{"a"}]
  $$
- Reset active registers:
  $$
  num = 0, \quad res = \text{""}
  $$

---

### Step 6: Character `'c'`
- Letter $\implies res = \text{""} + \text{'c'} = \mathbf{\text{"c"}}$.

---

### Step 7: Character `']'` (Close Inner Frame)
- Pop inner count: $k = s1.\text{pop}() = \mathbf{2}$.
- Pop inner prefix: $prev = s2.\text{pop}() = \mathbf{\text{"a"}}$.
- Frame reduction:
  $$
  res \leftarrow prev + res \times k = \text{"a"} + (\text{"c"} \times 2) = \mathbf{\text{"acc"}}
  $$
- Stacks after pop: $s1 = [3], s2 = [\text{""}]$.

---

### Step 8: Character `']'` (Close Outer Frame)
- Pop outer count: $k = s1.\text{pop}() = \mathbf{3}$.
- Pop outer prefix: $prev = s2.\text{pop}() = \mathbf{\text{""}}$.
- Frame reduction:
  $$
  res \leftarrow prev + res \times k = \text{""} + (\text{"acc"} \times 3) = \mathbf{\text{"accaccacc"}}
  $$
- Stacks after pop: $s1 = [], s2 = []$.

---

### Step 9: Termination
String scan complete. Return:
$$
\mathbf{\text{"accaccacc"}}
$$

---

## 4. Complete Execution Trace

```text
s = "3[a2[c]]"
Initial: num=0, res="", s1=[], s2=[]

c='3': num=3
c='[': s1=[3], s2=[""], num=0, res=""
c='a': res="a"
c='2': num=2
c='[': s1=[3, 2], s2=["", "a"], num=0, res=""
c='c': res="c"
c=']': k=2, prev="a"  -> res = "a" + "c"*2 = "acc"     (s1=[3], s2=[""])
c=']': k=3, prev=""   -> res = "" + "acc"*3 = "accaccacc" (s1=[], s2=[])

Final Output: "accaccacc"
```

| Step | Char $c$ | Action Taken | $num$ | Active $res$ | Multiplier Stack $s1$ | Prefix Stack $s2$ |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | `'3'` | Digit parse | 3 | `""` | `[]` | `[]` |
| 2 | `'['` | Push frame | 0 | `""` | `[3]` | `[""]` |
| 3 | `'a'` | Append char | 0 | `"a"` | `[3]` | `[""]` |
| 4 | `'2'` | Digit parse | 2 | `"a"` | `[3]` | `[""]` |
| 5 | `'['` | Push frame | 0 | `""` | `[3, 2]` | `["", "a"]` |
| 6 | `'c'` | Append char | 0 | `"c"` | `[3, 2]` | `["", "a"]` |
| **7** | **']'** | **Pop inner frame** | **0** | **`"acc"`** | **`[3]`** | **`[""]`** |
| **8** | **']'** | **Pop outer frame** | **0** | **`"accaccacc"`** | **`[]`** | **`[]`** |
| **Exit**| - | Complete | - | **`"accaccacc"`** | `[]` | `[]` |

---

## 5. Algorithmic Correctness

**Soundness.** In any balanced bracket language, each `]` matches the most recently opened unmatched `[`. By pushing $(k, prev)$ onto stacks when entering `[` and popping on `]`, the operation $prev + res \times k$ strictly preserves the precedence and repetition semantics of nested expressions without mixing outer and inner scopes.

**Completeness.** Every character in $s$ falls into exactly one of four disjoint cases: digit, open bracket, close bracket, or letter. Unbracketed letters (e.g. `"ef"` in `"2[a]ef"`) are appended directly to $res$ at depth 0, while multi-digit numbers are fully accumulated before encountering `[`, guaranteeing complete coverage of all valid grammar strings.

---

## 6. Traps This Instance Exposes

- **Multi-Digit Numbers:** Repeat counts can be multiple digits (e.g. `10[a]`, `100[leetcode]`). Writing `num = int(c)` resets the multiplier on every digit. It must be shifted: `num = num * 10 + int(c)`.
- **String Concatenation Order:** When popping on `]`, the order is strictly $prev + res \times k$, NOT $res \times k + prev$. The prefix was read *before* the brackets and must appear on the left.
- **Direct String Multiplication Memory:** In Python, string multiplication `"a" * 100` is efficient. However, in deeply nested inputs with large multipliers, output size dominates; ensuring that strings are concatenated in linear fashion prevents quadratic copying.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$, where $M = \text{len}(output)$ is the total length of the decoded string.
  - Parsing characters in $s$ takes $O(N)$ time.
  - Creating and repeating string characters takes time proportional to the output length $M$.
  - Since $M \ge N$, overall time complexity is $O(M)$.
- **Auxiliary Space Complexity:** $O(M + D)$, where $D$ is the maximum bracket nesting depth for stacks $s1$ and $s2$, and $M$ is the memory for string fragments stored in $s2$.
