# Guided Example: Toggle Light Bulbs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bulbs": [10, 30, 20, 10]}`
- **Required output:** `[20, 30]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `bulbs` of integers between 1 and 100.

The objective is to compute `[20, 30]` from `{"bulbs": [10, 30, 20, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A toggle is parity, not a full history

Every bulb begins off. Toggling one bulb twice returns it to off:

`off -> on -> off`.

Three toggles leave it on again. Therefore the final state depends only on whether its occurrence count in `bulbs` is odd or even:

- even count means off;
- odd count means on.

The order of toggles for different bulbs does not affect this conclusion because each operation changes only its named bulb.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bulbs": [10, 30, 20, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use one fixed state slot per bulb number

There are exactly 100 bulbs, numbered 1 through 100. The source creates:

`st = [0] * 101`.

Index `b` directly represents bulb `b`. Index 0 is unused, making the array indices align with the one-based bulb labels.

A zero means off and a one means on.

For every toggle number `x`, the source executes:

`st[x] ^= 1`.

XOR with 1 flips a binary state:

$$
0\mathbin{\mathrm{xor}}1=1,
\qquad
1\mathbin{\mathrm{xor}}1=0.
$$

This exactly simulates the operation without branches.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | There are exactly 100 bulbs, numbered 1 through 100.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the state equals occurrence parity

Initially every `st[b]` is zero, matching zero occurrences.

Each occurrence of bulb `b` flips `st[b]` and changes the occurrence count's parity from even to odd or odd to even. By induction, after every processed operation:

$$
\texttt{st}[b]=C(b)\bmod2.
$$

When all operations are processed, a stored one identifies exactly an odd-count bulb, which is exactly a bulb left on.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[20, 30]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bulbs": [10, 30, 20, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[20, 30]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Toggle membership in a set:** Add an absent bu:** - **Toggle membership in a set:** Add an absent bulb and remove a present bulb, then sort the set. This uses up to 100 entries and adds an $O(B\log B)$ final sort for $B$ on bulbs.
- **Counter frequencies:** Count every bulb and filter odd values. It stores more information than needed and still requires ordering the keys.
- **Boolean negation:** `st[x] = not st[x]` also flips state, though it changes entries from integers to booleans; XOR keeps the explicit parity representation.
- **Every bulb toggled an even number of times:** All states return to zero and the result is `[]`.
- **Repeated odd count:** Any odd number of toggles leaves the same final on state as one toggle.
- **Bulb one and bulb 100:** Direct indexing includes both valid boundary labels.
- **Unused index zero:** It remains off and is filtered from the enumerated result.
- **Already sorted requirement:** Scanning the fixed state array from low to high satisfies it without sorting.
- **Single toggle:** That bulb alone is returned.
- **Input length at most 100:** The fixed-domain method remains valid even if the same bulb appears many times.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+100)$. Let $N=\lvert\texttt{bulbs}\rvert$. Processing the operations costs $O(N)$. Scanning the fixed 101 slots costs $O(101)$, which is $O(1)$ with respect to $N$. Total time is $O(N+100)=O(N)$ under the fixed domain.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
