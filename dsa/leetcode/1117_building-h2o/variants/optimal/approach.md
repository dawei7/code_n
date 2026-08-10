## General

**The intended permit budget for one molecule**

One water molecule needs exactly two hydrogen callbacks and one oxygen callback. The protected implementation starts `h` with two permits and `o` with zero.

At the intended high level, two hydrogen threads consume the two hydrogen permits. Once both have printed, one oxygen permit should be released. Oxygen consumes it, prints, and releases two new hydrogen permits for the next molecule.

This creates molecule-sized rounds without explicitly assigning thread identities to a molecule.

**Hydrogen’s intended role**

Each hydrogen call acquires one `h` permit before invoking `releaseHydrogen`. Since only two permits exist at the beginning of a round, a third hydrogen thread cannot pass until oxygen finishes the round and replenishes them.

After printing, the code checks `self.h._value == 0`. The intention is that the hydrogen which observes both permits consumed is the second hydrogen and should release one oxygen permit.

**Oxygen’s intended role**

Oxygen waits on `self.o.acquire()`. With an initial count of zero, it cannot print before some hydrogen call releases permission.

After oxygen prints, `self.h.release(2)` restores two hydrogen permits. The next pair can then proceed. If exactly one oxygen permit were created per pair, the logical output would divide into groups containing two H values and one O value.

**Why the private-value check is not a safe handoff**

The exact code does not atomically combine “I am the second hydrogen” with the oxygen release. `Semaphore._value` is a private implementation field, and reading it after the callback is separate from the earlier acquire.

Consider this legal schedule:

1. Hydrogen H1 acquires the first permit, leaving one.
2. Hydrogen H2 acquires the second permit, leaving zero.
3. H1 finishes its callback, reads zero, and releases oxygen.
4. H2 finishes its callback, also reads zero, and releases oxygen again.

Both hydrogens can observe the same zero state because releasing oxygen does not change `h._value`. The oxygen semaphore then has two permits for one hydrogen pair.

Two oxygen threads may consequently pass. Each releases two hydrogen permits, allowing later groups to contain the wrong proportions. This violates the requirement that every three emitted callbacks contain exactly two hydrogen values and one oxygen value.

**The intended invariant versus the proven behavior**

The intended invariant is that zero hydrogen permits cause exactly one oxygen permit. The code proves only that no more than two hydrogens consume the initial permits before an oxygen replenishment under ordinary circumstances; it does not prove uniqueness of the oxygen release.

Because correctness must hold for every scheduler interleaving, a solution that usually works under one timing is insufficient. The local protected implementation therefore has a concurrency race despite matching the intended permit sketch.

**How to make the handoff reliable**

A correct design must make completion of the second hydrogen an unambiguous, atomic event. Options include a reusable barrier for three participants, a hydrogen completion counter protected by a mutex, or an additional semaphore chain where only one designated step can release oxygen.

The fix must also ensure the three callbacks of one molecule complete before permits for the next molecule are released. Oxygen should replenish hydrogen only after its own callback returns, as the current placement intends.

This approach document describes the exact source and its limitation; it does not alter the protected solution.

## Complexity detail

Let $m$ be the total number of atom threads, equal to three times the molecule count. Each call performs a constant number of intended semaphore operations and one callback, so the algorithmic target is $O(m)$ time with constant work per atom.

The two semaphores and fixed scalar state use $O(1)$ space. Threads and output storage belong to the execution environment.

The repository’s semantic validator requires complete three-callback groups with two H and one O. Complexity does not rescue the race: an $O(m)$ implementation must still satisfy safety and progress for every interleaving.

## Alternatives and edge cases

- **Reusable barrier:** Admit exactly two hydrogen threads and one oxygen thread, then release the group together. This directly models molecule formation.
- **Mutex-protected counter:** Update hydrogen completion count under a lock and let exactly the transition from one to two release oxygen. Reset only after oxygen completes.
- **Semaphore choreography without private fields:** Use explicit permits whose acquire/release operations encode which hydrogen is first and which is second.
- **Private `_value` access:** It is unsupported API and, more importantly, its observation is not atomic with the earlier acquire.
- **Two hydrogens acquire before checking:** Both may release oxygen, demonstrating the protected race.
- **Oxygen arrives first:** It blocks on zero permits, which is intended.
- **Many hydrogens arrive first:** At most two initially acquire, but the duplicate oxygen-release race can corrupt later permit counts.
- **One molecule:** The problematic interleaving can already create an extra oxygen permit even at the smallest domain.
- **Callback order within a molecule:** Any of HHO, HOH, or OHH is allowed if grouping is correct.
- **Cross-molecule mixing:** No callback from the next molecule may complete before the current three bond; replenishment timing must enforce this.
- **Callback exception:** Failure before a release can block progress; normal callback completion is assumed.
- **Complexity target:** A corrected method should retain constant work per atom and $O(1)$ coordination state.
