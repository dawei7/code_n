# Guided Example: Flip Game

We trace the step-by-step adjacent pair scanning ($s[i] == \text{'+'}$ and $s[i+1] == \text{'+'}$), single-move transition generation ($s[:i] + \text{"--"} + s[i+2:]$), overlapping pair handling, and edge case boundary termination on representative string instances:

- **Input:** $\text{currentState} = \text{"++++"}$
- **Required output:** `["--++", "+--+", "++--"]` (Three possible moves corresponding to flipping consecutive pluses starting at indices 0, 1, and 2)
- **No Consecutive Pluses:** $\text{currentState} = \text{"+-+-" } \implies []$ (No consecutive `"++"` exists; game cannot proceed)
- **Single Character Guard:** $\text{currentState} = \text{"+"} \implies []$ (Fewer than 2 characters; no pairs possible)
- **All Minuses Base Case:** $\text{currentState} = \text{"----"} \implies []$
- **Overlapping Pairs:** $\text{currentState} = \text{"+++"} \implies \text{["--+", "+--"]}$ (Index 0 and index 1 are evaluated independently for single-move transitions)

This instance demonstrates single-ply game state generation, explains why overlapping pairs yield distinct independent moves without interference, details the in-place list modification/backtrack cycle versus string slicing, and achieves strictly $O(N^2)$ output-sensitive time and $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a string $\text{currentState} = \text{"++++"}$ containing only `'+'` and `'-'`:
Find **all possible states** of the string after making **exactly one valid move**, where a valid move consists of flipping any two consecutive `"++"` into `"--"`:

```text
Initial string: "++++" (length 4)

Candidate consecutive pairs:
- Index 0: s[0] == '+', s[1] == '+' -> flip -> "--++"
- Index 1: s[1] == '+', s[2] == '+' -> flip -> "+--+"
- Index 2: s[2] == '+', s[3] == '+' -> flip -> "++--"

All possible single-move outcomes: ["--++", "+--+", "++--"]
```

### Key Clarification: One Move, Not Recursive Play
- Unlike Flip Game II (which requires Minimax game search to determine if a player can force a win), Flip Game I asks strictly for **all immediate successor states after 1 move**.
- The consecutive pairs can overlap in the original string (e.g. index 0 uses positions 0 and 1, while index 1 uses positions 1 and 2), but each returned state represents flipping **exactly one** adjacent pair from `currentState`.

---

## 2. Conceptual Foundation & Invariants

### Consecutive Pair Detection Protocol
Let $N = \text{len}(\text{currentState})$.
If $N < 2$, no adjacent pairs exist $\implies \text{return } []$.

For each starting index $i \in [0, N - 2]$:
1. **Check Condition:**
   $$
   \text{currentState}[i] == \text{'+'} \quad \text{and} \quad \text{currentState}[i + 1] == \text{'+'}
   $$
2. **Generate Successor State:**
   Form the new string by replacing positions $i$ and $i + 1$ with `"--"`:
   $$
   \text{next\_state} = \text{currentState}[:i] + \text{"--"} + \text{currentState}[i + 2:]
   $$
   Append `next_state` to the result list `ans`.

> **Invariant.** For every generated string in `ans`, exactly two characters that were originally `'+'` at positions $i$ and $i + 1$ have been replaced with `'-'`, while all other $N - 2$ characters remain unchanged.

---

## 3. Step-by-Step Worked Execution

We trace the linear pair scan on $\text{currentState} = \text{"++++"}$ ($N = 4$):
Loop range: $i \in [0, 2]$.

---

### Step 1: Evaluate Starting Index $i = 0$
- Adjacent pair: $\text{currentState}[0] = \text{'+'}, \quad \text{currentState}[1] = \text{'+'}$.
- Condition: Both characters are `'+'` (**Match!**).
- Slice & construct successor:
  $$
  \text{currentState}[:0] + \text{"--"} + \text{currentState}[2:] = \text{""} + \text{"--"} + \text{"++"} = \mathbf{\text{"--++"}}
  $$
- Append `" --++ "` to `ans`.
- Result list: `["--++"]`.

---

