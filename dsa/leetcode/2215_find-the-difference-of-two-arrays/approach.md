## General

**The requested results are mathematical set differences**

The output cares about distinct values, not about how many times each value appears. The first result must contain every value that occurs in `nums1` and does not occur in `nums2`. In mathematical notation, that is

$$
S_1 \setminus S_2,
$$

where `S_1` and `S_2` are the sets of values appearing in the two arrays. The second result reverses the direction and is `S_2 \setminus S_1`. These two differences are not interchangeable: a value unique to the first array belongs only in the first output list, while a value unique to the second belongs only in the second.

Python's `set` type directly represents the two facts the problem needs: each value is stored only once, and membership can normally be tested in constant time. The exact solution first constructs both sets with

`s1, s2 = set(nums1), set(nums2)`.

During construction, duplicates disappear automatically. For instance, `set([1, 2, 3, 3])` contains only `1`, `2`, and `3`. This is not accidental data loss; it exactly implements the word “distinct” in the output contract.

**Compute each direction separately**

The expression `s1 - s2` creates a new set containing values that belong to `s1` but not to `s2`. It does not mutate either original set. Similarly, `s2 - s1` creates values present only in the second input's set.

The return statement is

`[list(s1 - s2), list(s2 - s1)]`.

The outer list therefore always has exactly two entries. Position zero is the first directional difference, and position one is the second. Each difference set is converted to a list because the required return type is a list of lists rather than a pair of set objects.

The conversion does not sort the values. Set iteration order is not a promised numeric or input order, so the lists may appear in any order. That behavior is allowed explicitly by the problem. A caller or judge must compare each inner list as an unordered collection of distinct values rather than expect a particular arrangement such as ascending order.

**Why every returned value belongs**

Take any value `x` in the first returned list. It came from `s1 - s2`. By the definition of set subtraction, `x` is in `s1` and is not in `s2`. Being in `s1` means it appears at least once in `nums1`. Not being in `s2` means it never appears in `nums2`. Thus, `x` satisfies exactly the rule for `answer[0]`.

The same reasoning with the sets reversed proves that every value in the second returned list appears in `nums2` and not in `nums1`. Therefore, the method never includes a shared value on either side and never places a one-sided value in the wrong side.

**Why no required value is omitted**

Now take any distinct integer `x` that appears in `nums1` but not in `nums2`. Set construction necessarily places `x` in `s1`, no matter whether it occurs once or many times. Since it never appears in `nums2`, it is absent from `s2`. It must consequently be an element of `s1 - s2` and will be included when that set is converted to a list.

The reversed argument covers every integer that appears only in `nums2`. Hence, both returned lists contain all and only their required values. Set uniqueness also ensures each appears exactly once.

This two-sided argument matters because “difference” is sometimes confused with removing common occurrences one by one. That is not the task. If `nums1` contains three copies of `5` and `nums2` contains one copy, `5` appears in both sets and belongs in neither output list. Counts do not matter after presence has been established.

**Trace a representative input**

Consider `nums1 = [1, 2, 3, 3]` and `nums2 = [1, 1, 2, 2]`. Converting them produces `s1 = {1, 2, 3}` and `s2 = {1, 2}`. The first subtraction leaves `{3}` because `3` exists only in `s1`. The second subtraction is empty because every member of `s2` also belongs to `s1`. After list conversion, the structural result is `[[3], []]`.

For `nums1 = [1, 2, 3]` and `nums2 = [2, 4, 6]`, the shared value `2` is removed from both directional results. The first difference contains `1` and `3`, while the second contains `4` and `6`. Their order inside each list is immaterial.

Negative values and zero need no special handling. Hash sets store integers according to equality and hash value, so `-5`, `0`, and `5` are simply three distinct possible keys. The stated range limits do not require a custom indexing offset or frequency array.

**Why this is preferable to repeated list membership checks**

A direct beginner implementation might inspect every value of `nums1` and search all of `nums2` for a match, then repeat in the opposite direction. That can compare almost every pair of input positions and takes quadratic time in the worst case. It also needs an extra mechanism to avoid returning duplicate values.

