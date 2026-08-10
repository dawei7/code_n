## General

A parenthesis string is valid when two conditions hold:

1. In every left-to-right prefix, the number of kept closing parentheses does not exceed the number of kept opening parentheses.
2. After the complete string, the two counts are equal.

Letters do not affect balance and must remain in their original positions. Only parentheses may be removed. The result must include every distinct valid string using the minimum possible number of removals.

The source avoids exploring every possible removal count. It first computes exactly how many opening and closing parentheses must be deleted. It then backtracks over keep/delete decisions while enforcing those two fixed budgets.

**Computing the unavoidable removals**

The first scan uses `l` as the number of unmatched opening parentheses currently available and `r` as the number of unmatched closing parentheses that have already been proven invalid.

- On `(`, increment `l`. This opening parenthesis may match a later closing parenthesis.
- On `)`, if `l > 0`, decrement `l` and match it with one earlier opening parenthesis.
- On `)` when `l == 0`, increment `r`. No earlier unmatched opening exists, and a later opening cannot move backward to match this closing parenthesis.
- On a letter, change neither count.

At the end, `r` is the number of closing parentheses that could not be matched with anything before them. Every valid result must delete that many closing parentheses. The final `l` is the number of opening parentheses for which no later closing parenthesis exists. Every valid result must also delete that many opening parentheses.

These counts are not merely estimates. They are a lower bound because the unmatched parentheses cannot participate in any valid matching, and they are attainable because the scan greedily matched every possible closing parenthesis to a preceding opening one. Keeping those matched pairs and removing the unmatched occurrences produces a valid parenthesis structure. Thus, `l + r` is exactly the minimum number of deletions.

For `s = "()())()"`, the scan finishes with `l = 0` and `r = 1`. There is one excess closing parenthesis and no excess opening parenthesis, so every minimum solution must delete exactly one `)`.

For `s = ")("`, the first character creates `r = 1`, and the final opening parenthesis leaves `l = 1`. Both parentheses must be removed, producing the empty string.

**Meaning of the backtracking state**

The recursive function `dfs(i, l, r, lcnt, rcnt, t)` carries six pieces of information:

- `i` is the next input index to process.
- `l` is the number of opening-parenthesis deletions still required.
- `r` is the number of closing-parenthesis deletions still required.
- `lcnt` is the number of opening parentheses kept in `t`.
- `rcnt` is the number of closing parentheses kept in `t`.
- `t` is the output prefix built from already processed characters.

The initial call begins at index zero with the full deletion budgets, no kept parentheses, and an empty output prefix.

**The deletion branches**

When `s[i]` is `(` and `l > 0`, the source may delete it. The recursive call advances `i`, reduces `l` by one, and leaves the kept counts and `t` unchanged.

When `s[i]` is `)` and `r > 0`, it may similarly be deleted by reducing `r`. The code uses `elif` because one character cannot be both kinds of parenthesis.

There is no deletion branch for a letter: the task permits removing invalid parentheses, not arbitrary letters. There is also no deletion branch once the relevant budget reaches zero. Any extra deletion would exceed the proven minimum, so it cannot belong to an answer.

**The keep branch**

After considering a permitted deletion, the source also explores keeping the current character. It advances the index, leaves both deletion budgets unchanged, appends the character to `t`, and updates the kept count through Boolean arithmetic:

- `(s[i] == '(')` contributes 1 only for an opening parenthesis;
- `(s[i] == ')')` contributes 1 only for a closing parenthesis;
- for a letter, both expressions are `False`, numerically zero.

Thus, letters follow exactly one branch and remain in the output, while a parenthesis may have both a deletion branch and a keep branch when its budget is positive.

**Pruning a prefix with too many closes**

At the start of a recursive call, `lcnt < rcnt` means the kept prefix already contains a closing parenthesis with no earlier kept opening parenthesis available to match it. Future characters are appended after that invalid close. Even if a future opening parenthesis appears, it cannot repair the earlier prefix order.

The branch is therefore permanently invalid and returns immediately.

The source does not test this condition immediately before making the keep call. It allows the call to be formed, then rejects it at the top of that next call. The effect is the same: no descendants of an invalid prefix are explored. At the terminal index, the base case appears before this prune, but a branch with zero deletion budgets has equal total kept opening and closing counts, as shown below, so an invalid final excess of closes cannot be accepted.

**Pruning an impossible deletion budget**

The condition `n - i < l + r` compares the number of unprocessed characters with the number of deletions still required. If fewer total characters remain than required parenthesis deletions, completing both budgets is impossible, even under the optimistic assumption that every remaining character were the needed kind of parenthesis.

This is a safe, though not maximally strong, prune. It counts letters as potentially deletable for the numerical comparison, so it may fail to reject some impossible states early, but it never rejects a possible completion.

**Why the terminal condition is enough**

At `i == n`, the source adds `t` only if `l == 0 and r == 0`. Let the original string contain $O$ opening parentheses and $C$ closing parentheses. The preliminary scan matched some number $P$ of pairs, leaving

