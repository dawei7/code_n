# Guided Example: Find Indices of Stable Mountains

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"height": [1, 2, 3, 4, 5], "threshold": 2}`
- **Required output:** `[3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` mountains in a row, and each mountain has a height. You are given an integer array `height` where $\text{height}[i]$ represents the height of mountain `i`, and an integer `threshold`.

The objective is to compute `[3, 4]` from `{"height": [1, 2, 3, 4, 5], "threshold": 2}` while avoiding redundant calculations and unnecessary overhead.

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

Mountain `i` is stable based solely on mountain `i-1`. Its own height and all other mountains are irrelevant. Mountain zero has no predecessor and is explicitly excluded.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"height": [1, 2, 3, 4, 5], "threshold": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The list comprehension iterates `i` from one through `len(height)-1`. For each candidate, it tests `height[i - 1] > threshold`. When true, it emits the current index `i`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The strict greater-than comparison is essential. A predecessor exactly equal to the threshold does not make the next mountain stable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"height": [1, 2, 3, 4, 5], "threshold": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit loop:** Append qualifying indices in a standard loop. It is equivalent and may be easier to instrument, but the comprehension directly expresses filtering.
- **Compare the current mountain:** This is incorrect; stability depends on the previous mountain's height.
- **Use greater-than-or-equal:** It would wrongly include predecessors equal to `threshold`.
- **Start at zero:** Python negative indexing would compare mountain zero against the last mountain, violating the non-circular definition.
- **All predecessors high:** Every index one through $n-1$ is returned.
- **No predecessor high:** The output is empty.
- **Alternating high and low:** Each high mountain affects only the immediately following index.
- **Last mountain high:** It affects no output if there is no mountain after it.
- **First mountain high:** It can make index one stable even though index zero itself is never stable.
- **Minimum length two:** Exactly one candidate index is tested.
- **Duplicate heights:** They are evaluated independently against the threshold; uniqueness is irrelevant.
- **Output space:** A list is required by the contract, so a potentially linear result does not contradict constant auxiliary working memory.
- **Current height can be small:** A mountain of height one is stable if its predecessor exceeds the threshold. Stability does not describe the current mountain's own strength.
- **Current height can be large:** A very tall mountain is not stable when its predecessor fails the test. Looking at `height[i]` would reverse the relationship.
- **Threshold at maximum constraint:** When threshold is one hundred and heights are at most one hundred, strict comparison guarantees an empty result.
- **Threshold at minimum constraint:** With threshold one, every predecessor of height at least two qualifies, while height one still fails equality.
- **Consecutive stable indices:** If several consecutive predecessor heights exceed the threshold, their following indices can all be stable; there is no exclusivity rule.
- **Why no state carries between candidates:** Each predicate reads one fixed predecessor independently. Whether index `i-1` was itself stable has no bearing on index `i`.
- **Result contains indices, not heights:** The comprehension emits `i`. Emitting `height[i]` would lose location information and violate examples with repeated values.
- **Any-order allowance:** Ascending order is still a valid “any order” result and is helpful for deterministic testing.
- **No circular predecessor:** The row of mountains is linear. Explicitly excluding zero prevents Python's negative indexing from inventing a wraparound neighbor.
- **Read-only behavior:** The comprehension reads `height` without sorting or changing it, so predecessor relationships remain those of the original row.
- **Why every possible answer is examined:** Every stable index must lie between one and `n-1`, exactly the range traversed. The predicate is the definition itself, so there is no hidden candidate outside the scan.
- **One-pass optimality:** A correct method may need to inspect every predecessor height because any unchecked value could independently determine whether its following index belongs in the result. Linear time is therefore asymptotically optimal.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of mountains. The comprehension evaluates $n-1$ candidates with constant work, taking $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
