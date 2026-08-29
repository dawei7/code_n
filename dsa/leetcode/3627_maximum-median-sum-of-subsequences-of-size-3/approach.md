## General

Let `n=3g`, so exactly `g` triples will be removed and exactly `g` medians will contribute to the answer.

After sorting the values in nondecreasing order, the source:

- reserves the smallest `g` values as low fillers;
- divides the largest `2g` values into adjacent pairs;
- takes the smaller value from each pair as a median.

The slice:

`nums[len(nums)//3 :: 2]`

selects precisely those median positions.

**What one triple needs**

For a selected value to be the median of a triple, the triple needs:

- one value no greater than it;
- one value no smaller than it.

The low member does not contribute to the score, so it is best to spend the globally smallest available values in that role. The high member also does not contribute, but it must be at least the median.

This leaves the upper two-thirds to supply one median and one high partner per triple.

**Sorted indexing**

After sorting, write:

`a[0] <= a[1] <= ... <= a[3g-1]`.

The smallest third is `a[0...g-1]`.

The upper two-thirds are paired as:

- `(a[g],a[g+1])`;
- `(a[g+2],a[g+3])`;
- ...
- `(a[3g-2],a[3g-1])`.

In each pair, the first value is no larger than the second and can serve as the median while the second serves as the high element.

The slice starts at index `g` and advances by two, summing:

$$
a_g+a_{g+2}+\cdots+a_{3g-2}.
$$

**Constructing actual triples**

For each `i=0...g-1`, form:

`(a[i], a[g+2i], a[g+2i+1])`.

The first element comes from the smallest third and is no greater than the chosen median. The final element is the paired upper value and is no smaller than the median. Therefore, the middle value after sorting that triple is exactly `a[g+2i]`.

Every sorted array position is used once, so these triples form a valid sequence of removals achieving the slice sum.

**Why the largest values should be paired together**

Think from the largest end. The largest array value cannot contribute more than the second-largest value as a median while still having a distinct element at least as large in its triple. Pairing the largest as a high element with the second-largest as median realizes that best possible top median.

Remove those two role assignments. The same argument says the next available largest value should support the next-largest as median. Repeating selects indices:

`3g-2, 3g-4, ..., g`,

which are exactly the slice positions in reverse order.

Using a very large value as a low filler would waste it, because replacing that filler with a smaller unused value keeps the triple valid and frees the large value for a median or required high partner.

**Exchange argument**

Consider any valid grouping. Sort its `g` medians from largest to smallest. Each median needs a distinct high partner at least as large, so the largest median plus its high partner consume two values from the top of the global order. The largest median cannot exceed `a[3g-2]`.

After reserving those two values, the second-largest median cannot exceed `a[3g-4]`, and so on. Therefore, every solution's ordered medians are componentwise bounded by:

`a[3g-2], a[3g-4], ..., a[g]`.

The source constructs triples attaining every one of those bounds simultaneously. Its sum is therefore globally maximum.

**Following the first example**

Sorting `[2,1,3,2,1,3]` gives:

`[1,1,2,2,3,3]`.

Here `g=2`. The slice from index 2 with step 2 selects values 2 and 3, summing to 5.

One construction uses triples `(1,2,2)` and `(1,3,3)`, whose medians are 2 and 3.

**Following the second example**

Sorted values are `[1,1,10,10,10,10]`. The smallest two ones are fillers. Upper pairs are `(10,10)` and `(10,10)`, producing two medians of 10 and total 20.

**Why removal order is irrelevant**

The problem describes repeated removal steps, but any partition of the original multiset into triples can be executed in any order. A triple's median depends only on its three selected values, not on what was removed earlier.

The source therefore computes the optimal partition value without simulating mutations step by step.

**Input mutation**

`nums.sort()` sorts the caller's list in place. The original ordering is lost. Since the objective depends only on the multiset, this does not affect correctness, but callers needing original order must pass a copy.

## Complexity detail

Let `n=len(nums)`. Sorting dominates at `O(n\log n)` time. The slice contains `n/3` elements and summing it costs `O(n)`, so total time remains `O(n\log n)`.

Python's in-place sort can use `O(n)` temporary references in the worst case. In addition, `nums[n//3::2]` materializes a new list of `n/3` selected values before `sum` consumes it. Therefore, the exact auxiliary-space bound is `O(n)`, matching the manifest.

A generator over the same indices could avoid the explicit slice list, though sort workspace would still determine implementation-level memory.

## Alternatives and edge cases

- **Two-pointer construction:** Sort, then pair values from the upper end while consuming fillers from the lower end. It yields the same medians without materializing a slice.
- **Heap-based selection:** It can identify large values but is more complex and does not beat comparison sorting for the full grouping.
- **Enumerate triple partitions:** The number of partitions is enormous and unnecessary after the exchange argument.
- **Three elements:** `g=1`, and the slice selects the ordinary median of the whole array.
- **All values equal:** Every grouping has the same median sum, and the source returns `g` times that value.
- **Duplicate values:** Nondecreasing comparisons allow equality; median/high roles remain valid.
- **Very large outliers:** Each median still needs a distinct high partner, so not every large value can itself contribute.
- **Smallest third:** They are fillers, not necessarily grouped in any special order beyond one per triple.
- **Length divisibility:** The contract guarantees `n%3==0`, so exactly `g` complete triples exist.
- **Positive values:** The exchange proof does not rely on positivity, but the constraint supplies it.
- **Removal order:** Any constructed partition can be removed in arbitrary sequence.
- **Input mutation:** The exact source reorders `nums` in place.
- **Slice allocation:** The concise expression uses linear extra memory for selected medians.
