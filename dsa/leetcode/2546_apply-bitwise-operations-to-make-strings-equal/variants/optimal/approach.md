## General

**Only one global property matters**

The source and target are mutually reachable exactly when either:

- both contain at least one `1`;
- both contain no `1` and are therefore all zeroes.

The method compares these two Boolean properties:

`("1" in s)==("1" in target)`.

To understand why, inspect the operation on the selected pair of bits.

**Write the operation truth table**

For old ordered pair `(a,b)`, new pair is:

$$
(a\mathbin{|}b,\ a\mathbin{\mathtt{\char94}}b).
$$

All four cases are:

| Before | After |
|---|---|
| `00` | `00` |
| `01` | `11` |
| `10` | `11` |
| `11` | `10` |

The simultaneous-update requirement means both right-hand expressions use the old bits.

**All-zero state can never create a one**

Selecting two zeroes produces two zeroes. If the entire string contains no one, every possible operation acts on `00` and the string remains all zero forever.

Therefore, an all-zero source can reach only an all-zero target.

**A nonzero state can never lose its final one**

Every input pair containing a one transforms to `11` or `10`, both of which still contain at least one one.

Bits outside the selected pair do not change. Thus, if the whole string contains at least one one before an operation, it contains at least one afterward.

A nonzero source can never reach an all-zero target. This proves that matching one-presence is necessary.

**Why one-presence is sufficient**

When at least one one exists, use it together with a zero:

- `01` or `10` becomes `11`, so a one can be created at the zero position.

This lets the state spread ones to desired positions.

When two ones are selected:

- ordered pair `11` becomes `10`, clearing the second selected position while preserving the first as a one.

By choosing index order, keep a convenient anchor one and clear undesired one positions. Because the target also contains at least one one, one target-one position can serve as the final anchor.

A constructive strategy is:

1. use an existing one with zero positions to create ones where needed;
2. retain one desired target-one position;
3. apply `11->10` with that anchor first to clear positions that should be zero.

This can shape any nonzero string into any other nonzero string.

**Equal strings and zero operations**

Operations may be applied any number of times, including zero. If `s==target`, the presence comparison is naturally equal and returns true.

For two all-zero strings, zero operations suffice even though no operation could change them.

**Trace the impossible sample**

`s="11"` contains a one, while `target="00"` does not. Any operation on the only pair turns `11` into `10` or, with reversed indices, leaves one in the other position. The last one cannot disappear, so false is correct.

**Trace a nonzero transformation idea**

From a string with one at the wrong position, pair that one with a target-one zero position to create `11`. Then select the old unwanted one as the second bit of an ordered `11` operation, clearing it while retaining the desired one.

Repeated use moves and duplicates the available one pattern as required.

One may also first spread the seed until every position is one, then clear target-zero positions using a target-one anchor. The target's nonzero guarantee ensures such an anchor exists and is never cleared.

Every step uses two different indices, as required.

**Why counts of ones are not invariant**

The operation can change one one into two via `01->11` and two ones into one via `11->10`. Exact count and parity are not preserved.

Only zero versus nonzero is invariant, which is why checking counts or XOR parity would be overly restrictive.


The truth table proves operations preserve whether at least one one exists. It also supplies constructive moves for creating a one at a zero position and removing an extra one while retaining another. Hence equal one-presence is both necessary and sufficient, exactly matching the returned Boolean equality.

## Complexity detail

Membership test `"1" in s` scans up to `n` characters, and the target test does the same. Total time is $O(n)$.

No collection proportional to input is created; each membership operation uses constant state. Auxiliary space is $O(1)$.

Short-circuiting may find a one early, but all-zero strings require full scans.

## Alternatives and edge cases

- **Count ones:** Comparing only zero versus positive counts works, but exact counts need not match.
- **BFS over strings:** There are exponentially many states and it is unnecessary.
- **Both all zero:** Return true using zero operations.
- **Source zero, target nonzero:** A one cannot be created.
- **Source nonzero, target zero:** The final one cannot be destroyed.
- **Both nonzero:** Constructive spreading and clearing makes transformation possible.
- **Already equal:** Zero operations are allowed.
- **Exactly one one:** It can serve as the seed for all transformations.
- **Simultaneous assignment:** The truth table must use both old bits.
- **Index order:** It determines which position remains one after `11->10`.
