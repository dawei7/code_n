## General
**Reduce each label to its box number**

Visit every integer in the inclusive range. Repeatedly take its last decimal digit with remainder by $10$, add that digit to a running sum, and remove it with integer division by $10$. The resulting sum is exactly the destination box.

**Count occupancies as balls arrive**

Maintain a frequency array indexed by digit sum. A $D$-digit positive integer has digit sum at most $9D$, so only $9D+1$ slots are needed even though the problem describes infinitely many boxes. Increment the selected slot for each ball.

**Track the maximum incrementally**

After updating a box, compare its new occupancy with the best seen so far. Every ball contributes to exactly one box and every box count is updated for all of its balls, so the largest recorded count after the final label is precisely the requested maximum.

## Complexity detail
Computing one digit sum examines at most $D$ digits for each of the $R$ labels, giving $O(RD)$ time. The frequency array has $9D+1$ entries and therefore uses $O(D)$ auxiliary space. Under the stated upper bound, $D \le 6$, so this storage is also constant in the legal domain.

## Alternatives and edge cases
- **String conversion:** Summing the characters of each decimal representation has the same $O(RD)$ bound but allocates a temporary string per label.
- **Recount every digit sum:** Storing all sums and calling a linear count for each one is correct but can take $O(R^2)$ time.
- **Single label:** Exactly one box receives one ball, so the answer is one.
- **One-digit interval:** Distinct one-digit labels go to distinct boxes.
- **Powers of ten:** Zero digits still participate in the representation but add nothing to the box number.
- **Tied boxes:** Only the occupancy is returned, so no tie-breaking box identifier is needed.
- **Inclusive upper endpoint:** The ball labeled `highLimit` must be counted.
