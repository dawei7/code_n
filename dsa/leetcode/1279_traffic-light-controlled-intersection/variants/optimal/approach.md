## General
Store the identifier of the road whose light is currently green, initialized to Road A. Protect both that state and the complete crossing operation with one mutual-exclusion lock.

When a car arrives, acquire the lock before examining the green-road state. If the car belongs to the other road, invoke `turnGreen` and update the stored road. Then invoke `crossCar` while still holding the lock and release the lock afterward. A context-managed lock ensures release even if a callback raises.

Because only the lock holder can inspect or change the light, two calls cannot both decide to perform the same switch. Holding that same lock through `crossCar` also prevents any other road from changing the light or entering the intersection during a crossing. Every holder performs only finite callback work and releases the single lock without waiting for another resource, so cyclic waiting and deadlock cannot occur.

## Complexity detail
Each arrival performs one lock acquisition, one road comparison, at most one light callback, and one crossing callback, all $O(1)$ work with $O(1)$ stored state. A thread may wait for earlier cars, but the controller's own work per call remains constant.

The source contract fixes the workload at no more than $20$ concurrent calls. Correctness depends on mutual exclusion, callback semantics, and progress rather than asymptotic runtime, so the package uses a bounded-concurrency certificate with scheduler and deadlock regression.

## Alternatives and edge cases
- **Separate light and crossing locks:** Releasing one before acquiring the other creates a window in which the light can change while a car is crossing.
- **Check the road outside the lock:** Concurrent cars can observe stale state and redundantly call `turnGreen`.
- **Busy waiting on a shared flag:** It wastes CPU and still needs synchronization for visibility and atomicity.
- **First car on Road B:** It must switch the initially green Road A light before crossing.
- **Consecutive cars on one road:** Only the first after a road change calls `turnGreen`; later cars cross under the existing green light.
- **Simultaneous arrivals:** Their precise order may vary, but each car must cross exactly once without different roads occupying the intersection together.
