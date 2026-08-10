## General

**The extra difficulty created by duplicates**

This collection is a multiset: inserting the same integer twice creates two separate occurrences. `remove(val)` deletes only one occurrence, and `getRandom()` must sample occurrences uniformly. Thus, if the collection contains `[1, 1, 2]`, value `1` must be returned with probability $2/3$, while value `2` must be returned with probability $1/3$.

A dense list is ideal for that probability rule. If every occurrence occupies one list position, choosing a uniformly random position automatically weights a value by its number of copies. The challenge is removal. Deleting a middle list position normally shifts later entries and costs linear time.

As in the no-duplicates version, order is not part of the contract. The solution can overwrite the removed position with the last occurrence and then pop the physical last position. However, one dictionary index per value is no longer enough: a value can occupy several list positions. The exact solution therefore uses:

- `l`, a dense list containing every current occurrence;
- `m`, a dictionary mapping each distinct value to a set of all indices where that value occurs in `l`.

The representation invariant is:

> For every value `v`, `m[v]` is exactly the nonempty set of indices `i` for which `l[i] == v`. Values with no occurrences have no dictionary key.

This two-way correspondence is what makes membership, location, and occurrence-weighted sampling possible.

**Inserting an occurrence**

The method obtains the existing index set with `self.m.get(val, set())`. If `val` is absent, the default expression creates a new empty set. It then adds `len(self.l)`, the index at which the next appended item will be placed, assigns the set to `self.m[val]`, and appends `val` to the list.

After these steps, the new list position is included in the correct value’s index set. Existing positions and mappings are unchanged, so the invariant is preserved.

The return value is `len(idx_set) == 1`, evaluated after insertion. A size of one means the just-added occurrence is the only occurrence, so the value was not previously present and the method returns `True`. A larger size means at least one copy already existed, so the new copy is still inserted but the method returns `False`. This distinction is easy to miss: `False` does not mean the insertion failed; it reports that the value was already represented before this call.

**Locating one occurrence for removal**

If `val not in self.m`, the invariant says there is no matching occurrence, so the method returns `False` without changing the collection.

Otherwise, `idx_set = self.m[val]` refers to its nonempty set of positions. The exact code chooses one occurrence using `idx = list(idx_set)[0]`. Any occurrence is legal to remove, because equal copies have no separate identity exposed through the interface. It also computes `last_idx = len(self.l) - 1`, the position that can be popped without shifting anything.

There is an important implementation-level complexity detail here: constructing `list(idx_set)` copies all indices in that set. If `val` has $f$ occurrences, this exact line takes $O(f)$ time and temporary space, even though only one index is needed. The intended constant-time set operation would be to obtain or remove an arbitrary member directly, such as with `idx_set.pop()`. The remainder of the algorithm is the standard average-$O(1)$ design, but the supplied exact source’s conversion means its `remove` method is not strictly average $O(1)$ when one value has many copies. The approach must state this rather than hiding it behind the manifest’s intended bound.

**Moving the final occurrence into the gap**

After an index `idx` is chosen, the solution assigns `self.l[idx] = self.l[last_idx]`. Conceptually, the occurrence at the end moves into the position being removed. The list may temporarily contain the last value at both positions, but the final `pop()` will delete the trailing copy.

The index sets must be updated to describe that move:

1. `idx_set.remove(idx)` removes the selected occurrence’s old index from the set for `val`.
2. `last_idx_set = self.m[self.l[last_idx]]` obtains the set for the value currently at the end. The assignment to `l[idx]` does not change `l[last_idx]`, so this still identifies the moved value.
3. If `last_idx` occurs in that set, it is removed because the physical last list position is about to disappear.
4. If `idx < last_idx`, the moved value is added at `idx`, its new position.
5. If `idx_set` became empty, the key `val` is removed from the dictionary.
6. `self.l.pop()` removes the now-redundant last list entry.

The condition `idx < last_idx` distinguishes a genuine move from deleting the last position itself. If the chosen occurrence already sits at the end, there is no surviving occurrence at `idx` to add back after the pop.

**When the removed value and last value differ**

Suppose `l = [4, 7, 4, 9]`, with index sets `4 -> {0, 2}`, `7 -> {1}`, and `9 -> {3}`. If removal chooses index `0` for value `4`, the last value `9` is copied into index `0`. Index `0` leaves the set for `4`; index `3` leaves the set for `9`; and index `0` enters the set for `9`. After popping, the list is `[9, 7, 4]`, and the exact sets are `4 -> {2}`, `7 -> {1}`, and `9 -> {0}`.

Only the moved last occurrence changes position. Every other list entry stays in place, so no other set needs adjustment.

**When the removed value is also the last value**

This is the subtle case because `idx_set` and `last_idx_set` can be the same set object.

Suppose `l = [1, 2, 1]` and the chosen index for removing `1` is `0`. The set begins as `{0, 2}`. Removing `idx` leaves `{2}`. Removing `last_idx` then leaves the set empty. Because `idx < last_idx`, adding `idx` back produces `{0}`. After the list pop, `l = [1, 2]`, so `{0}` is exactly correct: the final occurrence was moved into the removed occurrence’s old slot.

