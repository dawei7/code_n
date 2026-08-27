# Guided Example: Restore IP Addresses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "25525511135"}`
- **Required output:** `["255.255.11.135", "255.255.111.35"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

The objective is to compute `["255.255.11.135", "255.255.111.35"]` from `{"s": "25525511135"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Meaning of the search state

In `dfs(i)`, the index `i` is the first digit not yet assigned to a component. The list `t` holds the valid components already chosen, in their original order. The invariant is that joining `t` without dots equals exactly the consumed prefix `s[:i]`.

The loop chooses an inclusive endpoint `j` from `i` through at most `i + 2`. Therefore `s[i:j + 1]` has length one, two, or three. If `check(i, j)` accepts it, the algorithm appends that substring, recursively processes the suffix beginning at `j + 1`, and then pops the substring to restore `t` for the next candidate endpoint.

The pop is what makes one mutable path list reusable. Without it, a component selected in one branch would remain present when exploring a sibling branch, so the path would no longer correspond to the consumed digits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "25525511135"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the component check is exact

The first condition rejects a substring such as `00`, `01`, or `025`: if `s[i] == "0"` and `i != j`, its length is greater than one and it has a forbidden leading zero. A one-character `0` is accepted because then `i == j`.

After the leading-zero rule, `int(s[i:j + 1])` converts the candidate to its numerical value. The input is guaranteed to contain only digits, and the loop guarantees a nonempty slice, so conversion is safe. Checking the inclusive range through `0 <= value <= 255` accepts exactly the permitted values. The lower-bound comparison is redundant for a digit-only nonnegative substring but documents the complete address rule.

Limiting candidate length to three is also necessary. Every four-digit nonnegative decimal string is either numerically above `255` or begins with a zero; in the latter case it is already invalid as a multi-digit component.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first condition rejects a substring such as `00`, `01`, ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When a path becomes an answer

The first base condition requires both all digits to be consumed and exactly four components to have been chosen. Only then does `".".join(t)` form and record an address.

Both halves are needed. Consuming the string with only three components is invalid because an IPv4 address requires four. Choosing four components while digits remain is also invalid because digits cannot be dropped. The second base condition stops either impossible state: no digits remain before four pieces are formed, or four pieces already exist before all digits are consumed.

Although the code says `i >= n`, valid recursion can only reach `i == n`: every endpoint is below `n`, and the recursive index is `j + 1`. The broader comparison is harmless.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["255.255.11.135", "255.255.111.35"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "25525511135"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["255.255.11.135", "255.255.111.35"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three nested cut loops:** Enumerate lengths of:** - **Three nested cut loops:** Enumerate lengths of the first three components; the fourth consumes the remainder. This avoids recursion and has the same fixed bound, but the repeated index arithmetic is more verbose.
- **Remaining-length pruning:** Before branching, reject states whose unconsumed digit count is outside one to three times the remaining component count. This reduces failed calls without changing asymptotic complexity.
- **Enumerating all dot positions:** For each choice of three gaps, validate four substrings. It is correct but examines more invalid layouts unless length bounds are incorporated.
- **Exactly four zeros:** `0000` permits only four single-character components, producing `0.0.0.0`. Any attempt to group two zeros fails the leading-zero check.
- **Too short or too long:** Fewer than four digits cannot fill four nonempty components; more than twelve cannot fit within four three-digit components. Both return an empty list.
- **Value boundary:** `255` is accepted and `256` is rejected. Three digits alone do not guarantee validity.
- **Leading-zero boundary:** `0` is valid, while `00` and `01` are invalid even though their integer values are within range.
- **Input preservation:** The method reads slices from `s` and never changes or reorders the source digits.
- **Output order:** DFS order follows shorter component choices first. The contract allows any order, so no final sort is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. There are at most three length choices at each of four component positions, so the search explores at most a constant multiple of $3^4$ states. Each check parses at most three digits, and each successful answer contains at most twelve digits plus three dots. Since both “four” and “three” are fixed protocol constants, time is $O(1)$ with respect to the input length, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
