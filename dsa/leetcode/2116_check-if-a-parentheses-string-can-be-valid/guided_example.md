# Guided Example: Check if a Parentheses String Can Be Valid

We trace the step-by-step execution of the optimal two-pass bidirectional greedy approach on a representative problem instance:

- **String ($s$):** `"))()))"`
- **Lock Mask ($\text{locked}$):** `"010100"`
- **Expected Output:** `true`

This instance illustrates how wildcard flexibility allows modifying strategically placed characters to balance fixed closing parentheses, and how dual forward and backward scans guarantee both prefix and suffix validity in linear time and constant space.

---

## 1. Problem Overview & Representative Instance

A parentheses string is valid if:
1. It is the empty string, or
2. It can be written as $AB$ (concatenation of valid strings $A$ and $B$), or
3. It can be written as $(A)$, where $A$ is a valid string.

We are given a string $s$ consisting of `'('` and `')'`, and a binary mask $\text{locked}$ of identical length. If $\text{locked}[i] = \text{'1'}$, character $s[i]$ is immutable. If $\text{locked}[i] = \text{'0'}$, character $s[i]$ is mutable and may be configured as either `'('` or `')'`.

In our representative instance:
- Index $0$: $s[0] = \text{')'}$, $\text{locked}[0] = \text{'0'}$ (mutable)
- Index $1$: $s[1] = \text{')'}$, $\text{locked}[1] = \text{'1'}$ (locked closing parenthesis)
- Index $2$: $s[2] = \text{'('}$, $\text{locked}[2] = \text{'0'}$ (mutable)
- Index $3$: $s[3] = \text{')'}$, $\text{locked}[3] = \text{'1'}$ (locked closing parenthesis)
- Index $4$: $s[4] = \text{')'}$, $\text{locked}[4] = \text{'0'}$ (mutable)
- Index $5$: $s[5] = \text{')'}$, $\text{locked}[5] = \text{'0'}$ (mutable)

Although string $s$ contains five `')'` characters and only one `'('` initially, four characters are unlocked. We must determine whether a configuration exists that yields a valid, well-formed parentheses sequence.

---

## 2. Mathematical & Algorithmic Principles

### Necessary Parity Invariant
Every valid parentheses sequence consists of matched pairs of opening and closing parentheses. Consequently, the length $n$ must be an even integer:

$$n \equiv 0 \pmod 2$$

If $n$ is odd, no assignment of mutable positions can ever balance the string, allowing immediate rejection.

### Prefix and Suffix Balance Inequalities
A sequence of parentheses is valid if and only if:
1. The prefix balance condition holds: in every prefix $s[0 \dots i]$, the number of opening parentheses is greater than or equal to the number of closing parentheses.
2. The total balance condition holds: the total number of opening parentheses equals the total number of closing parentheses.

When mutable characters exist, we evaluate feasibility via bidirectional upper-bound balances:
- **Forward Pass (Left-to-Right):** We verify that no prefix has an unavoidable excess of closing brackets. We treat every unlocked character ($\text{locked}[i] = \text{'0'}$) as an opening parenthesis `'('`. The running capacity $B_{\text{open}}$ is updated:
  - If $\text{locked}[i] = \text{'0'}$ or $s[i] = \text{'('}$, $B_{\text{open}} \leftarrow B_{\text{open}} + 1$.
  - If $\text{locked}[i] = \text{'1'}$ and $s[i] = \text{')'}$, $B_{\text{open}} \leftarrow B_{\text{open}} - 1$.
  - If at any index $B_{\text{open}} < 0$, a locked closing bracket cannot be matched by any preceding character. Feasibility fails immediately.
- **Backward Pass (Right-to-Left):** We verify that no suffix has an unavoidable excess of opening brackets. We treat every unlocked character as a closing parenthesis `')'`. The running capacity $B_{\text{close}}$ is updated:
  - If $\text{locked}[i] = \text{'0'}$ or $s[i] = \text{')'}$, $B_{\text{close}} \leftarrow B_{\text{close}} + 1$.
  - If $\text{locked}[i] = \text{'1'}$ and $s[i] = \text{'('}$, $B_{\text{close}} \leftarrow B_{\text{close}} - 1$.
  - If at any index $B_{\text{close}} < 0$, a locked opening bracket cannot be matched by any subsequent character. Feasibility fails immediately.

