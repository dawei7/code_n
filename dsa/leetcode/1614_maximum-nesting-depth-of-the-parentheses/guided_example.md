# Guided Example: Maximum Nesting Depth of the Parentheses

This guide demonstrates prefix counter accumulation to compute the maximum nesting depth of a valid parentheses expression in a single linear pass.

- **Input Expression:** `s = "(1+(2*3)+((8)/4))+1"`
- **Length:** $N = 21$ characters
- **Target Nesting Depth:** `3` (Attained inside the subexpression `((8)/4)`)

---

## 1. Instance & Teaching Goal

The nesting depth of a valid parentheses string measures the maximum number of open, unclosed parentheses enclosing any character at any position in the string. Non-parenthesis characters (such as digits `'0'-'9'` and arithmetic operators `'+'`, `'-'`, `'*'`, `'/'`) do not alter the nesting layer.

```
Nesting Contour Visualization:
  d=3 |                  ___(8)___
  d=2 |         _(2*3)_ /         \
  d=1 |  ______(       +           /4)______
  d=0 |_/                                   \___+1___
      s: (  1  +  ( 2 * 3 ) + ( ( 8 ) / 4 ) ) + 1
```

Because the input is guaranteed to be a syntactically valid parentheses string (VPS), we do not need to validate syntax or manage an explicit stack. An integer counter tracking currently open levels is necessary and sufficient.

Our teaching goal is to model linear prefix state tracking in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

```
+-------------------------------------------------------------------------+
|                    PREFIX DEPTH COUNTER MECHANISM                       |
|                                                                         |
|  State Variables:                                                       |
|    d   = Current open parentheses depth (initially 0)                   |
|    ans = Peak depth recorded across the scan (initially 0)              |
|                                                                         |
|  Character Transitions:                                                 |
|    When c == '(':                                                       |
|        d += 1                                                           |
|        ans = max(ans, d)                                                |
|                                                                         |
|    When c == ')':                                                       |
|        d -= 1                                                           |
|                                                                         |
|    When c in {'0'-'9', '+', '-', '*', '/'}:                             |
|        No-op (d remains unchanged)                                      |
+-------------------------------------------------------------------------+
```

| Token Encountered | Depth Effect $\Delta d$ | Maximum Candidate Check | Rationale |
|---|---|---|---|
| `'('` | $+1$ | $\text{ans} \leftarrow \max(\text{ans}, d)$ | Enters a strictly deeper nested sub-scope |
| `')'` | $-1$ | Ignored | Exits current scope; cannot establish a new peak |
| Other character | $0$ | Ignored | Non-structural arithmetic literal or operator |

> **Prefix Balance Invariant.** For any valid parentheses string, the running counter $d_i = \text{count}('(', s[0..i]) - \text{count}(')', s[0..i])$ satisfies $d_i \ge 0$ for all prefixes $0 \le i < N$, and concludes at $d_{N-1} = 0$. The nesting depth of the string is precisely $\max_{0 \le i < N} d_i$.

```mermaid
flowchart TD
    accTitle: Parentheses Depth Scanner
    accDescr: Sequential character evaluation updating active depth counter and peak tracker.
    Char["Read Character c"] --> Type{"Character Type?"}
    Type -->|'('| Inc["d += 1; ans = max(ans, d)"]
    Type -->|')'| Dec["d -= 1"]
    Type -->|Other| Skip["Ignore character"]
    Inc --> Next{"More characters?"}
    Dec --> Next
    Skip --> Next
    Next -->|Yes| Char
    Next -->|No| Ret["Return ans"]
```

---

## 3. Step-by-Step Worked Execution

### Scan Progression on `s = "(1+(2*3)+((8)/4))+1"`

- Initial state: $d = 0$, $\text{ans} = 0$.

1. Index $0$ (`'('`): Opening bracket.
   - $d \leftarrow 0 + 1 = 1$.
   - $\text{ans} \leftarrow \max(0, 1) = 1$.
2. Indices $1..3$ (`"1+"`): Arithmetic characters. Depth unchanged: $d = 1$.
3. Index $4$ (`'('`): Opening bracket.
   - $d \leftarrow 1 + 1 = 2$.
   - $\text{ans} \leftarrow \max(1, 2) = 2$.
