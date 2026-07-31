## General

**Separate global uniqueness from original order**

Whether a value is unique cannot be decided from its first occurrence; a duplicate may appear later. First count every value in the complete array. The constraint $1 \le \texttt{nums[i]} \le 100$ permits a fixed table of 101 counters, indexed directly by value.

**Scan again to enforce earliest-index priority**

Traverse `nums` from left to right after all frequencies are known. Return the first value that is divisible by $2$ and whose counter equals one. If the scan ends without finding such a value, return `-1`.

The first pass makes every stored count equal to that value's exact total frequency. During the second pass, a returned value is therefore both even and globally unique. Because the scan visits indices in increasing order, every earlier element has already failed at least one requirement, so the returned value has the earliest qualifying index. If none is returned, no array element meets both requirements and `-1` is correct.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each of the two passes visits $N$ elements and performs constant-time table operations, giving $O(N)$ time. The counter table always has 101 entries because the value domain is fixed by the contract, so the auxiliary space is $O(1)$.

The benchmark defines size as $N$. Every tier repeats the even value `2` until a single `100` at the final position, forcing both complete linear passes. An independent hash-map implementation should retain linear growth. A correct implementation that calls a linear frequency scan for every candidate position performs $O(N^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Hash-map frequencies:** A `Counter` or dictionary supports the same two-pass algorithm in $O(N)$ expected time and $O(U)$ space for $U$ distinct values; the fixed legal value range makes an array smaller and strictly bounded.
- **Repeated full-array counting:** Testing `nums.count(value) == 1` during the left-to-right scan is correct, but an input with many nonqualifying even values makes it $O(N^2)$.
- **Counts plus first positions:** One pass can store each frequency and first index, followed by a scan over the value domain. This is linear but must compare indices explicitly; scanning `nums` again expresses the ordering rule more directly.
- **Earliest is not smallest:** In `[10,2,3]`, both even values are unique, but `10` is returned because its index is earlier.
- **Repeated first even:** In `[2,3,2,8]`, the two occurrences of `2` disqualify it, so the later unique `8` is returned.
- **All values odd:** No element can satisfy divisibility by $2$, so the result is `-1`.
- **Only repeated evens:** Even values with frequency greater than one do not qualify, also producing `-1`.
