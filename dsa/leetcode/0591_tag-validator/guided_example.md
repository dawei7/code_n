# Guided Example: Tag Validator

We trace the step-by-step lexical token scanning, grammar state parsing, stack-based opening and closing tag matching (`stk`), CDATA block raw data jumping (`<![CDATA[` to `]]>`), tag name syntactic validation ($1 \le \text{length} \le 9$, all uppercase), and single-root enclosing envelope verification on representative markup snippets:

- **Input:** $code = \text{"<DIV>This is <![CDATA[<raw>]]></DIV>"}$
- **Required output:** `true`
  - Validation grammar rules:
    1. **Single Root Enclosure:** The entire snippet must be enclosed within one valid outer tag pair `<TAG_NAME> ... </TAG_NAME>`. If the tag stack becomes empty before reaching the end of the string, the snippet is invalid.
    2. **Tag Name Syntax:** `TAG_NAME` must contain between $1$ and $9$ characters, all uppercase English letters (`[A-Z]`).
    3. **Proper Nesting (LIFO):** Each closing tag `</TAG_NAME>` must match the most recently opened tag on top of the stack.
    4. **CDATA Exemption:** CDATA blocks start with `<![CDATA[` and end with `]]>`. The content inside CDATA is treated as literal text and is never parsed for tags. CDATA blocks must be enclosed inside a tag.
- **Parsing State Machine & Stack Trace:**
  - Let `stk` be the LIFO stack of active open tags.
  - Let pointer $i = 0$ scan the string of length $n = 35$.
  - **Invariant Check on Entry:**
    - If $i > 0$ and `stk` is empty, there are characters outside the root tag $\implies$ early fail!
  - **Step 1 ($i = 0$): Encounter Opening Tag `<DIV>`:**
    - Character at $i$ is `'<'`.
    - Next character is `'D'` (not `'/'` and not `'!'`).
    - Search for matching `'>'`: found at index $4$.
    - Extract tag name:
      $$
      t = code[1 \dots 3] = \mathbf{\text{"DIV"}}
      $$
    - Validate syntax of `"DIV"`:
      - Length $3 \in [1, 9]$ (Valid).
      - All characters uppercase (`'D', 'I', 'V'`) (Valid).
    - Push `"DIV"` onto stack:
      $$
      stk = [\text{"DIV"}]
      $$
    - Advance pointer to $i = 5$.
  - **Step 2 ($i = 5 \dots 12$): Parse Inner Content `"This is "`:**
    - Characters are standard text inside the open tag.
    - None of these are `'<'`, so pointer advances to $i = 13$.
  - **Step 3 ($i = 13$): Encounter CDATA Block `<![CDATA[`:**
    - Check prefix: $code[13 \dots 21] = \text{"<![CDATA["}$.
    - Exact match for CDATA start delimiter!
    - Search forward from index $22$ for closing delimiter `]]>`:
      - Found at index $28$.
    - The raw content inside is `"<raw>"`.
      - Even though `"<raw>"` contains tag-like characters `'<'` and `'>'`, the CDATA rule treats it as inert raw text!
    - Fast-forward pointer past delimiter: $i \leftarrow 28 + 2 = 30$.
  - **Step 4 ($i = 31$): Encounter Closing Tag `</DIV>`:**
    - Check prefix: $code[31 \dots 32] = \text{"</"}$.
    - Search for matching `'>'`: found at index $36$ ($i = 36$).
    - Extract closing tag name:
      $$
      t = code[33 \dots 35] = \mathbf{\text{"DIV"}}
      $$
    - Validate syntax: length $3 \in [1, 9]$, uppercase $\implies$ Valid.
    - Check stack top:
      - Top of `stk` is `"DIV"`.
      - Matches closing tag: $stk.\text{pop}() == \text{"DIV"} \implies \mathbf{True!}$
    - Stack becomes empty:
      $$
      stk = []
      $$
    - Advance pointer past closing tag: $i = 37$.
  - **Step 5: End of String Verification:**
    - Pointer $i = 37$ has reached end of string ($i == n$).
    - Check stack state:
      $$
      \text{stk is empty} \implies \mathbf{True}
      $$
    - Validation succeeds: return **`true`**.
- **Premature Root Closure / Multiple Roots Instance ($code = \text{"<A></A><B></B>"}$):**
  - `<A></A>` closes, causing `stk` to become empty at index 7.
  - When pointer inspects `<B>` at index 7, $i > 0$ and `stk` is empty $\implies$ violates single root enclosure $\implies \mathbf{false}$.
- **Tag Mismatch Instance ($code = \text{"<A><B></A></B>"}$):**
  - Stack contains `["A", "B"]`.
  - Closing tag `</A>` encountered: top of stack is `"B"`, but closing tag is `"A"` $\implies$ LIFO violation $\implies \mathbf{false}$.
- **Invalid Tag Name Syntax ($code = \text{"<divA></divA>"}$):**
  - Lowercase letters in tag name violate syntax rule $\implies \mathbf{false}$.

This instance demonstrates deterministic context-free markup parsing and stack-based balanced parenthesization, mathematically proves why root isolation and CDATA skip pointers ensure linear parsing without backtracking, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string `code`, validate whether it adheres to the HTML/XML-like syntax:
1. Entire string is wrapped in a **single closed root tag**.
2. Tag names must be **1 to 9 uppercase letters**.
3. Closing tags must strictly match open tags in **LIFO order**.
4. CDATA blocks `<![CDATA[ ... ]]>` can contain any characters and must be inside a tag.

