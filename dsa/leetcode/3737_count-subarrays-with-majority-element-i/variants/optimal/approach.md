## General

**Translate strict majority into one arithmetic test**

For a candidate subarray of length `L`, let `f` be the number of positions equal to `target`. The target is a strict majority exactly when

$$
f>\frac{L}{2}.
$$

Multiplying by two avoids fractions:

$$
2f>L.
$$

The exact source maintains `f` as `cnt` and tests

`cnt * 2 > j - i + 1`.

The strict greater-than sign matters. Equality means the target occupies exactly half of an even-length subarray, which is not a majority.

**Enumerate every subarray while reusing counts**

The outer loop fixes each possible left endpoint `i`. For that new left boundary, `cnt` starts at zero. The inner loop advances `j` from `i` through the end, growing

`nums[i:j + 1]`

one element at a time.

When the appended value equals `target`, `int(nums[j] == target)` is one and increments `cnt`. Otherwise it is zero and leaves the target frequency unchanged.

The current length is `j-i+1`. After updating the frequency, the code applies the exact majority inequality and adds one to `ans` when it holds.

For `nums=[1,2,2,3]` and `target=2`, fixing `i=1` produces candidates `[2]`, `[2,2]`, and `[2,2,3]`. Their target frequencies are one, two, and two; all satisfy twice the frequency greater than lengths one, two, and three. Other left endpoints discover the remaining valid ranges.

**Why repeated work is limited to endpoint enumeration**

Without reuse, counting target occurrences inside each selected subarray would cost another linear scan and produce $O(n^3)$ time. For a fixed `i`, extending `j` changes the frequency by at most one, so the source updates it in constant time.

Resetting `cnt` for the next left endpoint is necessary because the candidate family changes. The given limit `n<=1000` permits all endpoint pairs to be examined directly.

**Why the answer is exact**

Every nonempty contiguous subarray has one unique pair `(i,j)` with `0<=i<=j<n`. The nested loops visit every such pair exactly once. At that iteration, `cnt` equals the exact number of target occurrences because it began at zero and was incremented for each matching position from `i` through `j`.

The arithmetic condition is equivalent to the definition, so every counted pair is valid and every valid pair is counted. Since endpoint pairs are unique, overlapping subarrays and equal value sequences at different positions are correctly treated as separate subarrays.

If `target` never occurs, `cnt` remains zero and no positive length can satisfy the inequality. If every element equals `target`, `cnt=L` for every candidate and all `n(n+1)/2` subarrays are counted.

**The manifest does not describe this exact source**

The Optimal manifest summarizes a unit-step prefix-balance method with $O(n)$ time and $O(n)$ space. The actual protected source shown here does not implement that algorithm. It contains nested endpoint loops and one scalar counter.

This approach document follows the executed source, as requested. Its true complexity is quadratic time and constant auxiliary space. Calling it linear would misteach both the algorithm and its scaling behavior.

The code remains correct for the stated smaller version because `n` is at most 1000. A faster prefix-order-statistics method may be appropriate for a larger constraint, but it is an alternative rather than an explanation of this implementation.

## Complexity detail

For left endpoint zero, the inner loop performs `n` iterations; for left endpoint one, `n-1`; and so on. The total is

$$
n+(n-1)+\cdots+1=\frac{n(n+1)}2=O(n^2).
$$

Each iteration does constant work, so actual time complexity is $O(n^2)$.

Only `n`, `ans`, loop indices, and `cnt` are stored. The actual auxiliary space complexity is $O(1)$. These bounds explicitly contradict the manifest's $O(n)$ time and $O(n)$ space because the manifest describes a different algorithm.

The number of subarrays can be roughly $n^2/2$; Python integers safely hold the answer.

## Alternatives and edge cases

- **Recount every candidate from scratch:** This is correct but costs $O(n^3)$. Incremental right-end extension removes the extra scan.
- **Transform target to `+1` and others to `-1`:** A subarray has target majority when its transformed sum is positive. Counting positive-sum subarrays with prefix sums and an order-statistics structure can improve scaling, but that is not the exact source.
- **Use a sliding window:** Majority is not monotonic under arbitrary expansion and shrinking, so a standard two-pointer rule cannot count all valid ranges safely.
- **Follow the manifest's claimed linear method:** Counting earlier smaller prefix balances generally requires a Fenwick tree or equivalent and is not constant time per position without structure. It must not be attributed to these nested loops.
- **Exactly half target values:** `2f=L` fails because majority is strict.
- **Odd-length boundary:** Integer multiplication avoids rounding questions; `2f>L` works uniformly.
- **Single target element:** A one-element matching subarray is valid.
- **Single non-target element:** Its frequency is zero and it is invalid.
- **Target absent:** The answer remains zero.
- **Every value is target:** Every subarray is valid, yielding `n(n+1)/2`.
- **Duplicate value sequences at different indices:** They are different subarrays and are each counted because the task is index-based.
- **Large numeric values:** Only equality with `target` matters; magnitude does not affect memory or running time.
