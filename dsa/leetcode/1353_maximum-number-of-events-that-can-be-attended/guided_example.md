# Guided Example: Maximum Number of Events That Can Be Attended

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"events": [[1, 2], [2, 3], [3, 4]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of `events` where $\text{events}[i] = [\text{startDay}_{i}, \text{endDay}_{i}]$. Every event `i` starts at $\text{startDay}_{i}$_ and ends at $\text{endDay}_{i}$.

The objective is to compute `3` from `{"events": [[1, 2], [2, 3], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Group events by their start day

`g[start]` stores the end day of every event beginning on `start`. During the same pass, `l` becomes the earliest start day and `r` becomes the latest end day. The sweep only needs days from `l` through `r` because no event is available outside that range.

Unlike an approach that sorts the event list by start, this source uses a dictionary of start-day buckets.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"events": [[1, 2], [2, 3], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remove events whose opportunity has expired

At day `s`, an event with end day below `s` can no longer be attended. Because `pq` is a min-heap, its smallest end day is at the root. The loop pops while `pq[0] < s`. Once the root is at least `s`, every remaining heap entry also ends on or after the current day.

The comparison is strict. An event whose end equals the current day is still attendable because interval endpoints are inclusive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Add events that start today

Every end day in `g[s]` is pushed into the heap. The input guarantee `start <= end` means these newly starting events cannot already be expired on their start day.

After removal and insertion, the heap contains exactly the unattended events whose start is no later than `s` and whose end is no earlier than `s`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"events": [[1, 2], [2, 3], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sorted starts with a pointer:** Sort events by start day, add all whose start has arrived, and jump over empty calendar gaps. This gives $O(n\log n)$ time without an explicit $D$ term.
- **Disjoint-set day assignment:** Sort by end day and use a union-find structure to locate the earliest unused day in each interval. It is useful for very large sparse day coordinates.
- **Choose latest-ending event first:** This can waste an early deadline and reduce the total; earliest end is the exchange-safe rule.
- **End equals current day:** The event remains valid because expiration uses `end < day`.
- **Several events with the same deadline:** Attending any one of them today is equivalent for the greedy proof.
- **Duplicate intervals:** They are distinct events and may be attended on different days if their range permits.
- **One-day event:** It must be used on its only day or becomes expired on the next iteration.
- **Empty heap:** No event can be attended that day, so the algorithm correctly leaves `ans` unchanged.
- **Nonempty input:** The constraints guarantee at least one event, so `l` is replaced from infinity before `range` is constructed.
- **Sparse large span:** The exact source still visits every day and creates empty `defaultdict` buckets; a pointer-based sweep avoids that cost.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the number of events and let $D = r-l+1$ be the number of calendar days traversed.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
