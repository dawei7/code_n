# Guided Example: The Dining Philosophers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1, "start_order": [0, 1, 2, 3, 4]}`
- **Required output:** `{"calls": 5, "events_per_call": 5, "properties": ["both-picks-before-eat", "puts-after-eat", "no-shared-fork-overlap", "all-finish"]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers.

The objective is to compute `{"calls": 5, "events_per_call": 5, "properties": ["both-picks-before-eat", "puts-after-eat", "no-shared-fork-overlap", "all-finish"]}` from `{"n": 1, "start_order": [0, 1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use one shared transaction lock to remove circular waiting

The classic deadlock occurs when several philosophers each hold one fork and wait forever for the other. The exact solution avoids that situation by placing the entire pick-eat-put sequence inside one shared lock. The object constructor creates `transaction = Lock()` once, and every call to `wantsToEat` uses that same lock.

`with transaction` acquires the lock before running the indented callbacks and releases it automatically when the block exits. At most one call on this `DiningPhilosophers` object can therefore execute any fork callback at a time.

This is deliberately conservative. Philosophers whose forks do not conflict could theoretically eat concurrently, but the global transaction lock serializes them too. The benefit is a very small, easy-to-audit synchronization protocol.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1, "start_order": [0, 1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The callback order

Once a call holds the transaction lock, it invokes:

1. `pickLeftFork()`;
2. `pickRightFork()`;
3. `eat()`;
4. `putRightFork()`;
5. `putLeftFork()`.

The philosopher eats only after both pick callbacks have run. Both put callbacks run after eating, returning the two forks. Releasing them in reverse acquisition order is conventional and matches the exact source, although with no concurrent transaction inside the critical section, either release order would preserve mutual exclusion.

The `philosopher` identifier is not referenced directly. It is still part of the required interface, and the supplied callbacks are already associated with that philosopher’s left fork, right fork, and eating event. The lock discipline is identical for every identifier.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why two philosophers cannot hold the same fork

Suppose one call is inside the `with` block. Every other simultaneous call using the same object is blocked while trying to acquire `transaction` and cannot invoke either pick callback. The active call is consequently the only one that can hold any fork. It puts both down before leaving the block and releasing the transaction lock.

Thus fork ownership intervals from different calls never overlap. This is stronger than merely protecting adjacent fork pairs: the source prevents any two philosophers from holding any forks at the same time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"calls": 5, "events_per_call": 5, "properties": ["both-picks-before-eat", "puts-after-eat", "no-shared-fork-overlap", "all-finish"]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1, "start_order": [0, 1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"calls": 5, "events_per_call": 5, "properties": ["both-picks-before-eat", "puts-after-eat", "no-shared-fork-overlap", "all-finish"]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One lock per fork with a global acquisition order:** Philosophers acquire the lower-numbered fork before the higher-numbered fork. This breaks circular wait and permits nonadjacent philosophers to eat concurrently, but requires careful mapping of left and right callbacks.
- **Limit diners with a semaphore:** Allow at most four philosophers to attempt fork acquisition at once. This prevents all five from holding one fork simultaneously, though fork locks and fairness reasoning are still needed.
- **Arbitrator or waiter:** A coordinator grants both forks atomically when available. It can preserve more concurrency and implement a fair queue, but has substantially more state.
- **Asymmetric fork order:** Have one philosopher acquire right then left while others acquire left then right. This breaks the classic cycle but is less uniform than the single transaction.
- **Same philosopher called concurrently:** The shared lock serializes the calls just like requests from different philosophers.
- **Callback failure:** The context manager releases the transaction lock, but the exact source cannot guarantee logical fork cleanup if an exception occurs between pick and put callbacks. The supplied callback contract is assumed to complete normally.
- **Fairness limitation:** `threading.Lock` does not specify FIFO wakeups. A ticket queue or explicit condition protocol would be needed for a formal no-starvation guarantee independent of scheduler fairness.
- **Lost parallelism:** The source permits only one eater even when two philosophers use disjoint forks. This is a throughput tradeoff, not a safety error.
- **Shared object requirement:** All threads must call the same instance so they share `transaction`. Separate instances would have separate locks and would not coordinate.
- **Fixed problem size:** Five philosophers and bounded requests make safety and progress the meaningful properties; asymptotic scaling does not capture scheduler behavior.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. There are always five philosophers and each invocation performs one lock acquisition plus exactly five callbacks. Excluding time spent waiting for another thread and the callback implementations’ own cost, the method performs \(O(1)\) work per request.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
