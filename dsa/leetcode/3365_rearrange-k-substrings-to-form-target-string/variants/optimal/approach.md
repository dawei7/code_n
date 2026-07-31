## General

The split boundaries are fixed because all $k$ substrings have width $w=n/k$. A legal operation can change only the order of these complete blocks. Consequently, the target is reachable exactly when its own width-$w$ blocks form the same multiset as the source blocks.

Scan each string at offsets $0,w,2w,\ldots,(k-1)w$ and count every extracted substring in a hash map. Comparing the two maps checks both identity and multiplicity. This matters when a block occurs more than once: a set would lose the number of available copies.

If the maps are equal, pair every target occurrence with one source occurrence of the same block and order those source blocks according to the target, proving that the construction is possible. If a count differs, the target demands a block that the source cannot supply in the required quantity, and reordering cannot change any block's contents, so construction is impossible.

## Complexity detail

Let $n$ be the common string length and $w=n/k$ the block width. Creating all $k$ substring keys copies $kw=n$ characters in total for each string. Expected hash-map operations are proportional to the characters hashed, so the total expected time is $O(n)$. Stored keys and counts occupy $O(n)$ auxiliary space in the worst case.

The benchmark defines `size` as $n$, uses $k=n/2$, and supplies distinct two-character blocks in reverse target order. The reference counts them in $O(n)$ time. A correct direct-matching baseline that scans the source block list for each target block performs $\Theta(k^2)=\Theta(n^2)$ comparisons on this ordering.

## Alternatives and edge cases

- **Sort both block lists:** Sorting and comparing the blocks is correct, but costs $O(n\log k)$ time in the comparison model instead of expected linear time.
- **Repeated direct search:** Matching each target block to the first unused equal source block is correct but can require $O(k^2w)$ time.
- **Character counts only:** The strings are already guaranteed to be anagrams; equal character frequencies do not preserve fixed block boundaries.
- **Use a set of blocks:** A set ignores multiplicities and can accept a target that requests too many copies of one block.
- **One block:** When $k=1$, only exact equality succeeds because the block itself cannot be changed.
- **Character-sized blocks:** When $k=n$, the blocks are single characters, so the anagram guarantee makes every input succeed.
- **Duplicate blocks:** Count every occurrence rather than assigning a block identity only once.
