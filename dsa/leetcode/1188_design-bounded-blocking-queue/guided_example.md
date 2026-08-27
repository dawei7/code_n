# Guided Example: Design Bounded Blocking Queue

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"capacity": 2, "producer_threads": 1, "consumer_threads": 1, "operations": [["enqueue", 1], ["dequeue"], ["dequeue"], ["enqueue", 0], ["enqueue", 2], ["enqueue", 3], ["enqueue", 4], ["dequeue"], ["size"]], "blocking_checks": [{"operation_index": 2, "after_completed": [0, 1]}, {"operation_index": 6, "after_completed": [4, 5]}]}`
- **Required output:** `{"dequeued": [1, 0, 2], "final_size": 2}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement a thread-safe bounded blocking queue that has the following methods:

The objective is to compute `{"dequeued": [1, 0, 2], "final_size": 2}` from `{"capacity": 2, "producer_threads": 1, "consumer_threads": 1, "operations": [["enqueue", 1], ["dequeue"], ["dequeue"], ["enqueue", 0], ["enqueue", 2], ["enqueue", 3], ["enqueue", 4], ["dequeue"], ["size"]], "blocking_checks": [{"operation_index": 2, "after_completed": [0, 1]}, {"operation_index": 6, "after_completed": [4, 5]}]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enqueue reserves space before modifying the queue

`enqueue` first calls `s1.acquire()`. If the queue has spare capacity, this consumes one available-slot permit and the method continues. If the queue is full, `s1` has no permits and the producer blocks before it can append anything. This ordering is what protects the capacity limit.

After reserving a slot, the method calls `q.append(element)`. Appending on the right records this element after all elements that linearized earlier. Finally, `s2.release()` publishes one new available-item permit. A consumer waiting for an item may now wake.

The item semaphore is released only after the value is in the deque. Therefore, a consumer can never receive permission to remove an item that has not yet been stored.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"capacity": 2, "producer_threads": 1, "consumer_threads": 1, "operations": [["enqueue", 1], ["dequeue"], ["dequeue"], ["enqueue", 0], ["enqueue", 2], ["enqueue", 3], ["enqueue", 4], ["dequeue"], ["size"]], "blocking_checks": [{"operation_index": 2, "after_completed": [0, 1]}, {"operation_index": 6, "after_completed": [4, 5]}]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Dequeue reserves an item before removing it

`dequeue` is the mirror image. It first calls `s2.acquire()`. When the queue is empty, no item permit exists, so the consumer blocks before touching the deque. When a permit is available, the consumer has reserved one real queued item.

The method removes `q.popleft()`. Producers append on the right and consumers remove on the left, so elements leave in FIFO order according to the order in which the appends take effect. After removal, `s1.release()` announces that one storage slot is free. A producer blocked by a full queue may now wake. The removed value is returned.

The slot semaphore is released only after the item has left the deque. A producer therefore cannot treat the capacity as available too early.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dequeue` is the mirror image.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The two semaphore counts encode the queue state

At a stable point between completed calls, the number of item permits equals the queue length, and the number of slot permits equals `capacity - len(q)`. During the few instructions inside a call, a permit may be temporarily reserved by that call, but this reservation makes the system more conservative rather than unsafe.

For example, after a producer acquires a slot but before it appends, the sum of free-slot permits and stored items is temporarily below capacity. No other producer can steal that reserved slot, so the eventual append still cannot exceed the bound. Similarly, after a consumer acquires an item permit but before `popleft`, that particular item is reserved and cannot be claimed through the semaphore by another consumer.

This establishes the capacity and underflow safety properties. A producer must own a slot permit before appending, and only `capacity` such permits exist. A consumer must own an item permit before removing, and permits are published only for appended items.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"dequeued": [1, 0, 2], "final_size": 2}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"capacity": 2, "producer_threads": 1, "consumer_threads": 1, "operations": [["enqueue", 1], ["dequeue"], ["dequeue"], ["enqueue", 0], ["enqueue", 2], ["enqueue", 3], ["enqueue", 4], ["dequeue"], ["size"]], "blocking_checks": [{"operation_index": 2, "after_completed": [0, 1]}, {"operation_index": 6, "after_completed": [4, 5]}]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"dequeued": [1, 0, 2], "final_size": 2}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One mutex plus two condition variables:** Prot:** - **One mutex plus two condition variables:** Protect the deque with a lock, wait on `not_full` in enqueue, and wait on `not_empty` in dequeue. This is a standard design and makes all state predicates explicit, but requires careful use of loops around condition waits.
- **Busy waiting:** Repeatedly checking length until space or data appears wastes CPU and has poor progress behavior. Blocking synchronization primitives are the appropriate tool.
- **One semaphore only:** An item semaphore prevents underflow but not overflow; a slot semaphore prevents overflow but not underflow. The queue needs both resource counts.
- **Capacity one:** The design becomes a synchronized single-slot handoff. A second producer blocks until the stored item is removed, and an empty consumer blocks until a producer appends.
- **Consumer starts first:** `s2` begins at zero, so it waits safely. A later enqueue releases `s2` and enables the removal.
- **Producer reaches a full queue:** `s1` has zero permits, so the producer waits before append. A dequeue releases a slot only after removing an item.
- **Several producers:** Their scheduler order may vary, but each must acquire a distinct slot permit and each atomic append establishes a queue order that consumers then follow.
- **Several consumers:** Each successful item acquisition reserves one published item. No two consumers can remove the same queue entry.
- **FIFO direction:** `append` on the right combined with `popleft` on the left removes the earliest appended element first, matching the required logical queue even though the description names front and rear.
- **Final size:** Each completed enqueue adds one item and each completed dequeue removes one. After all calls finish, `len(q)` equals completed enqueues minus completed dequeues.
- **Exception safety:** In a more general production implementation, an unexpected exception between acquiring and releasing permits would require cleanup to restore semaphore counts. The judge supplies ordinary integer operations for which these deque actions are expected to complete.
- **Built-in bounded queue:** A library queue could provide the behavior directly, but the interview constraint explicitly asks for implementing the coordination rather than using that ready-made abstraction.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $c$ be the queue capacity. A completed `enqueue` or `dequeue` performs one semaphore acquisition, one deque operation, and one semaphore release. Semaphore bookkeeping and `deque.append` or `deque.popleft` are constant-time operations, so the active computational work per completed method is $O(1)$.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
