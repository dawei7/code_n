# Guided Example: Event Emitter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"actions": ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], "values": [[], ["firstEvent"], ["firstEvent", {"type": "constant", "value": 5}], ["firstEvent", {"type": "constant", "value": 6}], ["firstEvent"]]}`
- **Required output:** `[[], ["emitted", []], ["subscribed"], ["subscribed"], ["emitted", [5, 6]]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design an `EventEmitter` class. This interface is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The `EventEmitter` should allow for subscribing to events and emitting them.

The objective is to compute `[[], ["emitted", []], ["subscribed"], ["subscribed"], ["emitted", [5, 6]]]` from `{"actions": ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], "values": [[], ["firstEvent"], ["firstEvent", {"type": "constant", "value": 5}], ["firstEvent", {"type": "constant", "value": 6}], ["firstEvent"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map each event name to an ordered listener list

`EventEmitter` stores `this.events` as a `Map`. Each key is an event-name string, and its value is an array of callbacks in subscription order.

A Map cleanly separates event names and avoids special object-property names such as `constructor` or `__proto__`.

Arrays are used because order matters: emission must call listeners in exactly the sequence in which they subscribed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"actions": ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], "values": [[], ["firstEvent"], ["firstEvent", {"type": "constant", "value": 5}], ["firstEvent", {"type": "constant", "value": 6}], ["firstEvent"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Subscribe by appending

When `subscribe(eventName, callback)` sees a new event, it first stores an empty array for that name.

It obtains the array, pushes the callback at the end, and captures that exact `listeners` array inside the returned unsubscribe closure.

Appending preserves chronological registration order. The contract guarantees callbacks supplied to subscriptions are not referentially identical, which makes later identity lookup unambiguous.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Return a subscription handle

The method returns an object with one `unsubscribe` arrow function.

The closure retains:

- the callback to remove;
- the event name;
- the listener array in which it was registered;
- Boolean `active`, initially true;
- lexical access to the emitter through the arrow function's `this`.

The caller does not need to pass the event or callback again. The returned handle identifies one particular subscription.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[], ["emitted", []], ["subscribed"], ["subscribed"], ["emitted", [5, 6]]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"actions": ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], "values": [[], ["firstEvent"], ["firstEvent", {"type": "constant", "value": 5}], ["firstEvent", {"type": "constant", "value": 6}], ["firstEvent"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[], ["emitted", []], ["subscribed"], ["subscribed"], ["emitted", [5, 6]]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Set per event:** Offers expected constant-time deletion, but array order and snapshot semantics are more explicit here.
- **Linked list per event:** Can support constant-time removal with stored nodes, but emission and implementation become more complex.
- **Map callback to index:** Splicing shifts indices, so maintaining them correctly adds bookkeeping.
- **No listeners:** Returns a fresh empty array.
- **Several listeners:** Invoked and reported in subscription order.
- **Repeated unsubscribe:** The `active` flag makes later calls harmless.
- **Last listener removed:** The event key is deleted from the Map.
- **Optional argument array omitted:** Each callback receives zero arguments.
- **Callback returns undefined:** That undefined value occupies its position in the result array.
- **Callback throws:** The exact synchronous `map` stops and propagates the exception.
- **Subscribe during emit:** New listener is absent from the current snapshot and appears next time.
- **Unsubscribe during emit:** Current snapshot remains stable; future emissions use the updated live list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1 + k(a + 1))$. Let $k$ be the number of listeners for the relevant event and $a$ the number of emitted arguments. Subscription is amortized $O(1)$. Unsubscription uses `indexOf` and `splice`, so it is $O(k)$ in the worst case.
- **Auxiliary Space Complexity:** $O(s + k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
