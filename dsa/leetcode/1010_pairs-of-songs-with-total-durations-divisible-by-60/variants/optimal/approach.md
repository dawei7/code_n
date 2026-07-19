## General
**Reduce durations to remainders:** Divisibility by `60` depends only on each duration modulo `60`. Keep a fixed 60-entry array in which `counts[r]` records how many earlier songs have remainder `r`.

**Count a pair when its later index arrives:** For the current `remainder`, an earlier song must have remainder `(60 - remainder) % 60`. Add that bucket's current count to the answer, then increment `counts[remainder]`. Updating after counting ensures every pair is counted once with its earlier index already stored and prevents pairing a song with itself.

**Handle self-complementary remainders naturally:** Remainders `0` and `30` complement themselves. The same lookup still works: each new song contributes the number of earlier songs in its own bucket, producing all distinct index pairs without special-case formulas.

For any valid pair, when its later song is processed, the earlier remainder is present in exactly the required complement bucket, so the pair is counted. Conversely, every added bucket entry forms a sum congruent to zero modulo `60`; therefore no invalid or duplicate pair enters the answer.

## Complexity detail
Each of the $N$ durations performs constant-time remainder, lookup, and update operations, giving $O(N)$ time. The 60 counters occupy a fixed amount of memory independent of $N$, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Check every pair:** Two nested index loops are direct and correct but require $O(N^2)$ time.
- **Count first, combine later:** A frequency pass followed by pairing complementary buckets is also $O(N)$ time and $O(1)$ space, with separate combination formulas for remainders `0` and `30`.
- **One song:** No index pair exists, so return zero.
- **Repeated durations:** Equal values at different indices form distinct pairs when their sum is divisible by `60`.
- **Multiples of 60:** They pair only with other remainder-`0` durations.
