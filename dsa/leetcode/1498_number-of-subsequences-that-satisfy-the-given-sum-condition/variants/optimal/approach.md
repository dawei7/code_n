## General
**Sort without changing how many index selections exist**

The condition depends only on the minimum and maximum selected values, not on the positions between them. Sorting permutes the original indexed elements but gives a one-to-one correspondence between index subsets before and after the permutation. Duplicate values remain separate array positions, so their distinct subsequences are still counted separately.

After sorting, keep indices `left` and `right` around the unresolved range. Precompute $2^e \bmod M$ for every exponent $0 \le e \le N$, because each valid endpoint choice will contribute a power of two.

**Count every subsequence whose first selected index is `left`**

Suppose `nums[left] + nums[right] <= target`. Any subsequence that includes `nums[left]` and chooses an arbitrary subset of the `right - left` later positions through `right` is valid. Its minimum is `nums[left]`, and even if it includes the largest available value, its maximum is at most `nums[right]`.

Each of those later positions may be independently included or omitted, giving exactly

$$
2^{\texttt{right}-\texttt{left}}
$$

valid subsequences. This count includes the singleton containing only `nums[left]`. Add the power modulo $M$, then increment `left`. Every counted subsequence has `left` as its smallest selected sorted index, so no later iteration can count it again.

**Discard an endpoint that cannot participate**

If `nums[left] + nums[right] > target`, then `nums[right]` cannot belong to any valid subsequence made from the unresolved range. Every possible minimum there is at least `nums[left]`, so pairing it with `nums[right]` would make the endpoint sum no smaller.

Decrement `right` without adding anything. The right pointer never needs to move back: once an endpoint is too large for the smallest remaining value, it is too large for all later minima as well.

**Why the two pointer cases are exhaustive**

At each step, either the endpoint sum is valid or it is not. In the valid case, the power-of-two block contains exactly all unresolved subsequences whose first selected index is `left`; removing that left endpoint cannot affect subsequences whose first index is later. In the invalid case, no unresolved valid subsequence can contain `right`; removing that endpoint loses nothing.

The interval shrinks after every decision. By induction, all and only valid non-empty index subsets are counted when the pointers cross.

## Complexity detail
Sorting takes $O(N \log N)$ time. Building the powers table and moving both pointers take $O(N)$ additional time. The powers table and sorted copy use $O(N)$ auxiliary space.

The benchmark uses arrays of ones with `target = 1`, so no non-empty subsequence is valid. The reference moves the right pointer across the array once. A correct alternative that restarts a right-end search for every possible minimum performs $O(N^2)$ work, completes every tier, and is rejected by scaling.

## Alternatives and edge cases
- **Binary search for each minimum:** after sorting, find the last compatible maximum independently for every left index and add the same power-of-two contribution. This is correct in $O(N \log N)$ time but repeats searches that the monotone right pointer shares.
- **Restarted linear search:** scan down from the last index for every possible minimum. It preserves the counting formula but takes $O(N^2)$ time.
- **Enumerate all subsequences:** testing every non-empty index subset takes exponential time and is infeasible at $N=10^5$.
- **Duplicate values:** equal values at different indices represent distinct subsequence choices and must not be deduplicated.
- **Singleton subsequence:** its minimum and maximum are the same value, so it is valid exactly when twice that value is at most `target`.
- **No valid value:** if even twice the smallest number exceeds `target`, the result is `0`.
- **Every subsequence valid:** if the smallest-plus-largest condition holds for the whole sorted array, the answer is $2^N-1$ modulo $M$.
- **Modulo discipline:** reduce every accumulated power and answer update modulo $10^9+7$.
- **Input order:** sorting is valid for counting index subsets even though a subsequence normally preserves original order, because each selected index set has exactly one sorted-image index set.
- **Pointer equality:** when `left == right`, the contribution is $2^0=1$, representing the singleton at that position.
