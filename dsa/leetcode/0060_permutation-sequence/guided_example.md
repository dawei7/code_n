# Guided Example: Permutation Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "k": 3}`
- **Required output:** `"213"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

The objective is to compute `"213"` from `{"n": 3, "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Lexicographic permutations come in equal factorial-sized blocks

With $n$ distinct ordered digits, fixing the first digit leaves $n-1$ digits that can be arranged in $(n-1)!$ ways. Therefore, the sorted permutation list begins with a block of $(n-1)!$ permutations starting with 1, then an equally sized block starting with 2, and so on.

After the first digit is chosen, the same structure repeats among the remaining digits. Fixing the second position leaves $n-2$ digits and creates blocks of $(n-2)!$. The algorithm uses these nested blocks to jump directly to rank `k` rather than generate `k-1` earlier permutations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep `k` one-based and subtract skipped blocks

This source does not change `k` to a zero-based index. At position `i`, `k` is the one-based rank within the permutations sharing the already selected prefix.

For each unused candidate digit in increasing order, `fact` is the number of complete permutations under that choice. If `k > fact`, the requested permutation is not in this candidate's block, so the code subtracts `fact` and considers the next unused digit. If `k <= fact`, the target lies inside the current block; that digit is appended and marked visited.

The strict comparison matters. When `k == fact`, the requested permutation is the final member of the current block, not the first member of the next block. Using `>=` would shift boundary ranks incorrectly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the factorial is computed for each position

At output position `i`, there will be `n - i - 1` digits after the chosen one. Their number of arrangements is

$$
(n-i-1)!.
$$

The inner multiplication loop starts `fact = 1` and multiplies integers from 1 through `n - i - 1`, producing exactly that factorial. On the final position, the range is empty and `fact` stays 1, correctly representing $0! = 1$.

The source recomputes this factorial at every position rather than carrying it forward. This is simple and remains fast for $n \le 9$, though it contributes to the quadratic running time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"213"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"213"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Zero-based factorial digits:** Subtract one from `k`, divide by the current factorial to select a remaining-list index, then use the remainder. This avoids repeated block subtraction but removing a list element still costs linear time.
- **Carry the factorial forward:** Compute `(n-1)!` once and divide by the number of remaining positions after each choice. It removes the repeated factorial loop while keeping overall $O(n^2)$ list selection unless a stronger data structure is used.
- **Generate permutations in order:** Stop at the $k$th leaf. This may take $\Theta(k n)$ work and is infeasible near $n!$.
- **Order-statistics tree:** Select and delete the required unused digit in logarithmic time, reducing selection overhead at the cost of a complex data structure.
- **`k = 1`:** No block is skipped, so digits are selected in increasing order.
- **`k = n!`:** Every position skips as many earlier blocks as possible, producing descending digits.
- **`n = 1`:** `fact` remains $0! = 1$, digit 1 is selected, and `"1"` is returned.
- **Factorial boundary:** The use of `k > fact` keeps `k == fact` in the current block.
- **Input values:** `n` and `k` are integers passed by value; caller state is not mutated.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n$ output positions. Recomputing factorials across all positions uses a triangular number of multiplications, $O(n^2)$. Scanning digits 1 through $n$ at every position is also $O(n^2)$. Joining $n$ one-character pieces is $O(n)$, so total time is $O(n^2)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
