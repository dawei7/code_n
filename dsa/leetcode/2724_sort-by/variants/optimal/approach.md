## General

**Sort elements by a derived numeric key**

The elements of `arr` may be numbers, objects, or arrays. Their raw representation is not the ordering rule. The supplied function `fn` maps each element to the number that determines where it belongs.

The implementation delegates the reordering to JavaScript's in-place `Array.prototype.sort` and supplies a comparator:

`fn(left) - fn(right)`.

This is the standard numerical ascending comparator applied to derived keys.

**How a comparator controls the sort**

When the sorting engine asks how `left` and `right` should be ordered, the comparator returns:

- a negative number when `fn(left) < fn(right)`, placing `left` earlier;
- a positive number when `fn(left) > fn(right)`, placing `left` later;
- zero when the keys are equal.

The problem guarantees that `fn` does not return duplicate numbers for the given array, so legal comparisons between different elements do not produce a key tie. No secondary tie-breaking rule is required.

Subtraction matters. Calling `sort()` without a comparator would convert values to strings and use lexicographic ordering, which would put values such as ten and two in the wrong numeric relationship.

**The elements themselves are preserved**

The comparator only reads elements and calculates keys. `sort` moves the original element values or object references; it does not replace each item with its key.

For `arr = [{"x": 1}, {"x": 0}, {"x": -1}]` and `fn = d => d.x`, comparisons use one, zero, and negative one. The returned array still contains the three original objects, ordered as keys negative one, zero, one.

For nested arrays such as `[[3,4],[5,2],[10,1]]` with `fn = x => x[1]`, the second entries one, two, and four determine the order, yielding `[[10,1],[5,2],[3,4]]`.

**The original array is mutated**

`Array.prototype.sort` rearranges `arr` in place and returns a reference to that same array. Thus `sortedArr === arr` is true for this implementation.

The contract asks for a sorted array and does not require preserving the input order in a separate object, so mutation is acceptable. In an application where callers expect immutability, the code would need to copy first, but that would be a different implementation behavior.

**Why every comparison may call fn again**

The solution does not precompute keys. Whenever the sort engine invokes the comparator, it calls `fn(left)` and `fn(right)` again. Comparison sorting typically performs $O(n\log n)$ comparisons, so `fn` may be evaluated $O(n\log n)$ times rather than once per element.

Under the problem's intended simple key functions, this is concise and efficient enough. It also assumes `fn` is deterministic and has no disruptive side effects: the same element must keep the same ordering key throughout the sort for comparator consistency.

**Trace a small numerical case**

With `arr = [5,4,1,2,3]` and identity `fn`, consider comparing five with four. The comparator returns one, so five belongs after four. Comparing one with four returns negative three, so one belongs before four. The sorting engine chooses its own sequence of such comparisons, but every result agrees with ascending numeric-key order.

The algorithm does not dictate a particular sorting strategy. The JavaScript engine is responsible for arranging all elements so that no later element has a smaller key than an earlier one.

**Why the result is correct**

For any two elements $a$ and $b$, the comparator reports a negative value exactly when $fn(a)<fn(b)$ and a positive value exactly when $fn(a)>fn(b)$. A conforming comparison sort uses those signs to establish the order defined by `fn`. Because all keys are unique, this relation is a strict total order over the input elements. When `sort` finishes, the elements are therefore in ascending order of their computed keys, which is precisely the requested result.

**Numeric assumptions**

The contract says `fn` returns numbers. The intended values must behave as ordinary sortable finite numbers. Special JavaScript value `NaN` would make subtraction return `NaN`, which a comparator cannot use as a meaningful order, but such a key would conflict with the guarantee that numeric outputs determine the ordering.

## Complexity detail

Let $n$ be `arr.length` and let $C$ be the cost of one call to `fn`. A comparison sort performs $O(n\log n)$ comparisons in the standard worst-case model, and this comparator invokes `fn` twice per comparison. The time is therefore $O(Cn\log n)$. When `fn` is $O(1)$, this is the manifest's $O(n\log n)$.

The exact auxiliary storage of `Array.prototype.sort` is engine-dependent. Modern JavaScript engines may use $O(n)$ temporary storage, matching the manifest's conservative $O(n)$ bound. The comparator itself uses only constant local state.

The output array does not require a separate $O(n)$ allocation because `sort` mutates and returns `arr`. Engine-internal sort workspace is still auxiliary space.

## Alternatives and edge cases

- **Decorate, sort, undecorate:** Compute `fn` once per element, sort key-element pairs, and strip keys; this helps when `fn` is expensive but allocates $O(n)$ explicit records.
- **Copy before sorting:** `[...arr].sort(...)` preserves the input array at the cost of $O(n)$ additional visible storage.
- **Default `sort()`:** Incorrect for numeric keys because it uses string ordering.
- **Handwritten merge sort:** Gives direct control over stability and storage but adds substantial code without changing the target order.
- **Single element:** No meaningful comparison is needed, and the same one-element array is returned.
- **Unique-key guarantee:** Eliminates ambiguity and the need for a tie-breaker.
- **Objects and nested arrays:** They are valid because `fn` extracts the numeric key while sort moves the original values.
- **Mutation:** Callers holding `arr` observe its new order after the function returns.
- **Expensive `fn`:** Repeated comparator evaluation can dominate the runtime; precomputing keys would then be preferable.
- **Side-effecting `fn`:** Can make comparisons inconsistent and should be avoided even though the contract focuses only on numeric return values.
