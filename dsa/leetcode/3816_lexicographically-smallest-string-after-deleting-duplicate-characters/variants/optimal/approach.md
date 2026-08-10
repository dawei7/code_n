## General

**The final string need not contain each letter exactly once**

An occurrence may be deleted only while another copy of the same letter remains. Therefore every distinct letter in the original string must survive at least once. Any subsequence retaining at least one occurrence of each original letter is reachable: delete the unwanted occurrences one by one, always leaving a chosen survivor.

However, deleting every duplicate is not automatically best. Lexicographic order compares the first differing character; only when one string is a complete prefix of the other does the shorter string win. In `"aaccb"`, the one-copy result `"acb"` is larger than `"aacb"` because their first characters agree and then `a < c` at the second position. Keeping an extra small letter near the front can be beneficial.

The real task is to delete an occurrence only when its removal makes the earliest possible part of the string smaller, while never removing the last copy of any letter.

**Track how many undeleted copies still exist**

`cnt = Counter(s)` starts with the total frequency of every letter. The source decrements a count only when an occurrence is popped and permanently deleted. It does not decrement merely because the scan passes a character.

Consequently, `cnt[x]` always means the number of copies of `x` that have not been deleted: copies already stored in `stk` plus copies not processed yet. This is different from the common “remaining suffix frequency” interpretation.

The test `cnt[stk[-1]] > 1` therefore answers exactly the safety question: if the top stack occurrence is deleted, does at least one copy of that letter remain somewhere among the other kept or future occurrences? If yes, popping respects the operation rule. If the count is 1, that top occurrence is the last surviving copy and cannot be removed.

**Use the stack to repair a harmful adjacent order**

The stack holds the current subsequence after chosen deletions. Every new character `c` is compared with the most recent kept character.

While all three conditions hold—

- the stack is nonempty;
- `stk[-1] > c`, so the previous character is lexicographically larger;
- `cnt[stk[-1]] > 1`, so deleting it preserves another copy—

the source pops the stack top and decrements that letter's surviving count.

Why is this deletion beneficial? At the position occupied by the larger top character, keeping it would expose that character before the smaller current `c`. Removing it lets `c`, or another no-larger character uncovered by further pops, appear earlier. The first difference between the improved subsequence and one retaining the harmful top favors the improved subsequence.

After one pop, a still-earlier stack character may also be larger than `c` and safely duplicated. The `while` loop continues so that `c` moves left across the entire removable decreasing suffix, not just one character.

The current `c` is then always appended. Unlike the classic “remove duplicate letters” problem, there is no `in_stack` set and no rule skipping an already-kept letter. Extra copies can improve lexicographic order, so every occurrence remains unless a concrete greedy pop deletes it.

**Why smaller or equal stack tops should stay**

If `stk[-1] < c`, deleting the top to move `c` earlier would make the result larger at the first differing position: the existing smaller letter is preferable. This remains true even if another copy of the top exists later.

If `stk[-1] == c`, replacing the earlier copy with the current identical copy does not improve the visible prefix. It may only discard flexibility or do redundant work. The strict comparison `>` correctly leaves equal adjacent choices alone.

If `stk[-1] > c` but its count is 1, deleting it would remove that letter entirely, which no allowed sequence can do. The algorithm must keep it even though the local order looks unfavorable.

These three stopping cases explain every part of the loop condition.

**Trim a safely duplicated suffix**

After the scan, no future smaller character can arrive to trigger the main loop. Yet trailing duplicates may still make the string larger solely by making it longer.

If the final stack top has `cnt[top] > 1`, deleting that occurrence preserves another copy elsewhere in the stack. The resulting string is a strict prefix of the old one, so it is lexicographically smaller. The second `while` loop repeatedly performs this safe suffix shortening:

`while stk and cnt[stk[-1]] > 1`

Each pop decrements the live count. It stops when the top is the last surviving copy of its letter. Only a suffix can be removed this way without exposing a different following character; deleting an interior duplicate needs the main-loop comparison to prove the replacement suffix is smaller.

