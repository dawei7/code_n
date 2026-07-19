## General
**XOR treats each bit position as parity**

At each bit position, XOR records whether the number of set occurrences is odd. It is associative and commutative, so input order and conceptual pair grouping do not matter. Equal integers cancel because $x \oplus x = 0$, and zero is the identity.

**The accumulator contains exactly the odd-frequency prefix values**

After processing any prefix, the accumulator is the XOR of values with odd occurrence parity in that prefix. Encountering a value toggles all its bit contributions; the second identical occurrence toggles them back off.

**The frequency guarantee leaves one uncancelled value**

At the end, every paired value has even count and vanishes. Only the single value has odd count one, so it remains in the accumulator.

**Trace cancellation independent of ordering**

Reordering conceptually groups $1 \oplus 1$ and $2 \oplus 2$ into zeros; the result is $4 \oplus 0 \oplus 0 = 4$.

**Pair cancellation leaves the unmatched bit pattern**

XOR is associative and commutative, so input order may be regrouped conceptually. Every duplicated value contributes $x \oplus x = 0$, and zero changes no accumulator.

The frequency guarantee leaves exactly one value without a partner. All pairs cancel independently, so the final accumulator is precisely that unmatched value's bit pattern.

## Complexity detail
One XOR per input gives $O(n)$ time. A single integer accumulator gives $O(1)$ space.

## Alternatives and edge cases
- **Frequency map:** is linear time but uses $O(n)$ space.
- **Sort then compare pairs:** uses $O(n \log n)$ time.
- **Arithmetic set formula:** risks overflow in fixed-width languages.
- Negative integers work under the language's fixed-width or signed bitwise semantics because identical bit patterns still cancel.
- The method depends on every nonanswer value appearing exactly twice; different repetition counts require other bit-counting techniques.
