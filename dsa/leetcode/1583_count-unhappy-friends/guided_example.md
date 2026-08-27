# Guided Example: Count Unhappy Friends

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "preferences": [[1], [0]], "pairs": [[1, 0]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a list of `preferences` for `n` friends, where `n` is always **even**.

The objective is to compute `0` from `{"n": 2, "preferences": [[1], [0]], "pairs": [[1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What makes one person unhappy

Let person `x` be paired with `y`. Person `x` is unhappy if there is some person `u` whom `x` prefers over `y`, and `u` in turn prefers `x` over `u`’s assigned partner `v`.

The important quantifier is “there exists.” One witnessing person `u` is enough to mark `x` unhappy. The answer counts unhappy people, not unhappy relationships or witnessing pairs, so the implementation must stop searching once it finds the first witness for a particular `x`.

Two fast lookup structures make the condition efficient:

- `d[x][z]` gives the rank of person `z` in `x`’s preference list;
- `p[x]` gives `x`’s assigned partner.

With these structures, each preference comparison and partner lookup takes expected constant time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "preferences": [[1], [0]], "pairs": [[1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Converting preference order into rank

Each `preferences[x]` list is already ordered from most preferred to least preferred. Comparing two people by repeatedly searching that list would cost linear time per comparison. The solution instead builds

`d = [{x: j for j, x in enumerate(p)} for p in preferences]`.

For every person’s preference list `p`, the dictionary comprehension maps each friend identifier `x` to position `j`. A smaller position means stronger preference. Thus:

`d[a][b] < d[a][c]`

means person `a` prefers `b` over `c`.

The comprehension’s reused local name `x` is only the key variable inside construction; it does not conflict with the later loop’s person `x`. Each preference list contains every other person exactly once, so every needed rank lookup exists and no key is overwritten by a duplicate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each `preferences[x]` list is already ordered from most pref... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Building a partner lookup in both directions

The input gives unordered pairs such as `[x, y]`. For each pair, the code assigns both `p[x] = y` and `p[y] = x`. After processing all pairs, `p` is a symmetric mapping: asking for either member returns the other.

The constraints guarantee every person appears in exactly one pair. Therefore, every person has exactly one partner entry, and later lookups such as `p[x]` and `p[u]` are defined.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "preferences": [[1], [0]], "pairs": [[1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan preference lists for every comparison:** :** - **Scan preference lists for every comparison:** This avoids the rank dictionaries but can cost $O(N^3)$ time because each candidate condition may require linear searches. The inverse ranks are the standard time-space tradeoff.
- **Check every possible `u`:** Testing all $N-1$ other people is correct if both conditions are evaluated, but people ranked below partner `y` can never satisfy the first condition. Stopping the candidate range at `d[x][y]` avoids needless work.
- **Count all witnessing pairs:** A person can have several witnesses, but the requested answer counts that person once. The checked-in `break` is essential.
- **Mark unhappy people in a set:** A set can deduplicate counts when examining relationships from another iteration order. The person-centered loop already counts at most once, so no set is needed.
- **Two friends:** Each person is paired with the only other person, so the prefix before the partner is empty for both. The answer is zero.
- **Partner ranked first:** `d[x][y] == 0` makes `range(0)` empty. Person `x` cannot prefer anyone over the partner and is necessarily happy.
- **Partner ranked last:** Every other eligible person is examined until a witness is found or the prefix is exhausted.
- **Several valid witnesses:** The first one increments `ans` and terminates the inner loop, preventing double counting.
- **Mutual unhappiness:** If `x` and `u` prefer each other over their partners, each is evaluated and counted in its own outer iteration. That correctly contributes two unhappy friends.
- **One-sided preference:** If `x` prefers `u` but `u` prefers partner `v` over `x`, the rank inequality fails. Attraction from only one side is insufficient.
- **Symmetric partner mapping:** Both directions must be inserted. Storing only `p[x] = y` from each input pair would leave lookups undefined when the later search starts from the other member.
- **Unique preference entries:** The dictionary rank representation relies on each friend appearing once in a preference list. The problem guarantees uniqueness and excludes the person themself.
- **Even `n` and complete pairing:** These guarantees ensure every person has one partner. Without them, `p[x]` could be missing and the unhappy definition would need additional handling.
- **Dictionary variable names:** The inner comprehension’s `x` is local to that comprehension in Python 3. The later `for x in range(n)` independently represents the person being evaluated.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let $N$ be the number of friends.
- **Auxiliary Space Complexity:** $O(N^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
