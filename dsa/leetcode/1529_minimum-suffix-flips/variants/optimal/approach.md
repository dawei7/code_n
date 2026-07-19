## General
**Track the value produced by earlier suffix flips**

A flip started before the current index affects the current position and every later position. Only the parity of the number of earlier flips matters: after an even count the current constructed bit is `0`, and after an odd count it is `1`. Store that effective bit as `current`, initially `"0"`.

When the next target bit equals `current`, no operation should start there. Starting one would make that position wrong and would require an additional flip at the same boundary to repair it. When the bit differs, a flip must start at that index because later operations cannot change an earlier position. One flip is sufficient, and it toggles `current` for the rest of the scan.

**Count target transitions from an implicit leading zero**

The minimum is therefore the number of changes while reading the sequence consisting of an implicit initial `0` followed by `target`. A leading `1` contributes one flip; each later `0`-to-`1` or `1`-to-`0` boundary contributes another. Runs of identical bits require no extra operations.

Every counted boundary forces a flip to establish the required value at its first position, giving a lower bound. Starting exactly one suffix flip at each such boundary realizes all target runs in order, so the bound is attainable and minimal.

## Complexity detail
The algorithm inspects every target bit once, giving $O(n)$ time. It stores only the current effective bit and the flip count, so auxiliary space is $O(1)$.

No mutable representation of the constructed string is needed; suffix effects are represented entirely by their parity.

## Alternatives and edge cases
- **Explicit suffix simulation:** flipping every stored bit whenever a mismatch appears is correct but can require $O(n^2)$ time on an alternating target.
- **Count adjacent transitions separately:** initialize the answer from whether the first bit is `1`, then add every adjacent difference; this is algebraically equivalent.
- **Run-length encoding:** counting nonzero run boundaries works, but materializing runs adds unnecessary storage.
- **All zeros:** no boundary differs from the implicit initial zero, so the answer is 0.
- **All ones:** only the leading boundary differs, so one flip of the complete string is enough.
- **Alternating bits:** every position changes the required effective value and forces a flip.
- **Trailing run:** once its leading boundary is handled, all remaining equal bits need no further flip.
- **Single bit:** `"0"` needs zero operations, while `"1"` needs one.
