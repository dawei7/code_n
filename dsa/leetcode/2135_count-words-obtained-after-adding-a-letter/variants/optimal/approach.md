## General

**Represent letter sets as masks**

Because letters never repeat within a word and final order is arbitrary, a
word is completely described by a 26-bit mask. Set the bit for every letter
in each start word and store all resulting masks in a set.

For a target mask, the required appended letter must be one of its set bits.
Remove each target letter in turn. If any resulting mask belongs to the start
set, that start word gains exactly the removed, previously absent letter and
can be rearranged into the target. Count the target once and move to the next
one.

Removing every possible final letter examines all legal predecessors. A found
mask directly constructs a valid conversion, while any valid conversion must
appear among those removals. Thus the test is necessary and sufficient, and
duplicate target occurrences are correctly counted independently.

## Complexity detail

Let $L$ be the total character count across both arrays and $s$ the number of
distinct start masks. Building masks and trying each target letter take
$O(L)$ time. The start-mask set uses $O(s)$ space.

## Alternatives and edge cases

- **Compare every target with every start:** Direct set-difference tests are
  correct but take quadratic time in the word counts.
- **Sort each word:** Canonical sorted strings also capture letter sets, but
  deletion candidates require string construction and sorting adds overhead.
- The operation appends exactly one letter; an identical start and target word
  is not a valid conversion.
- Target order is irrelevant, but duplicate target occurrences each
  contribute to the answer.
- A target can have several valid predecessors and is still counted only once.
