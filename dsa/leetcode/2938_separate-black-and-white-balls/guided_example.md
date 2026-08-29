# Guided Example: Separate Black and White Balls

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "101"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` balls on a table, each ball has a color black or white.

The objective is to compute `1` from `{"s": "101"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: State maintained during the reverse scan

`cnt` is the number of `1` characters already seen in the suffix, including the current position after it is incremented. `ans` accumulates how many zeros lie to the right of every encountered one.

At index $i$ containing `1`:

1. Increment `cnt`.
2. The suffix length including $i$ is `n - i`.
3. Of those suffix characters, `cnt` are ones.
4. Therefore `n - i - cnt` are zeros to the right.

The source adds this number to `ans`.

At an index containing `0`, it does nothing immediately. That zero will be counted later once for each one encountered to its left.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "101"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A trace

For `s = "100"`:

- At index $2$, the character is zero.
- At index $1$, it is also zero.
- At index $0$, `cnt` becomes one. The suffix has length three, so there are $3-1=2$ zeros to its right.

The answer is two, matching the two adjacent swaps needed to move the one past both zeros.

For `"101"`, the rightmost one contributes zero. The leftmost one sees a suffix of length three containing two ones, hence one zero. Total cost is one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why inversion count is a lower bound

Take any inverted pair consisting of a particular one before a particular zero. In the target arrangement, that zero must end before that one. With only adjacent swaps, their relative order can change only when those two balls cross, which costs one swap.

Each adjacent `10 -> 01` swap changes the relative order of exactly that pair and removes exactly one inversion. No single swap can eliminate two distinct inverted pairs. Hence at least the initial inversion count operations are necessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "101"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Forward inversion count:** Track ones seen so far and add that count at every zero. It is equivalent to the exact reverse formulation.
- **Track white destinations:** For each zero, add the distance from its current index to its next final white position. This also sums the same inversions.
- **Simulate adjacent swaps:** Correct but may take $O(n^2)$ time and mutable storage when the answer itself is large.
- **Already separated:** A string of zeros followed by ones has no inverted pair and returns zero.
- **All one color:** No opposite-color pair exists, so no swaps are needed.
- **Alternating colors:** Every zero contributes the number of earlier ones; the reverse formula counts the same pairs.
- **Why strict order matters:** A one before another one or a zero before another zero is not an inversion and never needs crossing.
- **Individual ball identities:** Balls of the same color are interchangeable, but counting cross-color pairs remains exact.
- **Large answer:** Use a wide integer type in fixed-width languages because the count can approach $n^2/4$.
- **No matrix or queue:** The final arrangement is implicit; only the minimum operation count is requested.
- **Why suffix zeros equal the formula:** Among the `n-i` positions from $i$ onward, every character is either zero or one. After incrementing `cnt` for the current one, subtracting it from suffix length leaves precisely the zeros.
- **Crossing direction:** To place whites left, each inverted one must move right past each later zero, or equivalently each zero moves left past earlier ones. Both views charge the same crossing once.
- **Stable order within a color:** Adjacent swaps need never exchange two equal-color balls. Their relative identities are irrelevant, and avoiding such swaps preserves the minimum.
- **Worst arrangement:** A prefix of $p$ ones followed by $q$ zeros contains $pq$ inversions. This demonstrates why simulation can be quadratic even though counting is linear.
- **Reverse-loop boundary:** Starting at `n - 1` and ending at zero ensures every later character has already been classified when a one's contribution is calculated.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The reverse loop visits each of the $n$ characters once and does constant work, so time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