| Pass Direction | Monitored Metric | Increment Condition | Decrement Condition | Failure Trigger |
|---|---|---|---|---|
| Left-to-Right | Potential Openings ($B_{\text{open}}$) | Unlocked or `'('` | Locked `')'` | $B_{\text{open}} < 0$ |
| Right-to-Left | Potential Closings ($B_{\text{close}}$) | Unlocked or `')'` | Locked `'('` | $B_{\text{close}} < 0$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Length Verification
Length $n = 6$. Since $6 \pmod 2 = 0$, the parity constraint is satisfied.

### Forward Pass: Tracking Opening Capacity ($B_{\text{open}}$)
Initialize $B_{\text{open}} = 0$.

- **Index 0:** $s[0] = \text{')'}$, $\text{locked}[0] = \text{'0'}$. Position is unlocked. We treat it optimistically as `'('`.
  - Update: $B_{\text{open}} = 0 + 1 = 1$.
- **Index 1:** $s[1] = \text{')'}$, $\text{locked}[1] = \text{'1'}$. Locked closing bracket consumes one potential opening.
  - Update: $B_{\text{open}} = 1 - 1 = 0$. Valid ($B_{\text{open}} \ge 0$).
- **Index 2:** $s[2] = \text{'('}$, $\text{locked}[2] = \text{'0'}$. Unlocked position.
  - Update: $B_{\text{open}} = 0 + 1 = 1$.
- **Index 3:** $s[3] = \text{')'}$, $\text{locked}[3] = \text{'1'}$. Locked closing bracket consumes one potential opening.
  - Update: $B_{\text{open}} = 1 - 1 = 0$. Valid ($B_{\text{open}} \ge 0$).
- **Index 4:** $s[4] = \text{')'}$, $\text{locked}[4] = \text{'0'}$. Unlocked position.
  - Update: $B_{\text{open}} = 0 + 1 = 1$.
- **Index 5:** $s[5] = \text{')'}$, $\text{locked}[5] = \text{'0'}$. Unlocked position.
  - Update: $B_{\text{open}} = 1 + 1 = 2$.

The forward pass completes with $B_{\text{open}} \ge 0$ at all prefix boundaries.

### Backward Pass: Tracking Closing Capacity ($B_{\text{close}}$)
Initialize $B_{\text{close}} = 0$.

- **Index 5:** $s[5] = \text{')'}$, $\text{locked}[5] = \text{'0'}$. Position is unlocked. We treat it optimistically as `')'`.
  - Update: $B_{\text{close}} = 0 + 1 = 1$.
- **Index 4:** $s[4] = \text{')'}$, $\text{locked}[4] = \text{'0'}$. Unlocked position.
  - Update: $B_{\text{close}} = 1 + 1 = 2$.
- **Index 3:** $s[3] = \text{')'}$, $\text{locked}[3] = \text{'1'}$. Locked closing bracket contributes to closing capacity.
  - Update: $B_{\text{close}} = 2 + 1 = 3$.
- **Index 2:** $s[2] = \text{'('}$, $\text{locked}[2] = \text{'0'}$. Unlocked position can act as closing bracket in reverse scan.
  - Update: $B_{\text{close}} = 3 + 1 = 4$.
- **Index 1:** $s[1] = \text{')'}$, $\text{locked}[1] = \text{'1'}$. Locked closing bracket contributes.
  - Update: $B_{\text{close}} = 4 + 1 = 5$.
- **Index 0:** $s[0] = \text{')'}$, $\text{locked}[0] = \text{'0'}$. Unlocked position contributes.
  - Update: $B_{\text{close}} = 5 + 1 = 6$.

The backward pass completes with $B_{\text{close}} \ge 0$ at all suffix boundaries.
Since both passes succeed, a valid configuration exists, and the output is `true`.
For example, assigning indices $0, 2, 4$ as `'('` and index $5$ as `')'` produces `"()()()"`, which is valid.

