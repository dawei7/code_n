# Guided Example: Find the Town Judge

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "trust": [[1, 2]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

The objective is to compute `2` from `{"n": 2, "trust": [[1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the judge rules into directed degrees

Each trust pair `[a, b]` is a directed relationship from person `a` to person `b`.

- The number of people someone trusts is their outgoing degree.
- The number of people who trust someone is their incoming degree.

The judge trusts nobody, so the judge's outgoing degree must be zero. Every other person trusts the judge, so the judge's incoming degree must be exactly `n - 1`.

These two numbers completely characterize the judge. The algorithm does not need to build neighbor lists or traverse a graph; it only needs to count incoming and outgoing relationships for each label.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "trust": [[1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use arrays indexed by person label

People are labeled from one through `n`. The solution allocates arrays `cnt1` and `cnt2` with length `n + 1` so that a person's label can be used directly as an index. Position zero is intentionally unused.

Their meanings are:

- `cnt1[p]` is how many listed people person `p` trusts;
- `cnt2[p]` is how many listed people trust person `p`.

For each pair `[a, b]`:

`cnt1[a] += 1` records one outgoing relationship, and `cnt2[b] += 1` records one incoming relationship.

The trust pairs are unique, so repeated copies cannot artificially inflate these degrees. Self-trust is forbidden, so an incoming count of `n - 1` really can represent all other people.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check both conditions together

After counting, the loop examines labels one through `n`. It returns `i` only if

`cnt1[i] == 0 and cnt2[i] == n - 1`.

The outgoing condition prevents accepting a popular person who still trusts somebody. The incoming condition prevents accepting an isolated person who trusts nobody but is not trusted by everyone else.

If no label satisfies both, the method returns `-1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "trust": [[1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One score array:** Subtract one for every outgoing edge and add one for every incoming edge. A judge has score `n - 1`. This is more compact, though separate arrays make both requirements explicit.
- **Adjacency lists:** They can compute degrees but retain neighbor information the answer never uses.
- **Candidate elimination:** Trusting someone disqualifies the source as judge, after which a candidate can be verified. It is useful in query-based variants but unnecessary with the full edge list available.
- **Too few trust pairs:** Fewer than `n - 1` edges cannot supply the judge's required incoming degree; the normal count still returns `-1`.
- **Popular person who trusts someone:** Correctly rejected by nonzero `cnt1`.
- **Person who trusts nobody but lacks support:** Correctly rejected by incoming degree below `n - 1`.
- **Empty trust list with `n > 1`:** Every outgoing count is zero, but no incoming count reaches `n - 1`, so return `-1`.
- **Empty trust list with `n = 1`:** The sole label meets both zero-valued conditions and is returned.
- **Unique pairs:** They ensure degree counts represent distinct people rather than repeated records.
- **No self-trust:** It ensures the judge's incoming target is exactly all other `n - 1` people.
- **Maximum label:** Arrays have length `n + 1`, so label `n` is a valid direct index.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + E)$. Let `N` be the number of people and `E` the number of trust pairs.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
