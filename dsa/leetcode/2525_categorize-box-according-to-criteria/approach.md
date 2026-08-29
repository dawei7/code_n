## General

**Evaluate two independent properties**

The final category depends on two Boolean facts:

- whether the box is bulky;
- whether the box is heavy.

Neither property changes the definition of the other. The method computes them independently and then maps their four possible combinations to the required label.

**Compute volume exactly**

`v=length*width*height` is the box volume.

The box is bulky if either:

- at least one dimension is at least 10,000;
- volume is at least $10^9$.

These alternatives are joined by logical OR. A box with small individual dimensions can still be bulky through their product, and one very large dimension makes it bulky even if volume is otherwise below the threshold.

**Check dimensions with `any`**

The generator

`x>=10000 for x in (length,width,height)`

tests each of the three dimensions. `any` returns true when at least one test succeeds.

The outer `or v>=10**9` then incorporates the volume rule.

Boundary equality matters: `>=` correctly classifies a dimension exactly 10,000 or a volume exactly one billion as bulky.

**Compute heaviness**

`mass>=100` is the complete heavy predicate. A mass exactly 100 qualifies.

Dimensions and volume have no effect on this test.

**Convert Booleans to two bits**

The source converts both predicates to integers:

- false becomes 0;
- true becomes 1.

It constructs index

`i=heavy<<1|bulky`.

Left-shifting `heavy` by one places it in binary bit 1, while `bulky` occupies bit 0. The resulting truth-table indices are:

| Heavy | Bulky | Binary index | Decimal |
|---:|---:|---:|---:|
| 0 | 0 | `00` | 0 |
| 0 | 1 | `01` | 1 |
| 1 | 0 | `10` | 2 |
| 1 | 1 | `11` | 3 |

Bitwise OR combines the two independent bits.

**Map the index to the required word**

List

`['Neither','Bulky','Heavy','Both']`

is ordered to match those four indices:

- index 0: neither predicate;
- index 1: bulky only;
- index 2: heavy only;
- index 3: both.

Returning `d[i]` implements the complete category table without nested conditionals.

**Trace the first sample**

For dimensions 1000, 35, and 700:

- none reaches 10,000;
- volume is $1000\cdot35\cdot700=24,500,000$, below $10^9$.

So `bulky=0`. Mass 300 is at least 100, so `heavy=1`.

The index is $(1\ll1)\mathbin{|}0=2$, and `d[2]` is `"Heavy"`.

**Why the volume product is safe in this source**

At maximum dimensions, volume can be $10^{15}$, which exceeds a 32-bit integer. Python integers grow automatically, so multiplication is exact.

In a fixed-width language, a 64-bit integer is required or the comparison should be arranged to avoid overflow.


The bulky expression matches exactly the disjunction in the statement, and the heavy expression matches its threshold. These two correct Booleans have only four combinations.

The bit index uniquely encodes each combination, and the lookup list assigns exactly the specified label to each. Therefore, every possible valid input returns the correct category.

**No category priority ambiguity**

`"Both"` is not handled by letting one predicate override another. It has its own combination index three. Similarly, `"Neither"` is selected only when both facts are false.

This explicit combination avoids mistakes from checking `bulky` first and returning too early before considering `heavy`.

**Separate the two ways to become bulky**

The dimension test and volume test are not interchangeable. A box measuring $10{,}000\times1\times1$ is bulky because one dimension reaches the boundary even though its volume is only 10,000. A box measuring $1{,}000\times1{,}000\times1{,}000$ is bulky because its volume is exactly $10^9$, even though every dimension is below 10,000.

The logical OR preserves both examples. Replacing it with AND would incorrectly require both kinds of evidence.

**Why integer flags are deliberate**

The code could index a dictionary with Boolean pairs, but converting to zero and one makes the bit positions explicit. Shifting heavy guarantees it cannot collide with the bulky flag: heavy contributes either zero or two, while bulky contributes either zero or one. Their OR therefore produces each integer from zero through three exactly once across the four truth combinations.

The label array is constant and local. Its ordering is part of the algorithm, so changing the flag-bit assignment would require changing the array order too.

## Complexity detail

The method performs a fixed number of comparisons, multiplications, Boolean operations, and one list lookup. Time is $O(1)$.

It stores a fixed four-element label list and a few scalar values, so auxiliary space is $O(1)$.

The amount of work does not depend on the numeric magnitudes of the four inputs under the standard word-arithmetic model.

## Alternatives and edge cases

- **Nested conditionals:** Explicitly test both, bulky only, heavy only, and neither; it is equally correct but longer.
- **Tuple lookup:** Use `(bulky,heavy)` as a dictionary key instead of a bit index.
- **Dimension exactly 10,000:** It is bulky.
- **Volume exactly $10^9$:** It is bulky.
- **Mass exactly 100:** It is heavy.
- **Large dimension and heavy mass:** Return `"Both"`.
- **Large volume with small dimensions:** Volume alone is sufficient for bulky status.
- **Neither threshold met:** Return `"Neither"`.
- **Overflow:** Fixed-width implementations need safe volume arithmetic.
- **Independent predicates:** Compute both before selecting a label.
