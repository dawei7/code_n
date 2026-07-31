## General

**Count divisible occurrences first**

Let a prefix remainder be the sum of all values before a position, reduced modulo `k`. A subarray sum is divisible by `k` exactly when the prefix remainders at its two boundaries are equal. Scan `nums` while storing the frequency of each remainder; every earlier copy of the current remainder contributes one good subarray occurrence.

That standard prefix-sum count includes repeated occurrences, so it does not yet enforce the problem's sequence-based distinctness rule.

**Locate every possible duplicate sequence**

Because `nums` is sorted in non-descending order, each value occupies one contiguous run. A subarray containing two different values uniquely determines its first run, its last run, and how many values it takes from each; consequently, that sequence occurs at only one pair of endpoints.

Only constant sequences can occur more than once. Inside a run of $c$ copies of a value $v$, the sequence of length $L$ occurs $c-L+1$ times but must be counted once. It is good precisely when $Lv$ is divisible by `k`. If

$$
d = \frac{k}{\gcd(v,k)},
$$

then exactly the lengths $d,2d,\ldots,md$ qualify, where $m=\lfloor c/d\rfloor$. Their total excess occurrence count is

$$
\sum_{t=1}^{m}(c-td)
= mc - d\frac{m(m+1)}{2}.
$$

Subtract this quantity for every equal-value run from the prefix-remainder occurrence total. This removes every duplicate and retains one copy of each distinct good constant sequence.

## Complexity detail

Let $n$ be the length of `nums`. The prefix-remainder scan and the equal-value run scan each take $O(n)$ time. Hash-map operations take expected $O(1)$ time, and `gcd` is bounded by the value widths, so the total expected time is $O(n)$. The remainder-frequency map uses $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Store every sequence:** Enumerating subarrays and inserting tuples into a set is direct, but it requires at least quadratic enumeration and may copy a quadratic amount of data.
- **Count prefix pairs only:** This counts occurrences rather than distinct value sequences and overcounts repeated constant subarrays.
- **Unsorted input:** The proof that only constant sequences repeat depends on `nums` being sorted in non-descending order, which the source guarantees.
- **One equal-value run:** Good distinct sequences correspond exactly to the qualifying lengths, regardless of how many positions realize each length.
- **`k = 1`:** Every subarray sum is divisible, but repeated constant sequences still need deduplication.
- **Large values:** Only remainders and greatest common divisors are needed; no array value needs to be expanded into repeated work.
- **Large answer:** The number of distinct subarrays can exceed 32-bit signed range, so fixed-width implementations need a 64-bit result.
