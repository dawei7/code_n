## General

**Sorting turns a global duplicate question into adjacent comparisons**

In the original unsorted array, two equal values can be arbitrarily far apart.
Checking every pair would eventually find a duplicate, but an array of length
$n$ has $n(n-1)/2$ index pairs, which is quadratic work.

The exact solution first evaluates `sorted(nums)`. Sorting groups values in
non-decreasing order. If a value occurs at least twice, all copies of that value
form one consecutive block in the sorted list. Therefore some adjacent pair in
that block must be equal. Conversely, equal adjacent entries clearly came from
two different array positions with the same value and prove that a duplicate
exists.

This equivalence means the method no longer needs to compare arbitrary pairs.
It needs only one comparison between each neighboring pair after sorting.

**What `pairwise` produces**

For a sequence `[x0, x1, x2, x3]`, `pairwise` yields
`(x0, x1)`, `(x1, x2)`, and `(x2, x3)`. There are $n-1$ such pairs for a
length-$n$ sequence. Each interior element participates once as a right member
and once as a left member, ensuring that every adjacency boundary is examined.

The generator expression `a == b for a, b in pairwise(sorted(nums))` converts
each adjacent pair into a boolean. It produces `True` exactly at a boundary
where the two sorted values are equal.

`pairwise` and the generator are lazy: they provide the next pair or boolean
only when requested. They do not allocate a second list containing all pairs
or all comparison results.

**Why `any` is exactly the requested logical operation**

The problem asks whether at least one repeated value exists. Python's `any`
returns `True` if at least one generated condition is truthy and returns
`False` if every generated condition is false. It also short-circuits: as soon
as it receives the first `True`, it stops requesting more adjacent pairs.

For `nums = [1, 2, 3, 1]`, sorting creates `[1, 1, 2, 3]`. The first pair is
`(1, 1)`, its comparison is true, and `any` immediately returns `True`. For
`nums = [1, 2, 3, 4]`, every adjacent comparison is false, the generator is
exhausted, and `any` returns `False`.

The early exit applies only to the adjacency scan. `sorted(nums)` must finish
constructing and sorting the entire list before `pairwise` can yield its first
pair. Thus a duplicate discovered at the first sorted boundary does not avoid
the sorting cost.

**Why checking only neighbors cannot miss a duplicate**

Assume some value `v` appears in at least two original positions. In sorted
order, no value smaller than `v` can occur after `v`, and no value larger than
`v` can occur before `v`. All occurrences of `v` are consequently contiguous.
Among two or more contiguous copies, at least the first two are adjacent, so
the generator produces the comparison `v == v` and `any` returns true.

In the other direction, if `any` returns true, it received an adjacent pair
`(a, b)` with `a == b`. Those are two elements of the sorted copy and therefore
two elements from the input multiset. Sorting can reorder values but cannot
create an extra occurrence. Hence the input contains a duplicate.

If `any` returns false, every neighboring pair in sorted order differs. A
repeated value would have formed an equal neighboring pair by the first
argument, so no repeated value can exist. These cases cover every possible
input.

**Duplicates retain multiplicity**

The contract asks whether any value appears at least twice, not whether two
distinct values are somehow equal after transformation. Sorting retains every
element and its multiplicity. Two copies, ten copies, and duplicates of a
negative number are all handled the same way. The method does not convert the
input to a set or discard repeated entries before testing them.

**The exact source differs from the branch metadata**

The manifest summary says this branch scans once with a set of prior values and
declares $O(n)$ time. The exact source contains no set. It sorts a copied list
and compares adjacent values. Its actual worst-case time is $O(n\log n)$, not
$O(n)$. Both strategies solve the problem, but they have different data flow,
mutation behavior, and complexity, so this document follows the executable
source rather than repeating the inconsistent summary.

The source also references `List` and `pairwise` without local imports. It
assumes the execution environment provides the annotation name and
`itertools.pairwise`.

## Complexity detail

Let $n$ be `len(nums)`. Creating and sorting the copy takes $O(n\log n)$ time
in the worst case. The adjacent scan consumes at most $n-1$ pairs, which is
$O(n)$ time and is dominated by sorting. Total time is $O(n\log n)$. Python's
Timsort may exploit existing order on particular inputs, but the general bound
remains the appropriate source-level claim.

`sorted(nums)` allocates a new list of $n$ references, so auxiliary space is
$O(n)$. Python's sorting implementation can also use linear temporary storage
in the worst case. The `pairwise` iterator, generator expression, and `any`
state use only $O(1)$ additional space beyond that sorted list. The original
`nums` list is not modified.

## Alternatives and edge cases

- **Hash set of seen values:** Scan the original list and return immediately when a value is already in the set. This matches the manifest, gives expected $O(n)$ time and $O(n)$ space, and may stop before reading the whole array; hash operations have expected rather than unconditional constant time.
- **In-place sorting:** Calling `nums.sort()` avoids the separate top-level copy and then uses the same adjacent check. It changes the caller's order and Python sorting still has implementation-dependent temporary memory.
- **Nested pair comparison:** Compare each position with every earlier position. It uses $O(1)$ extra space and can stop early, but worst-case time is $O(n^2)$ and is unsuitable for $n$ up to $10^5$.
- **Counting array:** Direct frequencies are excellent for a small numeric domain, but values here span from $-10^9$ to $10^9$; allocating that range would be wasteful compared with sorting or hashing.
- **One element:** `pairwise` yields no pairs, and `any` over an empty generator returns `False`, which is correct because no value appears twice.
- **Two equal elements:** Sorting leaves them adjacent, the sole comparison is true, and the method returns `True`.
- **Two different elements:** The sole adjacent comparison is false, so the method returns `False`.
- **Many copies of one value:** The first two copies are adjacent after sorting. `any` stops at the first equal pair; it does not need to count all occurrences.
- **Negative and zero values:** Ordinary integer ordering places them correctly, and equality semantics are unchanged. No numeric offset is needed.
- **Already sorted or reverse-sorted input:** The logic is identical. Sorting still creates a separate list, and the later scan checks adjacent values in non-decreasing order.
- **Input preservation:** Because the code uses `sorted(nums)` rather than `nums.sort()`, callers observe the original list in its original order after the method returns.
