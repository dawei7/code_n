## General

**Preserve high set bits first.** Let $k$ be the set-bit count of `num2`. A bit where $x$ differs from `num1` contributes its place value to the XOR. Therefore, when selecting up to $k$ set bits already present in `num1`, matching a higher position avoids a larger XOR penalty than matching any lower position. Scan from bit 29 down to bit 0 and copy set bits from `num1` until either the scan ends or all $k$ bits have been placed.

**Add any remaining bits at the cheapest positions.** If `num1` contains fewer than $k$ set bits, every extra 1 in $x$ must differ from a zero in `num1`. Such a mismatch contributes $2^b$, so choose unused positions from least significant upward.

The first phase greedily takes every negative XOR-cost opportunity in descending value, while the second phase takes the necessary positive costs in ascending value. Any alternative selection would replace a chosen position with a more expensive one, so it cannot produce a smaller XOR.

## Complexity detail

At most $\lfloor\log_2 U\rfloor+1$ legal bit positions are examined, followed by at most the same number of low-position checks. The time is $O(\log U)$ and the auxiliary space is $O(1)$. Under the source constraint $U\le10^9$, this is a fixed maximum of 30 bit positions.

## Alternatives and edge cases

- **Enumerate candidate integers:** Searching values with the required bit count is exponential in the bit width and unnecessary.
- **Sort per-bit XOR costs:** Choosing the $k$ smallest costs independently is equivalent and useful as an oracle, but explicit sorting adds storage.
- **Equal set-bit counts:** Copying `num1` exactly gives XOR zero and is optimal.
- **Too many set bits in `num1`:** Keep only its highest set positions.
- **Too few set bits in `num1`:** Preserve all existing ones, then add the lowest zero positions.
- **One required bit:** Select the highest set bit of `num1`.
- **Maximum legal width:** Both inputs still occupy at most 30 positions.