### Step 2: Evaluate Starting Index $i = 1$
- Adjacent pair: $\text{currentState}[1] = \text{'+'}, \quad \text{currentState}[2] = \text{'+'}$.
- Condition: Both characters are `'+'` (**Match!**).
- Slice & construct successor:
  $$
  \text{currentState}[:1] + \text{"--"} + \text{currentState}[3:] = \text{"+"} + \text{"--"} + \text{"+"} = \mathbf{\text{"+--+"}}
  $$
- Append `"+--+"` to `ans`.
- Result list: `["--++", "+--+"]`.

---

### Step 3: Evaluate Starting Index $i = 2$
- Adjacent pair: $\text{currentState}[2] = \text{'+'}, \quad \text{currentState}[3] = \text{'+'}$.
- Condition: Both characters are `'+'` (**Match!**).
- Slice & construct successor:
  $$
  \text{currentState}[:2] + \text{"--"} + \text{currentState}[4:] = \text{"++"} + \text{"--"} + \text{""} = \mathbf{\text{"++--"}}
  $$
- Append `"++--"` to `ans`.
- Result list: `["--++", "+--+", "++--"]`.

---

### Loop Termination
All $N - 1 = 3$ adjacent pairs inspected.
Final collected states:
$$
\mathbf{[\text{"--++"}, \text{"+--+"}, \text{"++--"}]}
$$

---

## 4. Complete Execution Trace

```text
currentState = "++++", N = 4

i = 0: s[0:2] == "++" -> flip -> "--++" -> ans = ["--++"]
i = 1: s[1:3] == "++" -> flip -> "+--+" -> ans = ["--++", "+--+"]
i = 2: s[2:4] == "++" -> flip -> "++--" -> ans = ["--++", "+--+", "++--"]

Result: ["--++", "+--+", "++--"]
```

| Start Index $i$ | Pair Inspected $(s[i], s[i+1])$ | Is `"++"`? | Prefix $s[:i]$ | Flipped Pair | Suffix $s[i+2:]$ | Generated State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | `('+', '+')` | **Yes** | `""` | `"--"` | `"++"` | **`"--++"`** |
| **1** | `('+', '+')` | **Yes** | `"+"` | `"--"` | `"+"` | **`"+--+"`** |
| **2** | `('+', '+')` | **Yes** | `"++"` | `"--"` | `""` | **`"++--"`** |
| **End** | - | - | - | - | - | **3 States Generated** |

---

### Edge Case Contrast: Non-Matching Patterns
1. `currentState = "+-+-"`:
   - $i = 0$: `"+-"` $\implies$ No.
   - $i = 1$: `"-+"` $\implies$ No.
   - $i = 2$: `"+-"` $\implies$ No.
   - Output: `[]`.
2. `currentState = "+"`:
   - Length $1 < 2 \implies$ Loop range $[0, -1]$ is empty $\implies$ Output: `[]`.

---

## 5. Algorithmic Correctness

**Soundness.** A state is generated if and only if positions $i$ and $i + 1$ both contain `'+'`. The replacement strictly changes only those two characters into `"--"`, satisfying the single-move rule of the game.

**Completeness.** Any legal move must flip two adjacent `'+'` characters. The linear loop visits every index $i \in [0, N - 2]$, exhaustively discovering all possible adjacent pairs. Because distinct indices $i$ produce distinct successor strings, every valid move is enumerated without duplication.

---

## 6. Traps This Instance Exposes

- **Overlapping Pairs Trap:** In `"+++"`, flipping at index 0 yields `"--+"` and flipping at index 1 yields `"+--"`. An implementation must not "consume" characters so as to skip index 1; each candidate index must be evaluated independently against the original string.
- **Single Character Input ($N < 2$):** If `len(currentState) < 2`, attempting to check `currentState[i+1]` without guarding could trigger out-of-bounds errors.
- **Accidental Multiple Moves:** Only ONE pair of `"++"` may be flipped per resulting string. Flipping multiple pairs in the same string violates the definition of a single valid move.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the length of `currentState`. The loop performs $N - 1$ pair comparisons ($O(1)$ each). When a match occurs, string slicing and concatenation take $O(N)$ time. At most $N - 1$ matches can occur, giving a maximum runtime of $(N - 1) \times O(N) = O(N^2)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory (excluding the output list) for string slicing buffers.
