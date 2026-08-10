## General

**Count an inclusive interval by subtracting prefixes**

The source does not iterate through the interval. It counts odd numbers up to the high endpoint and subtracts the count strictly below the low endpoint:

$$
\#\text{odds in }[low,high]
=
\#\text{odds in }[0,high]
-\#\text{odds in }[0,low-1].
$$

Its exact expression is

`((high + 1) >> 1) - (low >> 1)`.

For nonnegative integers, shifting right by one bit is the same as floor division by two.

**Understanding the high prefix**

Among the integers from zero through `high`, the odds are one, three, five, and so on. Their count is

$$
\left\lfloor\frac{high+1}{2}\right\rfloor.
$$

If `high` is odd, adding one makes it even and division includes that final odd endpoint. If `high` is even, the floor naturally counts odds only through `high-1`.

The code writes this as `(high + 1) >> 1`.

For high seven, eight shifted right is four, counting one, three, five, and seven. For high ten, eleven shifted right is five, counting odds one through nine.

**Understanding the low prefix**

`low >> 1` equals $\lfloor low/2\rfloor$. For nonnegative `low`, this is exactly the number of odd integers strictly smaller than `low`.

If low is even eight, the smaller odds are one, three, five, and seven, totaling four. If low is odd three, only one is a smaller odd, and floor division also gives one.

Subtracting removes every odd value before the interval while preserving low itself when low is odd.

**Checking all endpoint parities**

There are four parity combinations:

- Odd low and odd high: both endpoints count, and an interval of odd length contains one more odd than even.
- Odd low and even high: low counts, high does not, and odds and evens balance.
- Even low and odd high: high counts, low does not, and odds and evens balance.
- Even low and even high: neither endpoint is odd, and the interval's internal odds are counted.

The prefix formula handles all four without branches.

For `low = 3` and `high = 7`, the high prefix is four and the low prefix is one, producing three. For eight through ten, the prefixes are five and four, producing one.

**Why bit shifting is valid here**

The inputs are nonnegative, so right shift has the same result as integer floor division by two. Signed negative values can have language-specific or floor-rounding subtleties, but they are outside the contract.

The parentheses around `high + 1` are essential because that addition must occur before shifting. Python operator precedence would also need to be understood; explicit grouping makes intent clear.

**A counting proof**

Pair consecutive nonnegative integers as `(0,1)`, `(2,3)`, and so on. Each complete pair contains exactly one odd number. A prefix ending at an odd value contains a complete final pair, while a prefix ending at an even value has one unmatched even after its complete pairs.

The floor formulas count those complete pairs. Prefix subtraction leaves exactly the complete and partial pairs belonging to the requested inclusive range, proving the result.

**Relationship to interval length**

The inclusive interval contains `high - low + 1` integers. Exactly half are odd when this length is even. When the length is odd, the parity of `low` decides which kind gets the extra element: an odd low means one more odd, while an even low means one more even.

That observation yields another formula, but it requires both an interval-length calculation and a parity branch. Prefix subtraction packages the same reasoning into two uniform floor counts. It is especially resistant to endpoint mistakes because the high prefix is explicitly inclusive and the low prefix is explicitly exclusive.

Consider consecutive intervals of length three. `[2,4]` contains only odd three, so it has one odd. `[3,5]` contains odd three and five, so it has two. The length alone is insufficient; the starting parity supplies the missing information, which is already encoded in `low >> 1`.

**Why no overflow adjustment is needed**

The largest input is one billion, so `high + 1` remains well within common signed 32-bit range. In languages with tighter or near-maximum bounds, adding one to an endpoint could overflow and a parity-based rearrangement might be safer. Under this contract and in Python, the direct expression is exact.

## Complexity detail

The method performs two shifts, one addition, and one subtraction on bounded integers. Its time is $O(1)$ and auxiliary space is $O(1)$, matching the manifest.

Under the stated limit of one billion, the values fit ordinary fixed-width integer representations. Python integers are exact regardless.

The running time does not depend on `high - low`. An interval spanning a billion values costs the same number of operations as a one-value interval.

## Alternatives and edge cases

- **Adjust low to the first odd:** If low is even, increment it, then compute spaced terms with division by two. It is constant time but needs a boundary check.
- **Parity-length formula:** Half the interval length is odd, with one additional odd when both interval length and starting parity require it. It is correct but easier to get off by one.
- **Iteration:** Checking every number costs $O(high-low+1)$ and is unnecessary.
- **Single odd value:** Both prefixes differ by one, returning one.
- **Single even value:** Both prefixes are equal, returning zero.
- **low equals zero:** The subtracted prefix count is zero.
- **Both endpoints odd:** Both are included by the high-plus-one and low-prefix definitions.
- **Both endpoints even:** Neither is accidentally counted as odd.
- **Maximum interval:** Constant-time arithmetic handles the full allowed range.
- **Nonnegative guarantee:** It is what makes shift and floor-division interpretations straightforward.
