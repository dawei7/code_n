## General

**Model availability directly**

The directory contains exactly the numbers from `0` through `maxNumbers - 1`. At any moment, each number is in one of two states: available, meaning a future `get()` may assign it, or assigned, meaning it must not be returned again until `release(number)` is called.

The exact solution stores only the available state explicitly. Its set `available` contains every number that is currently free. A number absent from the set is currently assigned. This gives one simple invariant that explains every operation:

> `number in self.available` if and only if that directory number is available.

A hash set is a particularly good match because the interface requires the three fundamental set operations:

- remove any available element for `get()`;
- test membership for `check(number)`;
- insert an element for `release(number)`.

Python’s `set` supports each of these in expected constant time. No ordering requirement appears in the contract, so there is no need to preserve the smallest available number, the earliest released number, or the same sequence of returns shown in the example.

**Initialization establishes the invariant**

The constructor executes `set(range(maxNumbers))`. The range produces every valid directory number exactly once, and the set initially contains all of them. This matches the starting state: no number has been assigned yet, so every slot is available.

It is useful to distinguish the one-time construction cost from the per-operation cost. Creating all `maxNumbers` set entries necessarily takes linear time and space. After that initialization, individual method calls do not scan all possible numbers.

**Getting a number**

The `get()` method first checks `if not self.available`. An empty set means no valid number satisfies the availability invariant: every number has already been assigned. The only legal response is then `-1`.

If the set is nonempty, `self.available.pop()` removes and returns one arbitrary member. Removing the number before returning it is essential. Once the caller receives that number, it is assigned, so a later `get()` must not return it again unless it has first been released. Set removal updates the representation and the real-world state in one operation.

The word “arbitrary” is intentional. A Python set is not an ordered collection, and `pop()` does not promise the numerically smallest member. This is fully compatible with the method contract, which asks for a number that is not assigned to anyone. For a fresh directory of size three, the example happens to describe returns `0`, then `1`, then `2`, but another legal execution could return those three values in a different order. What matters is that every returned value was available immediately before the call and becomes unavailable immediately afterward.

**Checking a number**

The method `check(number)` returns `number in self.available`. By the invariant, membership means available and non-membership means assigned, exactly matching the required Boolean answer.

The input constraints guarantee `0 <= number < maxNumbers`, so the method does not need a separate bounds check. It also does not mutate the set. Asking whether a number is free must not reserve it; a later `get()` may still return that number.

This difference between observation and assignment is important. `check(2)` can return `True`, but that result does not promise that `2` remains free forever. Another `get()` can assign it afterward. Within the sequential call model used by the problem, each operation observes the state left by all preceding operations.

**Releasing a number**

The method `release(number)` performs `self.available.add(number)`. If the number is currently assigned, it is absent from the set, so insertion makes it available again. If it is already available, adding the same value has no effect because sets never contain duplicate members.

That idempotence is exactly what this interface needs. Releasing an already-free number must not create multiple copies that could later be handed out more than once. A queue without an accompanying membership record could make that mistake by enqueuing the same number repeatedly. The set prevents it structurally: there is at most one occurrence of each phone number.

The method returns `None`, as required for a mutating operation with no result. Its important output is the changed directory state, not a returned value.

**Following a complete state transition**

Suppose `maxNumbers = 3`. Initially, the abstract set is `{0, 1, 2}`.

1. A first `get()` removes some member, say `0`, and returns it. The set becomes `{1, 2}`.
2. A second `get()` may remove `1`, leaving `{2}`.
3. `check(2)` tests membership and returns `True`; the set is unchanged.
4. A third `get()` removes `2`, leaving the empty set.
5. `check(2)` now returns `False` because `2` is absent.
6. `release(2)` inserts `2`, so the set becomes `{2}`.
7. `check(2)` returns `True` again.

If `get()` had chosen a different free value at either early step, the specific intermediate sets would differ, but every response would still satisfy the contract. The data structure represents availability, not a prescribed allocation policy.

