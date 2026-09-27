# Guided Example: Roman to Integer

We trace the step-by-step local neighbor evaluation and signed arithmetic accumulation on a representative Roman numeral instance:

- **Input:** $s = \text{"MCMXCIV"}$
- **Required output:** $1994$

This instance is selected because it thoroughly demonstrates both standard additive symbols and all three common subtractive pairs (`CM`, `XC`, `IV`), proving how a single local lookahead comparison deterministically resolves symbol polarity.

---

## 1. Instance & Teaching Goal

Roman numerals assign fixed values to seven elementary characters:

| Symbol | `I` | `V` | `X` | `L` | `C` | `D` | `M` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Value | 1 | 5 | 10 | 50 | 100 | 500 | 1000 |

In additive contexts, symbols are arranged in non-increasing order and summed directly (e.g. $\text{"VI"} = 5 + 1 = 6$). In subtractive contexts, a smaller value precedes a larger value to represent values like $4$ (`IV`), $9$ (`IX`), $40$ (`XL`), $90$ (`XC`), $400$ (`CD`), and $900$ (`CM`).

For $s = \text{"MCMXCIV"}$, the components represent:
$$
\text{M} (1000) + \text{CM} (900) + \text{XC} (90) + \text{IV} (4) = 1994
$$

The goal is to compute $1994$ in a single forward pass without maintaining arbitrary lookahead stacks or backtracking state.

---

## 2. Conceptual Foundation & Invariants

### The Local Lookahead Polarity Invariant
Instead of grouping symbols into variable-length tokens (1 or 2 characters), we evaluate each character $s[i]$ independently by inspecting only its immediate successor $s[i+1]$:

$$
\text{Contribution}(s[i]) = 
\begin{cases}
- \text{Value}(s[i]), & \text{if } i + 1 < |s| \text{ and } \text{Value}(s[i]) < \text{Value}(s[i+1]) \\
+ \text{Value}(s[i]), & \text{otherwise}
\end{cases}
$$

### Mathematical Equivalence
Consider a subtractive pair such as $\text{"IV"}$:
- Under tokenization: $\text{Value}(\text{"IV"}) = 5 - 1 = 4$.
- Under the local polarity rule:
  - For `'I'`: $\text{Value}(\text{'I'}) = 1 < \text{Value}(\text{'V'}) = 5 \implies -1$.
  - For `'V'`: Final character (or followed by smaller/equal) $\implies +5$.
  - Sum: $-1 + 5 = 4$.

The two interpretations are mathematically identical. The local polarity rule decomposes every composite subtractive pair into two signed additions, enabling a uniform linear scan.

> **Invariant.** At step $k$, the accumulator represents the exact signed sum of all characters $s[0 \dots k-1]$. Because every valid Roman subtractive pair contains exactly one subtraction followed by its positive counterpart, the sum is exact at termination.

---

## 3. Step-by-Step Worked Execution

We scan $s = \text{"MCMXCIV"}$ from left to right ($i = 0$ to $6$):

### Index 0: $s[0] = \text{'M'}$
- Current value: $\text{val} = 1000$.
- Next character: $s[1] = \text{'C'}$, $\text{val}_{\text{next}} = 100$.
- Comparison: $1000 \ge 100$.
- Polarity: Add $+1000$.
- Accumulator: $0 + 1000 = 1000$.

### Index 1: $s[1] = \text{'C'}$
- Current value: $\text{val} = 100$.
- Next character: $s[2] = \text{'M'}$, $\text{val}_{\text{next}} = 1000$.
- Comparison: $100 < 1000$. Subtractive trigger!
- Polarity: Subtract $-100$.
- Accumulator: $1000 - 100 = 900$.

### Index 2: $s[2] = \text{'M'}$
- Current value: $\text{val} = 1000$.
- Next character: $s[3] = \text{'X'}$, $\text{val}_{\text{next}} = 10$.
- Comparison: $1000 \ge 10$.
- Polarity: Add $+1000$.
- Accumulator: $900 + 1000 = 1900$.

