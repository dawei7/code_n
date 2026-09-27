# Guided Example: Generate Parentheses

We trace the step-by-step backtracking decision tree on a representative balanced parentheses instance:

- **Input:** $n = 3$
- **Required output:** `["((()))", "(()())", "(())()", "()(())", "()()()"]`

This instance demonstrates constrained recursive branching, open versus closed delimiter invariants, pruning illegal prefix states before they are explored, and Catalan number cardinality.

---

## 1. Instance & Teaching Goal

Given $n = 3$ pairs of parentheses, we must generate all valid combinations of well-formed parentheses strings of length $2n = 6$.

A naive brute-force generator creates all $2^{2n} = 2^6 = 64$ possible binary strings of `(` and `)`, filtering them with a stack validator in $O(2^{2n} \cdot n)$ time.

The optimal backtracking approach enforces validity during generation:
1. An open parenthesis `'('` can be placed whenever $\text{open} < n$.
2. A close parenthesis `')'` can be placed only when $\text{close} < \text{open}$.

This constructive pruning guarantees that every explored branch leads to a valid balanced string, reducing the search space directly to the $n$-th Catalan number:
$$
C_n = \frac{1}{n+1} \binom{2n}{n} \implies C_3 = \frac{1}{4} \binom{6}{3} = \frac{20}{4} = 5
$$

The gap between the unconstrained search space and the answer is the whole point of generating under a constraint, and it widens quickly:

| $n$ | String Length $2n$ | Unconstrained Strings $2^{2n}$ | Valid Strings $C_n$ | Fraction Retained |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | 2 | 4 | 1 | $1/4$ |
| $2$ | 4 | 16 | 2 | $1/8$ |
| $3$ | 6 | 64 | 5 | $5/64$ |
| $4$ | 8 | 256 | 14 | $7/128$ |
| $5$ | 10 | 1024 | 42 | $21/512$ |
| $8$ | 16 | 65536 | 1430 | $715/32768$ |

At $n = 3$ the filter would reject $59$ of $64$ strings, so the pruning is not a minor optimization: it removes the overwhelming majority of the candidate space before it is ever constructed.

---

## 2. Conceptual Foundation & Invariants

### State Representation
We track the partial string $s$ along with two non-negative integer counters:
- $\text{open}$: Count of `'('` placed so far ($0 \le \text{open} \le n$).
- $\text{close}$: Count of `')'` placed so far ($0 \le \text{close} \le \text{open}$).

### Branching Transitions
At any state $(s, \text{open}, \text{close})$:
1. **Branch 1 (Add `'('`):** Legal if $\text{open} < n$. Recurse on $(s + \text{'('}, \text{open} + 1, \text{close})$.
2. **Branch 2 (Add `')'`):** Legal if $\text{close} < \text{open}$. Recurse on $(s + \text{')'}, \text{open}, \text{close} + 1)$.
3. **Base Case:** When $|s| = 2n$ (i.e. $\text{open} = \text{close} = n$), record $s$ as a valid combination.

> **Invariant.** For every prefix $s$, $\text{close} \le \text{open} \le n$. This condition guarantees that no closing bracket can ever precede its opening counterpart, making stack underflow impossible.

---

## 3. Step-by-Step Worked Execution

We trace the recursive exploration for $n = 3$ from root state $(\text{""}, 0, 0)$:

### Level 1: Length 1
- From $(\text{""}, 0, 0)$:
  - $\text{open} = 0 < 3 \implies$ Add `'('` $\to (\text{"("}, 1, 0)$.
  - $\text{close} = 0 \not< \text{open} = 0 \implies$ Cannot add `')'`.

---

### Level 2: Length 2
- From $(\text{"("}, 1, 0)$:
  - Add `'('` ($\text{open} = 1 < 3$) $\to (\text{"(("}, 2, 0)$.
  - Add `')'` ($\text{close} = 0 < \text{open} = 1$) $\to (\text{"()"}, 1, 1)$.

