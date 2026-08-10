## General

**Rewrite a subarray sum using prefix sums.** A good subarray `nums[j..i]` must satisfy

$$
\lvert \texttt{nums}[j]-\texttt{nums}[i]\rvert=k.
$$

Equivalently, its first value must be either `nums[i] - k` or `nums[i] + k`. If `s` is the prefix sum through index $i$ and $P_j$ is the prefix sum strictly before index $j$, then

$$
\operatorname{sum}(j,i)=s-P_j.
$$

For a fixed right endpoint $i$ and a fixed required first value, maximizing the subarray sum means subtracting the smallest prefix-before-start sum among all earlier positions carrying that value. This is the reason for the dictionary `p`: it maps a possible first endpoint value to the minimum prefix sum seen immediately before an occurrence of that value.

**Understand the slightly unusual look-ahead update.** The source starts with

`p = {nums[0]: 0}`.

The prefix sum before index 0 is zero, so this correctly registers index 0 as a possible future starting position. Variable `s` also starts at zero.

At iteration $i$, the code first adds `nums[i]` to `s`. Thus `s` now equals the sum of `nums[0..i]`. It checks the dictionary before registering the next position. This guarantees every dictionary entry represents a start index no later than the current endpoint.

At the bottom of iteration $i$, if $i+1<n$, the source registers `nums[i + 1]` with prefix sum `s`. That is correct because `s` is exactly the prefix strictly before position $i+1$. The condition

`nums[i + 1] not in p or p[nums[i + 1]] > s`

keeps only the minimum such prefix for that endpoint value. The look-ahead may look less familiar than registering the current value before processing it, but it cleanly aligns each value with the prefix sum immediately preceding its position.

**Test the only two legal first values.** Let the current endpoint value be `x`. A good subarray ending here can begin with `x - k` or `x + k`, because these are exactly the values at absolute difference $k$. If `x - k` is present in `p`, the best sum using such a start is `s - p[x - k]`. The source updates `ans` with that value. It performs the symmetric lookup for `x + k`.

No other first value can meet the endpoint condition, so the two hash lookups are exhaustive.

**Why keeping only the minimum prefix is safe.** Suppose two earlier indices $j_1$ and $j_2$ have the same value required by the current endpoint, with prefix-before-start sums $P_1$ and $P_2$, and $P_1\le P_2$. Both starts satisfy the same absolute-difference condition. Their ending value and current prefix `s` are also identical. Then

$$
s-P_1\ge s-P_2.
$$

The second start can never produce a better sum for this or any later endpoint needing that value. Discarding every prefix except the minimum loses no optimal answer. This dominance argument is what compresses all possible starts into one dictionary entry per distinct value.

**Why negative sums must not be replaced by zero.** A valid good subarray can have a negative maximum, as in an all-negative input. Therefore `ans` begins at negative infinity rather than zero. Every valid candidate, including a negative one, can replace it. Only if no candidate was ever found does the final line return zero.

This distinction is essential: `ans == -inf` means “there was no good subarray,” whereas `ans = -6` means “good subarrays exist and the best has sum $-6$.” Initializing `ans` to zero would confuse those cases and violate the contract.

**A trace with a beneficial negative prefix.** Consider an endpoint value $5$ with $k=3$, so a legal start value is $2$. If earlier occurrences of 2 have prefix-before-start sums 7 and $-4$, the dictionary retains $-4$. If the current prefix sum is 10, the two candidate subarray sums would be 3 and 14. Keeping the smallest prefix chooses 14 automatically. Negative elements between earlier positions can make a later or earlier occurrence preferable; the map handles this without a sliding-window assumption.
For every right endpoint, the algorithm checks both and only possible first values. For each value, the dictionary retains the start with the minimum preceding prefix, which produces the maximum sum among all starts of that value. Therefore the candidate at this endpoint is the best good subarray ending there. Taking the maximum across all endpoints yields the best good subarray globally. If none exists, the untouched sentinel produces the required zero.

## Complexity detail

Let $N$ be the length of `nums` and $U$ its number of distinct values. The method performs one pass over the array. Each iteration uses a constant number of expected-$O(1)$ dictionary lookups or updates and constant arithmetic, so expected time is $O(N)$.

The dictionary stores at most one prefix sum for each distinct value that occurs as a possible start, hence $O(U)$ entries and $O(N)$ auxiliary space in the worst case. Variables `s`, `ans`, and loop indices use constant additional space. The input is not modified.

The expected-time qualification comes from Python hash-table behavior. Prefix sums and the answer can be much larger in magnitude than an individual element, but Python integers support the required range. Under standard problem analysis, their arithmetic and hashing are treated as constant time for the stated bounds.

## Alternatives and edge cases

- **Enumerate every subarray:** Checking both endpoints and summing directly costs up to $O(N^3)$; adding prefix sums reduces sums to $O(1)$ but still leaves $O(N^2)$ endpoint pairs.
- **Store every index per value:** This allows all legal starts to be revisited, but it can degrade to quadratic work. Only the minimum prefix-before-start value is relevant to maximizing a future sum.
- **Sliding window:** Negative values and a condition on endpoint values rather than window sum destroy the monotonicity a sliding window would need.
- **Kadane's algorithm alone:** Kadane finds an unconstrained maximum-sum subarray and does not enforce that the endpoint values differ by exactly $k$.
- **No good subarray:** Neither dictionary lookup ever succeeds for a legal endpoint pairing, `ans` remains negative infinity, and the method returns zero.
- **Best good sum is negative:** A valid negative candidate replaces the sentinel and is returned unchanged; zero is not used merely because it is numerically larger.
- **Repeated starting value:** The map retains the smallest preceding prefix, since every larger prefix is dominated for all future endpoints.
- **Both `x-k` and `x+k` exist:** They represent different possible start values and must both be tested. Either may produce the better sum.
- **Positive $k$:** The contract guarantees $k>0$, so the two searched values are distinct. The implementation would still perform two equivalent lookups if $k=0$, but that case is outside the stated input.
- **Length-two good subarray:** The first position was registered with prefix zero before iteration begins, so the earliest possible pair is considered correctly.
- **Input preservation:** The method only reads `nums` and never sorts or alters it.
