## General
**A consonant fixes the earliest legal boundary**

Scan `word` from left to right. Remember the index of the most recent consonant. Any all-vowel substring ending at the current position must start after that index, so a consonant discards every earlier candidate start at once.

**The least recent vowel controls completeness**

For each of the five vowels, store its latest index. At a vowel position, let $p$ be the minimum of those five indices. When $p$ lies after the latest consonant, every start from one position after that consonant through $p$ produces an all-vowel substring containing all five vowels. There are exactly `p - last_consonant` such starts, so add that quantity to the answer.

Every valid substring is counted at its right endpoint. Its start must be after the latest consonant, and it cannot pass the least recent last occurrence among the five required vowels. Conversely, every start in that interval includes each vowel and no consonant. The scan therefore counts every valid index range exactly once.

## Complexity detail
The scan processes each of the $n$ characters once. Taking the minimum of five stored indices is constant work, so the total time is $O(n)$. The latest positions of five vowels and a few counters use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every start position:** Extending each all-vowel range and tracking its vowels is straightforward, but it can require $O(n^2)$ time.
- **Two at-most counts:** Within each vowel-only segment, subtract substrings containing at most four distinct vowels from those containing at most five; this is also linear but uses more sliding-window bookkeeping.
- A consonant resets the allowable start range even if all five vowels appeared earlier.
- Repeated copies of a vowel create additional valid starts or endings and must count as separate index ranges.
- Strings shorter than five characters, and strings missing any one vowel, contribute zero.
