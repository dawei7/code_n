## General

**Protect the entire intersection state with one lock**

Several threads may call `carArrived` concurrently. Two shared facts must remain consistent: which road currently has the green light, and whether a car is currently crossing. The exact solution uses one `Lock` to serialize the complete sequence of checking the light, possibly changing it, and crossing.

The constructor initializes `self.road = 1` because Road A is green initially. It also creates `self.lock` once for the intersection. Every car shares these same fields through the same `TrafficLight` object.

At arrival, a thread calls `self.lock.acquire()` before reading or changing `self.road`. If another car holds the lock, the arriving thread waits. Therefore no two calls can execute the protected crossing protocol simultaneously.

**Change the light only when necessary**

Inside the critical section, the code compares `self.road` with the arriving `roadId`. If they are equal, the correct road is already green, so calling `turnGreen()` would be forbidden and is skipped.

If they differ, the code first records `self.road = roadId` and then calls `turnGreen()`. Because the lock excludes every other call, no thread can observe or modify the road between this state update and the callback. After it returns, the arriving road is green and the other road is red.

The `direction` and `carId` parameters do not affect synchronization. Both directions on one road share the same light, and a car's identifier is only descriptive. The road identifier contains exactly the information needed to decide whether a light change is required.

**Keep the lock while the car crosses**

The call to `crossCar()` occurs before releasing the lock. This is essential. If the lock were released immediately after switching the light, a car from the other road could acquire it, reverse the light, and begin crossing while the first car was still in the intersection.

Holding the lock makes the implementation stricter than the minimum requirement: even two cars on the same road cross one at a time. That sacrifices possible same-road concurrency but gives a simple safety proof and still satisfies the problem.

After `crossCar()` finishes, `self.lock.release()` lets one waiting arrival proceed. A single lock is acquired once and released once; there is no cycle of threads each holding one resource while waiting for another, so the design introduces no lock-order deadlock.

**Why redundant light changes cannot occur**

All accesses to `self.road` happen while holding the same lock. Suppose one Road B car sees Road A green. It changes `self.road` to two and invokes `turnGreen()`. A second Road B thread cannot check the field until the first releases the lock; it then sees two and crosses without calling `turnGreen()`. Thus simultaneous arrivals cannot cause duplicate callbacks.

Likewise, if Road A, then Road B, then Road A cars acquire the lock in that order, each change occurs only when the requested road differs from the last recorded green road. The stored field remains synchronized with callback history.

**Safety and progress reasoning**

While a car executes `crossCar()`, it owns the only lock, so no other car can cross or switch lights. Therefore cars from different roads never occupy the intersection together.

Before every crossing, either the arriving road was already recorded green or the thread called `turnGreen()` while exclusively holding the lock. Every car therefore crosses under a green light.

Assuming the judge callbacks terminate and waiting threads are eventually scheduled, the lock holder always reaches `release()` and another car can proceed. Since a thread waits for only this one lock and the holder waits for no second lock, the system is deadlock-free under the problem's callback contract.

The exact source uses explicit `acquire` and `release` rather than a `with` statement or `try/finally`. Judge callbacks are expected not to raise exceptions. In general application code, an exception between those calls would leave the lock held, so structured release would be safer.

## Complexity detail

Ignoring time spent waiting for other cars and the judge callback durations, each invocation performs a constant number of field accesses, comparisons, assignments, lock operations, and at most two callbacks. Its own protocol work is $O(1)$.

Contention can make wall-clock latency depend on the number and duration of earlier crossings because the solution intentionally serializes them. That waiting does not change the $O(1)$ local algorithmic work per call.

The object stores one lock and one integer road identifier, using $O(1)$ persistent space. Each call uses only its parameters and constant local state, so auxiliary space is also $O(1)$.

## Alternatives and edge cases

- **Release before `crossCar()`:** This is unsafe because another road may turn green while the current car is still crossing.
- **Separate lock per road:** That can allow cars from different roads into the intersection simultaneously unless another shared intersection lock coordinates them.
- **Condition variables:** They can support more elaborate scheduling or batches of same-road cars, but a single mutex is sufficient for correctness.
- **Context-manager locking:** `with self.lock:` guarantees release if a callback raises and is safer general Python style while preserving the same algorithm.
- **Several consecutive cars on one road:** Only the first after a road change calls `turnGreen()`; all cross under the retained green state.
- **Alternating roads:** Each acquisition may switch the light once, but never redundantly.
- **Simultaneous arrivals:** Lock acquisition selects a serial order; any such order is accepted if safety and completion hold.
- **Same-road concurrency:** The exact method disallows it even though the rules would permit it, choosing simplicity over maximum throughput.
- **Unused direction:** Directions one and two share Road A, while three and four share Road B, so `roadId` is sufficient.
- **Callback exception:** Outside the judge's normal contract, an exception can prevent explicit release; `try/finally` would harden the implementation.
- **Fairness:** Python's basic lock does not promise strict arrival-order fairness, but with finite judge calls and ordinary scheduling the method provides the required deadlock-free progression.
