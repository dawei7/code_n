## General
**Encode only frequency parity**

Whether a count is odd or even is all that matters. Represent the prefix ending at the current position with a 10-bit mask: bit `b` is one exactly when the corresponding letter has appeared an odd number of times. Reading a character toggles its bit with XOR.

The parity mask of a substring is the XOR of the masks at its two prefix boundaries. A substring has every count even when those boundary masks are equal. It has exactly one odd count when the masks differ in exactly one bit.

**Count compatible earlier boundaries**

Maintain how many earlier prefixes produced each of the $2^{10}=1024$ masks, beginning with one occurrence of mask zero for the empty prefix. After updating the current mask, add the frequency of the identical mask and the frequencies of the ten masks obtained by toggling one bit.

These are precisely all earlier boundaries whose XOR with the current boundary has zero or one set bits. Each earlier boundary identifies one distinct non-empty substring ending at the current position, so accumulating these frequencies counts every wonderful occurrence exactly once.

## Complexity detail
For each of the $N$ characters, the algorithm performs one mask update and eleven fixed-frequency lookups. Because the alphabet size is the fixed constant ten, this is $O(N)$ time. The array of 1024 mask frequencies occupies $O(1)$ space with respect to $N$.

## Alternatives and edge cases
- **Enumerate every substring:** Updating parity for each right endpoint avoids recounting characters but still takes $O(N^2)$ time.
- **Character-count arrays per substring:** Rebuilding ten counts for every interval adds work without using the prefix-XOR relationship.
- **One character:** Its sole substring has one odd count and is wonderful.
- **All one letter:** Every substring is wonderful, producing $N(N+1)/2$ occurrences.
- **Ten distinct letters:** Only the ten length-one substrings qualify.
- **Repeated text:** Equal substring contents at different positions are counted separately.
