## General
**Collapse each word to its distinct-letter mask.** Assign one bit to every lowercase letter and OR together the bits appearing in a word. Multiplicity does not affect either validity rule, so anagrams and repeated-letter variants with the same set share one mask. Count how many word entries produce each mask. Discard masks with more than seven set bits because no seven-letter puzzle can contain them.

**Generate only masks a puzzle can accept.** A valid word mask must include the puzzle's first-letter bit and may include any subset of the other six puzzle bits. There are only $2^6=64$ such possibilities. Build the mask for the six optional letters, enumerate all of its submasks with `submask = (submask - 1) & optional`, OR each with the required bit, and add its stored word frequency.

**Preserve multiplicity and order.** The frequency table makes all word entries with the same mask contribute together, while processing puzzles from left to right produces answers in their original order. Every counted mask contains the required first letter by construction and no bit outside the puzzle, so it satisfies both validity rules. Conversely, every valid word's optional letters form one enumerated submask, so none are missed.

## Complexity detail
Constructing word masks examines $W$ characters. Each puzzle has seven characters and exactly 64 relevant submasks, both fixed constants, so all puzzle work is $O(p)$. Total time is $O(W+p)$. The frequency map stores $u$ retained masks, using $O(u)$ auxiliary space; the answer array is output storage.

## Alternatives and edge cases
- **Check every word against every puzzle:** Set containment is direct and correct, but the cross product takes $O(\lvert\texttt{words}\rvert p)$ comparisons.
- **Trie over sorted distinct letters:** A trie can prune branches not present in a puzzle, but mask counting and 64 submasks are simpler for the fixed alphabet and puzzle length.
- **Word with more than seven distinct letters:** It can never fit any puzzle and should be omitted from the frequency map.
- **Repeated letters in a word:** They set one bit and do not need multiple puzzle occurrences.
- **Required first letter absent:** A subset of the other six letters alone never counts because the required bit is ORed into every lookup.
- **Duplicate word masks:** Each original word entry counts, so the map stores a frequency rather than a Boolean.
- **Required letter only:** A word consisting solely of repeated copies of the first puzzle letter corresponds to the zero optional submask.
