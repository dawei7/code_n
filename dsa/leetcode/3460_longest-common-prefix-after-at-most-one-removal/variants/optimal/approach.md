## General

Maintain one index in `s`, one index in `t`, and whether the single permitted deletion has already been used. Equal characters extend the common prefix, so advance both indices.

At the first mismatch, any result longer than the prefix already matched must remove the current character of `s`. Keeping it would leave the mismatch at the same prefix position, while removing a later character cannot change that position. Therefore advance only the `s` index and mark the deletion as used. If another mismatch occurs, no remaining legal operation can repair it, so the scan ends. The `t` index is exactly the number of characters successfully matched and is the required answer.

This rule also covers the option of making no deletion. If the strings match until either one ends, the loop stops without spending the operation. Deleting a character after the matched prefix cannot increase its length, so the current count is already optimal.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert t\rvert$. Each iteration advances the `s` index, and all but at most one iteration also advance the `t` index. The scan therefore performs $O(\min(n,m))$ work under the nonempty-string contract and uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try every deletion:** Constructing all $n$ possible strings and recomputing their common prefixes is correct but takes $O(n\min(n,m))$ time and may allocate $O(n)$ temporary space per candidate.
- **Delete from either string:** The operation applies only to `s`; skipping a character of `t` changes the problem and can overstate the answer.
- **Delay the deletion:** Once the first mismatch is reached, deleting any later character cannot repair the current prefix position.
- **Already equal strings:** Using no removal preserves the full common prefix; deleting a character is optional.
- **Mismatch at index zero:** Removing `s[0]` may expose a long match beginning at `s[1]`.
- **Second mismatch:** The deletion has already been spent, so comparison must stop immediately.
- **One string ends:** The common prefix cannot exceed the shorter resulting string, even if the deletion remains unused.
- **Deletion at the end:** Removing a final mismatching character does not add a character to the common prefix.
