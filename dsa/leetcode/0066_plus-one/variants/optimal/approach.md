## General
**Only the trailing run of nines can propagate a carry**

Scan indices from right to left. If a digit is below `9`, increment it and return immediately because that position absorbs the carry and every more-significant digit remains unchanged. If it is `9`, write `0` and continue carrying left.

**A carry leaving the array creates one new place**

If the loop finishes, every original digit was 9 and has become 0. Prepend a single 1 to represent the new most-significant place.

**The processed suffix is already final**

Before examining an index, every position to its right correctly represents the suffix after propagating a carry through it and is zero. The current position either absorbs the carry by incrementing below 9 or passes it left by changing 9 to 0.

**Trace partial and complete carry propagation**

For `[1,9,9]`, the final two digits each become 0 while carrying left. Digit 1 absorbs the carry and becomes 2, yielding `[2,0,0]`. For `[9,9]`, the carry leaves the array and creates `[1,0,0]`.

**Carry propagation touches exactly the trailing nines**

Adding one leaves every digit left of the first non-nine unchanged. Each trailing `9` becomes `0` and passes a carry left; the first smaller digit absorbs that carry by increasing once, after which no further digit can change.

If such a digit exists, these are exactly the rules of decimal addition. If every digit was `9`, the carry exits the most significant position and the only canonical result is a leading `1` followed by the produced zeroes.

## Complexity detail
At most `n` digits are visited, giving $O(n)$ worst-case time. The input array is reused and only indices are stored, so auxiliary space is $O(1)$; the overflow case necessarily returns one additional digit.

## Alternatives and edge cases
- **Convert to an integer:** is concise but may overflow or violate the arbitrary-length representation purpose.
- **Build a reversed output:** avoids mutation but uses $O(n)$ additional storage.
- **Recursive carry propagation:** performs the same work but spends $O(n)$ call-stack space in the all-9 case.
- If the final digit is below nine, the algorithm returns after constant work. The $O(n)$ bound is the all-nine worst case.
- The input has no leading zero, so prepending `1` to an all-zeroed suffix creates the unique canonical overflow representation.
