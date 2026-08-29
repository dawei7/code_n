# Guided Example: The Number of the Smallest Unoccupied Chair

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"times": [[1, 4], [2, 3], [4, 6]], "targetFriend": 1}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a party where `n` friends numbered from `0` to $n - 1$ are attending. There is an **infinite** number of chairs in this party that are numbered from `0` to `infinity`. When a friend arrives at the party, they sit on the unoccupied chair with the **smallest number**.

The objective is to compute `1` from `{"times": [[1, 4], [2, 3], [4, 6]], "targetFriend": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preserve identities while sorting arrivals

Chair assignments must be simulated in arrival order, but the answer refers to the original friend index. The solution appends each original index `i` directly to `times[i]`, turning each row into `[arrival, leaving, i]`, then sorts `times`.

Because all arrival times are distinct, sorting lists lexicographically orders friends by arrival without needing a tie rule. The appended index travels with the times and identifies `targetFriend` after sorting.

This modifies the caller's input: every inner list gains an element and the outer list is reordered. That side effect is part of the exact implementation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"times": [[1, 4], [2, 3], [4, 6]], "targetFriend": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use one heap for free chairs and one for occupied chairs

At most $N$ friends can be present, so chair numbers $0$ through $N-1$ are sufficient. `idle` initially contains that whole range and is heapified. Its smallest element is always the smallest currently unoccupied chair.

`busy` stores pairs `(leaving, chair)`. As a min-heap, it exposes the occupied chair whose friend leaves earliest.

Before assigning a chair to an arrival at time `arrival`, the loop repeatedly removes busy entries whose leaving time is at most the arrival. Each freed chair is pushed back into `idle`. The `<=` boundary is essential: a chair becomes available at the exact leaving moment and can be used by a friend arriving then.

After releasing all eligible chairs, `heappop(idle)` returns the smallest unoccupied chair `j`. If the arriving original index is the target, the method returns `j` immediately. Otherwise it records `(leaving, j)` in `busy` so that chair can be released later.

The target's busy entry is not inserted because the answer is already known and the function ends. This does not alter the returned assignment.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the heaps model the party exactly

Before each arrival, every chair in `busy` is occupied by a previously arrived friend who has not yet left, and every allocated chair not in `busy` is in `idle`. The release loop moves exactly the chairs whose owners have departed by the current time. Thus, after releases, `idle` contains all and only unoccupied chairs among the initialized range.

The minimum heap then implements the rule “take the unoccupied chair with the smallest number.” Recording the chosen chair with its leaving time preserves the invariant for the next arrival.

Induction over sorted arrivals proves every friend processed before the target receives the same chair as in the real event sequence. Therefore the chair returned at the target's arrival is correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"times": [[1, 4], [2, 3], [4, 6]], "targetFriend": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Linear chair scan:** For each arrival, scan chair states from zero upward. It is simple but can take $O(N^2)$ time.
- **Allocate chairs lazily:** Keep a next-new-chair counter plus a heap only for released chairs. This also gives $O(N\log N)$ time and can avoid preloading all chair numbers.
- **Separate event list:** Store arrival, leaving, and index tuples without changing `times`. It preserves the caller's data at the cost of another list.
- **Arrival at a departure time:** The release condition uses `<=`, so the newly freed chair is eligible immediately.
- **Several departures before one arrival:** The while loop releases all of them before selecting the minimum.
- **Departure order differs from arrival order:** The busy heap orders by leaving time independently, which is why one sorted arrival list alone is insufficient.
- **Distinct arrivals:** They guarantee one friend is processed at each arrival time and make lexicographic sorting unambiguous.
- **Target arrives first:** All chairs are idle and the method returns chair zero.
- **No chairs freed before target:** Earlier friends occupy chairs from zero upward, so the target receives the next smallest number.
- **Input mutation:** Rows gain original indices and the list is sorted in place; callers needing the original structure must pass a copy.
- **Imported heap functions:** The exact source assumes `heapify`, `heappop`, and `heappush` are available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the number of friends.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
