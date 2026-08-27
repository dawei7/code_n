# Guided Example: Traffic Light Controlled Intersection

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"cars": [11, 12, 13], "directions": [1, 2, 1], "arrival_times": [0, 1, 2]}`
- **Required output:** `{"cars": [11, 12, 13]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2. Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4.

The objective is to compute `{"cars": [11, 12, 13]}` from `{"cars": [11, 12, 13], "directions": [1, 2, 1], "arrival_times": [0, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Protect the entire intersection state with one lock

Several threads may call `carArrived` concurrently. Two shared facts must remain consistent: which road currently has the green light, and whether a car is currently crossing. The exact solution uses one `Lock` to serialize the complete sequence of checking the light, possibly changing it, and crossing.

The constructor initializes `road = 1` because Road A is green initially. It also creates `lock` once for the intersection. Every car shares these same fields through the same `TrafficLight` object.

At arrival, a thread calls `lock.acquire()` before reading or changing `road`. If another car holds the lock, the arriving thread waits. Therefore no two calls can execute the protected crossing protocol simultaneously.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"cars": [11, 12, 13], "directions": [1, 2, 1], "arrival_times": [0, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Change the light only when necessary

Inside the critical section, the code compares `road` with the arriving `roadId`. If they are equal, the correct road is already green, so calling `turnGreen()` would be forbidden and is skipped.

If they differ, the code first records `road = roadId` and then calls `turnGreen()`. Because the lock excludes every other call, no thread can observe or modify the road between this state update and the callback. After it returns, the arriving road is green and the other road is red.

The `direction` and `carId` parameters do not affect synchronization. Both directions on one road share the same light, and a car's identifier is only descriptive. The road identifier contains exactly the information needed to decide whether a light change is required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Inside the critical section, the code compares `road` with t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep the lock while the car crosses

The call to `crossCar()` occurs before releasing the lock. This is essential. If the lock were released immediately after switching the light, a car from the other road could acquire it, reverse the light, and begin crossing while the first car was still in the intersection.

Holding the lock makes the implementation stricter than the minimum requirement: even two cars on the same road cross one at a time. That sacrifices possible same-road concurrency but gives a simple safety proof and still satisfies the problem.

After `crossCar()` finishes, `lock.release()` lets one waiting arrival proceed. A single lock is acquired once and released once; there is no cycle of threads each holding one resource while waiting for another, so the design introduces no lock-order deadlock.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"cars": [11, 12, 13]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"cars": [11, 12, 13], "directions": [1, 2, 1], "arrival_times": [0, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"cars": [11, 12, 13]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Release before `crossCar()`:** This is unsafe :** - **Release before `crossCar()`:** This is unsafe because another road may turn green while the current car is still crossing.
- **Separate lock per road:** That can allow cars from different roads into the intersection simultaneously unless another shared intersection lock coordinates them.
- **Condition variables:** They can support more elaborate scheduling or batches of same-road cars, but a single mutex is sufficient for correctness.
- **Context-manager locking:** `with lock:` guarantees release if a callback raises and is safer general Python style while preserving the same algorithm.
- **Several consecutive cars on one road:** Only the first after a road change calls `turnGreen()`; all cross under the retained green state.
- **Alternating roads:** Each acquisition may switch the light once, but never redundantly.
- **Simultaneous arrivals:** Lock acquisition selects a serial order; any such order is accepted if safety and completion hold.
- **Same-road concurrency:** The exact method disallows it even though the rules would permit it, choosing simplicity over maximum throughput.
- **Unused direction:** Directions one and two share Road A, while three and four share Road B, so `roadId` is sufficient.
- **Callback exception:** Outside the judge's normal contract, an exception can prevent explicit release; `try/finally` would harden the implementation.
- **Fairness:** Python's basic lock does not promise strict arrival-order fairness, but with finite judge calls and ordinary scheduling the method provides the required deadlock-free progression.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Ignoring time spent waiting for other cars and the judge callback durations, each invocation performs a constant number of field accesses, comparisons, assignments, lock operations, and at most two callbacks. Its own protocol work is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
