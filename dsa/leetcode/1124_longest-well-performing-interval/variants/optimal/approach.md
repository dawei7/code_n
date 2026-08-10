## General

**Convert the condition into a positive-sum interval**

A tiring day should contribute one and a non-tiring day should contribute negative one. Then an interval’s sum equals:

`number of tiring days - number of non-tiring days`.

The interval is well-performing exactly when this sum is strictly positive.

The loop maintains prefix sum `s` through the current day. Each hour value greater than eight adds one; every value at most eight subtracts one. The original scheduling story is now a standard longest positive-sum subarray problem.

**Use prefix-sum differences**

Let the prefix sum through index `i` be $S_i$. An interval starting after earlier index `j` and ending at `i` has sum:

$S_i-S_j$.

It is positive when $S_j<S_i$. To maximize interval length for a fixed end, the algorithm wants the earliest earlier position whose prefix sum is smaller than the current sum.

**Handle a positive whole prefix**

If current `s > 0`, the interval from day zero through `i` is already well-performing. Its length is `i + 1`.

No interval ending at `i` can be longer because this one begins at the first array position. Therefore, the code directly assigns `ans = i + 1`.

The conceptual prefix before the array has sum zero at index negative one. This branch is equivalent to using that sentinel when current sum exceeds zero, without storing it in the dictionary.

**When the current sum is not positive, look for `s - 1`**

For `s <= 0`, a qualifying interval needs an earlier prefix strictly below `s`. Prefix sums are integers and change by exactly one each day. The nearest smaller value is `s - 1`.

If any earlier prefix is smaller than `s`, the running walk must have passed through `s - 1` on its way to that lower value. Therefore, finding an occurrence of exactly `s - 1` is sufficient; there is no need to search every smaller sum.

If `s - 1` appears in `pos` at index `j`, the interval `j + 1` through `i` has sum one and is well-performing. Its length is `i - j`.

The interval sum can be greater than one even though the lookup uses exactly `s - 1` only when an even earlier, lower prefix exists. On the path to that lower prefix, `s - 1` was necessarily visited; storing its first visit gives a span at least as long as using a later lower level reached afterward.

**Store only the earliest occurrence of each prefix**

`pos` records a prefix sum only when it is first seen. For a future end index, the earliest matching `s - 1` gives the longest possible interval because subtracting a smaller index produces a larger length.

Overwriting it with a later occurrence could only shorten future candidates.

The current prefix is stored after candidate checking. This prevents using the same index as its own earlier boundary and ensures `pos` represents strictly earlier prefixes during the query.

**Why every longest interval is found**

For each endpoint, if the whole prefix is positive, the algorithm checks the longest possible interval ending there. Otherwise, every positive interval must begin after a smaller earlier prefix, and existence of such a prefix implies an earlier `s - 1` occurrence. The dictionary holds its earliest occurrence.

Thus the best interval for every end is considered. Taking the maximum across all ends returns the global longest well-performing interval.

The algorithm never needs to recover the actual interval boundaries because the contract asks only for length. Nevertheless, the dictionary lookup implicitly identifies a valid start at one position after the stored prefix index.

## Complexity detail

Let $n$ be the number of days. The loop processes every day once. Dictionary membership, lookup, and insertion take expected $O(1)$ time, so total expected time is $O(n)$.

Prefix sums range from $-n$ through $n$, and the dictionary can store $O(n)$ distinct values. Space is therefore $O(n)$.

The answer and running sum use constant extra storage. No interval contents are copied.

## Alternatives and edge cases

- **Quadratic enumeration:** Compute every interval sum, taking $O(n^2)$ time even with prefix sums.
- **Monotonic-stack prefix method:** Build all prefixes, keep decreasing candidate indices, and scan from the right. It also achieves $O(n)$ but uses a more global proof.
- **Store every prefix occurrence:** Correct but unnecessary; only the earliest can maximize length.
- **All tiring days:** Every prefix is positive, so the answer grows to $n$.
- **No tiring days:** Prefix sums only decrease and no `s - 1` was seen earlier, so the answer remains zero.
- **Exactly balanced interval:** Sum zero is not sufficient because tiring days must be strictly more numerous.
- **Eight hours:** It is non-tiring because the threshold is strictly greater than eight.
- **Repeated prefix sum:** Later occurrences are ignored to preserve the longest future span.
- **Positive prefix after earlier negatives:** The whole prefix branch still dominates every shorter candidate ending there.
- **Single tiring day:** The answer is one.
- **Single non-tiring day:** The answer is zero.
- **Implicit prefix zero:** The `s > 0` branch replaces the need to store sum zero at index negative one.
