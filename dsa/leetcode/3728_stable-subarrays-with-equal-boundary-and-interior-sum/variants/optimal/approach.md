## General

**Rewrite the interior sum with prefix sums**

Let `s[t]` be the sum of the first `t` elements, with `s[0] = 0`. The source builds this array with `accumulate(capacity, initial=0)`, so

$$
s[t]=\sum_{i=0}^{t-1}\texttt{capacity}[i].
$$

For endpoints `l` and `r`, the elements strictly inside are indices `l+1` through `r-1`. Their sum is

$$
s[r]-s[l+1].
$$

A stable subarray requires both endpoints to equal each other and the interior sum:

$$
\texttt{capacity}[l]=\texttt{capacity}[r]
$$

and

$$
\texttt{capacity}[l]=s[r]-s[l+1].
$$

Move `s[l+1]` to the other side of the second equality:

$$
\texttt{capacity}[l]+s[l+1]=s[r].
$$

Therefore a left endpoint `l` matches a right endpoint `r` exactly when the pair

$$
(\texttt{capacity}[l],\ \texttt{capacity}[l]+s[l+1])
$$

equals

$$
(\texttt{capacity}[r],\ s[r]).
$$

This converts two conditions involving a whole interior range into equality of a two-part hash key.

**Insert a left endpoint only when it becomes length-eligible**

The loop visits right endpoints `r` from two through `n-1`, because a length-three subarray is the earliest possible candidate. Before querying `r`, it sets `l = r - 2` and inserts that left endpoint's key into `cnt`.

At right endpoint `r`, every valid left endpoint must satisfy `l <= r - 2`. Earlier iterations already inserted `0` through `r - 3`, and the current insertion adds `r - 2`. Thus the dictionary contains every and only length-eligible left endpoint.

This timing prevents length-one or length-two ranges from being counted. The dictionary is cumulative because an old left endpoint remains eligible for all later right endpoints.

**Count all matching left endpoints at once**

`cnt[key]` is the number of eligible left endpoints with that transformed key. After inserting the newly eligible `l`, the statement

`ans += cnt[(capacity[r], s[r])]`

adds one for every left endpoint satisfying both stability equalities with the current `r`.

Multiple left endpoints may share a key, especially with zeros or repeated prefix sums. A count rather than a Boolean is necessary because each endpoint pair defines a different subarray and all overlapping or nested stable ranges must be counted.

For `capacity = [9, 3, 3, 3, 9]`, the outer left endpoint zero has key

$$
(9,\ 9+s[1])=(9,18).
$$

At `r=4`, the query key is

$$
(9,\ s[4])=(9,18),
$$

so the full array is counted. The inner range `[3,3,3]` is detected by the analogous key for `l=1` and `r=3`.

Negative values require no special treatment. Prefix sums and tuple keys can be negative, and the algebra remains exact. In `[-4,4,0,0,-8,-4]`, cancellations make the interior sum negative, but matching integer keys still identify the valid full range.

**Why the total is exact**

Take any stable subarray `[l,r]`. Its length condition gives `l <= r-2`, so `l` has been inserted by the time the loop processes `r`. Stability makes its stored key equal the query key, so it contributes one.

Conversely, every dictionary match gives equal endpoint values from the first tuple component. Equality of the second components gives `capacity[l]+s[l+1]=s[r]`, which rearranges to the required interior-sum equality. Since only eligible left endpoints are stored, the length is at least three. Each pair is queried once at its unique right endpoint, so there are no omissions or duplicate counts.

## Complexity detail

Let `n` be the array length. Constructing the prefix-sum list takes $O(n)$ time and space. The loop performs `n-2` iterations, each with expected $O(1)$ dictionary insertion and lookup, so total expected time is $O(n)$.

The prefix array has `n+1` entries. The dictionary can contain up to `n-2` distinct keys, requiring $O(n)$ space. All remaining variables are constant-sized, giving $O(n)$ auxiliary space overall. Hash-table operations supply the expected-time qualification.

## Alternatives and edge cases

- **Enumerate all endpoint pairs:** Prefix sums make each stability test $O(1)$, but there are $O(n^2)$ pairs. The transformed-key count removes the quadratic enumeration.
- **Sum each interior directly:** This adds another linear factor and can reach $O(n^3)$. Prefix sums are the first essential reduction.
- **Key only by endpoint value:** Equal endpoints are necessary but not sufficient; their interior sum must also match. The transformed prefix component enforces that second condition.
- **Store a set of keys:** A set would lose multiplicity when several left endpoints share a key. The answer counts subarrays, so the dictionary stores counts.
- **Insert `r-1` before querying:** That would admit length-two ranges. Inserting exactly `r-2` enforces the minimum length without a later correction.
- **Length exactly three:** The interior consists of one value. The current insertion makes its left endpoint eligible immediately and handles this smallest case.
- **All zeros:** Every subarray of length at least three is stable. Repeated identical keys accumulate, allowing the query to add all eligible left endpoints.
- **Negative numbers:** Neither monotonic prefix sums nor a sliding window is assumed. Hashing exact signed sums works with arbitrary signs.
- **Large sums:** Prefix sums may exceed 32-bit range because values reach $10^9$ and length reaches $10^5$. Python integers are safe; fixed-width implementations need 64-bit storage.
- **Overlapping ranges:** The dictionary never removes earlier eligible endpoints, so all overlaps are counted independently.
