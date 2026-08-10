## General

**Treat each bit as an independent permission.** An integer permission mask is a compact set. If bit $b$ is one, the user has permission $b$; if it is zero, the user lacks it. The query asks for two reductions over every row:

- `common_perms` should contain bit $b$ only when every user's mask contains that bit;
- `any_perms` should contain bit $b$ when at least one user's mask contains that bit.

Bitwise AND and OR implement these definitions position by position.

**AND means universal membership.** For one bit position, AND returns one only if both input bits are one. Repeated over all rows, that bit remains one only if no user ever has zero there. Therefore

`BIT_AND(permissions)`

is exactly the mask of permissions common to all users. One missing permission clears its bit from the aggregate, and later rows cannot restore it.

**OR means existential membership.** OR returns one when either input bit is one. Repeated over all rows, a bit becomes one as soon as any user has it and remains one. Therefore

`BIT_OR(permissions)`

is exactly the mask of permissions held by at least one user.

The two aggregates appear in the same `SELECT`, so the database can conceptually maintain both running values during one scan. No `GROUP BY` is present because the desired scope is the entire table, not one output per user or category.

**Why exactly one result row is produced.** Aggregate queries without grouping produce one aggregate group containing all qualifying input rows. The select list contains only aggregates, so the result has one row with columns aliased `common_perms` and `any_perms`. “Any order” is automatically satisfied because there is only one row.

The `user_id` column does not enter either expression. It establishes row identity through the primary key, but permission union and intersection depend only on the masks.

**Follow the sample at the bit level.** The masks are:

`5 = 0101`, `12 = 1100`, `7 = 0111`, and `3 = 0011`.

No bit is one in all four rows. For example, the lowest bit is absent from $12$, while the $4$ bit is absent from $3$. Their repeated AND is `0000`, or zero.

Across the same rows, every one of the four shown bit positions appears somewhere. Repeated OR yields `1111`, or fifteen.

**Why numerical min or max would be wrong.** Integer ordering compares the combined positional value, not permission membership independently. The smallest mask need not be the common intersection, and the largest need not contain every bit seen elsewhere. For instance, masks $8$ (`1000`) and $7$ (`0111`) have numeric maximum $8$, but their OR is $15$ and their AND is zero. The bitwise aggregates are essential.

**A fold interpretation.** If the rows contain masks $p_1,\ldots,p_r$, the outputs are

$$
p_1\mathbin{\&}p_2\mathbin{\&}\cdots\mathbin{\&}p_r
$$

and

$$
p_1\mathbin{|}p_2\mathbin{|}\cdots\mathbin{|}p_r.
$$

Both operations are associative and commutative. The database may read rows in any physical order and still obtain the same result. This is why the query needs no ordering clause for correctness.

## Complexity detail

Let $r$ be the number of rows and let $w$ be the fixed bit width of the SQL integer type. The engine can update both aggregate masks once per row, doing $O(w)$ bit work per mask. With fixed-width integers, $w$ is constant, so the logical running time is $O(r)$.

Only two running aggregate values are required, so the algorithmic working space is $O(1)$ beyond the database's input storage and one-row output. No sorting, grouping table, or per-row result structure is required.

The manifest claims $O(r\log r)$ time and $O(r)$ space. Those are overly broad and do not reflect the exact ungrouped aggregate query. A database implementation may have execution-framework overhead, but the relational operation itself is a linear fold with constant accumulator state. The exact source therefore supports $O(r)$ time and $O(1)$ auxiliary space under fixed-width permission integers.

## Alternatives and edge cases

- **Application-side fold:** Fetch masks and reduce them with language-level AND and OR. It computes the same values but transfers all rows and moves simple aggregation out of the database.
- **Recursive SQL fold:** A dialect without `BIT_AND` or `BIT_OR` aggregates can number rows and combine masks recursively. It is longer and dialect-specific but preserves the linear reduction.
- **Per-bit conditional aggregation:** Test each known permission bit with Boolean counts. This becomes verbose, requires a predetermined bit width, and reconstructs operations the native aggregates already provide.
- **Use `MIN` and `MAX`:** Incorrect because numeric order is not set intersection or union.
- **One user:** Both aggregates equal that user's mask; a singleton set's intersection and union are identical.
- **All users identical:** Both outputs equal their shared mask.
- **No common permission:** AND becomes zero even if every user has several different permissions.
- **Every possible permission appears somewhere:** OR sets every corresponding bit, even if no one user has them all.
- **Permission mask zero:** One zero row forces `common_perms` to zero; it contributes no set bits to `any_perms`.
- **Duplicate masks:** They do not change either result because AND and OR are idempotent.
- **Row order:** Associativity and commutativity make physical scan order irrelevant.
- **Null permissions:** SQL bitwise aggregates may ignore nulls or have dialect-specific behavior. The intended schema treats the permission mask as a supplied value; nullable extensions need an explicit policy.
- **Empty table:** Ungrouped aggregates still return one row, commonly with null aggregate values because no identity seed is specified by SQL. The exact source adds no fallback.
- **Signed integer representation:** Permission masks are intended as nonnegative encoded sets. Negative masks would expose sign-bit and width semantics tied to the SQL type.
- **Manifest mismatch:** No sorting or row-proportional aggregate table is visible. The exact operation is a one-pass constant-state fold.