For `"aa"`, both copies are appended because neither is larger than the other. The final loop removes one trailing `a` and returns `"a"`, which is a prefix and therefore smaller. For `"abca"`, the trailing `a` is duplicated and can be removed, giving `"abc"`; deleting the leading `a` instead would begin with `b` and be worse.

**Trace the main example**

For `"aaccb"`, the two `a` characters are appended. The two `c` characters are also appended because `a < c` and equal `c` characters do not trigger a pop.

When `b` arrives, the top is `c`, which is larger. At that moment two undeleted `c` copies exist, so one `c` is popped and its count falls to 1. The newly exposed top is the other `c`. It is still larger than `b`, but its count is now 1, so it must survive. Appending `b` produces `"aacb"`. No trailing letter has a duplicate, so the final loop changes nothing.

This example shows why `cnt` must be decremented on every deletion. Without the decrement, the loop would incorrectly believe another `c` survived and delete the final mandatory copy.

**Why the greedy decisions lead to the smallest reachable subsequence**

Whenever the main loop pops a letter `x > c`, at least one other `x` remains. Any candidate that keeps this particular `x` before `c` can be improved by deleting it: all earlier characters stay the same, and at the first affected position the smaller `c` or another uncovered character moves earlier. The required letter `x` is still available, so this exchange stays reachable. Thus an optimal result never needs a safely removable larger character at that position.

When the loop stops, removing the top cannot create a better legal prefix: the top is smaller than `c`, equal to it, or indispensable. Appending `c` is therefore consistent with the smallest achievable prefix after processing this point. Repeating the exchange argument over the scan establishes the smallest possible nontrailing order.

Finally, any safely removable trailing occurrence only lengthens a string whose preceding characters remain identical. Removing all such suffix copies is always beneficial and stops exactly when another deletion would erase a distinct letter. The two phases together produce the lexicographically smallest reachable subsequence.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Building `Counter(s)` takes $O(N)$ time. Every character is pushed onto `stk` exactly once. An occurrence can be popped at most once, either during the scan or during final trimming. Although a `while` loop is nested inside the `for` loop, all its iterations across the entire run total at most $N$. The total running time is $O(N)$.

The stack can contain all $N$ characters, so it uses $O(N)$ space. The counter has at most 26 keys because the input contains lowercase English letters; that part is $O(1)$ under the fixed alphabet. Joining the stack constructs an output string of length at most $N$. The manifest's $O(N)$ auxiliary-space bound is therefore accurate.

## Alternatives and edge cases

- **Force one copy per distinct letter:** The classic monotonic-stack algorithm with a kept set solves a different problem. It would return `"acb"` for `"aaccb"` and miss the smaller legal answer `"aacb"`.
- **Enumerate reachable subsequences:** Every subsequence retaining all distinct letters is a candidate, giving exponentially many possibilities and making brute force infeasible for $N=10^5$.
- **Dynamic programming over positions and counts:** The state needed to compare arbitrary future suffixes is large; the exchange property captured by the stack eliminates that complexity.
- **All characters distinct:** Every count is 1, so no pop is legal. The original string is the only reachable result and is returned unchanged.
- **All characters equal:** The scan keeps every copy, then the final loop removes trailing copies until exactly one remains.
- **A decreasing string with no duplicates:** Larger leading letters cannot be removed because each is the last copy of its letter, so the result remains the original string.
- **A larger letter duplicated later:** An earlier copy can be popped when a smaller current letter arrives because `cnt` confirms another copy survives, allowing the smaller letter to move forward.
- **Another copy already lies earlier in the stack:** The safety count includes kept occurrences as well as future ones. A duplicated top may be deleted even when no copy remains in the unread suffix.
- **Trailing duplicates:** They require the second loop; no future character exists to trigger the main comparison, but shortening an equal-prefix result is still lexicographically beneficial.
- **Counter interpretation:** Counts are decremented only for deletions. Treating them as unread-suffix frequencies and decrementing every scanned character would change the safety condition and no longer match the exact source.