4. Indices $5..7$ (`"2*3"`): Literals. Depth unchanged: $d = 2$.
5. Index $8$ (`')'`): Closing bracket.
   - $d \leftarrow 2 - 1 = 1$.
6. Index $9$ (`'+'`): Operator. Depth unchanged: $d = 1$.
7. Index $10$ (`'('`): Opening bracket.
   - $d \leftarrow 1 + 1 = 2$.
   - $\text{ans} \leftarrow \max(2, 2) = 2$.
8. Index $11$ (`'('`): Opening bracket.
   - $d \leftarrow 2 + 1 = 3$.
   - $\text{ans} \leftarrow \max(2, 3) = 3$ (New peak recorded).
9. Index $12$ (`'8'`): Literal. Depth unchanged: $d = 3$.
10. Index $13$ (`')'`): Closing bracket.
    - $d \leftarrow 3 - 1 = 2$.
11. Indices $14..15$ (`"/4"`): Operators. Depth unchanged: $d = 2$.
12. Index $16$ (`')'`): Closing bracket.
    - $d \leftarrow 2 - 1 = 1$.
13. Index $17$ (`')'`): Closing bracket.
    - $d \leftarrow 1 - 1 = 0$.
14. Indices $18..20$ (`"+1"`): Unenclosed trailing literals. Depth unchanged: $d = 0$.

End of scan reached. Peak depth is $\text{ans} = 3$.

---

## 4. Complete Execution Trace

| Index $i$ | Character $s[i]$ | Action Taken | Active Depth $d$ | Recorded Peak $\text{ans}$ |
|---|---|---|---|---|
| Init | — | Initialize | $0$ | $0$ |
| $0$ | `'('` | Increment depth | $1$ | $1$ |
| $1..3$ | `'1'`, `'+'` | Ignored | $1$ | $1$ |
| $4$ | `'('` | Increment depth | $2$ | $2$ |
| $5..7$ | `'2'`, `'*'`, `'3'` | Ignored | $2$ | $2$ |
| $8$ | `')'` | Decrement depth | $1$ | $2$ |
| $9$ | `'+'` | Ignored | $1$ | $2$ |
| $10$ | `'('` | Increment depth | $2$ | $2$ |
| $11$ | `'('` | Increment depth | $3$ | **$3$** |
| $12$ | `'8'` | Ignored | $3$ | $3$ |
| $13$ | `')'` | Decrement depth | $2$ | $3$ |
| $14..15$ | `'/'`, `'4'` | Ignored | $2$ | $3$ |
| $16$ | `')'` | Decrement depth | $1$ | $3$ |
| $17$ | `')'` | Decrement depth | $0$ | $3$ |
| $18..20$ | `'+'`, `'1'` | Ignored | $0$ | $3$ |

Final result: $3$.

---

## 5. Algorithmic Correctness

**Soundness.** At any character index $i$, the quantity $d$ equals the number of preceding unmatched open parentheses. Because each unmatched open parenthesis denotes an enclosing pair containing the current index, $d$ exactly equals the physical nesting depth at character $i$. The running maximum $\text{ans} = \max_i d_i$ faithfully reflects the deepest level reached.

**Completeness.** Nesting depth can increase if and only if an opening parenthesis `'('` is encountered. Because every `'('` immediately increments $d$ and invokes $\text{ans} \leftarrow \max(\text{ans}, d)$, no peak candidate is omitted. Since all characters are processed in a single sequential sweep, the global maximum is certified.

---

## 6. Traps This Instance Exposes

- **Updating Peak Before Incrementing:** Evaluating $\text{ans} = \max(\text{ans}, d)$ before executing $d \mathrel{+}= 1$ causes the peak tracker to lag by 1 level, resulting in an off-by-one undercount.
- **Unnecessary Stack Allocation:** Allocating an explicit stack data structure to push and pop bracket indices consumes $\mathcal{O}(N)$ memory without providing any benefit over an integer counter.
- **Premature Reset on Operators:** Resetting the depth counter when encountering numbers or arithmetic operators (`+`, `*`) incorrectly breaks active nested scopes. Depth changes must be triggered strictly by parentheses.

---

## 7. Complexity Derivation

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of string $s$. The string is traversed once from left to right, spending $\mathcal{O}(1)$ operations per character.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$ auxiliary space, as only two scalar integer counters ($d$ and $\text{ans}$) are maintained throughout execution.