```text
code: "<DIV>This is <![CDATA[<raw>]]></DIV>"

1. Open root <DIV> -> push "DIV"
2. Text "This is " -> literal
3. <![CDATA[<raw>]]> -> skip raw block (do not parse <raw>)
4. Close root </DIV> -> pop "DIV" (match!)
5. String ends with empty stack -> Valid! (true)
```

### The Invariant of Single Root Enclosure
- In valid XML/HTML snippets, the whole document must form a single tree.
- If at any point $i > 0$ the stack becomes empty and there are still unparsed characters remaining, there are either siblings at the root level (e.g. `<A></A><B></B>`) or dangling text outside the root tag. Both are strictly invalid.

---

## 2. Conceptual Foundation & Invariants

### 1. Tag Name Checker:
A tag name $t$ is valid if and only if:
$$
1 \le |t| \le 9 \quad \text{and} \quad \forall c \in t: c \in ['A', 'Z']
$$

### 2. Lexical Branching:
At index $i$:
1. If $i > 0$ and `stk` is empty: return `False`.
2. If prefix is `<![CDATA[`:
   - Find closing `]]>`. If not found, return `False`.
   - Jump $i$ past `]]>`.
3. If prefix is `</`:
   - Find `>`. Extract closing tag $t$.
   - Must satisfy: `check(t)` and `stk.pop() == t`.
4. If prefix is `<`:
   - Find `>`. Extract opening tag $t$.
   - Must satisfy: `check(t)`.
   - Push $t$ to `stk`.

> **Grammar Containment Invariant.** The parser state requires `len(stk) >= 1` for every character position except index 0 and the final closing index $N$, guaranteeing that all text and CDATA live strictly within an open element.

---

## 3. Step-by-Step Worked Execution

We trace `"<DIV>This is <![CDATA[<raw>]]></DIV>"`:

---

### Step 1: Open Tag `<DIV>`
- $i = 0$: `<DIV>`.
- Tag name `"DIV"` has length 3, all uppercase $\implies$ Valid.
- $stk = [\text{"DIV"}]$.
- Jump to $i = 5$.

---

### Step 2: Plain Text
- Characters `"This is "` consume indices $5 \dots 12$.
- $stk$ remains `["DIV"]`.

---

### Step 3: CDATA Block
- At $i = 13$: prefix is `<![CDATA[`.
- Find `]]>` $\to$ found ending at index $30$.
- Skip past CDATA: $i \leftarrow 30$.

---

### Step 4: Close Tag `</DIV>`
- At $i = 31$: `</DIV>`.
- Closing tag name `"DIV"`.
- $stk.\text{pop}() == \text{"DIV"}$.
- Stack becomes empty `[]`.

---

### Step 5: Termination Check
- String index reached end ($i = n$).
- `stk` is empty.
- Returns **`True`**.

---

## 4. Complete Execution Trace

| Index $i$ | Substring / Token | Token Type | Stack Action | Stack State After | Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `<DIV>` | Opening Tag | Push `"DIV"` | `["DIV"]` | Yes |
| $5$ | `"This is "` | Literal Text | Advance $i$ | `["DIV"]` | Yes |
| $13$ | `<![CDATA[<raw>]]>` | CDATA Block | Skip to end of `]]>` | `["DIV"]` | Yes |
| $31$ | `</DIV>` | Closing Tag | Pop `"DIV"` | `[]` | Yes |
| **End** | End of string | Terminal | Check empty | `[]` | **Result: `True`** |

---

## 5. Boundary Cases & Failure Modes

- **Unclosed CDATA (`<![CDATA[raw`):** No `]]>` found $\implies \mathbf{false}$.
- **Unclosed Tag (`<DIV>` alone):** Loop ends with `stk` containing `"DIV"` $\implies \mathbf{false}$.
- **Tag Name Too Long (`<ABCDEFGHIJ>` of length 10):** Fails length check $\le 9 \implies \mathbf{false}$.
- **Empty Tag Name (`<>`):** Fails length check $\ge 1 \implies \mathbf{false}$.
- **Lowercase Tag (`<div>`):** Fails uppercase check $\implies \mathbf{false}$.

---

## 6. Traps & Common Anti-Patterns

- **Parsing Tags Inside CDATA:** Treating `<raw>` inside CDATA as an open tag corrupts the tag stack. The CDATA scanner must fast-forward directly to `]]>` without inspecting internal characters.
- **Dangling Sibling Roots (`<A></A><B></B>`):** Checking only that `stk` is empty at the end is insufficient; `stk` must NEVER become empty during intermediate steps ($i > 0$ and $i < n$).
- **Using Unbounded Regular Expressions:** Writing massive nested regular expressions often suffers catastrophic backtracking on malformed inputs. An explicit linear pointer scanner runs in strictly guaranteed $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The pointer $i$ advances monotonically through the string of length $N$.
  - Tag extraction and CDATA search (`find`) advance $i$ forward.
  - Every character is visited $\mathcal{O}(1)$ times.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the tag stack in the worst case of deeply nested tags.
