## General

**The condition is entirely local**

An array is special when every adjacent pair has different parity. A number's parity is its remainder modulo 2:

- even numbers have remainder 0;
- odd numbers have remainder 1.

Therefore, adjacent values `a` and `b` satisfy the rule exactly when

`a % 2 != b % 2`.

No relationship between nonadjacent elements is required. If all neighboring pairs alternate parity, the array is special; if even one neighboring pair has equal parity, the whole array fails.

**Generate adjacent pairs without indexing**

`pairwise(nums)` produces

`(nums[0], nums[1])`, `(nums[1], nums[2])`, and so on through the final adjacent pair.

The generator expression applies the parity inequality to each pair. Python's `all` returns true only if every generated Boolean is true, which exactly mirrors “every pair.”

`all` is short-circuiting. As soon as a same-parity pair produces false, it stops asking the generator for more pairs and returns `False`. Later elements cannot repair an earlier violation.

If the generator reaches the end without a false value, every adjacency has been checked and the result is `True`.

**Why a one-element array is special**

For an array of length one, `pairwise` produces no pairs. There is no adjacent pair that violates the rule. In logic, a universal statement over an empty collection is true; Python's `all` follows this convention and returns true for an empty iterable.

This is not an accidental special case. It is exactly why the example with one element is valid.

**Parity alternation**

Once the first element's parity is known, each valid next element must have the opposite parity. Thus a special array has a parity pattern such as

`odd, even, odd, even, ...`

or

`even, odd, even, odd, ...`.

Checking adjacent pairs is sufficient to enforce that entire pattern by transitivity through the sequence. We do not need to compare each position with an expected formula based on index, although that would be another valid formulation.

For `[2,1,4]`, remainders are `[0,1,0]`. Both adjacent comparisons differ, so `all` returns true.

For `[4,3,1,6]`, remainders are `[0,1,1,0]`. Pair `(3,1)` has remainders 1 and 1, so evaluation stops and returns false.


Every pair emitted by `pairwise(nums)` consists of two elements at consecutive indices, and every consecutive-index pair is emitted exactly once.

If the function returns true, each emitted predicate was true, so every adjacent pair has different parity and the array satisfies the definition.

If it returns false, some emitted adjacent pair had equal remainders modulo 2. Both values are therefore even or both are odd, directly violating the definition. Hence the result is correct in both directions.

**Why values themselves do not matter**

Only the least significant parity bit matters. Values 2 and 100 are different but both even, so they cannot be adjacent in a special array. Values 2 and 999 have opposite parity and satisfy their local pair regardless of their magnitudes.

The constraints contain positive integers, but Python's modulo parity test would work for negative integers too because even values still have remainder 0 and odd values remainder 1.

## Complexity detail

Let $n$ be the number of elements.

There are $n-1$ adjacent pairs. Each requires two modulo operations and one comparison, all constant time under the bounded integer model. Worst-case time is $O(n)$.

Short-circuiting can return after the first pair on some invalid arrays, giving best-case $O(1)$ time, but an alternating array requires all comparisons.

`pairwise` and the generator expression are lazy. They retain only enough state for the current neighboring values and do not build a list of pairs or parities. Auxiliary space is $O(1)$.

The output is one Boolean and the input list is not modified.

The linear worst-case bound is optimal: two equal-parity values could form the final adjacency, so an algorithm may need to inspect the entire array.

## Alternatives and edge cases

- **Index loop:** Iterate `i` from 1 and compare `nums[i-1] % 2` with `nums[i] % 2`. It is equivalent and works on Python versions without `pairwise`.
- **Bitwise parity:** Compare `(a & 1) != (b & 1)`. This avoids modulo and directly reads the low bit.
- **Expected parity by index:** Determine the first parity and require each index to alternate. It checks the same condition but is slightly less local.
- **Build a parity list:** Mapping every value to 0 or 1 first uses $O(n)$ extra space without simplifying the one-pass check.
- **One element:** There are no adjacent constraints, so the answer is true.
- **Two elements:** The answer is simply whether their parities differ.
- **All even or all odd:** Any array of length at least two fails on the first pair.
- **Repeated values:** Equal values have equal parity, so adjacent duplicates immediately fail.
- **Large magnitude gap:** It is irrelevant; only remainder modulo 2 matters.
- **First violation:** Returning immediately is safe because the definition requires every adjacency to pass.
- **Empty array outside the contract:** `all(pairwise([]))` would also return true vacuously, though the source guarantees at least one element.
- **Input preservation:** Lazy comparison reads values only and does not reorder or overwrite them.
