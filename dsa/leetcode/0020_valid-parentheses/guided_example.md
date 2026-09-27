# Guided Example: Valid Parentheses

We trace the step-by-step Last-In, First-Out (LIFO) stack evaluation on a representative nested bracket instance:

- **Input:** $s = \text{"([{}])"}$
- **Required output:** $\text{True}$

This instance demonstrates recursive bracket nesting across multiple delimiter types (parentheses, square brackets, and curly braces), push transitions for opening delimiters, pop-and-match verifications for closing delimiters, and final stack emptiness validation.

---

## 1. Instance & Teaching Goal

A bracket sequence is valid if and only if:
1. Every open bracket is closed by the same type of bracket.
2. Open brackets are closed in the exact reverse order of their opening (strict LIFO nesting).
3. Every closing bracket has a corresponding preceding opening bracket.

For $s = \text{"([{}])"}$:
- Index 0: `'('` opens outer frame.
- Index 1: `'['` opens middle frame.
- Index 2: `'{'` opens innermost frame.
- Index 3: `'}'` matches and closes innermost frame `'{'`.
- Index 4: `']'` matches and closes middle frame `'['`.
- Index 5: `')'` matches and closes outer frame `'('`.
- All opened brackets are closed, and the stack is empty $\implies \text{True}$.

A naive approach counting frequencies cannot distinguish valid nesting from interleaved errors: for example, $\text{"([)]"}$ has equal counts for both types but violates nesting order because `']'` attempts to close `'['` while `')'` is expected. The optimal algorithm maintains an explicit LIFO stack, verifying each character in $O(1)$ time for an overall $O(N)$ runtime.

---

## 2. Conceptual Foundation & Invariants

### Matching Table
We define a bijection mapping each closing bracket to its unique opening partner:
$$
\text{Match} = \{ \text{')'} \mapsto \text{'('}, \, \text{'\}'} \mapsto \text{'\{'}, \, \text{']'} \mapsto \text{'['} \}
$$

### Stack State Machine
For each character $c$ in string $s$ from left to right:
1. **Opening Delimiter ($c \in \{\text{'('}, \text{'\{'}, \text{'['}\}$):**
   - Push $c$ onto the stack $\text{stk}$.
2. **Closing Delimiter ($c \in \{\text{')'}, \text{'\}'}, \text{']'}\}$):**
   - **Empty Stack Underflow:** If $\text{stk}$ is empty, there is no opening bracket to pair with $c \implies$ return $\text{False}$.
   - **Type Mismatch:** Pop the top element $\text{top} = \text{stk.pop}()$. If $\text{top} \ne \text{Match}[c]$, nesting is violated $\implies$ return $\text{False}$.
3. **Termination:** After all characters in $s$ are processed, the string is valid if and only if the stack is completely empty ($\text{len}(\text{stk}) = 0$). If any unclosed opening brackets remain, return $\text{False}$.

> **Invariant.** At step $k$, $\text{stk}$ contains exactly the active, unclosed opening brackets from the prefix $s[0 \dots k-1]$ in order of discovery, with the most recent open bracket at the top of the stack.

---

## 3. Step-by-Step Worked Execution

We process $s = \text{"([{}])"}$ with initial stack $\text{stk} = []$:

### Step 0: Index 0 ($s[0] = \text{'('}$)
- Character is an opening bracket.
- Action: Push `'('` onto stack.
- Stack state: $\text{stk} = [\text{'('}]$.

### Step 1: Index 1 ($s[1] = \text{'['}$)
- Character is an opening bracket.
- Action: Push `'['` onto stack.
- Stack state: $\text{stk} = [\text{'('}, \text{'['}]$.

### Step 2: Index 2 ($s[2] = \text{'\{'}$)
- Character is an opening bracket.
- Action: Push `'{'` onto stack.
- Stack state: $\text{stk} = [\text{'('}, \text{'['}, \text{'\{'}]$.

### Step 3: Index 3 ($s[3] = \text{'\}'}$)
- Character is a closing bracket. Required partner: $\text{Match}[\text{'\}'}] = \text{'\{'}$.
- Check stack: $\text{stk}$ is non-empty. Top element is `'{'`.
- Match verification: $\text{top} = \text{'\{'} = \text{Match}[\text{'\}'}]$. Match confirmed!
- Action: Pop `'{'`.
- Stack state: $\text{stk} = [\text{'('}, \text{'['}]$.

