## General
**Use the digit-sum divisibility rule.** A decimal integer is divisible by $3$ exactly when its digit sum is divisible by $3$. Count the occurrences of all ten digits and compute the total sum. The order of selected digits does not affect divisibility.

**Discard as little value as possible.** If the sum has remainder one, either remove the smallest available digit with remainder one or, when none exists, remove the two smallest digits with remainder two. For remainder two, apply the symmetric choice. Removing one digit is always preferable to removing two because it leaves a longer decimal representation; within the same removal count, discarding the smallest digits preserves the greatest remaining multiset.

**Arrange the retained multiset maximally.** Emit remaining digits from `9` down through `0`. Descending order is the largest permutation of a fixed multiset. If nothing remains, no answer exists. If the first emitted digit is zero, every retained digit is zero, so normalize the result to `"0"`.

The remainder repair produces a divisible multiset while maximizing first its length and then its descending lexicographic order. Those criteria exactly maximize a nonnegative decimal integer, proving the returned string is optimal.

## Complexity detail
Counting and summing the $n$ input digits takes $O(n)$ time. Repairing the remainder and traversing ten counters take constant time; producing the output takes at most $O(n)$ time. The ten counters use $O(1)$ auxiliary space, excluding the required output string.

## Alternatives and edge cases
- **Sort then repair:** Sort all digits, remove the smallest remainder-compatible occurrence or pair, and reverse the remainder. This is correct but costs $O(n\log n)$ time.
- **Subset dynamic programming:** Track the best string for each remainder while processing digits. It works but repeatedly compares or copies long strings and is unnecessary for a ten-symbol alphabet.
- **Enumerate subsets:** Test every selected multiset and permutation, which is exponential and infeasible.
- **Two-digit repair:** When no digit has the total remainder, two smallest digits from the opposite nonzero remainder class must be removed.
- **All zeroes:** Any number of zeroes represents the same value, so return exactly `"0"`.
- **Only unusable digits:** If remainder repair removes every digit, return the empty string.
- **Duplicate occurrences:** Counts preserve multiplicity, and each occurrence is removed or emitted at most once.
