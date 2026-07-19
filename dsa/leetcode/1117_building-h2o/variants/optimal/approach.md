## General
**Reserve exactly one molecule's atom permits:** Initialize a hydrogen semaphore with two permits and an oxygen semaphore with one. A thread acquires its element's permit before joining a molecule, so no generation can contain a third hydrogen or second oxygen.

**Wait for a complete three-party group:** After acquiring a permit, every thread waits at one reusable barrier with three parties. No callback runs until two hydrogen threads and one oxygen thread have all arrived, because those are the only threads able to hold the three available permits.

**Release permits only after bonding:** Once the barrier opens, each thread invokes its callback and then releases its permit. A later generation cannot acquire all two hydrogen permits and the oxygen permit until all three callbacks from the current generation have returned. Therefore no next-generation barrier can open early. Each emitted block is a complete `HHO` multiset, and generations cannot overlap.

## Complexity detail
For $m$ molecules, $3m$ threads each perform constant semaphore, barrier, and callback work, giving $O(m)$ total work. The fixed semaphores and one three-party reusable barrier use $O(1)$ shared state. Blocking duration depends on arrivals but adds no polling iterations.

## Alternatives and edge cases
- **Condition variable with waiting counts:** It can admit two hydrogens and one oxygen per generation but requires careful generation state and wake-up predicates.
- **Semaphores without a barrier:** Capacity alone limits simultaneous element counts but may let callbacks run before a complete molecule has arrived.
- **Barrier without element permits:** Any three threads could pass, including three hydrogens, violating the required ratio.
- **Release permits before callbacks finish:** That can allow the next molecule to begin bonding before the current one completes.
- **Oxygen arrives first:** It holds the oxygen permit and waits at the barrier until two hydrogens arrive.
- **Many hydrogens arrive first:** Only two reach the barrier; all others block on the hydrogen semaphore.
- **Internal output order:** `HHO`, `HOH`, and `OHH` are equally valid for one molecule.
