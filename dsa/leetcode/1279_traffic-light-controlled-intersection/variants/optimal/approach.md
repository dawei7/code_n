## General
**Make the light state and the crossing one critical section**

Store the identifier of the road whose light is currently green, initialized to Road A. Protect both that state and the complete crossing operation with one mutual-exclusion lock. This is deliberately conservative: even cars on the same road cross one at a time, which is permitted and makes the safety boundary explicit.

When a car arrives, acquire the lock before examining the green-road state. If the car belongs to the other road, invoke `turnGreen` and update the stored road. Then invoke `crossCar` while still holding the lock and release the lock afterward. A context-managed lock ensures release even if a callback raises.

**Why this orders every observable action correctly**

Acquiring the lock is the linearization point for an arrival. Because only the lock holder can inspect or change `green_road`, two calls cannot both decide that the same road transition is needed. When a switch is necessary, `turnGreen` occurs before the stored state changes and before `crossCar`; without a switch, the stored state proves the road is already green. Holding the same lock through `crossCar` prevents another call from changing the light or starting a crossing on the other road before the callback finishes.

Each invocation reaches exactly one `crossCar` call after acquiring the lock, so every completed arrival crosses exactly once. Every holder performs only finite callback work and releases the one lock without acquiring another resource. There is therefore no circular wait; with the judge's finite set of scheduled calls, every invocation can complete.

## Complexity detail
Let $C$ be the number of car-arrival calls. Each arrival performs one lock acquisition, one road comparison, at most one light callback, and one crossing callback, all $O(1)$ controller work with $O(1)$ stored state. Under contention, one call may wait behind as many as $C-1$ other cars, so its wall-clock completion latency can be $O(C)$ even though its own executed work is constant.

The source contract fixes the workload at no more than $20$ concurrent calls. Correctness depends on mutual exclusion, callback semantics, and progress rather than asymptotic runtime, so the package uses a bounded-concurrency certificate with scheduler and deadlock regression.

## Alternatives and edge cases
- **Separate light and crossing locks:** Releasing one before acquiring the other creates a window in which the light can change while a car is crossing.
- **Check the road outside the lock:** Concurrent cars can observe stale state and redundantly call `turnGreen`.
- **Allow same-road cars to overlap:** More concurrency is possible, but it requires tracking active crossings and preventing a road switch until all of them finish. The single-lock solution satisfies the contract with much less state.
- **Busy waiting on a shared flag:** It wastes CPU and still needs synchronization for visibility and atomicity.
- **First car on Road B:** It must switch the initially green Road A light before crossing.
- **Consecutive cars on one road:** Only the first after a road change calls `turnGreen`; later cars cross under the existing green light.
- **Simultaneous arrivals:** Their precise order may vary, but each car must cross exactly once without different roads occupying the intersection together.
- **Unused identifiers:** `carId` and `direction` identify the judge's callback effects; the controller needs only `roadId` to choose the light.
