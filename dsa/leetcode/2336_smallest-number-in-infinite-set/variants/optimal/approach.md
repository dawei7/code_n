## General

**Represent only the observable part of the infinite set**

The mathematical set contains every positive integer, so it cannot literally be stored. The exact implementation uses the operation limits to replace it with a finite representation:

`SortedSet(range(1, 1001))`.

At most 1000 total calls are made to `popSmallest` and `addBack`. Even if every call is `popSmallest`, only the first 1000 positive integers can be removed and returned. Reaching 1001 would require a 1001st pop, which the contract forbids. Also, every number passed to `addBack` is at most 1000.

Therefore no legal sequence of calls can observe whether integers above 1000 were explicitly stored. Keeping 1 through 1000 is behaviorally equivalent to keeping the complete infinite set for every permitted test.

**Why a sorted set matches both required operations**

A set must contain each number at most once. A sorted set combines uniqueness with ascending order:

- inserting a value that is already present changes nothing;
- the element at index zero is the current minimum;
- removing a value makes it absent until it is added again.

The constructor fills `self.s` with every integer from one through 1000. This represents the initial state in which every observable positive integer is present.

The implementation relies on `SortedSet` from the execution environment. Unlike Python's built-in unordered `set`, it supports retrieving the smallest entry by ordered index.

**Pop the smallest present number**

`popSmallest` reads `x = self.s[0]`. Since the collection is sorted, no present value is smaller than `x`. It then calls `self.s.remove(x)`, making that number absent, and returns it.

The order of these steps matters. Reading before removal identifies the value to return, and removing before the method finishes ensures a second immediate pop cannot return the same number.

The set cannot be empty during any valid call. Emptying the initial 1000 values requires 1000 pop calls, and there would be no remaining call within the total-call limit to invoke `popSmallest` once more. Add-back calls only increase availability.

**Add a number back with idempotent insertion**

`addBack(num)` simply executes `self.s.add(num)`. If `num` was removed earlier, the insertion makes it available again in its correct sorted position. If it is already present, set semantics ignore the duplicate and the state remains unchanged.

No explicit membership condition is needed. The sorted set itself implements “if it is not already in the infinite set.”

For example, calling `addBack(2)` before any pop does nothing because 2 is already stored. After popping 1, 2, and 3, calling `addBack(1)` reinserts 1 at the beginning. The next pop returns 1, after which the following smallest values are 4 unless 2 or 3 were also restored.

**Why finite storage preserves every legal result**

Maintain the invariant that, for every integer from 1 through 1000, membership in `self.s` is exactly the same as membership in the conceptual infinite set after the same calls.

The invariant holds initially. `popSmallest` removes and returns the least stored value. All conceptual values above 1000 are larger, so they cannot precede any stored observable value. Under the call bound, at least one stored value remains whenever a pop is requested. Thus the returned and removed conceptual value is the same.

`addBack` changes membership of the supplied value only when it was absent, exactly as sorted-set insertion does. The supplied value lies within 1 through 1000, so the invariant is preserved.

By induction across calls, every returned value matches the infinite-set specification. Values above 1000 remain conceptually present but never need materialization.

**This is not the frontier-plus-heap implementation**

The manifest summary describes the common unbounded design: a frontier represents the untouched infinite suffix and a heap stores smaller restored values. The exact source instead exploits the fixed constraints with one prepopulated sorted set. Both satisfy the problem, but their state invariants and constant factors differ.

The bounded approach is simpler under this contract but would fail if the call limit were removed or increased beyond the initialized range.

## Complexity detail

Let `Q = 1000` be the maximum operation horizon and let `r` be the current sorted-set size. Indexing and removal from a balanced sorted-set structure take logarithmic time in `r`, as does insertion, so each method is `O(\log Q)`. Across at most `Q` calls, operation time is `O(Q \log Q)`, matching the manifest's aggregate form.

The stored set contains at most `Q` integers, giving `O(Q)` space. Construction also creates those `Q` entries. Because `Q` is fixed at 1000 by the source constraints, these bounds can be viewed as constant for this particular problem domain, but parameterizing by the operation limit describes the data structure honestly.

No caller input collection is mutated. The object intentionally mutates its internal set across method calls because maintaining state is the class's purpose.

## Alternatives and edge cases

- **Frontier plus min-heap and membership set:** Store the next never-popped positive integer and only restored smaller values. This represents a truly unbounded set and uses space proportional to add-backs, but needs two structures to deduplicate heap entries.
- **Frontier plus ordered set:** An ordered set of restored values removes the separate heap-membership set while retaining a truly infinite suffix frontier.
- **Built-in unordered set of 1 through 1000:** Membership is easy, but finding the minimum would require `O(Q)` scanning per pop.
- **Boolean presence array:** With the 1000 bound, scan from one upward for every pop and mark entries. This is simple but can make repeated minimum searches quadratic unless a frontier and restored-value handling are added.
- **Adding back a present number:** `SortedSet.add` is idempotent, so no duplicate appears and later pops remain correct.
- **Adding back a removed number:** It reenters at its numeric sorted position and may become the next minimum.
- **Adding back the same removed number repeatedly:** Only the first insertion changes the set.
- **Popping after an add-back below the current minimum:** The restored smaller number is at index zero and is returned first.
- **Popping without any add-backs:** Results are 1, 2, 3, and so on through the observable horizon.
- **Maximum legal number 1000:** It is initially stored and can be restored after removal.
- **Why 1001 is unnecessary:** Returning it would require more than 1000 pop calls, even if no values are ever restored.
- **Empty-set indexing:** A valid call sequence cannot request the 1001st removal within the total 1000-call cap.
- **Constraint dependence:** If total calls could exceed 1000, the finite initialization would no longer faithfully represent infinity.
- **External type availability:** The exact implementation requires `SortedSet` to be supplied or imported from its supporting library.
