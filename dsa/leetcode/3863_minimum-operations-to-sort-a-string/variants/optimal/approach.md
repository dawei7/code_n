## General

**Classify the answer instead of simulating substrings**

Sorting any permitted substring never changes the string's multiset of characters. The globally sorted target is therefore uniquely determined: it is the input characters in non-descending order.

The restriction is that one operation may not sort the entire string. This makes the two endpoints decisive. A proper substring must omit at least the first character or omit at least the last character. If an operation omits an endpoint, that endpoint cannot move during that operation.

The source uses this endpoint fact to prove that every input belongs to one of five outcomes: zero operations, impossible for one special length-two case, or exactly one, two, or three operations.

**Zero operations: the string is already sorted**

The expression

`all(a <= b for a, b in pairwise(s))`

checks every adjacent pair. A string is non-descending exactly when no adjacent inversion exists, so this returns zero precisely for an already sorted input.

For a one-character string, `pairwise(s)` produces no pairs and `all` of the empty sequence is true. That is correct: a single character is sorted without any operation.

**The unsorted length-two case is impossible**

If `len(s) == 2` and the sortedness check failed, the two characters are in descending order. The only proper nonempty substrings have length one. Sorting a single character changes nothing, while sorting both characters would select the forbidden entire string. No operation can alter the state, so the source returns minus one.

For every length at least three, sorting is possible in at most three operations, as the later construction shows.

**Exactly when one operation is enough**

Let `mn=min(s)` and `mx=max(s)`.

If `s[0] == mn`, leave the first character fixed and sort the proper suffix `s[1:]`. That suffix contains every other character in non-descending order after the operation, and none is smaller than the global minimum at index zero. The whole string is sorted in one operation.

Symmetrically, if `s[-1] == mx`, sort the proper prefix `s[:-1]`. Every sorted prefix character is at most the global maximum fixed at the end, so the whole result is sorted.

These conditions are also necessary. Suppose one proper substring sort produces the globally sorted string. Because the substring is not the whole string, it omits at least one endpoint:

- if it omits index zero, the first character never moves and must already equal a global minimum in the final sorted string;
- if it omits index `N-1`, the last character never moves and must already equal a global maximum.

Even when the substring omits both endpoints, both conclusions apply. Therefore an unsorted string is one-operation sortable exactly when its first character is a minimum or its last character is a maximum. This proves the source's next condition rather than merely giving a sufficient shortcut.

**Two operations when an extreme occurs internally**

Assume the answer is not zero or one. If an occurrence of `mn` appears at an internal index `j`, first sort the prefix `s[0:j+1]`. It is proper because `j<N-1`. Sorting moves one minimum to index zero. Now the resulting string satisfies the one-operation condition, so sorting the suffix from index one through the end finishes the job.

If an occurrence of `mx` appears internally, use the mirrored construction. Sort the suffix beginning at that occurrence; the maximum moves to the final index. Then sort the prefix that excludes that final maximum.

The source detects either possibility with

`any(c in [mn, mx] for c in s[1:-1])`

and returns two. Because the earlier one-operation condition already failed, the result cannot be one, so the construction is minimal.

Repeated minima or maxima cause no difficulty. One internal occurrence is enough to expose the required endpoint, regardless of other copies.

**The remaining case requires exactly three operations**

Suppose the string is unsorted, has length at least three, is not one-operation sortable, and contains neither `mn` nor `mx` internally.

The minimum and maximum must occur somewhere. With no internal occurrence, they can occur only at the endpoints. The failed one-operation test says the first character is not `mn` and the last is not `mx`. Therefore

$$
s[0]=mx
\quad\text{and}\quad
s[N-1]=mn.
$$

Two operations cannot suffice. After the first operation, the intermediate string would have to be sortable by one final proper-substring sort. The necessity result above says that intermediate string would need `mn` at its first position or `mx` at its last position. But the first operation cannot move the minimum from the last index to the first without selecting a substring containing both endpoints, which would be the forbidden whole string. It likewise cannot move the maximum from the first index to the last. Thus the first operation cannot create a one-operation-sortable state, proving a lower bound of three.

Three operations always suffice:

1. Sort the prefix `s[0:N-1]`, excluding the final `mn`. Since `mx` begins inside this prefix and has no other occurrence outside the endpoints, sorting moves `mx` to index `N-2`.
2. Sort the two-character suffix `s[N-2:N]`. It contains `mx` followed by `mn`, so sorting it places `mn` at index `N-2` and `mx` at the final index.
3. Sort the prefix `s[0:N-1]` again. The fixed final character is now a global maximum, and sorting everything before it produces the complete target.

All three substrings are proper. The lower bound and construction establish that the source's final return value three is exact.

For `"cba"`, the sequence is `"cba" -> "bca" -> "bac" -> "abc"` by sorting the first two, last two, and first two characters. This is the smallest hard-case example.

**Why the answer never exceeds three**

The classification is exhaustive. After excluding sorted and unsortable length-two inputs, either an endpoint already has the useful extreme, an extreme exists internally, or both extremes occupy the wrong endpoints with none inside. Those cases need one, two, and three operations respectively. No search over the `O(N^2)` possible substrings is needed.

The exact source requires `pairwise` from `itertools` to be available.

## Complexity detail

Let `N` be the string length. The adjacent sortedness check is `O(N)`. In the paths that continue, computing `min(s)` and `max(s)` takes two more linear scans, and checking the interior takes at most one linear scan. A constant number of `O(N)` passes remains `O(N)` total time.

The generator used by `all` and `pairwise` stores only iterator state. The remaining variables are two characters and a few scalars. No sorted copy or substring is actually constructed by the algorithm; the described sorts are existence constructions used to determine the count. Auxiliary space is therefore `O(1)`, matching the manifest.

The algorithm returns only the minimum number, not the sequence of operations. Constructing and applying the witness operations literally would add output or mutation work, but it is unnecessary for the required function.

## Alternatives and edge cases

- **Breadth-first search over strings:** Generate every proper-substring sort until the target appears. This proves small cases but the state space and `O(N^2)` operations per state are far too large for `N=10^5`.
- **Try every single substring:** This can test whether one operation works but does not efficiently classify two or three operations. The endpoint necessity condition gives the one-operation answer directly.
- **Compare with a sorted copy:** It detects the zero case and mismatch positions, but constructing the full target uses `O(N)` extra space and still does not by itself prove the operation count.
- **First character is a minimum:** Sorting the suffix is legal even when other copies of the minimum occur later. The resulting sequence remains non-descending.
- **Last character is a maximum:** The symmetric proper-prefix construction works with duplicate maxima.
- **Internal extreme:** Either one internal minimum or one internal maximum is sufficient for a two-operation construction; both are not required.
- **Wrong extremes at endpoints:** When `mx` is first and `mn` is last with neither internal, two operations are impossible because one proper first operation cannot transport either extreme across both endpoints.
- **Length one:** It is already sorted and returns zero before the length-two branch.
- **Unsorted length two:** It is the only impossible case because every legal substring has length one and sorting it is a no-op.
- **Sorted length two:** It returns zero before the impossibility branch.
- **All characters equal:** Every adjacent comparison succeeds, so zero is returned.
- **Operation count versus performing operations:** The method proves the minimum and returns it; it intentionally does not mutate `s` or produce witness intervals.
- **Import dependency:** The protected source relies on `itertools.pairwise`, which requires an execution environment where that name is imported and supported.
