## General

Cards with different numbers can never share a group, because every group must contain identical values. Therefore each distinct card value's total frequency must be split into groups of the same size $x>1$.

Let the distinct frequencies be

$$
c_1,c_2,\ldots,c_u.
$$

A group size $x$ is valid exactly when $x$ divides every $c_i$. This is a common-divisor question, and the greatest common divisor summarizes all possible common divisors.

The solution counts values with `Counter(deck)` and computes

```text
g = reduce(gcd, cnt.values())
```

It returns whether `g >= 2`.

**Why a valid partition implies GCD at least two.** Suppose groups of size $x>1$ exist. For card value $v$, all `cnt[v]` copies must be divided into complete groups of $x$, so `cnt[v]` is a multiple of $x$. Thus $x$ divides every frequency. Any common divisor divides their greatest common divisor, so the GCD is at least $x$ and therefore at least two.

**Why GCD at least two constructs a partition.** Suppose the frequency GCD is $g\ge2$. By definition, every frequency is divisible by $g$. Choose $x=g$. For each card value with count $c$, create $c/g$ groups, each containing $g$ copies of that value. These groups use every card, contain identical numbers internally, and all have the same allowed size.

These two directions prove that the boolean GCD test is both necessary and sufficient.

**Why the greatest divisor is enough even when a smaller group size works.** If the frequencies are 6 and 10, GCD is 2 and size 2 works. If frequencies are 8 and 12, GCD is 4, and both size 2 and size 4 work. The task asks only whether some $x>1$ exists. A GCD above one is itself one valid choice, so there is no need to enumerate its factors.

For `[1,2,3,4,4,3,2,1]`, all frequencies are 2 and GCD is 2. Pairing equal cards gives a valid partition. For counts 3, 3, and 2, the GCD is 1, so no common group size above one can divide all three.

For a less uniform example, frequencies 6, 9, and 12 have GCD 3. Choosing group size 3 produces two groups of the first value, three of the second, and four of the third. The number of groups per label may differ; only the number of cards inside every group must be the same. This distinction is why frequencies need to be divisible by `x` rather than equal to one another.

**Counter values, not card labels, drive the result.** Labels may be zero or any allowed integer and need not be consecutive. Only how often each occurs matters. The hash-based Counter creates exactly those frequencies without sorting.

The deck is guaranteed nonempty, so `cnt.values()` contains at least one number and `reduce` has a valid first operand. With only one distinct value, the GCD equals the full deck length; partitioning is possible exactly when that length is at least two.

## Complexity detail

Let $n$ be the number of cards and $u$ the number of distinct values. Counting takes $O(n)$ expected time. Reducing $u$ frequencies with Euclid's algorithm adds $O(u\log n)$ in a fine-grained arithmetic bound.

- **Time complexity:** $O(n)$ under the standard bounded-integer model used by the manifest.
- **Space complexity:** $O(u)$ for the Counter, at most $O(n)$.

The input deck is not modified, and the algorithm stores no actual group partition because the question asks only for existence.

## Alternatives and edge cases

- **Try every group size:** Test $x=2$ through the smallest frequency. This can take quadratic-style work and repeats divisibility information captured by the GCD.
- **Enumerate divisors of one frequency:** Then test each across all counts. It works but is more complex than reducing the GCD directly.
- **Sort the deck into runs:** Frequencies can be obtained after $O(n\log n)$ sorting, but Counter counting is linear expected time and preserves input order.
- **Check only the minimum frequency:** A size dividing the minimum may fail to divide another frequency; common divisibility is required.
- **One card:** Its sole frequency is one, GCD is one, and no $x>1$ group exists.
- **One distinct value with several cards:** Choose $x$ equal to the full count or any divisor above one.
- **All values distinct:** Every frequency is one, so the GCD is one.
- **Mixed frequencies with GCD one:** No valid uniform group size exists even if most counts share a divisor.
- **GCD exactly two:** Pairs always form a valid partition.
- **Zero card labels:** Counter treats zero like any other value; labels do not enter the GCD.
- **Multiple groups for one value:** A frequency may be several times $x$ and is split into that many identical groups.
- **Nonempty guarantee:** It avoids defining a GCD over an empty frequency collection.
- **Return boolean only:** Constructing group arrays would consume unnecessary time and space.
