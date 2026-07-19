## General
**Compress strings into character runs**

Represent a string as consecutive `(character, count)` groups. Encode the target once, then encode each candidate. Stretching can change only a run's count, so a candidate must have exactly the same sequence of group characters as the target.

**Check the only legal count changes**

For matching groups with target length `target_count` and word length `word_count`, reject when the word run is longer because stretching cannot delete characters. If the counts differ, the target run must have length at least three; a target run of length one or two cannot be the result of a stretch and therefore requires exact equality.

When every group passes, independently expanding each shorter word run to its target count constructs `s`, so the candidate is expressive. Conversely, any legal stretch preserves group order and characters, never shrinks a run, and can create a count difference only in a target group of length at least three. The tests are therefore necessary and sufficient.

## Complexity detail
Let `c` be the total number of characters in `s` and all candidates. Run-length encoding and comparing each group processes $O(c)$ characters overall. The target groups and one candidate's groups require at most $O(c)$ auxiliary space in the worst case.

## Alternatives and edge cases
- **Two pointers per candidate:** Scan target and word runs directly without materializing candidate groups; this uses constant per-word space but rescans the target for every word.
- **Regular expressions:** Pattern construction can express stretchable groups, but escaping and exact group-length semantics are less transparent.
- **Repeated suffix slicing:** Rebuilding the unprocessed suffix after every group is correct but can take $O(n^2)$ time on many short runs.
- **Exact word:** No stretching is required, so it is always accepted.
- **Target run shorter than three:** Its candidate run must have exactly the same length.
- **Candidate run longer than target:** It cannot be shortened and must be rejected.
- **Character-group mismatch:** Missing, extra, or reordered groups cannot be repaired by stretching.
