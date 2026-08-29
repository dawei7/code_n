## General

For a chosen integer `value`, every original element larger than `value` is replaced by `value`, while every element at most `value` stays unchanged. In mathematical form, the mutated contribution of an element $a$ is $\min(a,\texttt{value})$. We want the candidate whose resulting sum has the smallest absolute difference from `target`, and if two candidates have the same difference, we must choose the smaller one.

The exact Optimal solution sorts the array, builds prefix sums, and then evaluates every candidate from zero through the largest array value. Sorting and binary search make the mutated sum for one candidate much faster to compute than scanning the whole array again.

**Why candidates stop at the original maximum**

Let $M=\max(\texttt{arr})$. If `value >= M`, no array element is larger than `value`, so the mutation changes nothing. Every candidate at least $M$ produces exactly the original array sum.

Therefore, considering values above $M$ cannot produce a new sum. If that unchanged sum is optimal, the tie rule asks for the smallest candidate producing it, namely $M$. It is enough to test the inclusive range from zero through $M$, which is exactly what `range(max(arr) + 1)` generates.

Even though all array values and the target are positive, zero is a meaningful candidate. It changes every positive element to zero. The answer is not required to come from `arr`, so intermediate integers must also be considered.

**Sorting separates unchanged and capped values**

`arr.sort()` rearranges the input into nondecreasing order. For a fixed candidate `value`, `bisect_right(arr, value)` returns an index `i` with this division:

- indices from zero through `i - 1` contain values at most `value`, and
- indices from `i` through the end contain values strictly greater than `value`.

The “right” form of binary search places elements equal to `value` in the first region. That is convenient, although placing them in the capped region would produce the same numerical contribution because replacing `value` with itself changes nothing.

The first region remains unchanged by the mutation. Every element in the second region becomes exactly `value`. Once we know the sum of the first region and the number of elements in the second, the mutated sum follows immediately.

**Prefix sums for the unchanged region**

`s = list(accumulate(arr, initial=0))` creates a list of length `len(arr) + 1`. Its meaning is

$$
s[i]=\sum_{j=0}^{i-1}\texttt{arr}[j].
$$

The initial zero means `s[0] = 0`, the sum of an empty prefix. This removes a special case when no original value is at most the current candidate.

After `bisect_right` returns `i`, `s[i]` is exactly the sum of all unchanged elements. There are `len(arr) - i` elements greater than `value`, and each becomes `value`, so their total contribution is

`(len(arr) - i) * value`.

The full mutated sum is therefore

`s[i] + (len(arr) - i) * value`.

This formula is equivalent to summing $\min(a,\texttt{value})$ over every array element, but it costs only one binary search and constant arithmetic after preprocessing.

**Measuring the candidate's error**

The code computes

`d = abs(s[i] + (len(arr) - i) * value - target)`.

Absolute value matters because a mutated sum can fall below or rise above the target. A sum of 9 and a sum of 11 are equally close to a target of 10.

`diff` begins at positive infinity, so the first candidate, zero, necessarily improves it. `ans` begins at zero and is updated together with `diff` whenever a strictly smaller error is found:

`if diff > d`.

The strict comparison is how the tie rule is implemented. Candidates are visited in increasing order. If a later, larger candidate has the same error as the current best, `diff > d` is false, so `ans` keeps the earlier and smaller value. Using `>=` would overwrite it and incorrectly favor the larger tied candidate.

**Following a small example**

For `arr = [4,9,3]`, sorting gives `[3,4,9]` and the prefix sums are `[0,3,7,16]`.

At `value = 3`, `bisect_right` returns one because only the first element is at most three. The formula therefore gives

$$
s[1] + (3-1)\cdot 3 = 3+6=9.
$$

Its distance from target 10 is one. At `value = 4`, two elements stay unchanged and the $9$ becomes $4$, giving $3+4+4=11$, also distance one. Because value 3 was examined first and ties do not overwrite `ans`, the method returns 3.

This example also shows why using a prefix sum requires careful interpretation of `i`: it is a count and an exclusive boundary, not the last included index.

**Why exhaustive candidate evaluation is correct**

Every relevant integer candidate lies between zero and $M$, inclusive. The loop visits each exactly once. Sorting, `bisect_right`, and the prefix formula compute the exact mutated sum for that candidate, so `d` is its exact objective value.

After each iteration, `diff` is the smallest distance among candidates seen so far, and `ans` is the smallest candidate attaining that distance. A strict improvement replaces both; a tie preserves the smaller earlier candidate. When the loop finishes, “seen so far” covers the complete relevant domain. Therefore, `ans` is exactly the required value.

## Complexity detail

Let $n$ be the array length and $M=\max(\texttt{arr})$.

Sorting costs $O(n\log n)$ time. Building `s` with `accumulate` takes $O(n)$ time and stores $n+1$ numbers.

The candidate loop runs $M+1$ times. Each iteration performs `bisect_right` in $O(\log n)$ time and constant additional arithmetic. Thus, the exact total time is

$$
O(n\log n + M\log n).
$$

The prefix list requires $O(n)$ auxiliary space. Python's in-place sort can also use temporary memory, but the overall auxiliary bound remains $O(n)$.

These are the bounds of the exact source. The manifest's $O(n\log M)$ time and $O(1)$ space describe a different binary-search-on-answer strategy without a stored prefix list, not this exhaustive candidate loop. Because both $n$ and $M$ are at most $10^4$ or $10^5$ under the local constraints, the exact implementation can still be practical, but its explanation must retain the $M$ loop and prefix allocation.

## Alternatives and edge cases

- **Binary search on the monotone mutated sum:** The sum $\sum\min(a,v)$ never decreases as $v$ grows. Binary search can locate the crossing around `target` and compare neighboring candidates in $O(n\log M)$ time with $O(1)$ extra space if each sum is computed by scanning the array. This matches the manifest but is not the exact source.
- **Sorted analytic sweep:** After sorting, one can determine the best cap while moving through breakpoints and use prefix sums to avoid enumerating every integer up to $M$. This can reduce dependence on a large value range.
- **Rescan the array for every value:** It computes the same objective directly but costs $O(nM)$ time instead of using binary search and prefix sums.
- **Tie between adjacent candidates:** Increasing traversal plus the strict `diff > d` update keeps the smaller value automatically.
- **Target above the original sum:** All caps at least $M$ produce the unchanged sum, and $M$ is the smallest such cap. The loop includes it and returns it if that plateau is closest.
- **Target below every useful positive sum:** Candidate zero is included and may be the closest result even though zero is absent from the positive input array.
- **Single-element array:** The method tests every cap from zero through that element and chooses the integer closest to the target after capping.
- **Duplicate values:** `bisect_right` places all copies equal to the candidate in the unchanged prefix. The prefix sum and suffix count still represent every occurrence exactly once.
- **Input mutation:** `arr.sort()` changes the caller's list order. A caller that needs the original order must pass a copy, adding storage.
- **Large maximum value:** Runtime depends directly on $M$, even if `arr` contains very few elements. This is the main limitation of enumerating every candidate.
- **Integer arithmetic:** Python integers do not overflow. In a fixed-width language, the prefix and mutated sums may require a wider type than each individual array value.
