# Guided Example: Longest Valid Parentheses

We trace the step-by-step index stack tracking on a representative parentheses string instance:

- **Input:** $s = \text{")()())"}$
- **Required output:** $4$

This instance demonstrates sentinel index initialization, delimiter boundary updates upon invalid closing brackets, span calculation via stack difference ($i - \text{stk}[-1]$), and maintaining the global maximal contiguous valid length.

---

## 1. Instance & Teaching Goal

Given a string $s$ containing only `'('` and `')'`, we must find the length of the longest contiguous valid (well-formed) parentheses substring.

For $s = \text{")()())"}$:
- Index 0 is an invalid leading `')'`.
- Indices $1 \dots 4$ form the substring $\text{"()()"}$, which is completely balanced with length 4.
- Index 5 is an unmatchable `')'`, terminating the valid span.
- The maximal valid length is 4.

A naive approach tests all $O(N^2)$ substrings with an $O(N)$ stack validator, taking $O(N^3)$ time. The optimal index-stack algorithm stores unmatched barrier indices, computing the length of each newly closed valid component in $O(1)$ time per character for an overall $O(N)$ runtime.

---

## 2. Conceptual Foundation & Invariants

### Index-Tracking Stack
Instead of storing bracket characters, the stack stores the **indices** of unmatched characters:
- We initialize the stack with sentinel index $-1$:
  $$
  \text{stk} = [-1]
  $$
- Index $-1$ serves as the virtual boundary before the start of the string, ensuring that a valid substring starting at index 0 (e.g. $\text{"()"}$ at indices $0, 1$) correctly computes length $1 - (-1) = 2$.

### State Transitions
For each index $i \in [0, |s| - 1]$:
1. **If $s[i] == \text{'('}$:**
   - Push index $i$ onto $\text{stk}$.
2. **If $s[i] == \text{')'}$:**
   - Pop the top index from $\text{stk}$ (matching the most recent `'('` or clearing the previous barrier).
   - **Case A (Stack becomes empty):**
     - The current `')'` has no matching `'('`. It becomes the new reference boundary.
     - Push $i$ onto $\text{stk}$.
   - **Case B (Stack remains non-empty):**
     - A valid balanced sequence spans from index $\text{stk}[-1] + 1$ through $i$.
     - Current valid length is:
       $$
       \text{len} = i - \text{stk}[-1]
       $$
     - Update $\text{max\_len} = \max(\text{max\_len}, \text{len})$.

> **Invariant.** The top element of $\text{stk}$ is always the index immediately preceding the start of the current valid contiguous block of parentheses.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{")()())"}$ ($N = 6$):

### Initialization
- $\text{stk} = [-1]$.
- $\text{max\_len} = 0$.

---

### Step 0: Index $0$ ($s[0] = \text{')'}$)
- Character is `')'`.
- Pop top element: pop $-1$.
- Stack is now empty! Unmatched closer encountered.
- Action: Push current index $0$ as the new boundary.
- Stack state: $\text{stk} = [0]$. $\text{max\_len} = 0$.

---

### Step 1: Index $1$ ($s[1] = \text{'('}$)
- Character is `'('`.
- Action: Push index $1$ onto stack.
- Stack state: $\text{stk} = [0, 1]$.

---

### Step 2: Index $2$ ($s[2] = \text{')'}$)
- Character is `')'`.
- Pop top element: pop $1$ (matched `'('` at index 1).
- Stack is non-empty! Top element is now $0$.
- Valid span: from index $0 + 1 = 1$ to index $2$ ($\text{"()"}$).
- Computed length: $i - \text{stk}[-1] = 2 - 0 = 2$.
- Update: $\text{max\_len} = \max(0, 2) = 2$.
- Stack state: $\text{stk} = [0]$.

---

### Step 3: Index $3$ ($s[3] = \text{'('}$)
- Character is `'('`.
- Action: Push index $3$ onto stack.
- Stack state: $\text{stk} = [0, 3]$.

---

### Step 4: Index $4$ ($s[4] = \text{')'}$)
- Character is `')'`.
- Pop top element: pop $3$ (matched `'('` at index 3).
- Stack is non-empty! Top element is now $0$.
- Valid span: from index $0 + 1 = 1$ to index $4$ ($\text{"()()"}$).
- Computed length: $i - \text{stk}[-1] = 4 - 0 = 4$.
- Update: $\text{max\_len} = \max(2, 4) = 4$.
- Stack state: $\text{stk} = [0]$.

---

### Step 5: Index $5$ ($s[5] = \text{')'}$)
- Character is `')'`.
- Pop top element: pop $0$.
- Stack is now empty! Unmatched closer encountered.
- Action: Push current index $5$ as the new boundary.
- Stack state: $\text{stk} = [5]$.

### Termination
String exhausted. The maximum contiguous valid length found is $4$.

---

## 4. Complete Execution Trace

| Index $i$ | Character $s[i]$ | Action on Stack | Stack State After Step | Stack Empty? | Computed Valid Length | Current Max Length |
|:---:|:---:|:---|:---|:---:|:---:|:---:|
| Start | - | Initial boundary | `[-1]` | No | - | 0 |
| 0 | `')'` | Pop $-1$; push $0$ | `[0]` | Boundary reset | - | 0 |
| 1 | `'('` | Push $1$ | `[0, 1]` | No | - | 0 |
| 2 | `')'` | Pop $1$ | `[0]` | No | $2 - 0 = 2$ | 2 |
| 3 | `'('` | Push $3$ | `[0, 3]` | No | - | 2 |
| 4 | `')'` | Pop $3$ | `[0]` | No | $4 - 0 = 4$ | **4** |
| 5 | `')'` | Pop $0$; push $5$ | `[5]` | Boundary reset | - | 4 |

