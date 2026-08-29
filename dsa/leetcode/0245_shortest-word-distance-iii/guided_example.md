# Guided Example: Shortest Word Distance III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"wordsDict": ["a", "a"], "word1": "a", "word2": "a"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `wordsDict` and two strings that already exist in the array `word1` and `word2`, return *the shortest distance between the occurrence of these two words in the list*.

The objective is to compute `1` from `{"wordsDict": ["a", "a"], "word1": "a", "word2": "a"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Case 1: the target words are different

The variables `i` and `j` start at `-1`, meaning their targets have not yet appeared. During the left-to-right scan, `i` is replaced whenever `word1` occurs, and `j` is replaced whenever `word2` occurs. Once both are valid, `abs(i - j)` is a candidate distance.

Keeping only the latest indices is sufficient. When a new `word1` appears at index `k`, every seen `word2` is on or before `k`, and the greatest such index is closest to `k`. Any older `word2` is farther left. The symmetric statement holds when a new `word2` appears. Thus every new target occurrence needs to be compared only with the latest occurrence of the opposite target.

Consider



with `word1 = "makes"` and `word2 = "coding"`.

- Index `1` records the first `makes` in `i`; no `coding` exists yet.
- Index `3` records `coding` in `j`, producing distance `abs(1 - 3) = 2`.
- Index `4` replaces `i` with the newer `makes`, producing distance `abs(4 - 3) = 1`.

The minimum is `1`.

The source uses two separate `if` conditions. In this branch the words are known to differ, so a single array element can update at most one target index. Checking the distance on a non-target position only repeats an unchanged candidate and is harmless.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"wordsDict": ["a", "a"], "word1": "a", "word2": "a"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Case 2: both target names are equal

Now two “latest target” variables cannot both be assigned the current index, because that would treat one occurrence as both endpoints and yield zero. Instead, `j` means the index of the previous occurrence of the shared word.

When the scan finds another occurrence at index `i`:

1. If `j != -1`, compute `i - j`, the distance from the previous occurrence.
2. Update `j = i`, making this occurrence the previous one for the future.

The comparison must happen before replacing `j`; otherwise the subtraction would use the same index twice.

For the example array with both targets equal to `"makes"`, the first occurrence at index `1` merely sets `j = 1`. The next occurrence at index `4` creates the valid pair `(1, 4)` with distance `3`, then becomes the stored previous occurrence. The method returns `3`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why consecutive equal occurrences are sufficient

Suppose the shared word appears at sorted positions

$$
p_0<p_1<\cdots<p_{r-1}.
$$

For a fixed later occurrence $p_b$, the closest earlier occurrence is $p_{b-1}$, because every $p_a$ with $a<b-1$ is smaller and therefore farther away. Equivalently, any nonconsecutive gap decomposes into positive consecutive gaps:

$$
p_b-p_a=(p_{a+1}-p_a)+\cdots+(p_b-p_{b-1}).
$$

That sum cannot be smaller than each positive component. Hence the minimum distance between any two distinct occurrences must appear between consecutive occurrences. The single stored index `j` is all the history needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"wordsDict": ["a", "a"], "word1": "a", "word2": "a"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One unified “previous interesting index” scan:** Record the latest index holding either target. When another interesting word appears, compare if the labels differ or if the requested targets are equal. This also achieves $O(n)$ time and $O(1)$ space, but the exact source's branch structure makes the distinct-occurrence rule more explicit.
- **Store occurrence lists:** Collect positions for the targets, then merge two lists for different words or inspect consecutive gaps for equal words. It is correct and linear time but uses $O(n)$ extra space unnecessarily for a single query.
- **Binary search between occurrence lists:** Each occurrence from one list can search for neighboring positions in the other. This costs $O(n\log n)$ in the worst case and needs stored lists, so the streaming scan is stronger.
- **Compare every pair:** Testing all target occurrence pairs is simple but can require $O(n^2)$ time.
- **Equal targets:** Two different occurrences are mandatory. The separate branch deliberately never compares an index with itself.
- **Exactly two occurrences of an equal target:** The first initializes `j`, the second supplies the only valid distance, and the guarantee ensures that candidate exists.
- **Adjacent occurrences:** Distance `1` is the smallest possible valid distance. The source could return early when it finds `1`, but completing the scan does not change correctness or asymptotic complexity.
- **First target appears much earlier:** Sentinels prevent a distance calculation until a compatible second endpoint has actually appeared.
- **Repeated runs of the same word:** In the equal-target branch, every consecutive pair in the run is checked. In the different-target branch, repeated copies replace the latest same-label index so the next opposite word uses the nearest one.
- **A target missing from the array:** The contract says both target names exist and, when equal, represent two individual words. Outside that contract, `ans` might remain `n`, so a broader API would need defined missing-pair behavior.
- **Initialization with `n`:** Since the greatest legal distance is $n-1$, `n` is a safe finite sentinel. It avoids depending on floating-point infinity while still being replaced by any valid candidate.
- **Independent `if` statements in the different branch:** They are safe because that branch runs only when `word1 != word2`. Moving the equal-word case into the same code without adjustment would make both indices equal and incorrectly create a zero distance.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of strings in `wordsDict`. Exactly one branch runs, and that branch scans the list once. With word length bounded by `10`, each equality comparison is constant time under the problem constraints, giving $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
