## General

**Recognize a price as a whole token**

Split the sentence at its guaranteed single spaces. A token qualifies only if
it has at least two characters, its first character is `"$"`, and its entire
suffix consists of digits. Checking the complete suffix prevents embedded or
trailing dollar signs and letters from being modified.

**Format with integer cents**

If a price has integer value $p$, the percentage remaining after the discount
is `100 - discount`. The discounted number of cents is therefore
`p * (100 - discount)`. This is an integer, so it avoids floating-point
rounding entirely.

The quotient by 100 is the dollar part and the remainder is the cent part.
Render the remainder with two digits, including a leading zero when necessary,
then join all transformed and untouched tokens with single spaces.

Every token is classified by exactly the definition in the contract.
Recognized prices receive the exact percentage multiplication expressed in
cents; non-prices are copied. Joining in the original sequence consequently
produces precisely the required modified sentence.

## Complexity detail

Let $N$ be the sentence length. Splitting, validating all token characters,
formatting price tokens, and joining the result each process $O(N)$ total
characters, so the running time is $O(N)$. The token list and reconstructed
sentence use $O(N)$ space.

## Alternatives and edge cases

- **Floating-point formatting:** Converting prices through binary floating point may introduce avoidable precision concerns; integer cents are exact for the contract.
- **Regular-expression replacement over substrings:** A substring match can accidentally transform text embedded inside a non-price word unless whole-token boundaries are enforced.
- **Repeated sentence rescans:** Searching the complete sentence again for every word is correct when carefully implemented but can take $O(N^2)$ time.
- **Bare dollar sign:** `"$"` has no digit suffix and remains unchanged.
- **Mixed token:** Words such as `"5$"`, `"$5$"`, and `"$5a"` are not prices.
- **Zero-percent discount:** A valid integer price still gains exactly two decimal places.
- **Full discount:** Every recognized price becomes `"$0.00"`.
- **Large price:** Up to ten digits fit comfortably in the exact integer calculation.
- **Single spaces:** Rejoining with one space preserves the guaranteed sentence separator format.
