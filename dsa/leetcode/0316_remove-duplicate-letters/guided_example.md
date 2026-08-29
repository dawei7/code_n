# Guided Example: Remove Duplicate Letters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "bcabc"}`
- **Required output:** `"abc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

The objective is to compute `"abc"` from `{"s": "bcabc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why last occurrences are needed

`last = {c: i for i, c in enumerate(s)}` records the final index of every letter. Repeated assignments for the same key naturally leave its greatest index.

Suppose a letter is currently in the partial result but a smaller current letter would look better before it. Removing the old letter is safe only if another copy appears later. The test

`last[letter] > i`

answers exactly that question at current index `i`.

If the old letter's last occurrence has already been reached, removing it would make it impossible to include that required letter at all. Lexicographic improvement cannot justify producing an invalid result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "bcabc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The stack as a chosen subsequence

Characters are appended while scanning `s` from left to right. Hence, the stack always corresponds to characters chosen at increasing original indices and is a valid subsequence of the processed prefix.

Popping only removes a previous choice. Appending the current character after those removals still preserves index order. The algorithm never moves a later character before an earlier index artificially; it simply chooses not to use some earlier occurrences.

`vis` contains exactly the letters currently in `stk`. When a letter is appended, it is added to `vis`. When a letter is popped, it is removed from `vis`. Keeping these two structures synchronized allows constant-time duplicate checks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Skipping an already selected letter

If current character `c` is already in `vis`, the source immediately continues. Adding it would violate the requirement that each letter appear once.

Keeping the earlier selected occurrence is safe. Any later decisions that might pop that letter can still use an occurrence after the pop only when the last-occurrence condition permits it. The current duplicate does not need to replace the existing copy merely because it has been encountered.

This skip also prevents equal letters from appearing twice in the stack. The stack contains at most one copy of each lowercase letter at any moment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "bcabc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive smallest-feasible-first-letter selection:** Find the smallest character whose suffix still contains every needed letter, choose it, remove later duplicates, and recurse. It is correct and linear under the fixed 26-letter alphabet, but repeated slicing is less direct than the stack.
- **Sort the distinct letters:** This ignores subsequence order. The alphabetically sorted set may not be obtainable from `s` while preserving indices.
- **Keep the first occurrence of every letter:** It guarantees uniqueness but can be lexicographically suboptimal when a larger early letter safely appears later.
- **Keep the last occurrence of every letter:** It may also produce a larger prefix and does not greedily optimize the order of selected occurrences.
- **Pop whenever the top is larger:** Without checking for a later copy, this can permanently remove a required letter.
- **Pop whenever a later copy exists:** Without requiring `top > c`, this may remove a smaller letter and make the result lexicographically larger.
- **Forget to remove a popped letter from `vis`:** Its later occurrence would be skipped, causing the final result to omit that letter.
- **Forget the duplicate check:** Repeated letters would be appended, violating exactly-once output.
- **One character:** It is appended and returned unchanged.
- **All characters equal:** The first occurrence is appended and every later occurrence is skipped, yielding one letter.
- **Already strictly increasing distinct letters:** No top is greater than the next character, so the input is returned unchanged.
- **Strictly decreasing distinct letters:** No letter has a later duplicate, so none can be popped; the original order is the only feasible distinct-letter subsequence.
- **A smaller letter arrives late:** Larger suffix letters are popped only when each has another future occurrence; mandatory letters form a barrier.
- **Repeated smallest letter:** Once selected, later copies are skipped. Earlier larger letters may already have been removed when its first useful occurrence appeared.
- **Lowercase guarantee:** Lexicographic character comparisons match alphabetical order directly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. Building `last` takes $O(n)$ time, and the main loop visits every character once.
- **Auxiliary Space Complexity:** $O(26)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
