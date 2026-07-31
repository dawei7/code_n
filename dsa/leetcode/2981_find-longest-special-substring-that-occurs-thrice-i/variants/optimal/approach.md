## General

**Reduce substrings to runs.** A special substring lies wholly inside a run of
one letter. A run of length $r$ contains $r-L+1$ occurrences of that letter's
length-$L$ substring when $r\ge L$. Thus the locations of runs do not matter;
only their lengths do.

**Only three runs per letter matter.** Let $a\ge b\ge c$ be the three longest
run lengths for one letter, using zero for a missing run. Three occurrences of
a candidate can be distributed in only three relevant ways:

- all three in the longest run, permitting length $a-2$;
- two in the longest run and one in the second, permitting
  $\min(a-1,b)$; or
- one in each of three runs, permitting length $c$.

Every other distribution is bounded by one of these cases, so the best length
for the letter is their maximum. Scan `s` into runs, maintain the three largest
lengths for each of the 26 letters, and take the best candidate. A positive
candidate has three actual occurrences by its construction; conversely, any
three occurrences induce one of the distributions above, so the scan cannot
miss a longer answer.

## Complexity detail

The run scan touches each of the $N$ characters once. Updating and examining
three entries for each of 26 letters is constant work, so time is $O(N)$. The
table contains exactly $26\cdot3$ integers, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every special substring:** Counting every candidate occurrence is straightforward for $N\le50$, but repeated slicing and scanning can take cubic time.
- **Binary search the answer:** A counting predicate can test a fixed length, but binary search adds machinery and an $O(\log N)$ factor that the run formula avoids.
- **Overlapping occurrences:** A run of length $r$ contributes $r-L+1$ occurrences, not merely one.
- **Separate runs of the same letter:** Occurrences may come from different runs even though intervening characters differ.
- **No qualifying character:** If every computed candidate is non-positive, return `-1` rather than `0`.
