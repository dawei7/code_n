## General
**Encode only parity.** Assign one bit to each of the five vowels. While scanning the string, toggle a vowel's bit whenever that vowel appears; consonants leave the mask unchanged. The mask after index $i$ describes whether every vowel count in the prefix through $i$ is odd or even.

**Equal prefix states define a valid substring.** If the same mask occurs after two prefix endpoints, every bit toggled an even number of times between them. Therefore the intervening substring has even counts for all vowels. Record the earliest index at which each of the 32 masks appears; whenever a mask repeats, its distance from that earliest index is the longest valid substring ending here for this mask.

Initialize mask zero at virtual index $-1$, allowing an even-parity prefix beginning at index zero. Every valid substring corresponds to two equal prefix masks, and choosing the earliest occurrence maximizes its length. Thus the largest recorded distance is exactly the requested answer.

## Complexity detail
Each of the $n$ characters causes at most one bit toggle, one state lookup, and one maximum update, so time is $O(n)$. There are only $2^5=32$ parity masks, making auxiliary space $O(1)$.

## Alternatives and edge cases
- **Recount every prefix:** Recompute five vowel counts from the beginning for each endpoint, then apply the same prefix-state logic. It is correct but takes $O(n^2)$ total time.
- **Enumerate substrings:** Count vowels independently inside every candidate substring, which can take $O(n^3)$ time without prefix counts.
- **Five prefix arrays:** Store cumulative counts and test substring parities in constant time, but enumerating all endpoints still costs $O(n^2)$.
- **No vowels:** The mask remains zero, so the complete string is valid.
- **Single vowel:** Its only nonempty substring has an odd count, producing answer zero.
- **Zero counts:** A missing vowel satisfies the even-count condition.
- **Whole string valid:** Repeating mask zero at the final index returns length $n$.
- **Overlapping candidates:** Earliest-state storage automatically chooses the longest one without discarding later endpoints.
