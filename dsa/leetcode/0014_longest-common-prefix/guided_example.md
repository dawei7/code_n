# Guided Example: Longest Common Prefix

We trace the step-by-step vertical column scan on a representative string array instance:

- **Input:** $\text{strs} = [\text{"flower"}, \text{"flow"}, \text{"flight"}]$
- **Required output:** $\text{"fl"}$

This instance demonstrates column-wise character alignment, early-exit detection upon encountering the first discordant character, and safe termination before shorter strings are indexed out of bounds.

---

## 1. Instance & Teaching Goal

Given an array of strings $\text{strs}$, we seek the longest prefix shared by every string in the array.

For $\text{strs} = [\text{"flower"}, \text{"flow"}, \text{"flight"}]$, the characters align column by column as follows:

```text
Column Index:  0   1   2   3   4   5
------------------------------------
strs[0]:       f   l   o   w   e   r
strs[1]:       f   l   o   w
strs[2]:       f   l   i   g   h   t
------------------------------------
Agreement:     ✓   ✓   ✗
```

At index $0$ and index $1$, all three strings have `'f'` and `'l'`. At index $2$, $\text{strs}[0]$ has `'o'` while $\text{strs}[2]$ has `'i'`. Because a common prefix must be contiguous from index $0$, this first mismatch permanently halts the search, yielding $\text{"fl"}$.

A naive approach sorts the entire array of strings ($O(N \cdot M \log N)$), or performs pairwise longest common prefix reductions across all $N$ strings. The optimal vertical scanning algorithm examines only the necessary prefix columns in lockstep, terminating at the earliest possible character mismatch with $O(M \cdot N)$ worst-case and sublinear average-case runtime.

---

## 2. Conceptual Foundation & Invariants

### Vertical Scanning Logic
We select the first string $\text{strs}[0]$ as the reference template of length $M = |\text{strs}[0]|$.

For each column index $i = 0, 1, \dots, M-1$:
1. Let $c = \text{strs}[0][i]$ be the target character.
2. For every remaining string $s \in \text{strs}[1 \dots N-1]$:
   - **Length boundary:** If $i = |s|$, string $s$ is exhausted; the common prefix cannot exceed length $i$.
   - **Character mismatch:** If $s[i] \ne c$, the character differs; the common prefix ends at index $i$.
3. If all strings agree on character $c$ at column $i$, column $i$ is appended to the common prefix.

If the loop finishes all $M$ columns of $\text{strs}[0]$ without mismatch, $\text{strs}[0]$ itself is the common prefix.

> **Invariant.** Before inspecting column $i$, all characters at indices $0 \le k < i$ have been verified to match across every string in $\text{strs}$. The longest common prefix is guaranteed to start with $\text{strs}[0][0 \dots i-1]$.

---

## 3. Step-by-Step Worked Execution

We scan the array $\text{strs} = [\text{"flower"}, \text{"flow"}, \text{"flight"}]$ vertically:

### Column 0 ($i = 0$)
- Reference character: $c = \text{strs}[0][0] = \text{'f'}$.
- Check $\text{strs}[1] = \text{"flow"}$:
  - Length check: $0 < |\text{strs}[1]| = 4$ (safe).
  - Character comparison: $\text{strs}[1][0] = \text{'f'} = c$ (match).
- Check $\text{strs}[2] = \text{"flight"}$:
  - Length check: $0 < |\text{strs}[2]| = 6$ (safe).
  - Character comparison: $\text{strs}[2][0] = \text{'f'} = c$ (match).
- **Result for Column 0:** All strings agree on `'f'`. Valid prefix: $\text{"f"}$.

---

### Column 1 ($i = 1$)
- Reference character: $c = \text{strs}[0][1] = \text{'l'}$.
- Check $\text{strs}[1] = \text{"flow"}$:
  - Length check: $1 < |\text{strs}[1]| = 4$ (safe).
  - Character comparison: $\text{strs}[1][1] = \text{'l'} = c$ (match).
- Check $\text{strs}[2] = \text{"flight"}$:
  - Length check: $1 < |\text{strs}[2]| = 6$ (safe).
  - Character comparison: $\text{strs}[2][1] = \text{'l'} = c$ (match).
- **Result for Column 1:** All strings agree on `'l'`. Valid prefix: $\text{"fl"}$.

---

