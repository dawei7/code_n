## General

The result consists of two independent halves with a direct description. The first half is `nums` in its existing order. The second half visits the same elements from index $n-1$ down to index $0$. Concatenating `nums` with the reverse slice `nums[::-1]` expresses those two requirements exactly and leaves the input unchanged.

For each $0 \le i < n$, the concatenation places `nums[i]` at result index `i`. In the reverse slice, its element at offset $i$ is `nums[n - i - 1]`; concatenation places that value at result index `n + i`. Both required equations therefore hold at every index, and the returned array has exactly $2n$ elements.

## Complexity detail

Let $n$ be the length of `nums`. Producing the reverse copy and the final result touches $O(n)$ values, so the time complexity is $O(n)$. The returned array and the temporary reverse slice occupy $O(n)$ space. Even an implementation that writes directly into one preallocated result needs $O(n)$ output space because the contract requires $2n$ returned elements.

## Alternatives and edge cases

- **Preallocated two-pass construction:** Allocate $2n$ positions and fill both equations by index. This is also $O(n)$ time and makes the formal mapping explicit, but it is more verbose.
- **Reverse iterator:** Extend a copy of `nums` with a reverse iterator to avoid materializing a separate reverse slice before the final array; the asymptotic bounds remain $O(n)$ time and $O(n)$ result space.
- **Repeated front insertion:** Building the reversed half by inserting each value at index zero is correct but shifts the existing prefix each time and can take $O(n^2)$ time.
- **Singleton input:** Its reverse is identical, but the result still has two elements because both halves are required.
- **Duplicate values:** Every occurrence is copied independently; no deduplication or counting is involved.
- **Input preservation:** Reversing `nums` in place would destroy the forward half unless a copy had already been retained, so constructing a new result is the clearer contract-safe choice.