---

## 4. Comprehensive State Trace

The detailed execution trace across both linear scans is tabulated below:

### Forward Scan Trace
| Index ($i$) | Character $s[i]$ | Locked $\text{locked}[i]$ | Interpretation | Balance Delta | $B_{\text{open}}$ After Step | Prefix Valid? |
|---|---|---|---|---|---|---|
| $0$ | `')'` | `'0'` | Unlocked (assume `'('`) | $+1$ | $1$ | Yes |
| $1$ | `')'` | `'1'` | Locked `')'` | $-1$ | $0$ | Yes |
| $2$ | `'('` | `'0'` | Unlocked (assume `'('`) | $+1$ | $1$ | Yes |
| $3$ | `')'` | `'1'` | Locked `')'` | $-1$ | $0$ | Yes |
| $4$ | `')'` | `'0'` | Unlocked (assume `'('`) | $+1$ | $1$ | Yes |
| $5$ | `')'` | `'0'` | Unlocked (assume `'('`) | $+1$ | $2$ | Yes |

### Backward Scan Trace
| Index ($i$) | Character $s[i]$ | Locked $\text{locked}[i]$ | Interpretation | Balance Delta | $B_{\text{close}}$ After Step | Suffix Valid? |
|---|---|---|---|---|---|---|
| $5$ | `')'` | `'0'` | Unlocked (assume `')'`) | $+1$ | $1$ | Yes |
| $4$ | `')'` | `'0'` | Unlocked (assume `')'`) | $+1$ | $2$ | Yes |
| $3$ | `')'` | `'1'` | Locked `')'` | $+1$ | $3$ | Yes |
| $2$ | `'('` | `'0'` | Unlocked (assume `')'`) | $+1$ | $4$ | Yes |
| $1$ | `')'` | `'1'` | Locked `')'` | $+1$ | $5$ | Yes |
| $0$ | `')'` | `'0'` | Unlocked (assume `')'`) | $+1$ | $6$ | Yes |

Both scans remain strictly non-negative throughout, confirming validity.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Suppose a string is valid. Then there must exist an assignment where the count of opening brackets equals closing brackets, and every prefix has at least as many opening brackets as closing brackets. In the forward scan, treating every unlocked bracket as an opening bracket establishes the theoretical upper bound on prefix balance. If even this maximum possible balance drops below $0$, no assignment could ever maintain a non-negative prefix balance. By symmetry, the backward scan establishes the upper bound on suffix balance. If neither upper bound drops below $0$ and the overall length is even, intermediate value properties of discrete paths guarantee that a balanced configuration with non-negative prefix sums can be chosen.

**Completeness.** Any string with an odd length is eliminated at step 0. For even-length strings, checking both prefix dominance and suffix dominance covers all failure modes (excess locked closings early on, or excess locked openings late in the string). Thus, no false positives or false negatives are generated.

---

## 6. Edge Cases & Anti-Patterns

- **Odd Length Strings:** Strings with odd lengths (such as `"("` or `")))"`) are immediately rejected in $\mathcal{O}(1)$ time without scanning.
- **Unbalanced Ends:** A locked closing bracket at index $0$ (`s[0] == ')'` and `locked[0] == '1'`) immediately yields $B_{\text{open}} = -1$, correctly failing on the very first character.
- **Trailing Locked Openings:** A string like `"...(("` with locked opening brackets at the end will pass the forward pass, but the backward pass will encounter locked openings without remaining closing capacity, catching the defect.
- **All Characters Unlocked:** Any even-length string with all characters unlocked is unconditionally valid; both scans will simply increment the counters monotonically.
- **Anti-Pattern — Exponential Backtracking:** Trying all $2^k$ assignments of $k$ unlocked characters results in exponential time complexity $\mathcal{O}(2^k)$. The bidirectional greedy scan reduces this to $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of string $s$. We perform one forward traversal and one backward traversal across the string, spending $\mathcal{O}(1)$ operations per character.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. The algorithm requires only a few scalar integer counters to track balances and indices, requiring no dynamic heap allocation or call stack overhead.
