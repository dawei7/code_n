## General

**Characterize rows that one shared flip set can make uniform**

Flipping a column affects every row, so rows cannot choose flip sets independently. We need the largest group of rows for which one common column-flip pattern makes every row uniform.

For a particular row, there are only two ways it can become uniform:

- Make every final value zero.
- Make every final value one.

If a row begins `[0, 1, 0]`, making it all zero requires flipping exactly columns containing one. Making it all one requires flipping exactly the complementary columns containing zero.

Now compare two rows. They can both become uniform under the same flips exactly when they are either identical or exact bitwise complements. Identical rows react identically. Complementary rows remain complements after every shared column flip, so when one becomes all zero, the other becomes all one.

Rows with any other relationship cannot both be uniform: at some columns their equality relationship differs, so no shared flip vector can make both constant.

**Normalize a row and its complement to one key**

The solution chooses a canonical representation whose first bit is always zero:

```python
t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
```

If the row starts with zero, it is converted directly to a tuple.

If it starts with one, every bit is flipped with XOR one. For binary values:

- `0 ^ 1` is one.
- `1 ^ 1` is zero.

The complemented row now starts with zero.

An original row and its exact complement produce the same normalized tuple. If one starts with zero, it is kept. Its complement starts with one and is flipped back to the first row.

Conversely, two rows producing the same normalized tuple must be identical or complements. Each normalization either leaves all bits unchanged or flips all bits. Reversing those possibilities shows the original rows differ by either no flips at all or a flip at every position.

**Count equivalent row patterns**

`cnt = Counter()` starts an empty frequency map. For every row:

```python
cnt[t] += 1
```

adds one to its normalized pattern.

Each counter bucket therefore contains exactly one compatibility class: all rows that are identical to or complementary with one another. One shared column flip pattern can make every row in that class uniform.

To see the flip pattern, take the normalized key. Flip precisely the columns where the key contains one. Every row represented by the key becomes all zero or all one, depending on whether that row originally matched the key or its complement.

**Take the largest compatible class**

The result is:

```python
return max(cnt.values())
```

The matrix is nonempty, so the counter has at least one value and `max` is safe.

Every frequency is achievable because all rows in that bucket share a working flip pattern. No solution can combine rows from different buckets because rows made uniform by one flip pattern must be identical or complementary before the flips and therefore must have the same normalized key.

The largest bucket is consequently both a lower bound and an upper bound on the optimum, proving the returned count is exact.

**Why the first bit is a sufficient anchor**

Normalization could choose any fixed column as its anchor. The first column is convenient and always exists because every row is nonempty.

The key does not describe which final uniform value a row gets. It describes each bit relative to the row's first bit. A zero in the key means "same as the first bit," and a one means "different from the first bit." Complementing an entire row changes the actual first bit but preserves all these relative relationships.

That relative pattern is exactly what matters under shared column flips.

**A brief example**

Rows `[0, 1]` and `[1, 0]` both normalize to `(0, 1)`. Flipping the first column turns them into `[1, 1]` and `[0, 0]`, so both are uniform.

Row `[1, 1]` normalizes to `(0, 0)` and belongs to another class. No flip set can make all three rows uniform simultaneously.

## Complexity detail

Let `M` be the number of rows and `N` the number of columns.

Normalizing one row reads all `N` bits and creates a length-`N` tuple, taking `O(N)` time. Hashing the tuple for the counter also takes `O(N)` the first time its hash is needed. Across `M` rows, total time is `O(MN)`. Finding the maximum among at most `M` counters adds `O(M)` and does not change the bound.

In the worst case, all `M` normalized patterns are distinct and each stored tuple has `N` values. Counter storage is therefore `O(MN)`. Temporary generator state is constant beyond the tuple being created.

These exact bounds match the manifest.

## Alternatives and edge cases

- **String pattern key:** Record whether each bit equals the row's first bit using characters such as `T` and `F`. It is equivalent to the normalized tuple and has the same bounds.
- **Compare every row pair:** Count identical or complementary rows for each reference row. This takes `O(M^2N)` time and repeats the same class work.
- **Encode rows as integers:** With manageable column counts, pack the normalized bits into one integer key. This can reduce object overhead while preserving the same conceptual normalization.
- **One row:** Its pattern frequency is one, and any row can be made uniform by choosing flips based on that row.
- **One column:** Every row is already uniform, all rows normalize to the one-bit zero key, and the answer is `M`.
- **All rows identical:** They share one key and can all be made uniform together.
- **All rows split between a pattern and its complement:** Both groups normalize to one key, so every row is counted.
- **Already uniform zero and one rows:** All-zero and all-one rows are complements and normalize together.
- **Different relative patterns:** They cannot share a successful flip set, even if they have the same number of ones.
- **Binary constraint:** XOR one is a complement only because every cell is zero or one.
- **Nonempty rows:** Accessing `row[0]` is safe under the matrix constraints.
- **Input preservation:** Tuples and complemented generators are new objects; the matrix rows are never modified.
