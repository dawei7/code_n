## General

**Separate digits by index parity.** The definition uses zero-based indices. Positions $0,2,4,\ldots$ contribute to the even-index sum, while positions $1,3,5,\ldots$ contribute to the odd-index sum. The source stores these two totals in `f = [0, 0]`.

`map(int, num)` lazily converts each digit character to its numeric value. `enumerate` supplies the corresponding zero-based index. Expression `i & 1` extracts the index's least significant bit: zero for an even index and one for an odd index. Therefore `f[i & 1] += x` adds each digit to exactly its required bucket.

After the scan, `f[0] == f[1]` is precisely the balanced-string condition.

**Why numeric conversion is necessary.** Characters `"2"` and `"4"` cannot be meaningfully added as digit values without conversion; string addition would concatenate text. `int` maps each guaranteed digit character to zero through nine. Leading zeros pose no problem because the method treats the input as a sequence of digits, not as one integer whose textual leading zeros might disappear.

**A trace for `"24123"`.** Index zero adds two to `f[0]`. Index one adds four to `f[1]`. Index two adds one to the even total, index three adds two to the odd total, and index four adds three to the even total. Both totals finish at six, so the method returns true.

For `"1234"`, even positions contribute one plus three, while odd positions contribute two plus four. Four differs from six, so false is returned.
After processing positions zero through $r$, `f[0]` equals the sum of all processed digits with even indices and `f[1]` equals the corresponding odd-index sum. The invariant is initially true for empty prefixes. At each character, `i & 1` selects exactly the proper total and adds the digit, preserving it. At the end, equality of the stored totals is equivalent to the definition.

**Why two totals are enough.** The problem asks only whether sums match. It does not require retaining individual digits or their positions after classification. Once a digit has been added to the correct running total, no future operation needs it.

An equivalent implementation could accumulate one signed difference, adding even-index digits and subtracting odd-index digits, then test zero. The two-element array used here mirrors the statement and can be easier for beginners to inspect.

**Index parity is not digit parity.** Whether the digit itself is even or odd is irrelevant. A digit nine at position zero belongs to the even-index sum, and a digit two at position one belongs to the odd-index sum. The bit operation is applied to `i`, not `x`.

The source treats `num` as a string throughout and does not modify it. It assumes every character is a digit, as the constraints guarantee; a sign, decimal point, or letter would make `int` fail.

## Complexity detail

Let $n$ be the number of digit characters. The lazy map and loop visit each once, performing constant work, so time is $O(n)$. `f` always contains two integers, and the iterators use constant bookkeeping, so auxiliary space is $O(1)$.

Each total is at most $9\lceil n/2\rceil$, tiny under $n\le100$. There is no overflow concern in Python.

## Alternatives and edge cases

- **Signed difference:** Add digits at even indices and subtract digits at odd indices; balanced means the final difference is zero.
- **String slicing:** Sum `num[::2]` and `num[1::2]` after conversion. It is concise but allocates slice strings and temporary iterables.
- **Two explicit loops:** Iterate even and odd index ranges separately. It is correct but visits the structure less uniformly.
- **Leading zeros:** They contribute numeric zero while retaining their index positions, exactly as required.
- **All zeros:** Both totals remain zero and the string is balanced.
- **Even string length:** Both groups contain the same number of positions, but their sums need not match.
- **Odd string length:** The even-index group has one additional digit; equality is still possible.
- **Repeated digits:** Position, not uniqueness, determines the bucket.
- **Digit parity:** It has no relation to index parity and must not be used for classification.
- **Minimum length two:** Each parity group contains one position, so balance means the two digits are equal.
- **Non-digit input:** Outside the contract, `int` conversion raises an error rather than silently ignoring a character.
- **Zero-based indexing:** The first digit belongs to the even-index total because its index is zero.
- **No input mutation:** Iteration over the immutable string preserves it.
- **Iterator behavior:** `map(int, num)` converts digits only as the loop requests them. It avoids allocating a second list of all numeric digits.
- **Two-bucket invariant:** Each processed digit enters exactly one bucket, so the combined total `f[0] + f[1]` always equals the sum of the processed prefix. This offers a simple debugging check.
- **Comparison only at the end:** Prefix sums need not balance during the scan. A later digit can restore equality, so returning early on a temporary mismatch would be incorrect.
- **Maximum totals:** With at most 100 digits, each bucket sum is at most 450, though the algorithm does not rely on this bound.
