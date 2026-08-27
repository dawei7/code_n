# Guided Example: Maximum Candies You Can Get from Boxes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"status": [1, 0, 1, 0], "candies": [7, 5, 4, 100], "keys": [[], [], [1], []], "containedBoxes": [[1, 2], [3], [], []], "initialBoxes": [0]}`
- **Required output:** `16`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n` boxes labeled from `0` to $n - 1$. You are given four arrays: `status`, `candies`, `keys`, and `containedBoxes` where:

The objective is to compute `16` from `{"status": [1, 0, 1, 0], "candies": [7, 5, 4, 100], "keys": [[], [], [1], []], "containedBoxes": [[1, 2], [3], [], []], "initialBoxes": [0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The three pieces of state

`has` is initialized as `set(initialBoxes)`. Membership in `has` means that the box is physically available. Finding a key does not put a box in this set; a key can open a box only after that box has also been obtained.

`status` tells whether each box can currently be opened. Initially, its zeros and ones come from the input. When a key for box `k` is discovered, the exact code changes `status[k]` to one. Mutating the array turns it into the current “can open” state rather than merely the initial state.

`took` contains boxes that have already been scheduled for processing and whose candies have already been added. Its name is broader than “removed from the queue”: a box enters `took` at enqueue time. This choice guarantees that two different discoveries cannot enqueue and count the same box twice.

The key readiness condition is therefore:

`box in has`, `status[box] == 1`, and `box not in took`.

Whenever all three become true, the box is enqueued, marked in `took`, and its candy value is added to `ans`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"status": [1, 0, 1, 0], "candies": [7, 5, 4, 100], "keys": [[], [], [1], []], "containedBoxes": [[1, 2], [3], [], []], "initialBoxes": [0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initializing boxes that are immediately usable

The code examines every label in `initialBoxes`. An initially owned box whose `status` is one can be opened immediately, so it is placed in the queue, added to `took`, and its candies are counted.

An initially owned but closed box remains only in `has`. It is not lost. If a key is discovered later, the key-processing branch notices that the box is already owned and schedules it then.

Counting candies when a box is enqueued, instead of when it is dequeued, is safe because only owned, open, untaken boxes enter the queue. Once enqueued, nothing can revoke ownership or close the box. The queue will eventually remove it, so those candies are guaranteed to be obtainable.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code examines every label in `initialBoxes`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Processing keys found in an opened box

When `box = q.popleft()`, the current box is being opened and its contents become available. The first inner loop visits `keys[box]`.

For a discovered key label `k`, the code checks `if not status[k]` before changing it to one. If the box was already open or an earlier key had already opened it, no state transition occurs and no duplicate scheduling is attempted through this branch.

When a newly useful key opens box `k`, the code next checks whether `k` is already in `has` and not in `took`. If so, both readiness requirements have just become true. The box is enqueued, marked, and counted. If we do not possess it yet, its open status remains recorded. Finding the physical box later will trigger the other branch.

The same key label may appear in key lists of different boxes. The first useful discovery sets `status[k]` to one. Later copies see that it is already one and do nothing, so repeated keys cannot duplicate candies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `16` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"status": [1, 0, 1, 0], "candies": [7, 5, 4, 100], "keys": [[], [], [1], []], "containedBoxes": [[1, 2], [3], [], []], "initialBoxes": [0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `16` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated full scans:** One can repeatedly insp:** - **Repeated full scans:** One can repeatedly inspect all boxes until no new one becomes usable. This is easier to imagine but may rescan many unavailable boxes, while the queue reacts only to useful state changes.
- **Boolean arrays instead of sets:** Arrays such as `has_box` and `used` give worst-case constant-time access and avoid hash overhead because labels range from zero to $n-1$. They express the same state machine.
- **Recursive traversal:** Recursion can process newly ready boxes, but chains may be deep and Python's recursion limit is unnecessary risk. An explicit queue is safer.
- **Closed initial box:** It remains in `has` without entering the queue. A later key changes `status` and triggers scheduling.
- **Key found before its box:** The key sets `status` to one. When the box is later found inside another processed box, the contained-box branch schedules it.
- **Box found before its key:** The box enters `has` but stays unscheduled. A later key branch sees ownership and schedules it.
- **Key for an already open box:** The `if not status[k]` guard ignores it because it cannot create new reachability.
- **Same key found several times:** Only the first transition from closed to open is useful, so later duplicates cannot enqueue or count the target again.
- **A box reachable through several routes:** `took` is set at enqueue time, preventing duplicate queue entries and duplicate candy collection before either entry could be processed.
- **No initial boxes:** The queue is empty, no discovery can begin, and the correct answer is zero.
- **No initially open owned boxes:** The queue is likewise empty. Keys locked inside inaccessible boxes cannot help, so zero is correct.
- **All boxes become reachable:** Every one is scheduled once and the answer becomes the sum of all candy values.
- **Positive candy guarantee:** Since every box has at least one candy and opening a box has no cost, processing every reachable box is always optimal. With negative rewards or limited actions, the no-choice worklist argument would no longer be sufficient.
- **Duplicate labels in `initialBoxes` outside the intended contract:** The exact initialization loop does not check `box not in took` before enqueueing and counting. If duplicate initial labels were permitted, it could double count. A defensive version would apply the same untaken guard used elsewhere.
- **Input mutation:** Acquired keys change `status`. A caller that needs the original array afterward must pass a copy or use a separate `can_open` structure.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+S)$. Let $n$ be the number of boxes. Let
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
