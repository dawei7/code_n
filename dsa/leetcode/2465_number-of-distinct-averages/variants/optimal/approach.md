## General

**Sorting reveals the forced pairs**

Repeatedly removing the current minimum and maximum is equivalent to sorting the array once and pairing symmetric positions:

- smallest with largest;
- second smallest with second largest;
- and so on.

The input length is even, so every value belongs to exactly one pair and there is no unpaired middle element.

The source sorts `nums` in place. For `i` from zero through `n/2-1`, `nums[i]` is the next smallest remaining value and `nums[-i-1]` is the corresponding largest remaining value.

Ties do not cause ambiguity. If several equal minima or maxima exist, choosing any occurrence yields the same numeric pair values, so the multiset of calculated averages is unchanged.

**Store sums instead of averages**

The average of pair `a,b` is $(a+b)/2$. Two pair averages are equal exactly when their sums are equal because dividing both by the same positive constant two is one-to-one:

$$
\frac{a+b}{2}=\frac{c+d}{2}
\iff
a+b=c+d.
$$

The generator stores `nums[i]+nums[-i-1]` in a set rather than constructing floating-point values. This avoids fractions such as 2.5 and eliminates any concern about floating-point representation.

The number of distinct sums is therefore exactly the number of distinct averages.

Every possible average is either an integer or ends in one half because both inputs are integers. Multiplying an average by two recovers its pair sum exactly. There is no rounding step in the problem, so values such as 2 and 2.5 must remain distinct; their doubled values 4 and 5 remain distinct integers in the set. This scaled representation preserves all information while using exact arithmetic.

**Trace the example**

Sorting `[4,1,4,0,3,5]` gives `[0,1,3,4,4,5]`. Symmetric pairs are:

- 0 and 5, sum 5, average 2.5;
- 1 and 4, sum 5, average 2.5;
- 3 and 4, sum 7, average 3.5.

The set of sums is `{5,7}`, whose size is two.

For `[1,100]`, only one symmetric pair exists, so the set has one member regardless of its average.

**Why symmetric pairing exactly models repeated removal**

After sorting, the smallest remaining value initially occupies the leftmost unused position and the largest occupies the rightmost unused position. Removing them exposes the next two inward positions. Induction over removal rounds proves round `i` selects indices `i` and `n-1-i`.

The generator visits precisely those index pairs. Each produced sum corresponds to one required average, and every required average is represented once. Set cardinality then performs exactly the requested distinct count.

Tie choices cannot change this reasoning. If the current minimum occurs several times, all tied occurrences have the same value, and replacing one occurrence by another leaves the pair sum unchanged. The same holds for tied maxima. Removing any permitted tied occurrence therefore leads to the same remaining multiset and the same future numeric pairs, even if element identities differ.

Another useful invariant is that after `i` rounds, exactly the first `i` and last `i` positions of the sorted array have been consumed. The unused middle slice remains sorted, so its endpoints continue to be the required extremes for the next round. This proves the index formula for all rounds, not only the first.

**Input mutation**

`nums.sort()` changes the caller-provided list order. The problem does not require preserving it, so this is valid. An implementation that needs input preservation should use `sorted(nums)`.

The set comprehension is fed by a generator, so there is no separate list of all pair sums. The set itself retains only distinct sums.

## Complexity detail

Sorting $n$ values takes $O(n\log n)$ time. Generating $n/2$ sums and inserting them into a hash set takes expected $O(n)$ additional time. Sorting dominates, giving expected $O(n\log n)$ total time.

The set stores at most $n/2$ integers, using $O(n)$ space. Python's in-place sort can also require $O(n)$ temporary working space, so the manifest's $O(n)$ bound is appropriate.

Pair sums range from zero through 200, so a small boolean presence array could replace hashing under these constraints.

The return value is at most $n/2$, the number of removal rounds, and at least one because the even-length input contains at least two elements and therefore produces at least one pair.

## Alternatives and edge cases

- **Repeated minimum/maximum scans:** Literally finding extremes and deleting them each round can take $O(n^2)$ time because list deletion shifts elements.
- **Two pointers after sorting:** Explicitly advance left and right pointers while adding sums to a set. It is equivalent to the compact generator.
- **Frequency counting array:** Values are bounded from 0 to 100, so counts can simulate removals in $O(n+U)$ time with fixed domain $U$.
- **Use floating-point averages:** It works for halves of integers here, but sums are simpler and exact.
- **All pair sums equal:** The set has size one even when individual pairs contain different values.
- **Duplicate minima or maxima:** Equal choices yield the same numeric values, so arbitrary tie removal does not alter the answer.
- **Two elements:** Exactly one average is calculated.
- **Even-length guarantee:** It ensures the symmetric loop covers every value with no center leftover.
- **Zeros:** They participate normally as minima and require no special case.
- **Input mutation:** Sorting occurs in place and changes the original order.