### Index 3: $s[3] = \text{'X'}$
- Current value: $\text{val} = 10$.
- Next character: $s[4] = \text{'C'}$, $\text{val}_{\text{next}} = 100$.
- Comparison: $10 < 100$. Subtractive trigger!
- Polarity: Subtract $-10$.
- Accumulator: $1900 - 10 = 1890$.

### Index 4: $s[4] = \text{'C'}$
- Current value: $\text{val} = 100$.
- Next character: $s[5] = \text{'I'}$, $\text{val}_{\text{next}} = 1$.
- Comparison: $100 \ge 1$.
- Polarity: Add $+100$.
- Accumulator: $1890 + 100 = 1990$.

### Index 5: $s[5] = \text{'I'}$
- Current value: $\text{val} = 1$.
- Next character: $s[6] = \text{'V'}$, $\text{val}_{\text{next}} = 5$.
- Comparison: $1 < 5$. Subtractive trigger!
- Polarity: Subtract $-1$.
- Accumulator: $1990 - 1 = 1989$.

### Index 6: $s[6] = \text{'V'}$ (Terminal Symbol)
- Current value: $\text{val} = 5$.
- Next character: None ($i = |s| - 1$).
- Boundary rule: The final character is always added.
- Polarity: Add $+5$.
- Final Accumulator: $1989 + 5 = 1994$.

---

## 4. Complete Execution Trace

| Index $i$ | Symbol $s[i]$ | Value $\text{val}_i$ | Successor $s[i+1]$ | Next Value $\text{val}_{i+1}$ | Condition ($\text{val}_i < \text{val}_{i+1}$) | Signed Term Applied | Total Accumulated |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `M` | 1000 | `C` | 100 | False | $+1000$ | 1000 |
| 1 | `C` | 100 | `M` | 1000 | **True (Subtractive)** | $-100$ | 900 |
| 2 | `M` | 1000 | `X` | 10 | False | $+1000$ | 1900 |
| 3 | `X` | 10 | `C` | 100 | **True (Subtractive)** | $-10$ | 1890 |
| 4 | `C` | 100 | `I` | 1 | False | $+100$ | 1990 |
| 5 | `I` | 1 | `V` | 5 | **True (Subtractive)** | $-1$ | 1989 |
| 6 | `V` | 5 | - | - | Terminal Symbol | $+5$ | **1994** |

---

## 5. Algorithmic Correctness

**Soundness.** In any standard Roman numeral, a smaller numeral preceding a larger one strictly denotes subtraction of the smaller value from the larger one. Because subtractive pairs only involve immediately adjacent characters and cannot be nested, comparing $s[i]$ with $s[i+1]$ correctly assigns negative polarity to every subtracted unit. Summing these signed values is algebraically equivalent to parsing multi-character tokens.

**Completeness.** Every character in the string is evaluated exactly once in sequence. No character is skipped, and the terminal character is unconditionally added. Hence, the complete numeric value of the numeral is computed.

---

## 6. Traps This Instance Exposes

- **Multi-Character Lookahead Fallacy:** Attempting to consume 2-character chunks requires handling index bounds ($i+2$) and branch conditions for whether the next character was part of a subtractive pair. The local 1-character lookahead removes all branching: every index contributes exactly one signed term.
- **Terminal Element Boundary:** The last character has no successor. Checking $\text{val}_i < \text{val}_{i+1}$ must guard against out-of-bounds access or handle the final element explicitly.
- **Case Sensitivity and Canonical Validation:** The problem guarantees valid Roman numerals. If invalid inputs such as $\text{"IIV"}$ or $\text{"IL"}$ were possible, a full grammar validator would be required; for valid Roman numerals, the local neighbor rule is sufficient and optimal.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. The string is traversed once from left to right. Each character requires an $O(1)$ dictionary lookup and an integer addition. Since $N \le 15$ for numbers $\le 3999$, the runtime is $O(1)$ in practice.
- **Auxiliary Space Complexity:** $O(1)$. The symbol-to-value mapping requires 7 entries, and accumulation uses a single scalar variable.
