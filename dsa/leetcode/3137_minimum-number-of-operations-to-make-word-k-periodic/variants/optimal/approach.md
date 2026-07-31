## General

Because `k` divides $n$, partition `word` into $B=n/k$ non-overlapping blocks whose starting indices are multiples of `k`. A k-periodic result is exactly a sequence in which all $B$ blocks have the same length-`k` value.

One operation copies one currently existing block value into one block position. Choose a value that occurs $f$ times in the original partition. Its $f$ matching positions need no operation, and each of the other $B-f$ positions can be changed with one copy, so that choice costs $B-f$ operations.

No sequence ending with that value can do better: every original block position containing a different value must change at least once, and one operation changes only one destination block. Moreover, copying cannot invent a new block value; every final value descends from some original block. Therefore the global minimum is obtained by maximizing $f$, and the answer is $B$ minus the largest block frequency.

Scan `word` in jumps of `k`, use each slice as a hash-map key, and increment its frequency. After processing every aligned block, subtract the maximum stored count from the total number of blocks.

## Complexity detail

Creating and hashing all block slices processes $n$ characters in total, so the algorithm takes $O(n)$ expected time. The distinct block keys together contain at most $n$ characters, giving $O(n)$ auxiliary space. Hash-table operations use their standard expected constant-time behavior beyond the key hashing cost.

## Alternatives and edge cases

- **Compare every block with every candidate:** Count each candidate frequency by rescanning all $B$ blocks. This is correct but requires $O(B^2k)$ character comparison work in the worst case.
- **Sort the blocks:** Sorting and taking the longest equal run also finds the maximum frequency, but it adds $O(B\log B)$ block comparisons and extra storage.
- **Simulate copy operations:** Mutating the string is unnecessary; the frequency argument determines the minimum without constructing a final word.
- **Already k-periodic:** If all blocks are equal, the maximum frequency is $B$ and the answer is zero.
- **Single block:** When `k == n`, the only block already forms a k-periodic string.
- **Unit block length:** When `k = 1`, the problem reduces to keeping the most frequent character and replacing every other character.
- **Frequency tie:** Any tied most-frequent block yields the same minimum count; the algorithm does not need to choose which final word to construct.
