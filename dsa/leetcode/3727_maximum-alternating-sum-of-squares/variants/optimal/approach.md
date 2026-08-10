## General

**After squaring, only the choice of plus or minus positions matters**

For an arrangement of length `n`, indices zero, two, four, and so on have positive signs. Indices one, three, five, and so on have negative signs. Therefore there are

$$
\left\lceil\frac{n}{2}\right\rceil
$$

positive slots and

$$
\left\lfloor\frac{n}{2}\right\rfloor
$$

negative slots.

An element contributes its square, so `x` and `-x` have the same magnitude:

$$
(-x)^2=x^2.
$$

The original signs and the order within the positive slots do not affect the score. Likewise, order within the negative slots does not affect it. The entire optimization is to decide which squared magnitudes receive plus signs and which receive minus signs.

**Largest squares belong in positive slots**

Suppose an arrangement assigns square `a` to a positive slot and a larger square `b` to a negative slot, where `a < b`. Their contribution is initially

$$
a-b.
$$

Swap the corresponding elements, so `b` becomes positive and `a` becomes negative. Their new contribution is

$$
b-a.
$$

The score improvement is

$$
(b-a)-(a-b)=2(b-a)>0.
$$

Thus an arrangement with a smaller square added and a larger square subtracted cannot be optimal. Repeatedly removing such inverted assignments leaves all negative-slot squares no larger than all positive-slot squares.

It follows that the `floor(n / 2)` smallest squares must occupy the negative positions, and the remaining `ceil(n / 2)` largest squares must occupy the positive positions. This rule also handles ties: swapping equal squares changes nothing, so any distribution of equal boundary values is optimal.

**How the exact source creates the two groups**

The code sorts `nums` in place with

`nums.sort(key=lambda x: x * x)`.

The key is the square, not the signed numeric value. This distinction matters when negative numbers occur. Ordinary ascending order would place a large negative value early even though its square is large. Sorting by `x * x` produces nondecreasing squared magnitude.

Let `m = n // 2`. The first slice `nums[:m]` contains exactly the `m` smallest squares, which must be subtracted. The remaining slice `nums[m:]` contains `n - m = ceil(n / 2)` elements, which must be added.

The source computes

`s1 = sum(x * x for x in nums[: n // 2])`

and

`s2 = sum(x * x for x in nums[n // 2 :])`,

then returns `s2 - s1`. This is the maximum sum of positive-slot squares minus the minimum group assigned to negative slots.

**Why a corresponding rearrangement always exists**

The calculation groups values but does not explicitly build an output permutation. That is sufficient because any values in the positive group can be placed at even indices, and any values in the negative group can be placed at odd indices. The number of values in each group exactly equals the number of available slots.

For example, with `nums = [1, 2, 3]`, the squares in sorted order are one, four, and nine. There is one negative slot and two positive slots. Subtract one and add four plus nine:

$$
4+9-1=12.
$$

One realizing arrangement is `[2, 1, 3]`.

For `nums = [1, -1, 2, -2, 3, -3]`, the sorted square multiset is

$$
1,1,4,4,9,9.
$$

There are three slots of each sign. Subtracting `1+1+4` and adding `4+9+9` gives

$$
22-6=16.
$$

The signs of the selected original integers are irrelevant after squaring; any placement that assigns the correct square groups to alternating sign positions realizes the score.

**Why the grouping is globally optimal**

Take any permutation. If it has a positive-slot square smaller than a negative-slot square, the exchange above strictly improves it. Continue exchanging until no such pair remains. Then every square in a negative slot is at most every square in a positive slot, meaning the negative group consists of the smallest `floor(n/2)` squares.

The process never reduces the score and strictly raises it whenever the grouping violates the sorted split. Therefore no arrangement can beat the split used by the source. Conversely, placing those groups into their corresponding slots realizes the computed value, so the bound is attainable.

For odd `n`, there is one extra positive slot. The slice boundary automatically puts the median square into the positive group along with all larger squares. This is beneficial: every element must receive a sign, and the extra sign available is positive.

**Input mutation**

`list.sort` rearranges `nums` in place. This does not affect the returned numerical result because rearrangement is explicitly allowed and the method needs no later access to the original order. A caller that required the input list to remain unchanged could sort a copy, but the exact source chooses the lower-overhead in-place operation.

## Complexity detail

Let `n` be the number of elements. Sorting by squared magnitude takes $O(n\log n)$ time. Computing each key is constant time under the bounded integer model. The two generator-based sums together square and visit every element once, adding $O(n)$ time. The total time complexity is $O(n\log n)$.

Python's sort may use $O(n)$ temporary memory in the worst case. In addition, the exact slices `nums[:n // 2]` and `nums[n // 2:]` create new lists whose combined length is `n`. Thus the auxiliary space complexity is $O(n)$, matching the manifest. The generator expressions themselves do not build separate square arrays.

The maximum square is $(4\cdot10^4)^2=1.6\cdot10^9$, and summing up to $10^5$ such terms can exceed 32-bit range. Python integers handle the result; a fixed-width implementation should use a 64-bit integer.

## Alternatives and edge cases

- **Enumerate all permutations:** Up to `n!` arrangements exist, even though the score depends only on the two sign groups. The exchange argument reduces the problem to one sort.
- **Sort by the raw integer value:** This is wrong for negatives. For example, `-100` sorts before `2` numerically but has the much larger square and should receive a positive sign.
- **Sort a separate square array:** This produces the same grouping and can make the mathematical reduction explicit. The exact source sorts original values by a square key and squares them while summing, avoiding another stored numeric array.
- **Greedily alternate largest and smallest original values:** A constructed arrangement can work if it assigns square groups correctly, but raw signed size is not the relevant order. Grouping by squares first is safer.
- **Put the smallest squares in positive slots:** That minimizes rather than maximizes the expression because it forces large magnitudes to be subtracted.
- **Odd array length:** There is one more positive slot. `n // 2` selects only the smaller floor half for subtraction and assigns the entire larger ceiling half to addition.
- **Single element:** There are zero negative slots and one positive slot. The first slice is empty, `s1 = 0`, and the answer is the element's square.
- **Zero values:** A zero contributes nothing under either sign. Sorting places it among the smallest squares, usually in a negative slot when one is available, which is never worse.
- **Equal absolute values with opposite signs:** Their squares tie, and either can occupy either group without changing the score.
- **All values negative:** Squaring removes their signs. The same smallest-versus-largest square split remains valid.
- **Already sorted input:** The in-place sort may do less practical work, but the worst-case bound remains $O(n\log n)$.
- **Mutation-sensitive caller:** Sorting a copy would preserve the original list at an additional $O(n)$ allocation. The problem method's contract does not require preservation.
- **Large result:** Summation must use a wide numeric type even though each individual input fits comfortably in 32 bits.