---

### Subtree 1: Exploring from $(\text{"(("}, 2, 0)$
- **Length 3:**
  - Branch A: Add `'('` $\to (\text{"((("}, 3, 0)$.
  - Branch B: Add `')'` $\to (\text{"(()"}, 2, 1)$.
- **Length 4–6 from $(\text{"((("}, 3, 0)$:**
  - $\text{open} = 3 = n$; only `')'` can be placed now.
  - $(\text{"((("}, 3, 0) \to (\text{"((()" }, 3, 1) \to (\text{"((())" }, 3, 2) \to (\text{"((()))" }, 3, 3)$.
  - **Output 1:** $\text{"((()))"}$.
- **Length 4–6 from $(\text{"(()"}, 2, 1)$:**
  - Add `'('` ($\text{open}=2<3$) $\to (\text{"(()("}, 3, 1) \to$ only `')'` left $\to (\text{"(()()" }, 3, 2) \to (\text{"(()())" }, 3, 3)$.
    - **Output 2:** $\text{"(()())"}$.
  - Add `')'` ($\text{close}=1<\text{open}=2$) $\to (\text{"(())"}, 2, 2) \to$ add remaining `'('` then `')'` $\to (\text{"(())()"}, 3, 3)$.
    - **Output 3:** $\text{"(())()"}$.

---

### Subtree 2: Exploring from $(\text{"()"}, 1, 1)$
- **Length 3:**
  - $\text{close} = 1 \not< \text{open} = 1$; only `'('` can be placed.
  - $(\text{"()"}, 1, 1) \to (\text{"()("}, 2, 1)$.
- **Length 4–6 from $(\text{"()("}, 2, 1)$:**
  - Branch A: Add `'('` $\to (\text{"()(("}, 3, 1) \to$ only `')'` remaining $\to (\text{"()(())"}, 3, 3)$.
    - **Output 4:** $\text{"()(())"}$.
  - Branch B: Add `')'` $\to (\text{"()()"}, 2, 2) \to$ add remaining `'('` then `')'` $\to (\text{"()()()"}, 3, 3)$.
    - **Output 5:** $\text{"()()()"}$.

All branches terminate. Total valid combinations emitted: 5.

---

## 4. Complete Execution Trace

### Decision Tree State Progression

```text
Level 0:                             "" (0,0)
                                        |
Level 1:                             "(" (1,0)
                                   /           \
Level 2:                     "((" (2,0)      "()" (1,1)
                            /         \           |
Level 3:             "(((" (3,0)   "(()" (2,1)  "()(" (2,1)
                        |          /        \    /       \
Level 4:             "((()"      "(()("   "(())" "()(("  "()()"
                        |          |        |      |       |
Level 5:             "((())"     "(()()"  "(())(" "()(()" "()()("
                        |          |        |      |       |
Level 6 (Leaf):      "((()))"    "(()())" "(())()" "()(())" "()()()"
                      [Sol 1]     [Sol 2]  [Sol 3]  [Sol 4]  [Sol 5]
```

### Complete Backtracking State Table

| Branch Index | Explored Sequence of Choices | $\text{open}$ Count | $\text{close}$ Count | Final String Emitted | Validation Status |
|:---:|:---|:---:|:---:|:---|:---:|
| 1 | `'('` $\to$ `'('` $\to$ `'('` $\to$ `')'` $\to$ `')'` $\to$ `')'` | 3 | 3 | $\text{"((()))"}$ | Valid (Nested) |
| 2 | `'('` $\to$ `'('` $\to$ `')'` $\to$ `'('` $\to$ `')'` $\to$ `')'` | 3 | 3 | $\text{"(()())"}$ | Valid (Mixed) |
| 3 | `'('` $\to$ `'('` $\to$ `')'` $\to$ `')'` $\to$ `'('` $\to$ `')'` | 3 | 3 | $\text{"(())()"}$ | Valid (Nested + Disjoint) |
| 4 | `'('` $\to$ `')'` $\to$ `'('` $\to$ `'('` $\to$ `')'` $\to$ `')'` | 3 | 3 | $\text{"()(())"}$ | Valid (Disjoint + Nested) |
| 5 | `'('` $\to$ `')'` $\to$ `'('` $\to$ `')'` $\to$ `'('` $\to$ `')'` | 3 | 3 | $\text{"()()()"}$ | Valid (Sequential Pairs) |

