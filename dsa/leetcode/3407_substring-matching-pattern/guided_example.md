# Guided Example: Substring Matching Pattern

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leetcode", "p": "ee*e"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and a pattern string `p`, where `p` contains **exactly one** `'*'` character.

The objective is to compute `true` from `{"s": "leetcode", "p": "ee*e"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Separate the fixed parts around the wildcard.** Because `p` contains exactly one `"*"`, it has the form

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leetcode", "p": "ee*e"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

where $A$ is the fixed text before the star and $B$ is the fixed text after it. Either fixed part may be empty. Replacing the star with any sequence of zero or more characters means a matching substring must contain:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

1. an occurrence of $A$;
2. later, without overlapping backward, an occurrence of $B$;
3. any characters between the end of $A$ and the start of $B$, including no characters at all.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leetcode", "p": "ee*e"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual scan:** One can locate $A$ and then $B$ with explicit loops. This avoids relying on `str.find` but requires careful substring-comparison code and offers no conceptual advantage here.
- **Regular expression:** Converting `*` to something like `.*` can solve the task, but escaping, substring-versus-full-match semantics, and greedy behavior add avoidable complexity.
- **Dynamic programming wildcard matcher:** General wildcard matching DP handles many stars and question marks, but it is excessive for exactly one star and usually costs $O(nm)$ time or substantial state.
- **Empty prefix:** For a pattern such as `"*abc"`, `find("", 0)` succeeds at zero. The method then searches for `"abc"` anywhere in `s`, which is exactly the required meaning.
- **Empty suffix:** For `"abc*"`, after locating `"abc"` the empty suffix succeeds at its end. The star may consume zero characters, so merely finding the prefix is sufficient.
- **Only the star:** Although the stated pattern length permits `"*"`, both fixed parts are empty. Both searches succeed at index zero, correctly reporting that the empty replacement matches a substring position.
- **Zero-character wildcard:** The update to the end of the first part and the inclusive `find` start allow the second part to begin immediately, so adjacent $A$ and $B$ are accepted.
- **Overlapping fixed parts:** Overlap is not allowed because one wildcard replacement cannot move backward. Advancing by `len(t)` correctly rejects a suffix occurrence that begins inside the chosen prefix occurrence.
- **Repeated prefix occurrences:** The earliest prefix is always safe; it ends no later than any later equal-length occurrence and therefore leaves the largest possible suffix of `s` for finding $B$.
- **Pattern longer than the text:** A match can still exist only if the star's removal makes the fixed parts fit in order. The two searches test this directly without needing a separate length rule.
- **Exactly one star:** The correctness proof uses exactly two fixed pieces. Inputs with no star or multiple stars are outside the contract and should not be used to reinterpret this implementation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $n=\lvert\texttt{s}\rvert$ and $m=\lvert\texttt{p}\rvert$. Splitting the pattern scans and copies $O(m)$ characters and creates two fixed-part strings, so it uses $O(m)$ time and $O(m)$ space.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
