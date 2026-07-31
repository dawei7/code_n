## General

A transformation never mixes index parities. It only replaces the even-index sequence by one of its cyclic rotations and independently replaces the odd-index sequence by one of its cyclic rotations. Consequently, two equal-length words are equivalent exactly when their even sequences lie in the same rotation class and their odd sequences lie in the same rotation class.

Represent each rotation class by its lexicographically smallest rotation. Booth's algorithm finds that representative in linear time. For a sequence `text`, inspect the doubled sequence `text + text`, whose length-`len(text)` windows are exactly the rotations. Maintain two candidate starts and the offset through their currently equal prefixes. At the first mismatch, the start producing the larger character, together with every start skipped inside that matched prefix, cannot be minimal; advance that candidate past the mismatch and reset the offset. When one candidate leaves the original sequence, the smaller remaining start identifies the minimum rotation.

For each word, extract `word[::2]` and `word[1::2]`, canonicalize both, and insert their ordered pair into a set. Equivalent words produce the same pair because taking a cyclic shift does not change the minimum member of a rotation class. Conversely, equal pairs prove that both parity sequences differ only by allowed cyclic shifts, so one transformation connects the words. Each distinct pair therefore requires exactly one group, and the number of set entries is the minimum answer.

## Complexity detail

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

Booth's algorithm advances each candidate monotonically and takes linear time in its sequence length. The two parity sequences together contain every character of a word, so all canonicalizations and expected-time set operations take $O(S)$ time.

The extracted sequences, doubled working strings, canonical rotations, and stored signatures contain $O(S)$ characters in total. The auxiliary-space bound is therefore $O(S)$.

## Alternatives and edge cases

- **Enumerate and compare all rotations:** Materializing every rotation and selecting the smallest remains correct but takes $O(L^2)$ time for a sequence of length $L$.
- **Suffix array on the doubled sequence:** A suffix-array construction can identify the smallest legal rotation, but it is substantially more machinery than the linear two-candidate scan.
- **Different lengths:** A transformation preserves length, and the two signature components retain their lengths, so words of different lengths cannot collide.
- **One-character parity sequence:** Its sole cyclic rotation is itself; the same Booth helper handles it directly.
- **Empty odd sequence:** A one-character word has an empty odd-index sequence, whose canonical representative is the empty string.
- **Repeated or periodic characters:** Candidate elimination remains valid when long prefixes tie; the offset can reach the complete sequence length, selecting an equivalent minimal start.
- **Duplicate words:** Repeated signatures occupy one set entry and therefore do not create extra groups.
