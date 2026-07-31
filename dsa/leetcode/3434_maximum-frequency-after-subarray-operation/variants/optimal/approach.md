## General

Suppose the chosen operation is intended to turn a value $v\ne k$ into `k`. The added integer is then forced to be $k-v$. Within the selected subarray, every occurrence of $v$ becomes a new `k`, while every element already equal to `k` is shifted away and ceases to count. Other values neither become `k` nor were `k`, so they have no effect on the frequency change.

For a fixed source $v$, map each array element to a gain: `+1` for $v$, `-1` for `k`, and `0` otherwise. The net change produced by selecting any subarray is exactly its mapped sum. Kadane's algorithm finds the largest such sum in one pass, resetting a negative prefix because excluding it can only improve every later candidate.

Try every possible source value from 1 through 50. This covers every useful nonzero operation because only a value already present in the selected subarray can create a new `k`. Start with gain zero, corresponding to choosing an operation that does not reduce the existing answer. Adding the best gain to the original frequency of `k` yields the maximum attainable frequency.

## Complexity detail

The value domain has exactly 50 possibilities, a fixed constant independent of $n$. Each source performs one $O(n)$ Kadane scan, so total time is $O(50n)=O(n)$. Only scalar counters are maintained, giving $O(1)$ auxiliary space. Reading the array is necessary because any position can change the best subarray.

## Alternatives and edge cases

- **Enumerate all subarrays:** Evaluating the gain of every interval takes $O(n^2)$ time even with prefix counts.
- **Choose the globally most frequent source:** Its occurrences may be separated by enough existing `k` values that another source has a better contiguous gain.
- **Combine different source values:** One addition cannot turn two distinct original values into `k`, because each would require a different offset.
- **All elements already equal `k`:** Every nonzero operation loses frequency, so preserving the original $n$ occurrences is optimal.
- **No existing `k`:** Selecting all occurrences of the best source value creates the answer; there is no `-1` penalty.
- **Single element:** Either it already equals `k` or one operation converts it, so the answer is one.
- **Zero-gain operation:** Initializing the best gain to zero represents the allowed choice that leaves the frequency unchanged.
