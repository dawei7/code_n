# Guided Example: Minimum Possible Integer After at Most K Adjacent Swaps On Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "4321", "k": 4}`
- **Required output:** `"1342"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `num` representing **the digits** of a very large integer and an integer `k`. You are allowed to swap any two adjacent digits of the integer **at most** `k` times.

The objective is to compute `"1342"` from `{"num": "4321", "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the answer should be built left to right

To minimize a decimal string lexicographically, the earliest output position has priority over every later position. At each position, the greedy goal is to place the smallest digit that can be moved there using the remaining adjacent-swap budget.

Moving a digit left by one current position costs one adjacent swap. Once a digit is selected, it is removed from the remaining sequence and appended to the answer. The difficulty is calculating a digit's current position efficiently after earlier removals have shifted the sequence.

The stored solution combines ten queues with a Binary Indexed Tree, also called a Fenwick tree.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "4321", "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Queues of original positions

`pos[d]` is a deque containing the one-based original indices of every occurrence of digit `d`, in increasing order. The setup loop reads `num` with indices starting at one and appends each index to the corresponding digit queue.

When considering digit `d`, only `pos[d][0]` matters. Among identical digits, the earliest remaining occurrence is never more expensive to move left than a later one. Choosing a later equal digit cannot improve the output character and would cross the earlier equal digit unnecessarily.

After selecting an occurrence, `popleft` removes it from its digit queue in constant time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the Binary Indexed Tree records

The tree contains one at every original index already selected for the output and zero elsewhere. `update(j, 1)` marks a selected original position. `query(x)` returns how many selected positions are at most `x`.

The low-bit operation `x & -x` isolates the least significant set bit. Updates move upward through Fenwick responsibility ranges by adding that low bit. Queries move toward zero by subtracting it. Both operations visit $O(\log n)$ indices.

After `i-1` output digits have been selected, `tree.query(n)` equals `i-1`. For a candidate at original index `j`, `tree.query(j)` counts selected original positions no later than `j`. The difference `tree.query(n) - tree.query(j)` counts selected positions originally after `j`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1342"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "4321", "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1342"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct list simulation:** Repeatedly locate and remove a feasible digit from a list. Shifting elements can make total time quadratic.
- **Segment tree:** It can count removed positions and update them in $O(\log n)$, matching the asymptotic time with more implementation overhead.
- **Budget large enough to sort fully:** The greedy process chooses digits in ascending order, including duplicates, once every needed move is affordable.
- **Budget too small for a smaller digit:** The algorithm skips it for the current position but may choose it later after intervening digits are removed.
- **Repeated digit:** Only the earliest remaining occurrence is considered because it is the cheapest identical choice.
- **Leading zero output:** It is explicitly permitted, so zero receives normal greedy priority.
- **One digit:** Its cost is zero and the original string is returned.
- **k remains unused:** “At most” k swaps allows the algorithm to stop spending when the string cannot be improved.
- **One-based indexing:** Fenwick operations and stored positions consistently use indices one through n.
- **Required imports:** `defaultdict`, `deque`, and their supporting environment must be available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of digits. Building the ten position queues takes $O(n)$ time and space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
