## General

**Enumerate the small answer domain instead of index triples**

Every valid result is a three-digit even integer. There are only 450 such candidates: 100, 102, ..., 998. This fixed numeric domain does not grow with the input length.

The source first counts available digits with `cnt = Counter(digits)`. It then visits every candidate using `range(100, 1000, 2)`.

Starting at 100 guarantees three digits and automatically excludes leading zero. Stepping by two guarantees the last digit is even. Candidate order is increasing, so accepted values are already sorted. Each numeric candidate appears once, so uniqueness is automatic.

**Extract a candidate's required digit multiset**

For one candidate `x`, the code copies it to `y` and repeatedly applies `divmod(y, 10)`. The quotient becomes the remaining prefix, and the remainder `v` is the final digit just removed. `cnt1[v]` is incremented.

Because `x` is between 100 and 999, the loop executes exactly three times. The digits are extracted from right to left, but frequency counts do not depend on order.

For candidate 282, `cnt1` records two copies of digit 2 and one copy of digit 8. This distinguishes it from simply checking whether digits 2 and 8 are present.

**Test availability for every digit**

The condition

`all(cnt[i] >= cnt1[i] for i in range(10))`

requires the input to provide at least as many copies of every digit as the candidate uses. A `Counter` returns zero for missing keys, so absent digits fail naturally.

This condition is necessary: forming the candidate uses one separate array element per digit position, so no digit may be used more often than it occurs.

It is also sufficient: if the input frequency covers every required frequency, one can select the required number of indices for each digit and arrange them in the candidate's hundreds, tens, and units positions.

The same digit may therefore be reused only through distinct occurrences in `digits`.

**Why all output requirements are enforced**

The candidate range enforces the length and leading-digit rule. The step size enforces evenness. The frequency comparison enforces construction from three available array elements. Increasing enumeration enforces sorted order, and visiting each integer once enforces uniqueness.

Every appended number satisfies all requirements. Conversely, any valid number is a three-digit even integer, so it appears exactly once in the range. Its required digits are available by definition, making the frequency test pass. No valid answer is missed.

For `digits = [2, 2, 8, 8, 2]`, candidate 288 requests one 2 and two 8s and passes. A candidate such as 888 requests three 8s and fails because only two are available.

**Why the manifest calls this linear**

The candidate work is a fixed 450 candidates times a fixed ten-count comparison. It is constant with respect to input length. Building `cnt` is the only part that grows with `n`, so total time is $O(n)$.

The approach is especially attractive here because the answer domain is permanently bounded to three-digit numbers. It would not remain constant-domain if the requested number of digits grew as part of the input.

The input list is only read and remains unchanged.

## Complexity detail

Let $n$ be the length of `digits`.

Building the input counter takes $O(n)$ time. Exactly 450 candidates are examined; each extracts three digits and compares ten fixed digit counts. This is $O(1)$ work relative to $n$. Total time is $O(n)$.

`cnt` and `cnt1` have at most ten keys, so auxiliary space is $O(1)$. The output can contain at most 450 integers, also a fixed bound; conventionally required output is excluded from auxiliary space.

The source creates a fresh small `Counter` for each candidate. Its repeated allocations affect constants but not the asymptotic bound.

## Alternatives and edge cases

- **Enumerate three array indices:** This directly constructs arrangements but costs $O(n^3)$ before deduplication. Candidate enumeration exploits the fixed result domain.
- **Backtracking over digit counts:** It can generate hundreds, tens, and even units positions without reusing unavailable digits, but needs a set or careful ordering to avoid duplicates.
- **Store generated numbers in a set:** A set removes duplicates from index enumeration, followed by sorting. The exact method produces each numeric candidate only once and needs neither.
- **No even digit:** Every candidate frequency test fails because its units digit is even, so the result is empty.
- **Zeros in the input:** Zero may be used in the tens or units place. The candidate range prevents it from becoming a leading digit.
- **Repeated digits required:** The frequency comparison checks multiplicity, so 222 requires three copies of 2.
- **Extra input digits:** They do not hurt; the comparison requires at least the candidate counts, not exact equality.
- **Candidate order:** `range` is increasing, so appending preserves the required sorted order.
- **Uniqueness:** Each integer from 100 to 998 is tested once even when many index selections could form it.
- **Missing counter keys:** Both counters treat missing digit counts as zero, making the ten-way comparison safe.
- **Exactly three input elements:** The same logic applies; a candidate passes only if its multiset matches available elements.
- **Fixed-domain assumption:** The $O(n)$ analysis relies on exactly three decimal digits and ten possible digit values.
