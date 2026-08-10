## General

**Process decimal digits from right to left**

The source repeatedly applies `divmod(n,10)`. The remainder `v` is the current least significant digit, and the quotient becomes the unprocessed prefix.

Digits are discovered in reverse order, so a retained nonzero digit must be placed to the left of the filtered digits already processed.

**Maintain the filtered value's next place**

`x` is the filtered integer formed from processed nonzero digits in their original order. `p` is the decimal place immediately to their left.

Initially `x=0` and `p=1`. When `v` is nonzero:

`x += p*v`

places it before the already retained suffix, then `p*=10` reserves the next place farther left.

When `v=0`, neither `x` nor `p` changes. Advancing `p` would preserve a zero position instead of removing it.

**Accumulate the digit sum at the same time**

`s` adds every retained digit. Zero could be added harmlessly, but the source updates it inside the nonzero branch. At the end, `x*s` is exactly the requested product.

For `10203004`, digits arrive as four, zero, zero, three, zero, two, zero, one. The nonzero updates build four, then 34, 234, and finally 1234, while `s` becomes ten. The result is 12,340.

For `1000`, three zeros are skipped with `p=1`, then one is placed in the ones position. Both `x` and `s` equal one.

A detailed trace for `10203004` is:

| Extracted digit | Action | `x` | `s` | `p` |
| ---: | --- | ---: | ---: | ---: |
| 4 | retain | 4 | 4 | 10 |
| 0 | skip | 4 | 4 | 10 |
| 0 | skip | 4 | 4 | 10 |
| 3 | retain | 34 | 7 | 100 |
| 0 | skip | 34 | 7 | 100 |
| 2 | retain | 234 | 9 | 1000 |
| 0 | skip | 234 | 9 | 1000 |
| 1 | retain | 1234 | 10 | 10000 |

The filtered integer is built from the right, but each new retained digit receives the next higher place, restoring the original left-to-right order.

**Why right-to-left construction preserves order**

After processing a decimal suffix, assume `x` equals that suffix with zeros removed and `p=10^r` where `r` nonzero digits were retained. A new nonzero digit `v` lies immediately to their left in the original number. Adding `v*10^r` prepends it exactly. A zero contributes no retained position. This invariant proves the final `x` is correct.

The digit sum is order-independent, so adding each retained value once is sufficient.

At loop termination, the quotient has become zero, meaning every original decimal digit was examined. The invariant then identifies `x` with the complete filtered representation, while `s` is its digit sum. Multiplying them produces exactly the requested output.

**Why zeros do not contribute to either result**

A removed zero contributes neither a retained decimal position nor any digit-sum value. Skipping the entire branch is therefore equivalent to performing both required effects. This differs from retaining a zero digit, which would multiply the existing prefix by ten in a left-to-right construction.

The ordinary digit sum of `n` equals the sum of its nonzero digits because zeros add nothing. The code nevertheless accumulates only retained digits so its state definition mirrors the filtered number directly.

**The zero input**

When `n=0`, the loop does not execute. `x=s=0` and the method returns zero, matching the rule that no nonzero digits exist.

## Complexity detail

Let `D` be the number of decimal digits, treating zero as one digit. For positive input, every loop iteration removes one digit, so time is $O(D)$. Zero takes constant time and also fits this bound.

The source uses a constant number of numeric variables and no string or digit array. Under the fixed-width model for `n<=10^9`, actual auxiliary space is $O(1)$, which is tighter than the manifest's $O(D)$ claim.

If arbitrary-precision digit storage for growing `x` and `p` is counted, those integers contain $O(D)$ digits, making $O(D)$ a conservative representation-space bound. For the stated constraint they fit ordinary bounded integer storage.

## Alternatives and edge cases

- **Convert to a string:** Filtering characters left-to-right is clear and $O(D)$, but allocates $O(D)$ string storage.
- **Advance `p` for zeros:** This would preserve removed positions and build the wrong number.
- **Multiply `x` by ten while scanning right-to-left:** That appends in discovery order and reverses the retained digits.
- **All digits zero:** Only input zero has this canonical representation; it returns zero.
- **Trailing zeros:** They are encountered first and skipped without shifting later retained digits.
- **Internal zeros:** They likewise consume no place in `x`.
- **No zeros:** The invariant reconstructs `n` unchanged, and `s` is its ordinary digit sum.
- **One nonzero digit:** The product is that digit squared.
- **Maximum input length:** At most ten loop iterations are needed for the stated numeric bound, but the $O(D)$ analysis remains the general form.
- **Local parameter mutation:** Reassigning `n` through division does not modify caller state because Python integers are immutable.
- **Manifest space:** The exact implementation has constant explicit working state; $O(D)$ applies only if counting integer representation size.
