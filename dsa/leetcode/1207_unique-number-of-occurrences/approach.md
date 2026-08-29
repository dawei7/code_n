## General

The property concerns frequencies, not the values themselves. Two stages express it directly:

1. count how many times each distinct integer occurs;
2. check whether those frequency numbers are all different.

The exact solution performs both stages with Python’s hash-based collections.

**Map each value to its occurrence count**

`cnt = Counter(arr)` scans the array and creates one mapping entry per distinct integer. If a value appears three times, its counter entry is three regardless of where those occurrences appear.

For `[1, 2, 2, 1, 1, 3]`, the mapping is conceptually one to three, two to two, and three to one. The frequency multiset is therefore three, two, one.

Negative values require no special treatment. They are ordinary hash-map keys.

**A set reveals duplicate frequencies**

`cnt.values()` provides one count for every distinct input value. Converting those counts to a set keeps only unique frequency numbers.

If two different values share a frequency, the values view contains two entries but the set collapses them into one. Its size becomes smaller than the number of counter keys.

If every frequency is unique, inserting them into a set removes nothing. The set size equals the number of distinct values.

The return expression compares:

`len(set(cnt.values())) == len(cnt)`.

`len(cnt)` is the number of distinct input values, exactly the number of frequencies that must be unique.

For `[1, 2]`, the two values each occur once. The counter has two keys but the frequency set contains only `{1}`, so sizes one and two differ and the method returns false.

For the first example, both sizes are three because frequencies one, two, and three are distinct, so it returns true.

**Why the cardinality comparison is a complete test**

Mapping each distinct value to its frequency defines a collection of $k$ integers, where $k$ is the number of distinct values. A set built from those integers has size $k$ exactly when no two are equal.

If the sizes are equal, every original frequency survived as a separate set element, proving pairwise uniqueness. If the set is smaller, at least two original frequency entries mapped to the same set value, proving that two input values have equal occurrence counts.

This is an application of the one-to-one principle: the frequency mapping from distinct input values to count numbers is injective precisely when its image has the same cardinality as its domain.

No sorting is required because the problem asks only whether a collision exists, not which counts collide or in what order.

**Keep the two notions of uniqueness separate**

The counter keys are unique automatically because a mapping stores one entry per distinct array value. That fact alone does not solve the problem. The requirement is that the mapped values—the occurrence counts—also be unique. Converting `cnt.keys()` to a set would merely reproduce the already-distinct input values and would always have the same size as the counter. Converting `cnt.values()` is the essential step because it tests the frequency side of the mapping. This distinction is especially useful when reading the compact one-line return expression.

## Complexity detail

Let $n$ be the length of `arr` and $k$ be the number of distinct values.

Constructing the counter takes expected $O(n)$ time with hash-map operations. Creating the frequency set visits $k$ counts and takes expected $O(k)$ time. Because $k\leq n$, total expected time complexity is $O(n)$.

The counter stores $k$ key-count pairs and the set stores at most $k$ frequencies, so auxiliary-space complexity is $O(k)$. Under the input’s fixed value range from -1000 through 1000, $k$ is also bounded by 2001, but $O(k)$ describes the actual data-dependent allocation.

Hash-table bounds are expected rather than comparison-based worst-case guarantees. Python’s ordinary dictionary and set behavior follows this standard model.

## Alternatives and edge cases

- **Frequency map plus incremental seen set:** Iterate counts and return false immediately when a count already exists in the set. This can short-circuit instead of constructing the complete set first.
- **Sort the frequencies:** After counting, sort the $k$ counts and compare adjacent entries. This costs $O(k\log k)$ time and is unnecessary for a collision test.
- **Fixed counting array:** The bounded value range permits an array of 2001 counters, followed by a set or sorted uniqueness check over nonzero entries.
- **One distinct value:** There is one frequency and therefore nothing it can collide with; the method returns true.
- **All values distinct:** Every frequency equals one. The result is true only when there is one value; with two or more values it is false.
- **Negative and zero values:** They work as ordinary counter keys with no offset calculation.
- **Different values with the same count:** Set cardinality shrinks even though the values themselves are unrelated.
- **Frequency zero:** Values absent from the array are not counter keys, so zero is not part of the frequency collection.
- **Nonempty guarantee:** The method would also return true for an empty array because both sizes would be zero, but the contract always supplies at least one element.
- **Expected hashing complexity:** Adversarial collision details are abstracted by the normal expected $O(1)$ dictionary and set model.
