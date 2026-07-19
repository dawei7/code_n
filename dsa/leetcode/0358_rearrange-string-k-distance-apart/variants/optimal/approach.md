## General
**Why the most frequent available letter is the urgent choice**

A letter with many remaining copies needs the most future placement opportunities. At each output position, keep every currently eligible letter in a max-heap keyed by its remaining frequency and choose the most frequent one. Spending a rarer letter while a more frequent one is available can leave too few positions for the frequent letter's later copies, whereas choosing the most constrained letter first preserves the greatest flexibility.

**Enforce distance with release positions**

After placing a letter at position `i`, remove it from the heap and put its remaining count into a FIFO cooldown queue with release position $i + k$. Before choosing at a later position, return every entry whose release position has arrived to the heap. Therefore the same letter cannot be selected in any of the intervening $k - 1$ positions, and it becomes eligible exactly when its next occurrence would be far enough away.

**Recognize impossibility at the first empty choice**

If output positions remain but the heap is empty, every unplaced letter is still cooling down. No letter is legal at the current position, so no continuation of the already constructed prefix can satisfy the distance rule. The greedy frequency choice is safe because it always schedules the letter with the tightest remaining demand; the standard exchange argument swaps that letter with any less frequent eligible choice without making later placements harder. Thus exhausting the heap proves impossibility, while completing all positions produces a permutation whose repeated letters obey the required spacing.

**Trace the cooldown boundary**

For `s = "aabbcc"` and $k = 3$, placing `a` at index 0 releases it at index 3. The heap then supplies `b` and `c`; at index 3, `a` returns and the same cycle can repeat, giving `"abcabc"`.

## Complexity detail
Let `n` be the string length and `a` the number of distinct lowercase letters. Each character enters and leaves the heap at most once per occurrence, for $O(n \log a)$ time. Because $a \le 26$, this is $O(n)$. The heap and cooldown queue hold at most $O(a)$ entries, which is $O(1)$ auxiliary space for the fixed English alphabet; the returned string itself uses $O(n)$ output space.

## Alternatives and edge cases
- **Repeated full sorting:** sorting all remaining letter counts before every placement is straightforward but can cost $O(n a \log a)$ and obscures the cooldown boundary.
- **Backtracking over permutations:** explores choices directly but has factorial worst-case growth and repeats equivalent states created by identical letters.
- **Block-by-block greedy selection:** choosing up to `k` distinct letters per round can also work, but careful handling is needed for a final partial block and exhausted counts.
- When $k \le 1$, every ordering already satisfies the separation rule.
- A one-character string is valid even when `k` is larger than the string length.
- If the heap empties while cooldown entries remain, returning a partial string would violate the contract; the required result is `""`.
- Heap tie-breaking may produce a different valid permutation from the examples, so correctness depends on multiplicities and distances rather than exact serialization.
