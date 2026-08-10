## General

Checking all pairs would take quadratic time. Sorting reveals a much smaller candidate set: the globally closest values must be adjacent in sorted order.

**Why only adjacent sorted values matter**

Suppose sorted values `a` and `b` are not adjacent, with `a < x < b` for some input value `x` between them. Then both `x - a` and `b - x` are positive and smaller than `b - a`. Therefore, the nonadjacent pair `[a, b]` cannot achieve the global minimum difference.

Every pair that can be globally minimal is consequently among the $n-1$ adjacent pairs after sorting. Because the input values are distinct, every adjacent difference is positive.

The code begins with `arr.sort()`. This both orders the candidate pairs and guarantees that for adjacent values `a, b`, the absolute difference is simply `b - a`; no `abs` call is needed.

**Find the minimum adjacent gap**

`pairwise(arr)` yields consecutive tuples:

`(arr[0], arr[1])`, `(arr[1], arr[2])`, and so forth.

The generator expression `b - a for a, b in pairwise(arr)` produces every adjacent gap. Applying `min` finds the smallest one and stores it in `mi`. The constraint that the array has at least two values guarantees that this generator is nonempty.

The exact code makes a second `pairwise` traversal rather than storing all gaps. A `pairwise` iterator is consumed as it runs, so constructing a new one for the result pass is necessary.

**Collect every adjacent pair with that gap**

The list comprehension again visits adjacent sorted values and includes `[a, b]` exactly when `b - a == mi`.

Every returned pair automatically satisfies `a < b` because input values are distinct and sorted. The pairs themselves appear in ascending order because their first elements follow sorted array order. No additional sorting of the output is needed.

For `arr = [4, 2, 1, 3]`, sorting gives `[1, 2, 3, 4]`. The gaps are one, one, and one, so `mi` is one and all three adjacent pairs are returned.

For `[3, 8, -10, 23, 19, -4, -14, 27]`, the sorted values are `[-14, -10, -4, 3, 8, 19, 23, 27]`. The smallest adjacent gap is four. The second pass returns `[-14, -10]`, `[19, 23]`, and `[23, 27]` in the required order.

**Why the output is complete and exclusive**

Every returned pair consists of input values, is ordered increasingly, and has difference `mi`. Since `mi` is the minimum over all adjacent gaps and every global minimum must be adjacent, it is also the minimum over all possible input pairs. Thus every returned pair is valid.

Conversely, take any pair with global minimum absolute difference. If another sorted value lay strictly between its endpoints, that intermediate value would form a smaller pair, a contradiction. The pair must be adjacent, the second traversal visits it, and its gap equals `mi`, so it is included. No valid minimum pair is omitted.

Sorting is the main structural step. Once it is done, both passes are simple linear scans that never compare distant pairs.

## Complexity detail

Let $n$ be the length of `arr`.

Python sorting takes $O(n\log n)$ time in the worst case. Each `pairwise` traversal visits $n-1$ adjacent pairs, so the two scans together take $O(n)$ time. Overall time complexity is $O(n\log n)$.

Python’s Timsort may use $O(n)$ temporary memory in the worst case even though it sorts the input list in place. The returned list can itself contain $O(n)$ pairs, for example when the input is an arithmetic progression. Thus implementation-aware auxiliary space is $O(n)$ for sorting, and output space is $O(n)$.

The method mutates `arr` by sorting it. The generators themselves use constant iterator state rather than materializing all adjacent pairs.

## Alternatives and edge cases

- **One post-sort pass:** Track the smallest gap and current answer simultaneously, clearing the answer when a smaller gap appears. It removes one linear pass but retains the same $O(n\log n)$ bound.
- **Counting over the bounded value range:** Mark all values from the allowed range and scan in numerical order. This can take $O(n+R)$ time and $O(R)$ space for range width $R$.
- **Brute-force all pairs:** It is simple but costs $O(n^2)$ time and ignores the ordering insight.
- **Exactly two values:** There is one adjacent pair, `min` receives one gap, and that pair is returned.
- **Negative values:** Sorting and subtraction work unchanged; adjacent order ensures `b - a` is positive.
- **Equal minimum gaps:** The comprehension includes all of them, not only the first.
- **Distinctness guarantee:** It ensures `a < b` and a positive minimum. Duplicate inputs would introduce zero-gap pairs and require interpreting whether duplicate occurrences are allowed.
- **Output ordering:** Scanning adjacent pairs from left to right after sorting automatically gives lexicographic pair order.
- **Consumed iterator:** The first `pairwise` generator cannot be reused after `min`. The code correctly constructs a second iterator.
- **Input mutation:** Use a sorted copy if preserving the caller’s original order is required outside this contract.
