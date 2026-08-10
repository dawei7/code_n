## General

The word “intersection” has a precise set meaning: keep a value if it occurs in both inputs. The output must contain each qualifying value only once, even when either array contains many copies. Its order is irrelevant. Those two contract details make sets a natural representation because a set records membership while automatically discarding duplicate occurrences.

The exact solution performs the whole transformation in one return expression:

1. `set(nums1)` converts the first array into the set of distinct values found in `nums1`.
2. `set(nums2)` does the same for the second array.
3. The `&` operator constructs the set intersection: it keeps precisely the values present in both operand sets.
4. `list(...)` converts that result to the required list type.

The source is short because Python's set operations perform the loops internally. The explanation must still account for every stage; neither set construction nor intersection is a constant-time operation.

**Why duplicates disappear without special cases.**

Suppose `nums1` contains `[1, 2, 2, 1]`. Inserting the first `1` creates membership for `1`; inserting the later `1` does not create a second copy. The same is true for `2`. Thus `set(nums1)` represents `{1, 2}`. If `nums2` is `[2, 2]`, its set is `{2}`. Their intersection is `{2}`, and converting it to a list produces `[2]`.

No frequency table is needed because the result does not care whether a common value occurs once or a thousand times. It asks only the yes-or-no question “does this value occur in each input?” A set stores exactly that information and no irrelevant multiplicity.

**Why the intersection is correct.**

Consider any value `x` that appears in the returned list. It came from the temporary intersection set. By the definition of `&`, `x` can be in that set only if it is a member of both `set(nums1)` and `set(nums2)`. Set construction includes a value exactly when that value appeared in the corresponding array. Therefore every returned value truly appears in both input arrays.

Now consider any distinct value `y` that appears in both arrays. The first set construction includes `y`, and the second set construction also includes `y`. The intersection operator consequently includes `y`, and converting the set to a list retains it. Therefore no required common value is omitted.

Finally, the intermediate result is a set, so it cannot contain duplicate entries. The conversion to a list copies each set member once; it does not reintroduce duplicates. These three facts establish that the returned list contains exactly the distinct common values.

**Why arbitrary output order is acceptable.**

Sets are not used here to preserve the arrays' encounter order. Their iteration order is an implementation detail and should not be treated as sorted order or as a stable part of this algorithm's contract. For the second example, either `[9, 4]` or `[4, 9]` is valid because both describe the same mathematical set. If the judge required a particular order, an extra ordering step or an order-preserving scan would be necessary. This problem explicitly removes that requirement.

**The exact source differs from the manifest summary.**

The variant manifest says that the method builds a set from the shorter array and scans the longer array while deduplicating matches. That would be a sensible one-set implementation, but it is not what `solution.py` executes. The checked-in source constructs a complete set from each input before applying built-in intersection. It never compares the input lengths, never chooses the shorter array, and never explicitly scans the longer array.

This difference matters most for auxiliary space. If the arrays contain many distinct values, both full operand sets coexist. The exact implementation therefore needs storage proportional to the distinct values from both arrays, rather than only the distinct values in the shorter input. The manifest's $O(\min(n,m))$ space claim does not describe this source.

**A concrete data-flow example.**

For `nums1 = [4, 9, 5]` and `nums2 = [9, 4, 9, 8, 4]`, the first conversion produces a set containing `4`, `9`, and `5`. The second produces a set containing `9`, `4`, and `8`; repeated `9` and `4` entries do not enlarge it. Intersection tests membership between those distinct collections and retains `4` and `9`, while excluding `5` because it is absent from the second set and excluding `8` because it is absent from the first. The final list contains the two retained values in whichever iteration order the result set supplies.

The input arrays themselves are not sorted or mutated. Each set is a new object, the intersection is another new set, and the returned list is another new container. This immutability of the inputs can be useful when callers still need their original order and duplicates after the method returns.

## Complexity detail

Let $n$ be `len(nums1)`, let $m$ be `len(nums2)`, let $u_1$ and $u_2$ be their respective numbers of distinct values, and let $r$ be the number of distinct values present in both. Then $u_1\le n$, $u_2\le m$, and $r\le\min(u_1,u_2)$.

Constructing the first set examines all $n$ elements, and constructing the second examines all $m$ elements. With expected constant-time hashing and insertion, those stages take expected $O(n+m)$ time. Set intersection examines membership information for the operand sets; Python can base this work on the smaller set, so it takes expected $O(\min(u_1,u_2))$ time. Converting the intersection set to a list copies $r$ values and costs $O(r)$ time.

Combining the stages gives expected

$$
O(n+m+\min(u_1,u_2)+r)=O(n+m)
$$

time, because the distinct and result counts cannot exceed the input lengths. This matches the manifest's time bound in the ordinary expected-cost model for hash sets. Abstract hash tables can have worse behavior under pathological collisions, but the bounded integer values in this problem use straightforward integer hashing; the expected linear analysis is the useful one here.

For space, the first set stores $u_1$ values and the second stores $u_2$. The intersection temporarily stores $r$ values, and the returned list also stores $r$ references. During evaluation, multiple containers can coexist, so the exact additional-space expression is

$$
O(u_1+u_2+r)=O(u_1+u_2),
$$

which is $O(n+m)$ in the worst case. Even if output storage is excluded, both operand sets still require $O(u_1+u_2)$ space. Therefore $O(\min(n,m))$ is not a valid auxiliary-space claim for this exact one-line implementation. The constraints cap values between `0` and `1000`, so at most `1001` distinct integers can appear in either set, but asymptotic analysis conventionally describes growth in the input lengths or distinct counts rather than treating this small published bound as a constant universe.

## Alternatives and edge cases

- **One set from the smaller input:** Store the distinct values of the shorter array, scan the other array, and add matches to a result set or remove each match after output. This can use $O(\min(n,m))$ membership storage plus output, matching the manifest summary, but it is not the checked-in source.

- **Sort and use two pointers:** Sort both arrays, advance the pointer at the smaller value, and emit equal values while skipping duplicates. This avoids hash assumptions but costs $O(n\log n+m\log m)$ time and may mutate the inputs if sorting is done in place.

- **Boolean presence table:** Because values lie from `0` to `1000`, a fixed table can record membership from one array and a second state can prevent duplicate output. It provides deterministic linear scanning time and bounded storage, but it relies on the small value range and generalizes poorly to arbitrary integers.

- **Nested membership scans:** For every distinct value in one array, search the other array linearly. This uses little auxiliary state but can require $O(nm)$ time and needs an additional mechanism to avoid duplicate output.

- **No common values:** The intersection set is empty, so `list(...)` returns `[]`. There is no special branch because ordinary set intersection already represents this case.

- **All values common:** If the two arrays have the same distinct value set, the intersection contains every one of those values exactly once, regardless of different frequencies in the arrays.

- **Many duplicates:** Repetition increases the time needed to read the arrays but not the final set sizes. One thousand copies of one value still create only one set entry.

- **One-element inputs:** Equal elements produce a one-element list; unequal elements produce an empty list. The general membership reasoning needs no boundary-case adjustment.

- **Zero values:** Zero is a normal hashable integer and must not be confused with a false or missing marker. Direct set membership handles it correctly.

- **Do not promise sorted output:** A test should compare the returned members without depending on list order. Sorting solely for presentation would add unnecessary $O(r\log r)$ time.

- **Input preservation:** Because both `set(...)` calls create new containers, the original arrays retain their order and duplicates. An in-place sorting alternative would not preserve that property.
