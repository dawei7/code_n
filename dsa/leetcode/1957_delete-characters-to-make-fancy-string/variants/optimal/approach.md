## General
**Keep a fancy prefix**

Scan `s` from left to right and store the characters that survive. Before the
next character is considered, the stored prefix is already fancy. Appending
the current character can violate the rule only when the stored prefix ends
with two copies of that same character.

**Delete exactly the forced characters**

If the last two retained characters equal the current one, skip the current
character; otherwise append it. Within any maximal run of equal characters,
at most two may remain, so every later character in that run must be deleted
by every valid result. Keeping the first two deletes no character unless the
constraint forces it. Applying this independently to every run therefore
produces a fancy string with the minimum number of deletions, and the forced
choice for each run also explains why the result is unique.

## Complexity detail
The scan examines each of the $N$ characters once and joining the retained
characters is linear, for $O(N)$ time. The result buffer may contain $N$
characters and therefore uses $O(N)$ space.

## Alternatives and edge cases
- **Run-length processing:** Measure each maximal equal-character run and copy
  its first two characters. This is also $O(N)$ time but requires more explicit
  index bookkeeping.
- **Repeatedly delete triples:** Searching for a violation and rebuilding the
  string after each deletion remains correct, but repeated scans and copies
  can take $O(N^2)$ time.
- Strings of length one or two are already fancy and remain unchanged.
- A run of exactly three characters loses one character, while every longer
  run is truncated to exactly two.
- Separate runs of the same letter are independent when another character
  occurs between them.
