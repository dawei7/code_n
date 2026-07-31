## General

A legal deletion can never remove the last occurrence of a letter. Thus the task is to choose the smallest subsequence that still contains every distinct letter from `s`, while allowing extra copies when they improve lexicographic order. The first example demonstrates why this differs from the standard “keep exactly one of each letter” problem: the second `'a'` makes `"aacb"` smaller than `"acb"`.

Count how many occurrences of each letter remain unprocessed. Also maintain a stack for the current result prefix and a count of each letter already kept in that stack.

Before processing a character `char`, decrement its remaining count. While the stack ends with a letter greater than `char`, ask whether that top occurrence is removable. It is safe to pop exactly when the number of that letter already kept plus the number still remaining is greater than one. After the pop, at least one copy survives either earlier in the stack or later in the input. Replacing the larger top character with the smaller current character improves the first position where the two candidate subsequences differ.

Stop popping when the top is no greater than `char` or when it is the letter's only surviving copy, then append `char`. Each pushed occurrence remains available for later decisions; duplicates are deliberately not skipped.

After the input ends, remove duplicate occurrences from the end of the stack while the trailing letter has another kept copy. Such a deletion leaves the entire preceding prefix unchanged and makes the result a strict prefix of its former value, which is lexicographically smaller. Cleanup stops at the first trailing letter whose only copy must be retained. This is equivalent to processing an end sentinel smaller than every lowercase letter but unavailable for output.

Every pop preserves at least one copy of the removed letter, so the final stack is reachable. Whenever a smaller current character can legally displace a larger suffix character, the loop performs that exchange; refusing it would make the first differing position larger. When it cannot pop, deleting that top would lose a required letter, so no feasible result can move the current character before it. The final cleanup performs every remaining deletion that can only shorten an otherwise equal prefix. These forced local choices establish that no reachable subsequence is lexicographically smaller.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Each occurrence is pushed once and popped at most once. Frequency updates are constant time over the fixed 26-letter alphabet, so the total running time is $O(N)$.

The stack can hold $N$ characters. The two 26-entry frequency arrays are constant-sized, giving $O(N)$ auxiliary space overall.

The benchmark defines size as $N$ and uses many leading `'a'` characters followed by one required `'b'`. Keeping every leading `'a'` is optimal. The stack processes the string once, whereas the slower constructive greedy repeatedly scans the remaining feasible window to choose the next output character, taking $O(N^2)$ time on this input.

## Alternatives and edge cases

- **Keep exactly one copy of each letter:** The usual remove-duplicate-letters stack is incorrect here because additional copies can improve the result; `"aacb" < "acb"`.
- **Enumerate all subsequences:** Filtering all $2^N$ subsequences by distinct-letter coverage gives an exact tiny-input oracle but is infeasible for the legal limit.
- **Repeated feasible-window selection:** Choosing the smallest next character before the earliest required last occurrence is correct, but rescanning overlapping windows can take $O(N^2)$ time.
- **Delete every trailing duplicate:** Trailing cleanup is safe only while another kept copy of that same letter exists; the final required copy must remain.
- **All characters equal:** The shortest one-character result is smallest because all longer choices have it as a prefix.
- **All characters distinct:** No operation is legal, so the original string is returned unchanged even if it is decreasing.
- **Helpful leading duplicates:** In a string such as `"aaab"`, every leading `'a'` is retained because each extra `'a'` precedes the larger required `'b'` and improves lexicographic order.
- **Larger duplicate before a smaller character:** A larger stack suffix may be removed only if another copy survives; the remaining-frequency test enforces that condition.
