## General

**Test each index independently.** Traverse `words` together with its
0-based indices. For each word, perform a character-membership search for
`x`. Append the current index exactly once when that search succeeds and
append nothing when it fails. Finding one occurrence is sufficient because the
output represents words, not individual character positions.

Every appended index is valid because its membership test found `x` in the
corresponding word. Conversely, the traversal visits every word, so any index
whose word contains `x` is appended when that word is examined. The result
therefore contains exactly the required indices. Producing them in increasing
index order is valid even though the contract also accepts other orders.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

In the worst case, membership search examines every character of every word,
so the algorithm takes $O(S)$ time. Aside from the returned index list, it
stores only the current index and word, giving $O(1)$ auxiliary space. This
time bound is worst-case optimal because an absent target cannot be ruled out
without inspecting all $S$ characters.

## Alternatives and edge cases

- **Build a set for every word:** Membership becomes constant-time after construction, but constructing the sets still takes $O(S)$ time and uses avoidable extra space.
- **Count target occurrences:** Counting is also linear, but does unnecessary work after the first occurrence because only presence matters.
- **Repeated character scans:** Rechecking every character once for every other character remains correct but can take $O(\sum_w\lvert w\rvert^2)$ time.
- **Multiple occurrences in one word:** Emit that word's index only once.
- **No matching words:** Return an empty list.
- **Every word matches:** Return every index from $0$ through $W-1$.
- **Result order:** Any permutation of the correct indices is accepted.