### Column 2 ($i = 2$)
- Reference character: $c = \text{strs}[0][2] = \text{'o'}$.
- Check $\text{strs}[1] = \text{"flow"}$:
  - Length check: $2 < |\text{strs}[1]| = 4$ (safe).
  - Character comparison: $\text{strs}[1][2] = \text{'o'} = c$ (match).
- Check $\text{strs}[2] = \text{"flight"}$:
  - Length check: $2 < |\text{strs}[2]| = 6$ (safe).
  - Character comparison: $\text{strs}[2][2] = \text{'i'} \ne c$ (**Mismatch!**).
- **Termination Triggered:** A mismatch is discovered at column $i = 2$.
- The prefix search aborts immediately, emitting $\text{strs}[0][0 \dots 2] = \text{"fl"}$.

---

## 4. Complete Execution Trace

| Column $i$ | Reference $\text{strs}[0][i]$ | Checked String $\text{strs}[j]$ | Character $\text{strs}[j][i]$ | In-Bounds? | Match Status | Action Taken |
|:---:|:---:|:---|:---:|:---:|:---:|:---|
| 0 | `'f'` | $\text{strs}[1] = \text{"flow"}$ | `'f'` | Yes ($0 < 4$) | Match | Continue scan |
| 0 | `'f'` | $\text{strs}[2] = \text{"flight"}$ | `'f'` | Yes ($0 < 6$) | Match | Column 0 verified; prefix $\leftarrow \text{"f"}$ |
| 1 | `'l'` | $\text{strs}[1] = \text{"flow"}$ | `'l'` | Yes ($1 < 4$) | Match | Continue scan |
| 1 | `'l'` | $\text{strs}[2] = \text{"flight"}$ | `'l'` | Yes ($1 < 6$) | Match | Column 1 verified; prefix $\leftarrow \text{"fl"}$ |
| 2 | `'o'` | $\text{strs}[1] = \text{"flow"}$ | `'o'` | Yes ($2 < 4$) | Match | Continue scan |
| 2 | `'o'` | $\text{strs}[2] = \text{"flight"}$ | `'i'` | Yes ($2 < 6$) | **Mismatch (`'o'` vs `'i'`)** | **Halt immediately; emit $\text{"fl"}$** |

### Edge Case Comparison Table

| Edge Scenario | Input Sample | Failure Mechanism | Output |
|:---|:---|:---|:---:|
| Disjoint first character | `["dog", "racecar", "car"]` | Mismatch at column $i = 0$ (`'d'` vs `'r'`) | `""` |
| Empty string present | `["", "b", "c"]` | Length boundary at $i = 0$ ($0 = \lvert \text{strs}[0] \rvert$) | `""` |
| One string is a prefix of another | `["ab", "a"]` | Length boundary at $i = 1$ ($1 = \lvert \text{strs}[1] \rvert$) | `"a"` |
| Single string input | `["alone"]` | Outer loop exhausts all columns without checks | `"alone"` |

---

## 5. Algorithmic Correctness

**Soundness.** A string $P$ is a prefix of string $S$ if $S$ begins with $P$. By verifying every column $k < i$ matches across all array elements, the emitted slice $\text{strs}[0][0 \dots i-1]$ is provably a prefix of every string in $\text{strs}$.

**Completeness.** Since a common prefix cannot extend beyond the shortest string in the array or beyond the first index where any two strings differ, checking columns from left to right and halting at the first mismatch or length exhaustion identifies the exact maximal length prefix.

---

## 6. Traps This Instance Exposes

- **Index Out-of-Bounds on Shorter Strings:** If string $A$ has length 3 and string $B$ has length 10, inspecting index 3 on string $A$ without a boundary check causes an out-of-bounds error. Checking $i = |s|$ *before* accessing $s[i]$ avoids crashes.
- **Empty Array or Empty String:** An empty input array $\text{strs} = []$ or an array containing an empty string $\text{strs} = [\text{""}, \text{"b"}]$ must safely return `""` without attempting invalid indexing.
- **Whole-String Common Prefix:** If one string is a complete prefix of all others (e.g. `["th", "the", "their"]`), the algorithm correctly terminates when the shortest string is exhausted.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$, where $S$ is the sum of characters across all strings. In the worst case where all strings are identical of length $M$, the algorithm checks $M \times N$ characters. In typical cases where mismatches occur early, the algorithm inspects only $i \times N$ characters, executing in $O(k \cdot N)$ where $k$ is the length of the common prefix.
- **Auxiliary Space Complexity:** $O(1)$. No dynamic structures or string copies are created during the comparison loop. The output slice references the existing characters.
