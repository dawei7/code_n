# Guided Example: Valid Phone Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"stdin": "", "files": {"file.txt": "987-123-4567\n123 456 7890\n(123) 456-7890\n"}}`
- **Required output:** `"987-123-4567\n(123) 456-7890"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

The objective is to compute `"987-123-4567\n(123) 456-7890"` from `{"stdin": "", "files": {"file.txt": "987-123-4567\n123 456 7890\n(123) 456-7890\n"}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Use the whole line as the candidate value

The file contains one phone number candidate per line, and valid output must
preserve each accepted line exactly. `awk` is well suited to this streaming
filter: it reads lines in input order, tests each complete record against a
regular expression, and prints the record when the pattern matches.

The script names `file.txt` directly, matching the contract that input comes
from that relative file rather than from command-line arguments or standard
input.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"stdin": "", "files": {"file.txt": "987-123-4567\n123 456 7890\n(123) 456-7890\n"}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Anchor the pattern at both boundaries

The regular expression begins with `^` and ends with `$`. These anchors mean
the match must cover the entire line from its first character to its last.

Without them, a line such as `abc987-123-4567xyz` would contain a valid-looking
substring and could be accepted even though the whole line is not a valid phone
number. Anchoring converts a substring search into full-format validation.

The Reference guarantees no leading or trailing whitespace. The anchors still
matter: they reject any extra digit, punctuation, or text, and they make the
format contract explicit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Express the two allowed prefixes as alternatives

The parenthesized group contains:

`[0-9]{3}-|\([0-9]{3}\) `

The left alternative matches exactly three digits followed by a hyphen. It is
the beginning of the `xxx-xxx-xxxx` form.

The right alternative matches a literal opening parenthesis, exactly three
digits, a literal closing parenthesis, and exactly one ordinary space. The
parentheses are escaped because unescaped parentheses group regular-expression
syntax rather than matching punctuation. The literal space after `\)` is
essential to the `(xxx) xxx-xxxx` form.

Because the two alternatives are enclosed in one group, the surrounding
anchors and the remaining suffix apply to both of them. Without this grouping,
regular-expression alternation could bind too broadly and allow one branch to
escape an anchor.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"987-123-4567\n(123) 456-7890"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"stdin": "", "files": {"file.txt": "987-123-4567\n123 456 7890\n(123) 456-7890\n"}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"987-123-4567\n(123) 456-7890"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`grep -E`:** The same POSIX extended expression can directly filter matching full lines.
- **`sed -n -E`:** Print only records satisfying the anchored expression; also a valid one-command solution.
- **PCRE `grep -P`:** Allows `\d`, but `-P` is not available in every grep implementation.
- **Missing anchors:** Would wrongly accept a valid phone substring embedded in a longer line.
- **Parentheses:** Must be escaped to match literal characters rather than create only a regex group.
- **Single required space:** `(123)456-7890` and `(123)  456-7890` are invalid.
- **Extra digits:** Exact interval counts and `$` reject them.
- **Blank line:** Matches neither branch and is omitted.
- **Input order:** Streaming default print preserves it automatically.
- **CRLF files:** A retained carriage return may require normalization in a generalized Unix environment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $c$ be the total number of characters and $n$ the number of lines. The
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