### Step 4: Index 4 ($s[4] = \text{']'}$)
- Character is a closing bracket. Required partner: $\text{Match}[\text{']'}] = \text{'['}$.
- Check stack: $\text{stk}$ is non-empty. Top element is `'['`.
- Match verification: $\text{top} = \text{'['} = \text{Match}[\text{']'}]$. Match confirmed!
- Action: Pop `'['`.
- Stack state: $\text{stk} = [\text{'('}]$.

### Step 5: Index 5 ($s[5] = \text{')'}$)
- Character is a closing bracket. Required partner: $\text{Match}[\text{')'}] = \text{'('}$.
- Check stack: $\text{stk}$ is non-empty. Top element is `'('`.
- Match verification: $\text{top} = \text{'('} = \text{Match}[\text{')'}]$. Match confirmed!
- Action: Pop `'('`.
- Stack state: $\text{stk} = []$.

### Termination Verification
- String is exhausted.
- Check stack: $\text{stk} = []$ (empty).
- Final output: $\text{True}$.

---

## 4. Complete Execution Trace

| Step $i$ | Character $s[i]$ | Delimiter Category | Action Taken | Stack State Before | Stack State After | Invariant Status |
|:---:|:---:|:---:|:---|:---|:---|:---:|
| 0 | `'('` | Opening | Push `'('` | `[]` | `['(']` | Valid prefix |
| 1 | `'['` | Opening | Push `'['` | `['(']` | `['(', '[']` | Valid prefix |
| 2 | `'{'` | Opening | Push `'{'` | `['(', '[']` | `['(', '[', '{']` | Valid prefix |
| 3 | `'}'` | Closing | Pop `'{'`; matches $\text{Match}[\text{'\}'}]$ | `['(', '[', '{']` | `['(', '[']` | Innermost frame closed |
| 4 | `']'` | Closing | Pop `'['`; matches $\text{Match}[\text{']'}]$ | `['(', '[']` | `['(']` | Middle frame closed |
| 5 | `')'` | Closing | Pop `'('`; matches $\text{Match}[\text{')'}]$ | `['(']` | `[]` | Outermost frame closed |
| Final | - | End of input | Verify $\text{len}(\text{stk}) = 0$ | `[]` | `[]` | **Balanced ($\text{True}$)** |

### Invalid Mismatch Tracing (Failure Modes)

| Invalid Input | First Failure Point | Mechanism of Detection | Result |
|:---|:---:|:---|:---:|
| `"([)]"` | Index 2 ($s[2] = \text{')'}$) | Top of stack is `'['`, but expected $\text{Match}[\text{')'}] = \text{'('}$ | $\text{False}$ (Nesting mismatch) |
| `")("` | Index 0 ($s[0] = \text{')'}$) | Stack is empty when attempting to pop | $\text{False}$ (Stack underflow) |
| `"(()"` | Index 3 (End of input) | Stack retains unclosed `['(']` after all characters consumed | $\text{False}$ (Unclosed open bracket) |

---

## 5. Algorithmic Correctness

**Soundness.** A sequence of brackets is well-formed under the context-free grammar $S \to \epsilon \mid (S) \mid [S] \mid \{S\} \mid SS$. The pushdown automaton implemented by the stack strictly recognizes this Dyck language. Because every closing bracket is compared against the most recently opened unmatched bracket, any violation of symmetry or nesting triggers an immediate rejection.

**Completeness.** Every character in the input string is evaluated. If the string is well-formed, each opening bracket is matched and popped by its corresponding closing partner, leaving the stack empty at the end. Since the transition rules accept every grammatically valid derivation, no valid string can be erroneously rejected.

---

## 6. Traps This Instance Exposes

- **Premature True on Balanced Counts:** Simple character frequency counters cannot detect order violations like $\text{"([)]"}$. A stack is necessary and sufficient to preserve LIFO precedence.
- **Stack Underflow on Closing First:** An input like `")"` or `"())"` encounters a closer when the stack is empty. Checking `if not stk` before popping prevents `IndexError` and immediately rejects the string.
- **Unclosed Open Brackets:** An input like `"("` or `"(("` encounters only opening brackets and no mismatches during the loop. Testing `return len(stk) == 0` at the end ensures unclosed brackets are correctly reported as invalid.
- **Odd Length Strings:** Any valid bracket string must pair each opening delimiter with a closing delimiter. If $|s|$ is odd, it is impossible to be valid; an early check `if len(s) % 2 != 0: return False` provides an immediate $O(1)$ filter.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. We iterate through the string of length $N$ once. Each character triggers either an $O(1)$ push or an $O(1)$ pop and dictionary lookup. Total runtime is strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. In the worst case (e.g. $s = \text{"(((((("}$), the stack stores all $N$ opening brackets. The hash map stores a fixed 3 key-value pairs ($O(1)$).
