# Guided Example: Minimum Jumps to Reach End via Prime Teleportation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 4, 6]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `2` from `{"nums": [1, 2, 4, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prime-factor preprocessing

`factors[x]` lists every distinct prime divisor of `x` for values through `10^6`.

The global sieve visits `i` from 2 upward. An empty `factors[i]` means no smaller prime divided `i`, so `i` is prime. It then appends `i` to every multiple `j`.

Consequently:

- a prime `p` has `factors[p]=[p]`;
- a composite has its distinct prime divisors;
- 1 has an empty list.

This table is built once when the module loads.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 4, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map each prime to divisible indices

For each array value `x` and each `p in factors[x]`, index `i` is appended to `g[p]`.

Thus `g[p]` contains exactly all indices whose values are divisible by prime `p`.

When the BFS reaches an index whose value itself is prime `p`, looking up `g[nums[i]]` produces precisely its legal teleport destinations.

If `nums[i]` is composite, `g[nums[i]]` is normally an empty newly created list because keys populated during construction are primes only. This correctly yields no teleportation: the rule requires the current value itself to be prime.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each array value `x` and each `p in factors[x]`, index `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: BFS state

`q` contains all indices at the current distance `ans` from index 0. `vis` prevents revisiting indices, and index 0 is marked before the search begins.

For every current index:

- if it is `n-1`, the current BFS level is the minimum distance and is returned;
- its legal teleport list is retrieved;
- adjacent indices are temporarily appended to the same list;
- every unvisited destination is marked and placed in `nq`.

After the whole level, `q=nq` and `ans` increments.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 4, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Test primality during BFS and scan nums:** Sca:** - **Test primality during BFS and scan nums:** Scanning all destinations per reached prime can become quadratic.
- **Reverse BFS:** The editorial describes factor-based reverse edges; forward BFS in the exact source is equally shortest-path correct.
- **Do not clear groups:** Correctness remains, but the same large list may be scanned many times.
- **One-element array:** Index 0 is already the destination, so answer is zero.
- **Value 1:** It has no prime teleport and only adjacent moves apply.
- **Composite current value:** It cannot initiate teleportation even though its index belongs to groups of its prime factors.
- **Prime current value:** It reaches every index whose value is divisible by that prime.
- **Teleport to self:** The group includes the current index, but `vis` skips it.
- **Repeated prime values:** The first reached occurrence expands the group; later occurrences need no repeat.
- **No teleportation:** Adjacent steps guarantee answer `n-1`.
- **Right boundary:** The destination is returned before `i+1` is appended.
- **Missing imports:** Standalone use must supply `defaultdict` and `List`.
- **Input preservation:** The source mutates only group lists, not `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M\log\log M+n\log M)$. Let `M=10^6` and `n=len(nums)`.
- **Auxiliary Space Complexity:** $O(n+M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
