## General

**Turn each left value into a complement search**

For an index `i`, the only value that can pair with `numbers[i]` is:

`x = target - numbers[i]`.

Because `numbers` is sorted in non-decreasing order, the source can search for
`x` with binary search rather than scanning every later element. It loops over
all possible first indices from zero through `n - 2`.

The search begins at `lo = i + 1`. This boundary is essential: it prevents
using the same array element twice and guarantees the returned first index is
smaller than the second. A matching value at index `i` itself is irrelevant
unless another equal copy exists later.

**Use lower bound and verify the candidate**

`bisect_left(numbers, x, lo=i + 1)` returns the first index at or after
`i + 1` where `x` could be inserted without breaking sorted order.

There are two possible outcomes:

- if `j < n` and `numbers[j] == x`, the complement actually exists and the
  source returns the pair;
- if `j == n` or `numbers[j] != x`, there is no occurrence of `x` in the
  searched suffix, so this `i` cannot begin the solution.

The equality check cannot be omitted. A lower-bound function always returns an
insertion position, even when the requested value is absent.

Duplicates are handled correctly. Lower bound chooses the first suitable copy
after `i`, and the contract's unique-solution guarantee ensures whichever
matching pair is found is the required one.

**Why the sorted property makes each rejection conclusive**

Binary search compares `x` with middle values of the suffix. If a middle value
is smaller, every earlier value in that current search portion is also too
small; if larger, every later value is too large. This halves the suffix until
the first possible location remains.

If that location is not equal to `x`, no later element can be equal after a
larger value, and no earlier allowed element was skipped by the lower-bound
definition. Moving the outer loop to `i + 1` is therefore safe.

**Trace the examples**

For `[2,7,11,15]` with target nine, the first outer index holds two and the
complement is seven. Lower bound in indices one through three returns index
one, whose value is seven. The source converts zero-based positions to
`[1,2]`.

For `[2,3,4]` with target six, the complement to the first value is four.
Searching from index one returns index two, producing `[1,3]`.

For `[-1,0]` with target negative one, complement zero is found at index one.
Signs do not affect binary-search correctness; only non-decreasing order
matters.

Consider `[1,2,3,4,6]` with target ten. Early left values search for absent
large complements. Eventually index three, value four, searches the suffix for
six and returns the final index. This illustrates why the outer loop may
perform many separate binary searches before reaching the guaranteed pair.

**Convert to the required indexing convention**

All Python accesses are zero-based. The problem asks for one-based indices, so
the return statement adds one to both `i` and `j`.

The loop never allows `i == j`, and `lo=i+1` preserves `i < j`. The source has
no fallback return after the loop, but the Reference guarantees exactly one
solution. Under that contract, some iteration must return. On invalid input
with no solution, Python would implicitly return `None`.

**Why the found pair is correct**

For each earlier `i`, a complete lower-bound search proves whether its unique
needed complement exists to the right. When a match appears,

`numbers[j] == target - numbers[i]`,

so their sum is `target`, and their indices are distinct and ordered. If the
solution begins at a later position, all earlier rejections are conclusive and
the loop reaches it.

The input is never modified, and no auxiliary array or hash table is created.

**Exact-source dependencies**

The method uses `List` annotations and `bisect_left` without imports. A
standalone module needs `from typing import List` and
`from bisect import bisect_left`. Otherwise it fails before realizing the
described search.

## Complexity detail

Let $n$ be the array length. There can be $O(n)$ outer iterations, and each
lower-bound search takes $O(\log n)$ time. The exact worst-case time is
$O(n\log n)$, not the manifest's $O(n)$.

The algorithm stores scalar indices and complement values, while
`bisect_left` is iterative library machinery. Auxiliary space is $O(1)$,
matching the manifest.

## Alternatives and edge cases

- **Two pointers:** Start at both ends; move the left pointer for a sum below target and the right pointer for a sum above target. It achieves the required $O(n)$ time and $O(1)$ space.
- **Hash map:** Finds complements in expected $O(n)$ time but uses $O(n)$ storage, violating the constant-space requirement.
- **Brute force:** Tests every index pair in $O(n^2)$ time.
- **Duplicate values:** Searching from `i + 1` permits two equal values at distinct indices.
- **Negative target and values:** Subtraction and sorted comparisons remain valid.
- **One-based output:** Both internal indices must be incremented exactly once.
- **Unique solution:** It justifies returning the first match and omitting a no-solution result.
- **Same-element prohibition:** The lower search boundary enforces it.
- **Manifest mismatch:** Repeated binary searches are $O(n\log n)$, not linear.
- **Missing imports:** Both `bisect_left` and `List` must be provided for standalone execution.