If the chosen occurrence itself is at `last_idx`, removing that one index is sufficient. The subsequent membership guard sees that `last_idx` is no longer present, and the `idx < last_idx` condition is false. The list pop deletes the occurrence, and an empty set causes the dictionary key to be removed.

These conditions prevent both stale final indices and accidental loss of a duplicate.

**Random selection has the required weighted probability**

`getRandom()` returns `random.choice(self.l)` when the list is nonempty. If there are $n$ total occurrences, each index has probability $1/n$. A value appearing $f$ times owns $f$ different indices, so its total probability is

$$
\frac{f}{n}.
$$

That is exactly the required linear relationship with multiplicity. The list must contain duplicate entries physically; storing only distinct dictionary keys would make all distinct values equally likely and would violate the contract.

The problem guarantees that `getRandom()` is called only when the collection contains at least one item. Even so, the exact implementation includes an empty guard and returns `-1` if the list is empty. That fallback is outside the guaranteed call path and does not affect valid executions. It should not be confused with a stored value, because `-1` is itself a legal collection value; callers should rely on the nonempty-call guarantee rather than treat `-1` as a universally distinguishable sentinel.

**Why the representation remains correct**

Both structures start empty, satisfying the invariant. Insertion creates one list occurrence and adds exactly its position to the corresponding set. A failed removal changes nothing. During successful removal, the chosen occurrence’s index is deleted, the last occurrence’s old index is deleted, and its new index is added exactly when it survives at a different position. Empty keys are removed. No other positions move. Random selection is read-only.

Therefore every current occurrence is always represented by one list slot and one matching set index, and no stale index remains. This proves correct multiplicities, correct insert/remove results, and correct sampling weights across any valid sequence of operations.

## Complexity detail

Let $n$ be the total number of stored occurrences, and let $f$ be the number of occurrences of the particular value passed to `remove`.

Insertion performs expected-$O(1)$ dictionary and set operations plus an amortized-$O(1)$ list append, so it takes $O(1)$ expected amortized time. `getRandom` chooses one list position in $O(1)$ time.

The intended hash-map-plus-index-sets removal design is expected $O(1)$, and all structural updates after choosing an index have that cost. In the exact solution, however, `list(idx_set)` copies $f$ indices before selecting the first one. Consequently, exact removal time is $O(f)$ and uses $O(f)$ temporary space in that call; in the worst case, all $n$ occurrences have the same value, giving $O(n)$. Replacing that conversion with a direct arbitrary-set-element operation would restore the advertised expected $O(1)$ removal.

Persistently, `l` contains $n$ entries. Across all dictionary sets, there is exactly one stored index per list occurrence, so their combined size is $n$, plus one dictionary key per distinct value. Total persistent auxiliary space is $O(n)$. Hash-table operations carry the usual expected-time qualification, and list appends/pops are amortized constant time.

## Alternatives and edge cases

- **Direct set `pop` for the index:** Removing an arbitrary index from `idx_set` directly avoids the exact source’s `list(idx_set)` copy and gives the intended expected-$O(1)$ removal. The subsequent moved-last-index updates remain necessary.

- **Linear search in the occurrence list:** A list alone already gives correct weighted random selection, but locating `val` for removal costs $O(n)$. The dictionary of index sets exists specifically to avoid that search.

- **Dictionary of counts only:** Counts can support insertion and removal, but cannot select an occurrence-weighted random value in constant time without an additional sampling structure. Choosing a random dictionary key would weight distinct values equally instead of by multiplicity.

- **Tombstones in the list:** Leaving deleted positions empty avoids moving the last entry but makes random samples hit holes. Rejection sampling can degrade badly when the list is sparse, and compaction costs linear time. Keeping `l` dense guarantees one successful random access.

- **First insertion versus duplicate insertion:** Both calls append an occurrence. Only the Boolean differs: the first occurrence returns `True`, and every later occurrence of the same value returns `False`.

- **Removing one of many copies:** Exactly one index is removed. The dictionary key remains as long as at least one position survives, so later removals and sampling still see the remaining multiplicity.

- **Removing the final copy:** Once `idx_set` becomes empty, deleting the dictionary key is essential. Otherwise `val in self.m` would incorrectly report that the absent value can still be removed.

- **Removing the physical last position:** The `idx < last_idx` guard prevents adding an index that disappears immediately during `pop()`.

- **Moved value equals removed value:** Both names refer to the same index set, but the ordered remove-old, remove-last, add-new updates correctly transform the set. A separate-value assumption here would introduce subtle duplicate bugs.

- **Only one total occurrence:** The sole index is both `idx` and `last_idx`. Its set becomes empty, its key is removed, and the list becomes empty.

- **Negative values and `-1`:** Values are dictionary keys and list contents, so all signed 32-bit inputs work. The empty fallback from `getRandom` is not a safe out-of-contract signal when `-1` may be stored; valid calls are guaranteed nonempty.

- **Randomness tests:** With duplicates, a single return cannot prove the distribution. Correctness comes from the one-slot-per-occurrence representation; statistical tests should allow natural random variation rather than require an exact short-run ratio.
