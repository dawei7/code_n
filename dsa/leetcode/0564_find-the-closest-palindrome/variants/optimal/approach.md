## General

The nearest palindrome does not require searching outward integer by integer. For a number with `l` digits, any nearby palindrome is determined almost completely by a prefix of length `ceil(l/2)`: mirror that prefix to form the remaining digits.

The solution creates a small candidate set, removes the input itself, and chooses the candidate with smallest absolute difference, breaking ties toward the smaller integer.

Let `x = int(n)` and `l = len(n)`.

**Include candidates that change digit length.** The set begins with:

- `10 ** (l - 1) - 1`, the all-nines palindrome immediately below the smallest `l`-digit power of ten;
- `10 ** l + 1`, the one-zeroes-one palindrome immediately above the largest `l`-digit all-nines boundary.

These handle inputs such as `"1000"`, whose closest lower palindrome is `999`, and `"999"`, whose closest higher candidate is `1001`.

For `l = 1`, the lower boundary formula gives zero, which is a valid palindrome and correctly handles input one.

**Extract the significant left half.** The slice:

`n[: (l + 1) >> 1]`

takes `ceil(l/2)` digits. For even length it is exactly half; for odd length it includes the middle digit.

Call its integer value `left`.

Only three nearby prefixes need consideration:

`left - 1`, `left`, and `left + 1`.

Mirroring the unchanged prefix gives the palindrome with the same leading half. Incrementing or decrementing covers the closest palindrome when the central region must cross a carry or borrow.

**Mirror a prefix correctly for even length.** When `l` is even, `j = i`. The loop repeatedly appends `j % 10` to the end of `i` and removes that digit from `j`. This adds the entire prefix in reverse order.

For prefix 12, the process builds 1221.

**Avoid duplicating the middle digit for odd length.** When `l` is odd, `j = i // 10`. Dividing once discards the prefix's last digit, which represents the central character. Only the digits before the center are mirrored.

For prefix 12 of a three-digit number, the process builds 121 rather than 1221.

The local variable `i` is deliberately mutated while building the candidate; each new loop iteration receives a fresh integer from the range.

**Why the three prefixes are sufficient.** For a fixed digit length, palindromes increase in the same order as their defining left prefixes. The closest palindrome below or above `x` must therefore use the same prefix or an immediately adjacent prefix. A prefix farther away produces a palindrome separated by at least another available candidate.

The two boundary candidates cover the exceptional carry/borrow cases where an adjacent prefix changes the resulting digit length or loses leading zeroes.

The set removes duplicate candidate values automatically. It then executes `res.discard(x)` because the problem explicitly excludes the input itself when it is already a palindrome.

For `"123"`, prefix 12 produces candidates from 11, 12, and 13: 111, 121, and 131, plus 99 and 1001. After comparison, 121 has difference two and wins.

For `"1"`, boundary zero and mirrored small prefixes include zero and two. Both are distance one, so the smaller tie rule chooses zero.

**Choose by the exact ordering rule.** Candidate `t` replaces `ans` when its distance is smaller, or when distances tie and `t < ans`. This directly implements nearest-first, smaller-on-tie ordering.

**Why negative construction artifacts do not win.** For the legal positive input domain, the boundary and meaningful mirrored candidates include the valid nearest choices. Small-prefix edge cases are dominated by zero or another nonnegative candidate. The set comparison follows integer distance exactly.

The answer is converted back to decimal string only after the winning integer is known.

No candidate retains leading zeroes; integer construction produces canonical decimal values, as the return contract expects.

## Complexity detail

Let $d$ be the number of digits. Extracting and parsing the prefix, mirroring a constant number of candidates, and formatting the result each process $O(d)$ digits. Time is $O(d)$.

The candidate set has constant cardinality, but its integers and output contain $O(d)$ digits, giving $O(d)$ representation space under the manifest's model.

With at most 18 input digits, all candidate work is small and bounded.

## Alternatives and edge cases

- **Search outward one integer at a time:** The nearest palindrome can be far away, making this needlessly slow.
- **Generate every palindrome of the digit length:** There are exponentially many prefixes; only three nearby ones matter.
- **Mirror only the unchanged prefix:** It fails around values where the nearest palindrome requires a middle carry or borrow.
- **Omit digit-length boundaries:** Inputs near powers of ten or all-nines values can be answered incorrectly.
- **Input already palindrome:** It is explicitly removed, so the next closest palindrome is chosen.
- **Power of ten:** The lower all-nines candidate is essential.
- **All nines:** The upper `10^l + 1` candidate is essential.
- **One digit:** Zero and neighboring one-digit palindromes are compared normally.
- **Odd length:** The middle prefix digit is not mirrored twice.
- **Even length:** The complete half is mirrored.
- **Equal distances:** The smaller candidate wins.
