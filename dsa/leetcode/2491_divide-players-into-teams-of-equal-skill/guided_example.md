# Guided Example: Divide Players Into Teams of Equal Skill

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"skill": [3, 2, 5, 1, 3, 4]}`
- **Required output:** `22`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer array `skill` of **even** length `n` where $\text{skill}[i]$ denotes the skill of the $$i^{\text{th}}$$ player. Divide the players into $n / 2$ teams of size `2` such that the total skill of each team is **equal**.

The objective is to compute `22` from `{"skill": [3, 2, 5, 1, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting reveals the only possible partner pattern

Every team must contain two players, and every team must have the same total skill. After sorting `skill` in nondecreasing order, the smallest remaining skill is at the left end and the largest is at the right end.

If a valid division exists, those two extremes must be paired. To see why, suppose the smallest value $a$ were paired with some value $b$ smaller than the current maximum $d$. The maximum would need a partner $c$ that is at least $a$. Then

$$
d+c \ge d+a > b+a,
$$

so the maximum's team would have a larger sum than the smallest player's team. That contradicts the equal-sum requirement.

Therefore, pair the smallest with the largest, remove them, and repeat the same argument on the remaining sorted interval. This forces symmetric pairs from the two ends.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"skill": [3, 2, 5, 1, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Establish the required sum from the first pair

The code sorts the list in place and defines

`t = skill[0] + skill[-1]`.

Since the extreme pair is forced in any valid division, its sum must be the common team sum. Every later symmetric pair must equal `t`. There is no need to guess or search for another target.

Pointers `i` and `j` begin at the first and last indices. While `i<j`, the method checks the current extreme pair. If its sum differs from `t`, no valid equal-sum division exists and it immediately returns `-1`.

If the sum matches, the pair's chemistry `skill[i]*skill[j]` is added to `ans`. Both pointers then move inward, ensuring each player is used exactly once.

Because the input length is even, the pointers meet between elements after exactly $n/2$ pairs. There is never an unpaired middle player.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code sorts the list in place and defines

`t = skill[0] ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a failed symmetric pair proves impossibility

The sorted-extremes argument applies at every stage, not only to the original minimum and maximum. Once outer pairs are fixed and removed, the remaining players still need to form teams with the same target `t`. Their smallest and largest remaining values must pair with each other.

If their sum is smaller than `t`, the smallest cannot obtain a larger partner because the current largest is already the largest available. If their sum is larger, the largest cannot obtain a smaller partner because the current smallest is already the smallest available. Either way, rearranging interior players cannot repair the mismatch.

Thus the early `-1` is logically conclusive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `22` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"skill": [3, 2, 5, 1, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `22` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency table:** Since skills are at most 10:** - **Frequency table:** Since skills are at most 1000, pair complementary values by counts in $O(n+U)$ time and $O(U)$ space, where $U=1000$. It avoids comparison sorting but requires careful handling of equal complements.
- **Hash-map counts:** Determine the common sum from total skill divided by the number of teams, then consume complements. It offers expected linear time but has more bookkeeping.
- **Two players:** They always form the sole team, and their product is returned.
- **Duplicate skills:** They represent different players and must be consumed with their full multiplicity.
- **Equal-skill pair:** When both endpoints have the same value, there must be an even number of remaining copies to pair.
- **Even length:** It guarantees no player remains after pointers move inward.
- **First target pair:** The global minimum and maximum are forced partners in any valid solution.
- **Early mismatch:** A failed remaining-extremes sum cannot be repaired by a different pairing.
- **Large chemistry:** Use a sufficiently wide integer type in fixed-width languages.
- **Mutation:** The exact implementation sorts the input list in place.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of players. Python's sort takes $O(n\log n)$ time in the worst case. The two-pointer scan performs $n/2$ iterations, which is $O(n)$. Sorting dominates, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
