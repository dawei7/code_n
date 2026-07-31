## General

**Accumulate only qualifying values.** Bitwise OR is associative, commutative, and has 0 as its identity. Therefore, the qualifying values can be incorporated one at a time in any order without storing them separately. Initialize `result` to 0, scan `nums`, and test each value's parity. When a value is even, update `result |= value`; when it is odd, leave the accumulator unchanged.

**Track which even-number bits have appeared.** After any prefix of the array has been processed, each bit in `result` is set exactly when that bit appeared in at least one even value in the prefix. Processing an odd value preserves this statement because odd values are excluded by the contract. Processing an even value extends the statement to include precisely the bits of that new qualifying value. The invariant therefore holds after the full scan and gives the requested OR.

Starting from 0 also handles the no-even-number case without a special final branch: if no update occurs, the accumulator remains 0.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each value is inspected once and requires constant-time parity and bitwise operations under the bounded integer contract, so the time complexity is $O(n)$. The accumulator and loop value occupy $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Filter then reduce:** Materializing all even values before applying OR is correct, but uses $O(n)$ extra space without reducing the scan time.
- **Frequency table:** OR-ing values that occur at least once also works because repeated OR is idempotent, but a table is unnecessary for this direct aggregation.
- **No even values:** Zero is returned because it is the initial accumulator and the identity of OR.
- **Duplicate even values:** Repeatedly OR-ing the same number does not change the result, but every occurrence may safely be processed.
- **Odd values with useful bits:** Their bits must still be ignored; parity filtering happens before the OR update.
