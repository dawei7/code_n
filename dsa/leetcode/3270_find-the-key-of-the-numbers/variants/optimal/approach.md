## General

**Process one decimal place at a time**

Start with the units place. The expression `number % 10` extracts the current digit from each input, including an implicit zero after all of a shorter number's real digits have been removed. Take the minimum of the three extracted digits and add it to the key at the current power of ten.

Use integer division by ten to discard the processed digit from every input, multiply the place value by ten, and repeat. Exactly four repetitions cover units, tens, hundreds, and thousands.

At each iteration, the three remainders are precisely the digits occupying one aligned position in the zero-padded representations. The algorithm writes their minimum into the same position of the key. Since all four positions are handled independently and once, the accumulated integer has exactly the required digits. Ordinary integer representation removes leading zeros automatically.

## Complexity detail

The source domain fixes the width at four digit positions. The algorithm performs exactly four iterations, each with constant arithmetic, so it uses $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases

- **Pad decimal strings:** Formatting all inputs to width four and zipping their characters is correct, but arithmetic extraction avoids temporary strings.
- **Take the minimum input number:** Numeric order does not imply coordinate-wise digit minima.
- **Ignore missing leading positions:** Shorter inputs contribute zero at those positions and can force leading key digits to zero.
- If every position has a zero among the three inputs, the key is `0`.
- Equal digits simply remain that digit in the key position.
- Inputs at the upper bound `9999` still require exactly four iterations.
- Leading zeros in the constructed four-digit form disappear when the integer is returned.
- The three inputs play symmetric roles; their order cannot change the result.