$$
O=P+l_0
$$

and

$$
C=P+r_0,
$$

where $l_0$ and $r_0$ are the initial deletion budgets. A terminal branch that exhausts both budgets keeps $O-l_0=P$ openings and $C-r_0=P$ closings. Its final kept counts are therefore automatically equal.

The prefix prune ensures no earlier prefix contains too many closes. Equal final counts plus valid prefixes are exactly the validity conditions, so no additional full-string validation is needed.

**Why every result uses the minimum number of removals**

The recursion can add an answer only after reducing the opening budget from $l_0$ to zero and the closing budget from $r_0$ to zero. Every accepted branch has deleted exactly $l_0+r_0$ parentheses. The preliminary scan proved that fewer deletions cannot suffice, so every returned string is minimum-removal.

Conversely, any minimum-removal valid result must delete exactly $l_0$ openings and $r_0$ closings. As the recursion reaches each parenthesis, it explores the keep choice and, while the appropriate budget remains, the delete choice. Therefore, it follows the exact decisions that produce any particular minimum solution. Its valid prefixes survive pruning, and its budgets reach zero at the end, so that solution is added.

**Why the answer is a set**

Deleting different occurrences can produce the same text when equal parentheses are adjacent or structurally interchangeable. For example, removing the first or second of two identical consecutive closing parentheses may leave the same characters. `ans` is a set, so repeated construction paths collapse into one returned string. Converting it to a list satisfies the required output type, and the arbitrary set iteration order is permitted by the contract.

## Complexity detail

Let $n$ be the full string length and $p$ the number of parentheses. Letters do not branch, while each parenthesis has at most a keep and a delete choice. Before pruning, there are at most $2^p$ decision patterns. Building prefixes through `t + s[i]` and hashing a completed string can each involve up to $O(n)$ character work. A conservative worst-case time bound is therefore $O(2^p\cdot n)$, matching the manifest.

The recursion depth is exactly $O(n)$ because every call advances `i` by one. In an abstract backtracking implementation with one mutable path buffer, non-output auxiliary space would be $O(n)$.

The exact Python source uses immutable prefix strings. Along a keep-heavy active branch, ancestor frames retain prefixes of lengths 0, 1, 2, and so on while the deepest call holds the longest prefix. Their simultaneous character storage can sum to $O(n^2)$ in the worst case. The result set additionally stores $A$ unique answers of length at most $n$, requiring $O(An)$ output space. Thus, $O(n)$ describes the recursion-state model excluding immutable-prefix copies and output; the concrete source can have $O(n^2+An)$ peak storage.

## Alternatives and edge cases

- **Mutable character buffer:** Append a kept character, recurse, and pop it afterward. This avoids retaining a separate copied string at each stack level and realizes $O(n)$ non-output backtracking space.
- **Breadth-first deletion search:** Generate all strings after one deletion, then two deletions, stopping at the first level containing valid strings. The first valid level guarantees minimum removals, but deduplicating many intermediate strings can consume substantial memory.
- **Unrestricted keep/delete backtracking:** Try deleting every parenthesis and track the smallest removal count discovered at leaves. It is correct with careful result replacement, but the precomputed budgets prune all branches that delete too few or too many of either type.
- **Validity check only at the end:** It permits large subtrees beneath prefixes that already have more closing than opening parentheses. Prefix pruning rejects those branches immediately.
- **Greedily delete a particular unmatched occurrence:** A scan can determine the number and type of required removals, but choosing only one occurrence may miss other distinct valid strings. Backtracking is still needed to enumerate all answers.
- **Memoizing only `(i, l, r)`:** Two calls with the same index and budgets can have different kept balances and different output prefixes, so that state is insufficient for enumerating exact strings.
- **Adjacent identical parentheses:** Multiple deletion choices may create the same result. The set removes duplicates even though the DFS does not skip equivalent sibling choices explicitly.
- **Already valid input:** Initial budgets are zero. No deletion branch is allowed, every character is kept, and the set contains only the original string.
- **Only letters:** Parenthesis budgets are zero and letters have only keep branches, so the original string is returned unchanged.
- **Only unmatched closing parentheses:** Each one contributes to `r`; exhausting the budget removes them all, leaving any letters and no invalid prefix.
- **Only unmatched opening parentheses:** The final `l` equals their count; minimum validity requires removing all of them.
- **Empty valid result:** Although the input length is at least one, deleting all parentheses may produce `""`, as in `")("`. The empty parenthesis string is valid.
- **Letters between parentheses:** Letters never affect `lcnt` or `rcnt` and are always copied, but their positions relative to kept parentheses remain unchanged.
- **Minimum-removal guarantee:** A valid string formed by deleting additional matched pairs is deliberately excluded because the DFS has no deletion budget beyond `l_0+r_0`.
- **Output order:** The returned list comes from a set and is not sorted. Any order is explicitly accepted.
- **At most 20 parentheses:** The exponential factor depends on $p$, not on all letters in $n$. This constraint keeps the decision space bounded even though the full string may contain 25 characters.