### The Same Instance Under the Dynamic-Programming Model

The index stack is not the only way to read this string. Let $g(i)$ be the length of the longest valid substring that ends exactly at index $i$, with $g(i) = 0$ for every $i < 0$ and for every index holding `'('`. A closer at $i$ either completes a pair opened at $i - 1$, giving $g(i) = g(i - 2) + 2$, or closes an opener standing immediately before a run of length $g(i - 1)$; that opener sits at index $i - g(i - 1) - 1$, and if it holds `'('` the run grows to $g(i) = g(i - 1) + 2 + g(i - g(i - 1) - 2)$.

| Index $i$ | $s[i]$ | Case Applied | Dependency Evaluated | $g(i)$ | Reading |
|:---:|:---:|:---|:---|:---:|:---|
| 0 | `')'` | closer with no preceding pair | candidate opener index $0 - g(-1) - 1 = -1$ falls outside the string | 0 | The first closer is unmatched, so no valid substring ends here. |
| 1 | `'('` | opener | none | 0 | An opener never terminates a valid substring, so the state stays 0. |
| 2 | `')'` | pair opened at $i - 1$ | $g(2) = g(0) + 2 = 0 + 2$ | 2 | Indices 1 and 2 form `"()"`, the first measurable component. |
| 3 | `'('` | opener | none | 0 | Opens the component that will close at index 4. |
| 4 | `')'` | pair opened at $i - 1$ | $g(4) = g(2) + 2 = 2 + 2$ | 4 | The adjacent pair extends the run that ended at index 2, merging `"()"` and `"()"` into `"()()"`. |
| 5 | `')'` | closer after a closer | candidate opener index $5 - g(4) - 1 = 0$ holds `')'`, not `'('` | 0 | The run of length 4 cannot be extended, and index 0 is not an opener, so nothing valid ends at index 5. |

$\max_i g(i) = 4$, the same answer the stack produced. The models agree because each measurement is anchored on the most recent unmatched opener: the stack stores that index directly, while the recurrence recovers it from the length of the run that just ended. The recurrence keeps one integer per index, whereas the stack keeps at most one entry per unmatched opener; neither changes the $O(N)$ time bound.

---

## 5. Algorithmic Correctness

**Soundness.** A pair of brackets is valid if every closing bracket matches the most recently opened unmatched open bracket. By storing indices rather than characters, popping an open bracket leaves the index of the boundary immediately preceding the entire valid substring that just closed. The distance $i - \text{stk}[-1]$ measures the exact span of this uninterrupted valid component.

**Completeness.** Every character is scanned. The algorithm updates $\text{max\_len}$ whenever a valid matching pair closes. Because adjacent valid blocks naturally merge (since internal delimiters have been popped from the stack), concatenated valid sequences like $\text{"()()"}$ are correctly measured as a single unified window.

---

## 6. Traps This Instance Exposes

- **Missing Initial Sentinel:** Without initializing the stack with $-1$, an input like $\text{"()"}$ would pop $0$ and leave the stack empty, failing to compute the valid length of 2.
- **Unmatched Closing Delimiters:** When a `')'` appears with no preceding `'('`, it permanently divides the string into disjoint components. Resetting the base index to the current `')'` index prevents valid lengths from erroneously spanning across this invalid delimiter.
- **Unclosed Opening Delimiters:** For an input like $\text{"(()"}$, index 0 (`'('`) remains on the stack. When index 2 (`')'`) pops index 1, the top of the stack is 0. The length is computed as $2 - 0 = 2$, correctly excluding the leading unclosed `'('`.

### Boundary Instances and the Stack Reading That Decides Them

| Boundary Scenario | Concrete Input | Expected | Stack Reading |
|:---|:---|:---:|:---|
| Empty string | $s = \text{""}$ | 0 | No index is pushed or popped, so no span is measured and the maximum stays 0. |
| Only openers | $s = \text{"(((((("}$ | 0 | Six indices are pushed and none is popped, so no length is ever computed. |
| Only closers | $s = \text{"))))))"}$ | 0 | Every closer pops the current boundary and then installs itself as the new one, so the span $i - \text{stk}[-1]$ never exceeds 0. |
| A whole region followed by unmatched openers | $s = \text{"(()())(()"}$ | 6 | The stack returns to the sentinel while closing index 5, so that run measures $5 - (-1) = 6$; the trailing openers then keep the final `")"` confined to the span $8 - 6 = 2$. |
| Two regions split by an unmatched opener | $s = \text{"()(()"}$ | 2 | The opener at index 2 stays on the stack; the run closing at index 4 therefore measures $4 - 2 = 2$, and the earlier run measured $1 - (-1) = 2$. |
| Invalid prefix before a nested region | $s = \text{"())((()))"}$ | 6 | The closer at index 2 empties the stack and installs boundary 2; the nested region closing at index 8 then measures $8 - 2 = 6$. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. We iterate through the string of length $N$ once. Each index is pushed and popped from the stack at most once, performing $O(1)$ operations per character.
- **Auxiliary Space Complexity:** $O(N)$. In the worst case (e.g. $s = \text{"(((((("}$), the stack holds $N + 1$ indices.