## General

**Use contiguity to replace each subarray sum with a prefix difference.**

A subarray must contain consecutive positions. That makes prefix sums useful because subtracting two cumulative totals cancels everything before the subarray.

Let $P_i$ be the sum of `nums[0]` through `nums[i]`, and define $P_{-1}=0$ for the empty prefix before the array. The sum of a subarray from index $a$ through index $i$ is

$$
P_i - P_{a-1}.
$$

To make that sum equal `k`, the prefix immediately before the subarray must satisfy

$$
P_i - P_{a-1} = k,
$$

or, after rearranging,

$$
P_{a-1} = P_i-k.
$$

This equation turns the problem around. When the scan reaches ending index `i` and its running prefix sum is `s`, there is no need to test every possible start. It only needs to know whether the specific earlier prefix sum `s - k` has occurred. A hash map provides that lookup in expected constant time.

**What the map stores and why it stores the earliest index.**

The dictionary `d` maps each prefix-sum value to the earliest index where that sum occurred. If `s - k` was first seen at index `p`, then the elements from `p + 1` through `i` sum to `k`, and their length is

$$
i-p.
$$

For a fixed ending index `i`, making `p` as small as possible makes this length as large as possible. That is why the source inserts a prefix sum only if it is not already present:

`if s not in d: d[s] = i`.

Overwriting an earlier occurrence with a later one could only shorten every future subarray that uses that prefix value. The actual numeric sum is identical, so the later occurrence provides no advantage for this maximum-length objective.

Repeated prefix sums are common when the array contains positive and negative values. For example, the running sums of `[1,-1,1,3]` are `1,0,1,4`. The sum `1` appears at indices `0` and `2`. If a later end needs a preceding sum of `1`, index `0` always creates a longer subarray than index `2`.

**Why the map begins with `{0: -1}`.**

A valid subarray may start at index zero. If the running sum at index `i` equals `k`, then the desired earlier prefix is `s-k=0`. Conceptually, that zero belongs to the empty prefix ending immediately before index zero, at index `-1`.

Storing `0: -1` unifies this boundary with every other lookup. Its computed length is

$$
i-(-1)=i+1,
$$

which is exactly the number of elements from index `0` through `i`. No separate `if s == k` branch is required.

This initialization is also important when `k = 0`. A zero-sum prefix ending at `i` can use the earliest zero at `-1`, giving the full prefix length rather than starting after a later occurrence of the same cumulative sum.

**The one-pass data flow.**

The variable `s` is the prefix sum at the current index, and `ans` is the greatest valid length found so far. Both begin at zero. At each pair `(i, x)`:

1. add `x` to `s`, so `s` becomes $P_i$;
2. look for `s - k` in `d`;
3. if it exists at index `p`, update `ans` with `i - p`;
4. record the current sum and index only if this is the sum's first occurrence.

The lookup uses only earlier prefixes because insertion happens afterward. More importantly, retaining the first occurrence maintains the map invariant: after processing index `i`, `d[v]` is the earliest index in `-1,0,\ldots,i` whose prefix sum equals $v$.

The source never allocates a full prefix-sum array. Once an older prefix has been summarized in the dictionary, only its value and earliest index matter. The running variable `s` is sufficient for the current prefix.

**Walk through `[1,-1,5,-2,3]` with `k = 3`.**

Initially, `d = {0: -1}`, `s = 0`, and `ans = 0`.

- At index `0`, `s = 1`. The needed prefix is `-2`, which is absent. Store `1: 0`.
- At index `1`, `s = 0`. The needed prefix is `-3`, which is absent. Do not overwrite the existing `0: -1`; the earlier index is better.
- At index `2`, `s = 5`. The needed prefix is `2`, which is absent. Store `5: 2`.
- At index `3`, `s = 3`. The needed prefix is `0`, found at `-1`. The subarray from `0` through `3` has length `3 - (-1) = 4`, so `ans` becomes `4`. Store `3: 3`.
- At index `4`, `s = 6`. The needed prefix is `3`, found at `3`. That identifies the one-element subarray `[3]`, whose length does not beat `4`.

The method returns `4`, corresponding to `[1,-1,5,-2]`.

**Why every reported length is valid.**

Suppose the lookup finds `d[s-k] = p` at current index `i`. By the map definition, the prefix through `p` sums to `s-k`, while the prefix through `i` sums to `s`. Their difference is

$$
s-(s-k)=k.
$$

That difference is exactly the sum from `p + 1` through `i`, so `i-p` is the length of a genuine contiguous subarray with the required sum. The algorithm never updates `ans` from an unrelated or noncontiguous selection.

**Why the longest valid subarray cannot be missed.**

Take any valid subarray from index $a$ through $b$. When the scan reaches $b$, its running sum is $P_b$, and the prefix before the subarray is $P_{a-1}=P_b-k$. That value has already been stored in `d`—including the special index `-1` when $a=0$.

The stored index is the earliest occurrence of that prefix value, so it is no later than $a-1$. The candidate length computed by the algorithm is therefore at least

$$
b-(a-1),
$$

the length of the chosen valid subarray. Thus, at every end index, the map produces the longest valid subarray ending there. Taking the maximum across all ends produces the global maximum.

## Complexity detail

Let $n$ be `len(nums)`. The method scans the array once. Each iteration performs a constant number of dictionary lookups or insertions, which are expected $O(1)$ in Python. The expected time complexity is therefore $O(n)$.

In the worst case, every prefix sum is distinct, so `d` stores the initial zero plus $n$ additional entries. Its space complexity is $O(n)$. The running sum and answer use $O(1)$ space beyond the map.

Hash-table operations have a theoretical collision-dependent worst case, but the standard complexity model for this solution uses expected constant-time hashing. The input values may be negative, yet that does not change the number of states or operations.

## Alternatives and edge cases

- **Enumerate all starts and ends:** There are $n(n+1)/2$ subarrays. Prefix sums can make each sum query $O(1)$, but enumerating all pairs still takes $O(n^2)$ time, which is too large for $n$ up to $2\cdot10^5$.

- **Sliding window:** A two-pointer window works when all numbers are nonnegative because expanding cannot decrease the sum and shrinking cannot increase it. Here negative values break that monotonic behavior, so a window can skip valid answers. Prefix differences impose no positivity requirement.

- **Store the latest prefix index:** This is appropriate for some minimum-length objectives, but it is wrong here. The earliest matching prefix always yields the longest subarray for a fixed end.

- **Store every occurrence:** Keeping a list of indices for each prefix sum is unnecessary. Only the earliest occurrence can maximize a future length, so the exact dictionary is both sufficient and smaller.

- **No matching subarray:** `ans` starts at zero and changes only after a valid prefix-difference match. If none exists, returning zero satisfies the contract.

- **The whole array is the answer:** The synthetic prefix `0: -1` detects it without a special case whenever the total running sum equals `k`.

- **`k = 0`:** Equal prefix sums identify zero-sum subarrays. Preserving the earliest occurrence is especially important because it maximizes the distance between equal cumulative totals.

- **Single element:** If that element equals `k`, the lookup finds the initial zero and returns length one. Otherwise, no update occurs and the answer is zero.

- **Large cumulative totals:** Python integers grow as needed. In a fixed-width language, the running prefix and `s-k` should use a sufficiently wide signed type; intermediate prefix differences can exceed the nominal range of individual elements or `k`.