**Why the design remains correct after any operation sequence**

Correctness follows by preserving the set invariant.

The constructor establishes it because all legal numbers begin available and all are inserted. Assume it holds before an operation.

- For `get()` on an empty set, no number is available, so `-1` is correct and the unchanged set keeps the invariant true.
- For `get()` on a nonempty set, `pop()` chooses a member, which the invariant says is free. Returning it is legal. Removing it makes the representation say assigned, matching its new state. All other memberships remain correct.
- For `check(number)`, the membership test returns the state asserted by the invariant and changes nothing.
- For `release(number)`, set insertion makes that number a member and hence available. If it was already a member, both the actual state and representation remain available. Other numbers are unaffected.

Therefore the invariant holds after every possible method call. By induction over the operation sequence, no assigned number is returned twice without an intervening release, every check is accurate, a released number becomes reusable, and `-1` is returned exactly when the directory is exhausted.

## Complexity detail

Let $M$ be `maxNumbers`.

Constructing `range(maxNumbers)` and inserting its $M$ values into the set takes $O(M)$ expected time. The set can contain at most all $M$ directory numbers, so the total auxiliary space is $O(M)$.

After construction, `get()` performs an emptiness test and, when possible, one set `pop`; `check()` performs one membership test; and `release()` performs one set insertion. Each method therefore takes $O(1)$ expected time. “Expected” is the precise qualification for a hash table: pathological hash collisions can degrade theoretical worst-case performance, but Python integers have stable, well-distributed hashes for this bounded use, and the standard complexity model treats these operations as constant time.

The amount of storage changes with availability, but its asymptotic maximum remains $O(M)$. When every number is assigned, the set is empty; when every number is free, it has $M$ entries. The solution does not allocate memory proportional to the number of method calls, so repeated release/get cycles do not make storage grow beyond the directory’s fixed capacity.

## Alternatives and edge cases

- **Boolean array with a linear `get`:** Store one availability flag per number and scan from the beginning for a free slot. `check` and `release` are constant time, but a single `get` can take $O(M)$ time, especially when few slots remain. The hash set avoids that scan.

- **Queue plus Boolean array:** Keep all free numbers in a queue for constant-time removal and use a Boolean array to make checks constant time and prevent duplicate releases. This also gives $O(1)$ operations and $O(M)$ space, but maintains two synchronized structures. The set expresses both membership and arbitrary removal in one structure.

- **Linked free list inside an array:** The available numbers can be chained through array entries, with a separate Boolean state for constant-time checks. This offers deterministic constant-time operations but is more intricate and easier to corrupt during repeated releases.

- **Ordered set or heap:** These structures could always return the smallest available number, but that guarantee is not requested. Their insertion and removal costs are generally $O(\log M)$, paying for order that the interface does not use.

- **Directory of size one:** The set begins as `{0}`. The first `get()` returns `0`, subsequent calls return `-1` until `release(0)`, and then `0` is available again. No special case is required.

- **Calling `get()` when exhausted:** The explicit emptiness test is required because calling `pop()` on an empty Python set would raise an exception. The contract instead requires the sentinel `-1`.

- **Repeated release:** `release(number)` may be called when the number is already available. `set.add` is idempotent, so this never creates a duplicate allocation opportunity and needs no preliminary membership branch.

- **Repeated check:** Any number of `check` calls are harmless because membership testing does not alter availability.

- **Valid-number guarantee:** All method arguments satisfy `0 <= number < maxNumbers`. If an external API allowed invalid values, `release` would need validation to prevent inserting an out-of-range number; the exact solution correctly relies on the stated contract.

- **Concurrency:** The challenge applies operations sequentially. In a genuinely concurrent service, `check`, `get`, and `release` would need synchronization, and a `check` result could become stale immediately. Thread safety is outside this problem’s contract and is not supplied by the class.
