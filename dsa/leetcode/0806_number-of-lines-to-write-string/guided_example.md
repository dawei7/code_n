# Guided Example: Number of Lines To Write String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"widths": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "s": "abcdefghijklmnopqrstuvwxyz"}`
- **Required output:** `[3, 60]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` of lowercase English letters and an array `widths` denoting **how many pixels wide** each lowercase English letter is. Specifically, $\text{widths}[0]$ is the width of `'a'`, $\text{widths}[1]$ is the width of `'b'`, and so on.

The objective is to compute `[3, 60]` from `{"widths": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "s": "abcdefghijklmnopqrstuvwxyz"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate the required greedy layout

Characters must stay in their original order, and each line should contain as many consecutive characters as fit within 100 pixels.

There is no optimization choice to compare. For each next character:

- put it on the current line if the width remains at most 100;
- otherwise start a new line with that character.

This is exactly the formatting rule from the statement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"widths": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "s": "abcdefghijklmnopqrstuvwxyz"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map letters to widths

Array `widths` is aligned with the lowercase alphabet. Character `a` uses index zero, `b` index one, and so on.

The expression:

`widths[ord(c) - ord("a")]`

retrieves a character's pixel width.

The `map` call lazily applies this expression to each character in `s`. The loop receives widths directly as `w`, so it does not need to keep the characters or build a separate width list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Define the rolling state

`lines` is the number of lines opened so far. `last` is the used pixel width on the current last line.

Because `s` is nonempty, the method initializes:

`lines = 1`

and:

`last = 0`.

The first character will either fit that initially empty line or, under a broader contract, cause a new line. Here every letter width is at most ten, so it always fits.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 60]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"widths": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "s": "abcdefghijklmnopqrstuvwxyz"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 60]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build explicit line strings:** It can reproduce the layout but stores information the answer does not request.
- **Precompute all character widths:** A list makes the iteration explicit but uses $O(n)$ extra space unnecessarily.
- **Start with zero lines:** Then the first character needs a special case. Nonempty `s` makes one initially open line simpler.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. Each character is converted to one width and processed once with constant work, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
