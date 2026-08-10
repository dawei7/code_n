## General

**Turn the editing problem into a pairing problem**

Two neighboring letters are almost equal when the absolute difference between their character codes is less than `2`. Because the word contains lowercase English letters, this means the letters are either identical or consecutive in the alphabet. The task asks for the minimum number of character changes needed so that no adjacent pair has that property.

The implementation scans from left to right with index `i` beginning at `1`, so the current pair is `word[i - 1]` and `word[i]`. If the pair is already safe, the scan advances by one and checks the next overlapping pair. If it is almost equal, at least one of those two positions must be changed in every valid final word: leaving both untouched would preserve this forbidden adjacency. The solution counts one mandatory operation and advances by two.

That two-position jump is the heart of the greedy method. Conceptually, it chooses to change the right character `word[i]`. The implementation does not need to construct the replacement because only the minimum number of operations is requested. After assigning this operation to the bad pair, neither position needs to participate in another charged pair.

**Why one change can safely repair the chosen pair**

Suppose `word[i - 1]` and `word[i]` are almost equal. Change `word[i]` to a lowercase letter that is not almost equal to `word[i - 1]` and, when `i + 1` exists, is also not almost equal to `word[i + 1]`. Each neighboring character forbids at most itself and its immediate alphabet neighbors, so two neighbors forbid at most six of the 26 lowercase letters. At least one permissible replacement always remains.

This observation justifies skipping directly to `i + 2`. The changed position can be made compatible with both its left and right neighbors. The next pair that could still require a new operation starts at `word[i + 1]` and `word[i + 2]`; that is exactly the pair examined after the jump.

The source code expresses the almost-equal test as `abs(ord(word[i]) - ord(word[i - 1])) < 2`. The `ord` calls convert each lowercase letter to its integer code. Lowercase letters occupy consecutive code points, so a difference of zero means the same letter, a difference of one means adjacent alphabet letters, and every larger difference is allowed.

**Why the greedy count is minimal**

Every time the algorithm finds a bad pair, any valid solution must change at least one of its two positions. The algorithm charges exactly one operation to that pair and then skips both positions. Therefore, the bad pairs to which it charges operations are disjoint: no character belongs to two charged pairs.

If the scan charges $t$ disjoint bad pairs, every valid editing plan needs at least $t$ operations because one character change cannot cover two disjoint pairs. This is a lower bound on the optimum. On the other hand, the replacement argument above shows that the algorithm’s $t$ chosen changes can actually make all charged positions compatible with their neighbors; all uncharged adjacencies were found safe when examined. Thus $t$ operations are sufficient. Since the same value is both necessary and sufficient, the greedy answer is optimal.

For a concrete trace, consider `word = "aaaa"`. At `i = 1`, the first two letters form a bad pair, so the answer becomes one and `i` jumps to `3`. The last two letters form another bad pair, so the answer becomes two. Two edits are necessary because the disjoint original pairs at positions $(0,1)$ and $(2,3)$ each require a change. They are also sufficient, for example by replacing positions 1 and 3 with suitably distant letters.

Now consider `word = "abc"`. The pair `"ab"` is bad, so the algorithm counts one edit and skips to the end. Although `"bc"` was also bad in the original word, changing the shared middle character can repair both adjacencies. Counting both overlapping pairs separately would overestimate the answer; the skip prevents that error.

**What the state variables mean**

`ans` is the number of mandatory disjoint bad pairs found so far. `i` identifies the right endpoint of the next pair being tested. When a pair is safe, incrementing `i` preserves overlap so that the right character becomes the left character of the next pair. When a pair is bad, incrementing `i` by two records that the current right character will be changed and avoids charging an overlapping pair that the same change can repair.

The word itself is never modified. That is intentional: after a bad pair, the scan skips the position whose hypothetical replacement could affect future comparisons. The next actual comparison involves only untouched characters, so the original string remains sufficient for computing the count.

## Complexity detail

Let $N$ be the number of characters in `word`. Index `i` only moves forward, by either one or two positions, and never exceeds $N$. Each visited pair requires two `ord` conversions, a subtraction, an absolute value, and a comparison, all constant-time operations. The total running time is $O(N)$.

The implementation stores only `ans` and `i` plus temporary scalar values, so its auxiliary space is $O(1)$. It does not create a character list or a modified copy of the word. The input string itself occupies $O(N)$ space but is not auxiliary storage created by the algorithm.

## Alternatives and edge cases

- **Edit every detected overlap independently:** Counting all almost-equal adjacent pairs is wrong because one change to their shared character may repair two pairs, as in `"abc"`.
- **Dynamic programming:** A DP over positions and chosen replacement letters can find the minimum, but it introduces an alphabet-sized state even though the disjoint-pair greedy argument gives a linear, constant-space solution.
- **Actually constructing replacements:** Construction is possible by selecting a letter far from both neighbors, but the task asks only for the number of changes. Materializing the edited word adds work without changing the count.
- **A one-character word:** There is no adjacent pair, the loop never runs, and the correct answer is zero.
- **A two-character word:** The answer is one exactly when the two characters are equal or consecutive in the alphabet; otherwise it is zero.
- **Long overlapping runs:** For strings such as `"aaaaa"`, the jump by two counts disjoint pairs and avoids double-charging overlaps. The result is the size of a maximum greedy packing of mandatory bad pairs.
- **Alphabet boundaries:** Letters `'a'` and `'z'` are not considered adjacent; ordinary code-point distance correctly gives `25`. There is no wraparound in the definition.
- **Replacement feasibility:** Even when a changed position has two neighbors, those neighbors collectively forbid at most six lowercase choices, so the proof never depends on an unavailable character.
- **Input immutability:** Python strings cannot be changed in place, and this implementation only reads the original characters.
