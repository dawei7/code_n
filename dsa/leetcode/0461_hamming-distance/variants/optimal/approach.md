## General

The Hamming distance asks, bit position by bit position, whether `x` and `y` disagree. The bitwise exclusive-or operation, XOR, performs exactly that comparison in parallel:

| Bit from `x` | Bit from `y` | XOR bit |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

An XOR bit is one precisely when the two input bits differ. Therefore `x ^ y` creates a mask whose set bits mark all and only the differing positions. The answer is the number of set bits in that mask.

The exact solution expresses both steps directly:

`(x ^ y).bit_count()`

**Why XOR isolates differences**

Write both nonnegative integers in binary and align them at the least significant bit. Leading positions omitted from the shorter representation are zeros. XOR applies the truth table independently at every position, so equal pairs become zero and unequal pairs become one.

For `x = 1` and `y = 4`, use four displayed bits:

```text
x = 0001
y = 0100
    ----
XOR 0101
```

The XOR result is decimal `5`, whose binary representation contains two ones. The Hamming distance is therefore two.

For `x = 3` (`11`) and `y = 1` (`01`), XOR gives `10`, which has one set bit, so the answer is one.

**What `bit_count` returns**

Python's integer method `bit_count()` returns the number of ones in the integer's binary representation, also called the population count. Because both inputs are nonnegative, their XOR is nonnegative. Each counted one corresponds to one differing bit position, and no equal position contributes.

This is not the same as counting the number of binary digits. For example, XOR result `8` is binary `1000`: it spans four positions but contains only one set bit, so the Hamming distance is one.

Leading zeros need no explicit padding. Above the highest set bit of both inputs, both conceptual bits are zero and therefore equal. Between their bit lengths, the shorter number contributes conceptual zero bits, and ordinary integer XOR already handles those positions correctly.

**Why the one-line result is exact**

Take any bit position `p`. If `x` and `y` have different bits there, XOR places one at `p`, and `bit_count` adds exactly one for it. If their bits are equal, XOR places zero there, and it adds nothing. Since bit positions are independent, summing the set bits counts every disagreement once and no agreement. That is exactly the definition of Hamming distance.

The method also handles equality naturally. If `x == y`, XOR returns zero. Zero has no set bits, so the result is zero.

If one input is zero, XOR returns the other input. The distance is then the number of ones already present in that number, which is correct because those are precisely the positions where it differs from zero.

**Why using the built-in operation is still the complete algorithm**

`bit_count` does not replace the central reasoning; XOR is the transformation that turns the original comparison problem into a population-count problem. Once that reduction is established, using the language's dedicated and well-tested primitive is appropriate. Implementing a manual loop would expose the mechanics of counting set bits, but it would not change which bits must be counted or improve the asymptotic result under this fixed-width contract. The one-line source is concise because each operation matches one exact logical step.

## Complexity detail

Let $w$ be the number of relevant bits, which is $O(\log(\max(x,y)+1))$. At the bit-operation level, forming the XOR and counting its set bits process $O(w)$ machine-word information, giving the manifest-style time bound $O(\log\max(x,y))$ for positive inputs.

The contract limits both values to 31 non-sign bits. Under the usual fixed-width machine model, $w\le31$ is a constant, so the same operation is commonly described as $O(1)$ time. Both descriptions are compatible: one exposes dependence on bit length, while the other treats the fixed integer width as constant.

Auxiliary space is $O(1)$ under the fixed-width model: only the XOR result and returned count are needed. For arbitrary-size Python integers outside the constraints, the temporary XOR integer occupies $O(w)$ bits, but the source's bounded domain supports the manifest's constant-space convention.

## Alternatives and edge cases

- **Brian Kernighan's method:** Repeatedly replace `z` with `z & (z - 1)`. Each iteration clears the lowest set bit, so the iteration count equals the answer. It is useful when a built-in population count is unavailable.
- **Shift and inspect:** Repeatedly add `z & 1` and shift `z` right. It is straightforward but examines zero bits between set bits as well.
- **Convert to a binary string:** `bin(x ^ y).count('1')` is concise but allocates a textual representation and performs more conversion work than `bit_count`.
- **Compare decimal digits:** Hamming distance concerns binary positions, not decimal notation; decimal comparison gives unrelated results.
- **Equal inputs:** XOR is zero and the answer is zero.
- **One input zero:** The answer is the population count of the other input.
- **Different bit lengths:** Conceptual leading zeros are handled automatically by integer XOR.
- **Maximum allowed value:** At most 31 relevant bits are processed, so no loop or recursion depth concern exists.
- **Negative values outside the contract:** Python defines bitwise operations using an infinite two's-complement model, which changes how leading sign bits should be interpreted. The nonnegative-input guarantee avoids that ambiguity.
