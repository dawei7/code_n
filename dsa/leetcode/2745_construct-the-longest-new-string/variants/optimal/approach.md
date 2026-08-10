## General

**Understand which equal-letter blocks can touch**

Every chosen piece has length two:

- `AA` starts and ends with `A`;
- `BB` starts and ends with `B`;
- `AB` starts with `A` and ends with `B`.

Two `AA` pieces cannot be adjacent because `AAAA` contains `AAA`. Similarly, two `BB` pieces cannot be adjacent.

An `AA` piece also cannot be followed directly by `AB`, because `AAAB` begins with `AAA`. An `AB` piece cannot be followed by `BB`, because `ABBB` contains `BBB`.

The safe structure must therefore alternate `AA` and `BB` pieces, while `AB` pieces can be arranged at a compatible edge or together as `ABAB...`.

**Use every possible AA-BB pair**

Let $p=\min(x,y)$. We can use $p$ copies of `AA` and $p$ copies of `BB` in alternating order. This contributes $2p$ pieces without creating three equal consecutive characters.

If $x=y$, all equal-letter pieces are used.

If $x>y$, after pairing every `BB`, at most one additional `AA` can be used. A second surplus `AA` would have no `BB` separator and force an invalid adjacency.

If $y>x$, symmetrically at most one additional `BB` can be used.

Thus the maximum number of equal-letter pieces is:

$$
2\min(x,y)+[x\ne y],
$$

where the bracket is one when counts differ and zero otherwise.

**Why all AB pieces can be included**

Repeated `AB` pieces form `ABABAB...`, which never contains `AAA` or `BBB`. They do not need separators from each other.

When `x>y`, arrange the `AB` chain before an alternating sequence that begins and ends with `AA`:

`AB ... AB, AA, BB, AA, ... , BB, AA`.

The boundary `AB + AA` is `ABAA` and is safe.

When `y>x`, arrange the alternating sequence beginning and ending with `BB` first, then append the `AB` chain:

`BB, AA, BB, ... , AA, BB, AB ... AB`.

The boundary `BB + AB` is `BBAB` and is safe.

When `x=y`, an alternating equal-block sequence can be oriented to accept the `AB` chain at an appropriate side. Therefore every one of the `z` pieces can always be used.

**Translate piece count into character length**

Every selected piece contributes exactly two characters; joining pieces never deletes characters in this problem.

When `x<y`, the source returns:

`(x * 2 + z + 1) * 2`.

Inside the parentheses are two equal-letter pieces per available `AA`, all `z` AB pieces, and one surplus `BB`.

When `x>y`, it uses the symmetric expression with `y`.

When `x==y`, every piece can be used, so it returns `(x + y + z) * 2`.

**Trace x=2, y=5, z=1**

Two `AA` pieces can alternate with two `BB` pieces, and one extra `BB` can be used. All one `AB` piece is included. That is:

$$
2\cdot2+1+1=6
$$

pieces and length twelve. Three of the five `BB` pieces are used; the other two cannot be separated because no additional `AA` remains.

The example ordering `BB, AA, BB, AA, BB, AB` realizes this length.

**Trace x=3, y=2, z=2**

Use two AA-BB pairs, one surplus `AA`, and both `AB` pieces. This is:

$$
2\cdot2+1+2=7
$$

pieces and length fourteen.

An arrangement beginning with the AB chain and then alternating equal blocks realizes it.

**Why no longer construction exists**

Remove all `AB` pieces conceptually. In any valid remaining sequence, `AA` and `BB` must alternate because identical equal-letter blocks cannot touch. An alternating sequence can contain at most one more block of one type than the other. Therefore it uses at most twice the smaller count plus one when counts differ.

Adding back all $z$ AB pieces can increase the count by at most $z$, and the constructions above achieve exactly that upper bound. The formula is optimal.

**No dynamic programming is needed**

Only the count imbalance matters. The internal identities of pieces are identical within each type, and the transition restrictions yield a closed structural bound.

## Complexity detail

The exact solution performs a few comparisons, multiplications, additions, and one return. Its time is $O(1)$ and auxiliary space is $O(1)$.

The magnitude of `x`, `y`, and `z` does not cause loops or stored constructions. Python arithmetic on the small constrained integers is constant-time in the problem model.

The function returns only the maximum length and does not allocate the actual string.

## Alternatives and edge cases

- **Dynamic programming over remaining counts and endpoints:** Can solve the problem but creates many states for a pattern captured by a simple count bound.
- **Greedily append any safe piece:** May strand usable pieces without a proof or careful boundary ordering.
- **Equal x and y:** Every AA and BB piece can alternate, and every AB piece is also usable.
- **More AA than BB:** Use all BB, the same number plus one of AA, and all AB.
- **More BB than AA:** Use all AA, the same number plus one of BB, and all AB.
- **Large surplus:** All but one unmatched equal-letter block must be discarded.
- **Many AB pieces:** They can repeat as `ABAB...` without creating triples.
- **Boundary after AA:** Do not place AB directly there; orient AB pieces on the other safe side.
- **Boundary before BB:** Do not place AB directly before BB; choose the constructive orientation described.
- **Length conversion:** Multiply selected piece count by two because every piece has length exactly two.
