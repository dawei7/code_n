## General

**Reduce substrings to runs.** A special substring lies wholly inside a run of
one letter. A run of length $r$ contains $r-L+1$ occurrences of that letter's
length-$L$ substring when $r\ge L$. Thus the locations of runs do not matter;
only their lengths do.

**Retain only three runs per letter.** Let $a\ge b\ge c$ be the three longest
run lengths for one letter, with zero standing for a missing run. Three
occurrences of a candidate have only three relevant distributions:

- all three inside the longest run, allowing length $a-2$;
- two inside the longest run and one inside the second, allowing
  $\min(a-1,b)$; or
- one inside each of three runs, allowing length $c$.

Any other choice of runs is no better than one of these three. Therefore the
best length for a letter is the maximum of those expressions. Scan `s` into
runs, maintain its three largest run lengths per letter, and maximize across
the 26 letters. Each positive expression explicitly supplies three
occurrences; conversely, every possible triple of occurrences fits one of the
three distributions, proving that no longer answer is omitted.

## Complexity detail

The scan visits each of the $N$ characters once. Each run updates three stored
values, and the final 26-letter pass is constant work, so time is $O(N)$. The
fixed $26\cdot3$ table uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Store and sort all runs:** This is correct but requires $O(N\log N)$ time and $O(N)$ space in the worst case, unnecessary under the large constraint.
- **Binary search the length:** A linear counting predicate gives $O(N\log N)$ time, while the three-run formula obtains the answer in one pass.
- **Enumerate substrings:** Direct counting grows at least quadratically and is unsuitable when $N$ may reach $5\cdot10^5$.
- **Overlapping occurrences:** A run of length $r$ contributes $r-L+1$ occurrences of length $L$.
- **Separate runs:** The required three occurrences may be distributed over two or three runs of the same letter.
- **No qualifying character:** Return `-1` when every candidate is non-positive.
