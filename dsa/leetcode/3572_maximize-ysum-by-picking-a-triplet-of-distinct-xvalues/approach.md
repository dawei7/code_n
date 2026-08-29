## General

The constraint concerns only the chosen `x` values: the three indices must come from three different `x` groups. Within one group, only its largest `y` can ever be useful. Replacing a chosen index by another index with the same `x` and larger `y` preserves distinctness and improves or preserves the sum.

The exact source realizes this idea by sorting every `(x,y)` pair in descending `y` order, then scanning until it has selected the first three previously unseen `x` values.

The manifest summary says the solution keeps the greatest `y` per `x` and selects the top three “in one additional pass,” with `O(n)` time. That describes a possible dictionary-based algorithm, not the executable source. The source constructs and sorts all `n` pairs, so its time is `O(n\log n)`.

**Pairing corresponding array entries**

`zip(x,y)` associates values at the same index. The list comprehension creates

`arr = [(x[0],y[0]), (x[1],y[1]), ...]`.

The input guarantees equal lengths, so no element is lost through `zip` truncation.

Each pair still represents one concrete selectable index, even though the original numeric index is not stored. The output needs only the maximum sum, not the chosen positions, and equal `x` groups are handled by the visited set.

**Sorting by descending y**

`arr.sort(key=lambda x: -x[1])` orders pairs by the negative of their `y` value. Smaller negative keys correspond to larger original values, so the scan visits `y` from greatest to smallest.

The lambda parameter named `x` is merely a local tuple variable and is unrelated to the method’s input list after key evaluation.

Tie order among equal `y` values does not matter. Choosing either equal-valued representative produces the same contribution, and the set will still enforce distinct `x` values.

**Why the first occurrence of an x group is its best representative**

When the scan first encounters a particular `x` value `a`, no later pair with `x=a` can have a greater `y`, because the complete list is sorted descending by `y`. Therefore the first pair for group `a` contains that group’s maximum possible contribution.

The source adds `a` to `vis` and adds its `b` value to `ans`. Every later pair with the same `a` is skipped.

Although it does not explicitly build a dictionary `a -> maximum_y`, the sorted scan implicitly identifies the same group maximum.

**Why taking the first three distinct groups is optimal**

After replacing each `x` group by its maximum `y` representative, the task is simply to choose the three largest representative values.

The global descending scan encounters group representatives in nonincreasing order. Nonmaximum members of a group may appear too, but they are skipped after that group’s first occurrence. Consequently, the first three distinct `x` groups encountered are exactly the groups with the three largest maxima.

Suppose an alleged better triplet used a group encountered later instead of one of these three. Its best possible `y` is no greater than the earlier selected group’s representative. Replacing it cannot increase the sum. Thus no triplet has a larger total.

As soon as `len(vis)==3`, the source returns `ans`. Later pairs cannot improve any selected group maximum or introduce a group with a larger maximum than those already encountered.

**Why fewer than three groups means impossibility**

If the scan ends with fewer than three distinct values in `vis`, the input contains fewer than three distinct `x` values. No three indices can satisfy pairwise distinctness, regardless of their `y` values, so the method returns `-1`.

There are at least three indices by constraint, but those indices may belong to only one or two `x` groups.

**A representative trace**

For `x=[1,2,1,3,2]` and `y=[5,3,4,6,2]`, pairs sorted by descending `y` begin:

`(3,6), (1,5), (1,4), (2,3), (2,2)`.

The method selects group three with six and group one with five. The next pair has group one again and is skipped. Group two with three becomes the third distinct group, yielding `6+5+3=14`.

The skipped `(1,4)` cannot help because using two indices whose `x` values both equal one is forbidden.

## Complexity detail

Creating `arr` takes `O(n)` time and space. Sorting `n` pairs takes `O(n\log n)` time in the worst case. The subsequent scan visits at most `n` pairs, with expected constant-time set operations.

Total time is therefore `O(n\log n)`, not the manifest’s `O(n)` claim for a different representative-map implementation.

The pair list stores `n` tuples, so it uses `O(n)` auxiliary space. `vis` stops growing after three successful distinct selections because the function returns immediately; in a failure case it contains all `u<3` distinct values, still constant under that path. More generally the set is `O(\min(u,3))` here.

The manifest’s `O(u)` space omits the actual sorted pair list. Faithful auxiliary space for this source is `O(n)`.

## Alternatives and edge cases

- **Dictionary of maximum y per x:** Scan once, update `best[x]=max(best[x],y)`, then find the top three dictionary values. With a three-value tracker, this achieves expected `O(n)` time and `O(u)` space and matches the manifest summary.
- **Heap over group maxima:** After building the dictionary, `nlargest(3, best.values())` selects representatives in `O(u\log 3)` time. It is useful when generalizing from three to `k` groups.
- **Sort group maxima only:** Deduplicate through a dictionary before sorting. This costs `O(n+u\log u)` and may sort far fewer entries than the exact source.
- **Choose the three largest y values without checking x:** This can select repeated `x` groups and violate the central constraint.
- **Repeated x with a better later input position:** Input order is irrelevant because sorting places that group’s largest `y` first.
- **Equal y values:** Any ordering among them is optimal; only distinct group membership matters.
- **Exactly three distinct x values:** The method chooses each group’s maximum representative, which is the only possible optimal group set.
- **Fewer than three distinct x values:** It returns `-1` even though at least three indices exist.
- **Many duplicate indices for one x:** All but the first sorted occurrence are skipped, so they cannot occupy multiple triplet slots.
- **Positive y constraint:** Every selected contribution is positive. The same top-three-representatives proof would still work with negative values because exactly three groups must be chosen.
- **No need to return indices:** Discarding original indices is safe because only the sum is requested. If reconstruction were required, the pair records would need to retain an index.
- **Early return after three groups:** Sorting has already established that no unseen group can have a larger representative, so scanning the rest is unnecessary.
- **Input arrays remain unchanged:** Sorting is applied to a new tuple list, not to `x` or `y`.