---

## 5. Algorithmic Correctness

**Soundness.** A string of brackets is valid if and only if every prefix has at least as many opening brackets as closing brackets ($\text{close} \le \text{open}$) and the total counts are equal ($\text{open} = \text{close} = n$). Because the backtracking guard strictly forbids placing `')'` when $\text{close} \ge \text{open}$, every constructed string satisfies the Dyck language property by invariant induction.

**Completeness.** Every valid parentheses sequence can be read character by character from left to right. At each character, it must satisfy $\text{open} \le n$ and $\text{close} \le \text{open}$. Because the backtracking tree branches on every legal option at each index, every possible valid sequence corresponds to a unique path from the root to a leaf.

The five outputs can also be counted without running the tree at all. Every well-formed string of length $2n$ decomposes uniquely as $\text{"("} A \text{")"} B$, where $A$ holds the characters up to the match of the first `'('` and $B$ is whatever follows. If $A$ has $2k$ characters, then $A$ and $B$ are themselves well-formed, and the count obeys $C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k}$. For $n = 3$ that recurrence reproduces exactly the five strings the trace emitted:

| $k$ | Characters in $A$ | Choices for $A$ | Characters in $B$ | Choices for $B$ | Product $C_k C_{2-k}$ | Strings Produced |
|:---:|:---:|:---|:---:|:---|:---:|:---|
| $0$ | 0 | $A = \epsilon$ (1 choice) | 4 | $B \in \{\text{"(())"}, \text{"()()"}\}$ (2 choices) | 2 | `"()(())"`, `"()()()"` |
| $1$ | 2 | $A = \text{"()"}$ (1 choice) | 2 | $B = \text{"()"}$ (1 choice) | 1 | `"(())()"` |
| $2$ | 4 | $A \in \{\text{"(())"}, \text{"()()"}\}$ (2 choices) | 0 | $B = \epsilon$ (1 choice) | 2 | `"((()))"`, `"(()())"` |

The column total $2 + 1 + 2 = 5$ equals $C_3$, which confirms that the constrained branching explores exactly the well-formed strings and nothing else: no output is duplicated by two different decompositions, and no well-formed string is missing from the table.

---

## 6. Traps This Instance Exposes

- **Placing Closing Brackets Early:** Allowing `')'` when $\text{close} == \text{open}$ creates strings like $\text{")("}$, which immediately violates prefix balance.
- **Exceeding $n$ Open Brackets:** Without the check $\text{open} < n$, the recursion would run indefinitely or produce strings with uneven delimiter counts.
- **String Immutability and State Rollback:** In languages with mutable character buffers, appending a character requires popping it upon backtracking. In languages with immutable strings, passing $s + \text{'('}$ directly into the recursive call creates a clean immutable state for each branch.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left(\frac{4^n}{\sqrt{n}}\right)$. The number of generated strings is the $n$-th Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n} \sim \frac{4^n}{n^{3/2} \sqrt{\pi}}$. Copying each string of length $2n$ into the output list takes $O(n)$ time, yielding total time $O\left(\frac{4^n}{\sqrt{n}}\right)$. For $n = 3$, $C_3 = 5$, requiring negligible time.
- **Auxiliary Space Complexity:** $O(n)$. The maximum recursion depth is $2n$ stack frames. Storing the output requires $O(n \cdot C_n)$ memory.