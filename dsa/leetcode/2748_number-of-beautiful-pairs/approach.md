## General

**At each right endpoint, only earlier first digits matter**

A beautiful pair $(i,j)$ uses the first digit of `nums[i]` and the last digit of `nums[j]`. Process `nums` from left to right, treating current value `x` as the right endpoint `j`.

Store how many earlier numbers have each possible first digit. Then the current last digit can be compared with only ten digit buckets instead of every earlier index.

**Frequency array meaning**

`cnt[d]` is the number of already processed values whose first decimal digit is `d`.

Positive integers have first digits one through nine. The array has length ten for direct digit indexing; bucket zero remains unused.

The current last digit is `x % 10`. The constraint guarantees it is nonzero, although the gcd computation itself would still have defined behavior with zero.

**Count all compatible earlier values**

For every digit `y` from zero through nine, the code checks whether `cnt[y]` is positive and:

`gcd(x % 10, y) == 1`.

If so, every earlier number in that bucket forms a beautiful pair with current `x`. Adding `cnt[y]` counts all of them at once.

The actual earlier number values do not matter after their first digits are known, because the pair definition uses no other information from the left endpoint.

**Record the current first digit afterward**

The first digit is obtained with `int(str(x)[0])`. The code increments that bucket only after counting current pairs.

This order ensures the current index cannot pair with itself. It also enforces $i<j$: the frequency array always contains exactly earlier indices.

**Trace nums equal to 2, 5, 1, 4**

For two, all buckets are empty, so no pair is added; record first digit two.

For five, last digit five is coprime with earlier first digit two, so add one; record five.

For one, gcd of one with every positive digit is one, so it pairs with both earlier values; add two and record one.

For four, it is not coprime with first digit two, but it is coprime with five and one; add two. Total is five.

**Why ten checks per number are constant**

Decimal digits form a fixed universe. Even for a large array, the inner loop always performs exactly ten iterations. Thus the nested appearance does not make the algorithm quadratic.

The constraints cap each value at 9999, so converting to a decimal string is also bounded by four characters. More generally, first-digit extraction by string conversion costs proportional to the number of digits.

**Why gcd is the exact test**

Two positive digits are coprime exactly when their greatest common divisor is one. There is no need to enumerate common factors manually.

Digit one pairs with every last digit. Digits sharing factors two, three, five, or seven are rejected as appropriate.

**No double counting**

Every index pair is considered when and only when its later index becomes current. It is added through exactly one bucket corresponding to the earlier value's unique first digit.

The algorithm never revisits that pair in a later iteration because the right endpoint would differ. Thus all beautiful pairs are counted exactly once.

**Why a Counter of full numbers would be wasteful**

Only nine meaningful first-digit categories exist. Compressing earlier values into buckets loses no information relevant to future gcd checks and bounds storage by a constant.


Before processing current index `j`, `cnt[y]` exactly counts earlier indices with first digit `y`. For each bucket, the gcd test is true exactly when those earlier indices form beautiful pairs with `j`'s last digit, so adding the bucket count includes all and only valid pairs ending at `j`. Updating afterward preserves the invariant for the next index. Summing across all right endpoints yields the exact total.

## Complexity detail

Let $n$ be the array length. The outer loop runs $n$ times and the inner digit loop always runs ten times. GCD on single decimal digits is constant time. With values limited to four digits, first-digit string conversion is constant time. Total time is $O(n)$.

The ten-entry frequency array and scalar variables use $O(1)$ auxiliary space.

For generalized arbitrarily large integers with $D$ digits, conversion would add $O(D)$ per number, but that is outside the fixed numeric constraints.

## Alternatives and edge cases

- **Check every index pair:** Directly follows the definition but costs $O(n^2)$.
- **Arithmetic first-digit extraction:** Repeatedly divide by ten instead of creating a string; useful for generalized large values.
- **Precompute a 10-by-10 coprime table:** Replaces repeated gcd calls with constant table lookups.
- **First digit one:** Compatible with every legal nonzero last digit.
- **Equal digits:** Only digit one is coprime with itself.
- **Bucket zero:** Never receives a positive number's first digit.
- **Nonzero-last-digit guarantee:** Avoids pairs involving gcd with zero.
- **Repeated numbers:** Allowed; indices remain distinct and bucket counts handle multiplicity.
- **Update after query:** Prevents pairing an index with itself.
- **Maximum pair count:** Python integers safely store up to $n(n-1)/2$.
