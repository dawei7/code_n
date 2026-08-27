# Guided Example: Number of Changing Keys

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aAbBcC"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed **string `s` typed by a user. Changing a key is defined as using a key different from the last used key. For example, `s = "ab"` has a change of a key while `s = "bBBb"` does not have any.

The objective is to compute `2` from `{"s": "aAbBcC"}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate a physical key from the case of the character.** The string records typed letters, but uppercase and lowercase versions of the same English letter represent the same keyboard key. A “change” happens only when two consecutive characters, after ignoring case, name different letters. For example, moving from `'a'` to `'A'` is not a key change, while moving from `'A'` to `'b'` is.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aAbBcC"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution expresses that definition in one line:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution expresses that definition in one line:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`return sum(a != b for a, b in pairwise(s.lower()))`

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aAbBcC"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Manual one-pass normalization:** Keep the lowe:** - **Manual one-pass normalization:** Keep the lowercase form of only the previous character, lowercase each new character, compare, and update the previous value. That preserves $O(N)$ time while reducing auxiliary space to $O(1)$, but it is not the exact implementation shown here.
- **Compare character codes with a fixed offset:** ASCII arithmetic can ignore case, but it is less clear and easier to get wrong. The language's lowercase operation directly communicates the intended equivalence.
- **Count runs after normalization:** The answer equals the number of normalized runs minus one. Building or grouping all runs works, but directly counting unequal adjacent pairs obtains the same value with less machinery.
- **Count distinct normalized letters:** This is incorrect because a key may be revisited many times. `"ababa"` has two distinct keys but four changes.
- **Length-one string:** `pairwise` yields no pairs, and `sum` of an empty generator is zero. This correctly represents typing one key without changing from a previous key.
- **Every character has the same letter in mixed case:** Lowercasing makes all adjacent pairs equal, so the answer is zero.
- **Every adjacent character differs:** Every one of the $N-1$ comparisons is true, producing the maximum possible answer $N-1$.
- **A key is revisited:** A sequence such as `"aba"` changes at both boundaries. The fact that A appeared before does not cancel the later transition back to it.
- **Input preservation:** `lower()` returns a new string rather than editing `s`, so the caller's original casing remains intact.
- **Space accounting:** Calling the generator lazy does not make the whole expression constant-space, because the complete lowercase string already exists before `pairwise` begins.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `s`. Python's `s.lower()` visits all $N$ characters and constructs a new normalized string, taking $O(N)$ time and $O(N)$ space. `pairwise` then traverses the normalized string once and `sum` performs one comparison for each of the $N-1$ adjacent pairs, taking another $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
