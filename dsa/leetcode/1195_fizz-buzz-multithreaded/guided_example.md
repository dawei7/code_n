# Guided Example: Fizz Buzz Multithreaded

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "threads": ["fizz", "buzz", "fizzbuzz", "number"]}`
- **Required output:** `[1, 2, "fizz", 4, "buzz"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have the four functions:

The objective is to compute `[1, 2, "fizz", 4, "buzz"]` from `{"n": 5, "threads": ["fizz", "buzz", "fizzbuzz", "number"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Express each thread’s ownership as a predicate

All four public methods call the same helper, `_run`, with a predicate and an action.

The fizz predicate accepts values divisible by three but not five. The buzz predicate accepts values divisible by five but not three. The fizzbuzz predicate accepts values divisible by 15. The number predicate accepts values divisible by neither three nor five.

These categories are mutually exclusive: one value cannot satisfy two predicates. They are also exhaustive: every positive integer belongs to exactly one. This partition is the foundation for safe coordination because at every `current <= n`, exactly one worker is eligible.

The string-output wrappers adapt callback signatures. `_run` supplies the current integer to every action. Fizz, buzz, and fizzbuzz use lambdas that ignore that argument and call their zero-argument print functions. The number thread passes `printNumber` directly because that callback needs the integer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "threads": ["fizz", "buzz", "fizzbuzz", "number"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Wait in a loop until this thread owns the current value

Each worker acquires the condition lock and enters an outer loop while work remains. If its predicate is false for `current`, it executes:

`while current <= n and not predicate(current): condition.wait()`.

The inner test is a `while`, not an `if`. A waiting thread can wake because another value was printed even though the new value belongs to a different thread. Condition waits can also wake spuriously. In either case, rechecking under the lock prevents the wrong callback from running.

Waiting releases the condition lock. Therefore, an ineligible thread does not prevent the one eligible worker from acquiring the lock and making progress.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Print and advance as one protected transition

Once the predicate is true, the worker still holds the condition lock. It calls `action(current)`, increments `current` by one, and calls `notify_all()`.

Holding the lock through the callback and increment gives the operation a clear order. No second worker can inspect the same current value between deciding ownership and advancing it. The callback for value `i` completes before `current` becomes `i + 1`, so output tokens remain in numerical sequence.

Waking every worker is simple and safe. At most one predicate matches the new value; all other awakened workers return to waiting. With exactly four threads, this constant amount of extra wake-up work does not change linear complexity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, "fizz", 4, "buzz"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "threads": ["fizz", "buzz", "fizzbuzz", "number"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, "fizz", 4, "buzz"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four semaphores with explicit handoff:** The current worker could release the semaphore for the next category. This can avoid waking all threads but requires routing logic after every integer and careful termination signaling.
- **Busy-wait on a shared counter:** Repeated predicate checks waste CPU and require additional memory-visibility synchronization. A condition variable provides blocking waits.
- **One worker prints everything:** It would be simpler but violates the required four-method, four-thread interface.
- **Use `if` around `wait`:** This is unsafe because notifications are not promises that the awakened thread’s predicate is now true, and spurious wakeups are permitted. The condition must be rechecked in a loop.
- **`n = 1`:** The number thread prints one, advances to two, and wakes every other worker so all methods terminate.
- **Multiples of 15:** The fizz and buzz predicates explicitly exclude the other divisor, leaving `fizzbuzz` as the sole eligible worker.
- **Scheduler starts threads in any order:** Ineligible starters wait and release the lock. Eventually the worker matching `current` can run.
- **Final notification:** After processing `n`, waking all waiters lets them observe `current > n` and return instead of sleeping forever.
- **Callback executed under the lock:** This preserves token order and single ownership. It assumes callbacks are short and do not recursively require the same coordination object.
- **Spurious wakeup:** The nested predicate loop simply sends the thread back to sleep without producing an incorrect token.
- **Progress assumption:** As with ordinary condition-variable algorithms, a runnable eligible thread must eventually be scheduled. The code introduces no circular lock dependency.
- **No output buffering in the class:** The provided callbacks own printing or capture. The class coordinates when to invoke them and does not accumulate the sequence itself.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For each integer from one through $n$, the solution runs one output callback, increments one shared counter, and performs one notification. `notify_all` can wake the other three fixed workers, each of which performs a constant predicate check and may wait again. Because the thread count is fixed at four, total synchronization work is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
