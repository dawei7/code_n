## General

**Why sorting reveals the only possible progression order**

An arithmetic progression has one constant difference between every adjacent pair. If a collection of numbers can be rearranged into such a progression, arranging it in nondecreasing order must also form a progression. A positive-difference progression appears in ascending order, a negative-difference progression appears in descending order, and a zero-difference progression looks the same in every order.

The stored source sorts `arr` in place. It then defines `d = arr[1] - arr[0]` as the required adjacent gap and checks whether every remaining adjacent pair has that same gap.

The input length is at least two, so accessing positions zero and one is safe. Negative values and duplicate values require no special syntax: subtraction handles negatives, and all-equal input produces `d = 0`.

**How pairwise drives the check**

`pairwise(arr)` yields adjacent tuples:

`(arr[0], arr[1])`, `(arr[1], arr[2])`, and so forth.

For each tuple `a, b`, the generator tests `b - a == d`. `all` consumes those Boolean results lazily. It returns false as soon as one adjacent difference disagrees, or true if every pair agrees.

The first pair is tested again even though its difference defined `d`. That comparison is necessarily true, but keeping it in the generator makes the expression uniform. For a two-element array, `pairwise` yields exactly one pair and `all` returns true, as any two numbers can form an arithmetic progression.

The source assumes `pairwise` is available, normally from `itertools`. It was added to Python in version 3.10.

**Why equal sorted gaps are sufficient**

If every adjacent sorted difference equals `d`, then

$$
arr[i] = arr[0] + i d
$$

for every index $i$. This follows by repeatedly adding the common adjacent difference. Therefore, the sorted array itself is a valid rearrangement into an arithmetic progression, proving sufficiency.

**Why equal sorted gaps are necessary**

Suppose some rearrangement forms an arithmetic progression. If its common difference is negative, reverse it to obtain the same values with positive difference. If the difference is zero, all values are equal. Thus there is a valid nondecreasing progression using the collection.

The nondecreasing order of a multiset is uniquely determined up to exchanging equal values, so it matches the order produced by sorting. Consequently, the sorted adjacent gaps must all be equal. If the code finds two different gaps, no other permutation can repair the missing or duplicated spacing.

For `[3, 5, 1]`, sorting gives `[1, 3, 5]` and both gaps are two. For `[1, 2, 4]`, the gaps are one and two, so the generator fails.

**Mutation is part of the exact behavior**

`arr.sort()` rearranges the caller-provided list. The method returns only a Boolean, but the caller will observe the sorted input afterward. If preserving input order matters, a copy must be sorted instead.

Sorting also means the method is not the linear-time hash-set approach described by the Optimal manifest. It is the straightforward sort-and-check implementation from the editorial's first approach.

## Complexity detail

Let $N$ be the array length. Python sorting costs $O(N\log N)$ worst-case time. The adjacent-pair generator visits $N-1$ pairs in the worst case, adding $O(N)$. Total time is $O(N\log N)$.

`pairwise` and the generator used by `all` are lazy and use $O(1)$ explicit additional state. However, Python's Timsort can require $O(N)$ temporary memory in the worst case. Thus the implementation's practical auxiliary-space bound is $O(N)$.

The manifest states expected $O(N)$ time and $O(N)$ space for an endpoint-arithmetic plus hash-set method. Its space bound is compatible, but its time bound does not describe the exact stored sort. A set-based membership proof can achieve expected linear time, while an in-place placement method can achieve linear time and constant extra data under careful conditions.

## Alternatives and edge cases

- **Endpoint arithmetic plus set:** Compute minimum, maximum, and the required gap, then verify every expected term exists with appropriate uniqueness handling. It achieves expected $O(N)$ time and $O(N)$ space.
- **In-place index placement:** Map each value to its required progression index and swap values into position. It can use $O(1)$ extra data but must handle zero difference, divisibility, and duplicates carefully.
- **Sort a copy:** `sorted(arr)` preserves the caller's list but allocates a new list.
- **Two elements:** They always form an arithmetic progression because there is only one adjacent difference.
- **All equal:** The common difference is zero and every comparison succeeds.
- **Duplicates mixed with distinct values:** Sorting exposes a zero gap next to a nonzero gap, so the method returns false.
- **Negative values:** Sorting and subtraction work without modification.
- **Descending valid order:** Sorting converts it to the corresponding ascending progression with the negated common difference.
- **Input mutation:** The exact source permanently sorts `arr`.
- **Early mismatch:** `all` stops checking when the first unequal gap is found, although sorting has already completed.
- **Missing import:** `pairwise` must be supplied from `itertools` in a standalone module.
