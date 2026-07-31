## General

Store every array value in a hash set, then inspect the positive multiples in their natural increasing order: $k, 2k, 3k, \ldots$. Stop at the first value absent from the set.

The stopping value always exists quickly. An array of length $n$ cannot contain all of the first $n+1$ distinct positive multiples, so the answer is at most $(n+1)k$. Each earlier candidate was explicitly found in the array, while the returned candidate was not. Because candidates are visited in increasing order, that absent value is necessarily the smallest one requested.

## Complexity detail

Let $n$ be `nums.length`. Building the set takes $O(n)$ expected time and space. At most $n+1$ multiples are checked, each with expected $O(1)$ hash-set membership, so total expected time is $O(n)$ and auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Repeated list membership:** Checking each multiple directly against `nums` is correct but can take $O(n^2)$ time when many consecutive multiples are present.
- **Sorting:** Sorting can scan the relevant multiples in $O(n\log n)$ time, but it is slower asymptotically and may mutate the input unless a copy is made.
- **Duplicates:** Repeated array values do not cover additional multiples; the set naturally collapses them.
- **Unrelated values:** Numbers not divisible by `k` never affect which positive multiple is first missing.
- **First multiple absent:** If `k` itself is missing, return it even when larger multiples occur.
- **Answer beyond the input bound:** The missing multiple can exceed every `nums[i]`, such as `101` when `k = 1` and the array contains `1` through `100`.