Building a set pays one pass over each input. Hash-table membership and insertion are expected `O(1)` operations, so the set differences can be formed in expected linear time relative to the number of distinct values. The data structure simultaneously solves the membership and deduplication requirements.

The implementation creates both full input sets before computing either result. It then creates temporary difference sets and converts them to lists. Original arrays and sets remain unchanged, which makes the two directional operations independent and avoids a mutation on the first difference affecting the second.

## Complexity detail

Let `n = len(nums1)` and `m = len(nums2)`. Constructing `s1` performs `n` expected constant-time hash insertions, and constructing `s2` performs `m`. Their combined expected time is `O(n + m)`.

Set subtraction examines the elements of its left operand and tests them against the right operand's hash table. Across `s1 - s2` and `s2 - s1`, no more than the distinct elements of both sets are processed, which is bounded by `n + m`. Converting the two result sets to lists is proportional to the output size, also at most `n + m`. The complete expected time complexity is therefore `O(n + m)`.

Hash-table complexity is described as expected or average-case because it relies on effective hashing. A pathological collision pattern can degrade individual set operations, but for Python integers under normal analysis, expected constant-time insertion and membership are the standard model.

The two input-derived sets can hold up to `n + m` distinct values in total. The two difference sets and returned lists can also collectively contain at most `n + m` values. Peak additional storage is therefore `O(n + m)`. The output itself may require linear space, and the implementation also uses linear auxiliary set storage; excluding the returned lists does not reduce the asymptotic bound.

The input arrays are not modified. Any temporary difference set can become eligible for cleanup after its corresponding list conversion, but asymptotic peak storage remains linear.

## Alternatives and edge cases

- **Nested scans with a result set:** For each value in one array, scan the other array to decide membership and insert qualifying values into a set, then repeat in reverse. This is logically correct but takes `O(nm)` time in the worst case.
- **Frequency arrays over the bounded value range:** Because values lie between `-1000` and `1000`, two boolean arrays with an offset could mark presence and then enumerate the domain. This is also efficient for these constraints, but it depends on the small numeric range and normally emits values in sorted domain order; hash sets express the actual set operation more directly.
- **Sort and use two pointers:** Sorting copies of both arrays would allow duplicate skipping and a linear merge afterward. Its total time is `O(n \log n + m \log m)`, and sorting the original lists in place would modify caller data unless copies were made.
- **Symmetric difference:** `s1 ^ s2` finds every value that appears in exactly one set, but it loses which input owned the value. The required answer has two directional lists, so two subtractions are necessary unless the symmetric difference is partitioned again.
- **Intersection removal by mutating sets:** One could calculate the intersection and remove it from both sets. That adds a separate structure or mutates the input-derived sets, whereas direct subtraction already returns the required two results clearly.
- **Duplicates within one input:** Set construction collapses them. A value exclusive to one side appears once in its output no matter how many times it occurs in that source array.
- **Different duplicate counts across inputs:** If a value appears at least once in both arrays, it appears in neither output. The method compares presence, not multiplicity.
- **Identical sets of values:** Both differences are empty, so the method returns `[[], []]` even if the arrays have different orders or repetition counts.
- **No overlap:** Every distinct value of `nums1` appears in the first list, and every distinct value of `nums2` appears in the second.
- **One side's values are a subset of the other's:** The subset side's directional difference is empty; the other side contains only its additional distinct values.
- **Negative numbers and zero:** Python integer sets handle them without an offset or separate branch.
- **Arbitrary output order:** Converting a set with `list(...)` does not promise sorted order. This is contract-compliant; sorting would add unnecessary `O(k \log k)` work for an output of size `k`.
- **Outer-list position:** Even though inner order is arbitrary, the two inner lists cannot be swapped. Index `0` always describes values exclusive to `nums1`, and index `1` always describes values exclusive to `nums2`.
- **Input preservation:** Neither `set(nums1)` nor subtraction changes the original arrays. The result can be computed safely even if the caller retains and later reuses them.
