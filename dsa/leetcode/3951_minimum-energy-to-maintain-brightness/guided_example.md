# Guided Example: Minimum Energy to Maintain Brightness

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "brightness": 5, "intervals": [[6, 12]]}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`, representing `n` light bulbs arranged in a line and indexed from 0 to $n - 1$.

The objective is to compute `14` from `{"n": 5, "brightness": 5, "intervals": [[6, 12]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Minimum bulbs for one time unit

One bulb illuminates at most three positions: its own position and its immediate neighbors. Hence $q$ active bulbs can illuminate at most $3q$ distinct positions. To illuminate at least `brightness` positions, every solution needs at least

$$
\left\lceil\frac{\texttt{brightness}}{3}\right\rceil
$$

bulbs.

For integers, the source computes this ceiling as:

`(brightness + 2) // 3`.

The lower bound is achievable on a line. Place bulbs with enough spacing that their three-position neighborhoods cover consecutive groups, adjusting the first or final placement near a boundary. With

$$
q=\left\lceil\frac{\texttt{brightness}}{3}\right\rceil,
$$

the line contains at least `brightness` positions because `brightness <= n`, and $q$ bulbs can cover at least that many distinct positions. Boundary bulbs may cover only two positions, but placements can be shifted inward; the familiar minimum dominating placement for all $n$ path positions uses $\lceil n/3\rceil$ bulbs, and covering only a requested prefix of at most $n$ positions is no harder.

For small lines the same formula remains exact:

- with $n=1$, one bulb covers the one required position;
- with $n=2$, one bulb covers both positions;
- with $n=3$, the middle bulb covers all three.

Thus the per-active-time minimum is precisely the ceiling, independent of which time is being considered.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "brightness": 5, "intervals": [[6, 12]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the same spatial minimum can be repeated

At every active integer time, bulbs may be chosen independently. There is no startup cost, switching penalty, persistence rule, or limit on how often a bulb is toggled.

The same optimal placement can simply be used at every active time, consuming the minimum number of energy units each time. Inactive times use zero bulbs.

Consequently, if $T$ distinct time units are covered by at least one interval, total minimum energy is:

$$
\left\lceil\frac{\texttt{brightness}}{3}\right\rceil T.
$$

Overlapping interval requirements do not add together. A time covered by several intervals still asks for the same brightness once and consumes one time unit's energy.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort intervals before forming their union

The source sorts `intervals` lexicographically, which orders them by start time and then by end time. It initializes `merged` with the first sorted interval.

For each later interval `x`:

- if the previous merged end is strictly less than `x[0]`, the intervals do not overlap, so `x` starts a new merged component;
- otherwise, they overlap at one or more inclusive integer times, and the previous end is extended to the larger endpoint.

An interval contained completely inside the previous component changes nothing because `max` keeps the existing farther end.

The condition uses `merged[-1][1] < x[0]`. Thus intervals `[1,3]` and `[3,5]` merge because they share time 3. Intervals `[1,2]` and `[3,5]` remain separate. They are adjacent on the integer timeline but share no active time; keeping them separate or combining their lengths would give the same total count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "brightness": 5, "intervals": [[6, 12]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterate every active time unit:** Endpoints reach $10^9$, so expanding intervals into individual times is infeasible. Union lengths summarize them.
- **Add every interval length independently:** Overlapping time units would be charged more than once even though brightness is one shared requirement.
- **Use `brightness // 3` bulbs:** This rounds down and fails whenever brightness is not a multiple of three. Ceiling division is required.
- **Assume boundary bulbs always cover three:** A boundary placement covers fewer positions, but optimal bulbs can be shifted inward; the global ceiling remains achievable.
- **Optimize bulb positions separately for every interval:** The per-time minimum is identical, and overlap is handled through union length. Actual position identities do not affect energy.
- **Single-position line:** One bulb is necessary and sufficient for the only possible brightness.
- **Brightness equals `n`:** The formula becomes the domination number $\lceil n/3\rceil$ for the whole path.
- **One-point interval:** Inclusive length is one, so it consumes exactly one active time's bulb count.
- **Nested intervals:** The smaller interval adds no new active time and is absorbed by the larger merged component.
- **Touching at one endpoint:** They overlap at that integer time and are merged.
- **Adjacent but non-overlapping intervals:** `[a,b]` and `[b+1,c]` remain separate, but their summed inclusive lengths still equal the contiguous union size.
- **Caller-visible changes:** Sorting and endpoint extension mutate `intervals` and some of its row lists.
- **Large overlapping collection:** Sorting dominates; the linear merge prevents duplicate energy charges.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m\log m)$. Let $m$ be the number of intervals. Sorting takes $O(m\log m)$ time. The merge scan and energy sum are each $O(m)$, so total time is $O(m\log m)$.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
