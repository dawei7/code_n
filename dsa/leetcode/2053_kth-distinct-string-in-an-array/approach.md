## General

**Distinct means global frequency exactly one**

A string is not distinct merely because it differs from its immediate neighbors. It must occur exactly once in the entire array.

The source begins with `cnt = Counter(arr)`. This scans all array entries and maps each string value to its total occurrence count.

Duplicates are recorded regardless of how far apart their occurrences are.

**Make a second pass to preserve original order**

A frequency map identifies which values are distinct, but map iteration order is not the requested ordering rule. The $k$th distinct string is based on positions in `arr`.

The source therefore scans `arr` again from left to right. Whenever `cnt[s] == 1`, the current occurrence is one distinct string in the required sequence.

It decrements `k` for those entries only. When `k` reaches zero, the current `s` is returned.

**Why duplicate occurrences are skipped**

If a value appears twice or more, every occurrence has the same counter value greater than one. None decrements `k`.

This correctly excludes the string value altogether. The task does not ask for the first occurrence of each different value; it asks only for values appearing once.

**Trace the first example**

For `["d","b","c","b","c","a"]`, the counts are one for `d`, two for `b`, two for `c`, and one for `a`.

Scanning in array order, `d` is the first distinct string and decrements `k` from two to one. Both copies of `b` and `c` are skipped. `a` is the second distinct string, reduces `k` to zero, and is returned.

**Why the returned occurrence is unique**

The method returns only under `cnt[s] == 1`. That condition proves no other index contains the same string.

It also returns at the exact moment the number of distinct entries encountered equals the original requested rank. Earlier distinct values each caused one decrement, while all non-distinct values caused none.

**What happens when too few distinct strings exist**

If the second scan finishes while `k` is still positive, fewer than the requested number of globally unique strings occurred. The source returns the empty string.

Input strings are guaranteed nonempty, so `""` cannot be confused with a valid array element and serves as an unambiguous failure result.

**Why two passes are useful**

During the first occurrence of a string, a one-pass algorithm does not yet know whether the value will appear again later. Returning early based only on seen-so-far frequency could select a value that later becomes a duplicate.

The first complete pass settles global frequencies. The second then makes safe rank decisions in original order.

**Classification and ranking use different information**

The counter answers a value-based question: “How many times does this string occur anywhere?” The array scan answers a position-based question: “In what order do the strings with count one appear?”

Keeping these responsibilities separate prevents a subtle mistake. Even if a dictionary preserves insertion order in modern Python, iterating its keys would order values by their first occurrence, but it would no longer be visibly tied to the array positions being ranked. Scanning `arr` makes the contract direct, and because a qualifying value occurs only once, it can decrement the rank only at its one genuine position.


For every array position, `cnt[s] == 1` is necessary and sufficient for its string to be distinct. The second pass filters by exactly this condition without changing order.

Therefore the sequence of entries that decrement `k` is precisely the problem's ordered sequence of distinct strings. Returning on the $k$th decrement gives the requested element. If that decrement never occurs, returning empty is required.

**Hash-map behavior**

`Counter` is a dictionary subclass. Expected counting and lookup time is constant per string under normal hashing behavior. Strings are short under the constraints, though hashing still conceptually depends on string content.

The original array is not modified, and the method does not build a separate list of distinct strings.

## Complexity detail

Let $N$ be the number of strings and $S$ their total character count. Building the counter takes expected $O(S)$ time when string hashing is included, and the second pass takes expected $O(S)$ worst-case character work for lookups. With maximum string length treated as constant, this is $O(N)$.

The counter stores at most $N$ distinct keys, so space is $O(N)$ entries, or $O(S)$ including stored string-key content references. The second pass uses $O(1)$ scalar state.

## Alternatives and edge cases

- **Two sets:** Move values from a once-seen set to a duplicate set, then scan the array again.
- **Nested comparisons:** Test every string against every other string, costing $O(N^2)$.
- **Build a distinct list:** Filter after counting and index `k-1`; correct but allocates another list.
- **All strings distinct:** The answer is simply the original $k$th array entry.
- **No distinct strings:** Return the empty string.
- **Exactly `k` distinct strings:** Return the final one encountered.
- **Fewer than `k`:** The scan ends and returns `""`.
- **Separated duplicates:** Counter still excludes all occurrences.
- **Repeated string many times:** It remains one map key with a larger count.
- **Original order:** The second array scan, not counter order, determines rank.
- **One-element array:** Its only nonempty string is the first distinct.
- **Input preservation:** `arr` is read twice but never changed.
