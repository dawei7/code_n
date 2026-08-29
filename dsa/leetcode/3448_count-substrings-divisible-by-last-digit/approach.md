## General

**Count substrings by their ending position.** When the current character is digit $d$, every substring ending here has last digit $d$. If $d\ne0$, the valid ones are exactly those whose numeric value has remainder zero modulo $d$.

The difficulty is that future last digits may be any value from $1$ through $9$. The source simultaneously maintains remainder counts for all nine possible moduli.

For modulus $q$, `counts[q][r]` is the number of substrings ending at the previous processed position whose numeric value has remainder $r$ modulo $q$. The outer list begins with an unused empty entry for modulus zero, followed by arrays of lengths $1,2,\ldots,9$.

**Append one digit to every previous substring.** If an old substring represents value $v$ and the new digit is $d$, the extended value is

$$
10v+d.
$$

If $v\bmod q=r$, the new remainder is

$$
(10r+d)\bmod q.
$$

For each modulus, the source creates a fresh `next_counts` array. It first records the one-character substring containing only $d$:

`next_counts[digit % modulus] = 1`.

Then every old remainder bucket transfers its `amount` to the calculated new remainder. Replacing `counts[modulus]` with this new array means all stored substrings now end at the current position.

Fresh arrays are important. Updating a remainder array in place could extend a substring more than once with the same digit because newly written counts might be read again during the same iteration.

**Use the actual last digit after all moduli are updated.** If `digit != 0`, `counts[digit][0]` is the number of current-ending substrings divisible by that last digit, so it is added to `answer`.

If the digit is zero, the statement excludes it as a divisor. The source still updates all modulus tables because a substring ending in zero may later be extended by a nonzero digit and then become relevant. It simply does not add a count for modulus zero.

For example, while processing `"12"`, the modulus-$2$ table contains the one-digit value $2$ and the extended value $12$, both at remainder zero. Since the last digit is $2$, both substrings count.

**Leading zeros are naturally supported.** Numeric recurrence treats `"01"` as value $1$, exactly as ordinary divisibility does. The new one-character and extension transitions distinguish substrings by their start indices even when their numeric values are equal, so `"1"` and `"01"` are counted separately.

**Why all and only valid substrings are counted.** Inductively, before processing a digit, each table partitions every substring ending at the prior position by its exact remainder. Adding the one-character substring and extending every previous substring produces every substring ending now exactly once. The remainder recurrence is mathematically exact.

At this endpoint, selecting remainder zero under modulus equal to the nonzero last digit is precisely the problem's condition. Each substring has one unique ending position, so accumulating these counts neither omits nor duplicates any valid substring.

The digit conversion uses character-code subtraction rather than `int`. Because input characters are guaranteed decimal digits, `ord(character) - ord("0")` yields the correct value.

**A concrete remainder transfer.** Suppose modulus is $3$, an old bucket says four substrings have remainder $2$, and the new digit is $5$. Every one of those extensions has remainder $(2\cdot10+5)\bmod3=1$, so all four counts move together into `next_counts[1]`. The algorithm never needs the substrings' full values or starting indices once equal remainders are grouped. Counts from different old remainders may land in the same new bucket and are added, preserving their distinct substring multiplicities.

Rebuilding all nine modulus tables even when the current digit is small is necessary for future endpoints. A state modulo $9$ created now may be queried many characters later when a substring finally ends in digit $9$.

## Complexity detail

For each input character, the source processes modulus arrays of total length

$$
1+2+\cdots+9=45.
$$

This is a fixed constant, so total time is $O(45n)=O(n)$. Creating the small next arrays is included.

The current tables contain only 45 counters, and one temporary array has at most nine entries. Auxiliary space is $O(1)$ with respect to $n$, matching the manifest.

## Alternatives and edge cases

- **Convert every substring to an integer:** There are $O(n^2)$ substrings, and values become extremely large. Remainder DP avoids both problems.
- **Track only the current last-digit modulus:** Future endpoints may have different last digits, so all moduli $1..9$ must be ready after every prefix.
- **Update tables in place:** This can reuse newly extended counts and count nonexistent substrings. A fresh table per modulus preserves the previous layer.
- **Last digit zero:** No substring ending there is counted, but its remainder states must survive for later extensions.
- **Leading zeros:** They do not change numeric value but do create distinct index substrings, all represented independently by counts.
- **One-character nonzero substring:** A digit is always divisible by itself, and the singleton initialization guarantees it contributes.
- **Repeated numeric values:** Counts represent occurrences by endpoints and starts, not unique integer values.
- **Long input:** Only bounded remainders are stored, so numeric magnitude never grows.
- **Digit one:** Every substring ending in `1` has remainder zero modulo one and is counted.
- **Answer size:** Python integers safely store the potentially quadratic number of valid substrings.
