## General

**Translate “replace consistently” into a two-way mapping**

For `s` to become `t`, every occurrence of one source character must always
produce the same target character. That requires a function from source
characters to target characters.

The problem also forbids two different source characters from producing the
same target character. That injectivity requirement is easiest to enforce with
the inverse function as well. Dictionary `d1` maps characters from `s` to `t`,
while `d2` maps characters from `t` back to `s`.

Together, the dictionaries maintain a one-to-one correspondence among all
characters encountered so far.

**Read corresponding positions together**

`for a, b in zip(s, t)` pairs the character at each source position with the
character at the same target position. Processing left to right automatically
preserves character order: the algorithm never rearranges positions; it only
checks whether every aligned pair can belong to one consistent mapping.

The Reference guarantees `t.length = s.length`, so `zip` visits every character
of both strings. In a generalized function without that guarantee, `zip` would
silently stop at the shorter string, and an explicit length comparison would be
required before the loop.

**Reject a source character that changes its target**

The first conflict test is:

`a in d1 and d1[a] != b`

If source character `a` has appeared before, `d1[a]` records the only target it
is allowed to produce. A different current `b` would require replacing the same
source character in two different ways, contradicting the “all occurrences”
rule.

For `s = "f11"` and `t = "b23"`, the first `'1'` establishes `'1' -> '2'`.
The next `'1'` is aligned with `'3'`, so this condition detects the mismatch
and returns false.

**Reject two source characters sharing one target**

Checking only `d1` is insufficient. For example, `s = "ab"` and `t = "cc"`
would permit mappings `'a' -> 'c'` and `'b' -> 'c'` in a one-way dictionary,
but the contract explicitly forbids that collision.

The inverse conflict test is:

`b in d2 and d2[b] != a`

If target character `b` already belongs to another source character, the test
returns false. This enforces uniqueness of target assignments.

The two conflict expressions are connected by `or`, so either direction is
enough to disprove isomorphism. Python short-circuit evaluation may skip the
second expression when the first is already true, which is safe because the
method returns immediately.

**Record or reaffirm both directions**

If neither conflict exists, the assignments `d1[a] = b` and `d2[b] = a`
store the correspondence. On a first encounter, they create a new pair. On a
later consistent encounter, they overwrite each entry with the same value,
which changes nothing.

The code does not need separate “both unseen” and “both seen consistently”
branches because unconditional identical assignment handles both cases after
conflicts have been excluded.

**Trace `egg` and `add`**

The first position records `'e' -> 'a'` and `'a' -> 'e'`. The second records
`'g' -> 'd'` and `'d' -> 'g'`. At the third position, the same `'g'` and `'d'`
pair appears. Both dictionary lookups agree, so no conflict is found.

The loop finishes and returns true. Replacing `e` with `a` and every `g` with
`d` indeed yields `add`.

For `paper` and `title`, the repeated-position pattern is the same: positions 0
and 2 repeat together in both strings, while each other newly encountered
character pairs with a new target. The maps remain mutually consistent.

**Why a successful scan proves isomorphism**

After each processed prefix, `d1` and `d2` are inverses on every encountered
pair. The conflict checks preserve this invariant: an inconsistent extension
returns false, while a consistent extension adds or reaffirms one inverse pair.

If the loop ends, define replacement of every source character using `d1`.
At every position, the recorded target is exactly the aligned character in
`t`, so replacement produces `t`. Because `d2` is an inverse, no two source
characters map to the same target. The mapping therefore satisfies every part
of the definition.

**Why an early false result is conclusive**

A `d1` conflict proves one source character would need two target values. No
global mapping can satisfy both positions. A `d2` conflict proves two distinct
source characters would need the same target. No one-to-one mapping can satisfy
that either.

Later characters cannot repair a contradiction already present in aligned
positions, so returning immediately is correct and avoids unnecessary work.

**ASCII and self-mapping behavior**

Characters may be any valid ASCII character, including spaces, punctuation,
digits, and control characters represented in the strings. Dictionary keys
handle them uniformly. A character may map to itself: pair `a == b` creates
matching entries in both dictionaries and violates no condition.

Uppercase and lowercase characters are distinct ASCII characters. The method
does not normalize case, which is correct because the Reference does not ask it
to.

## Complexity detail

Let $n$ be the common string length and $k$ the number of distinct characters
appearing across the mappings. The loop processes $n$ aligned pairs with
expected $O(1)$ dictionary operations each, so time is $O(n)$.

Each distinct mapped character contributes at most one entry to each dictionary,
giving $O(k)$ auxiliary space as recorded in the manifest. Because ASCII has a
fixed alphabet, $k \le 128$ and this can also be described as $O(1)$ under a
fixed-alphabet model; $O(k)$ makes the actual storage behavior explicit.

## Alternatives and edge cases

- **First-occurrence pattern:** Transform each string into the sequence of first-occurrence indices and compare those sequences; correct but builds proportional output.
- **Last-seen arrays:** Two fixed 128-entry arrays can replace dictionaries for strict ASCII input.
- **One dictionary only:** Insufficient because it allows two source characters to share one target.
- **Set of paired characters:** Comparing counts of source, target, and pair sets can work but is less direct than inverse maps.
- **Equal characters:** Self-mapping is explicitly allowed.
- **Repeated source with new target:** Rejected by `d1`.
- **New source with used target:** Rejected by `d2`.
- **Same-length guarantee:** Makes `zip` complete; otherwise compare lengths first.
- **One-character strings:** Always isomorphic because one correspondence suffices.
- **Empty strings:** Outside the minimum-length constraint, but two empty strings would return true naturally.
