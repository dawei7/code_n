## General

If $n>m$, no version of `s` can be a subsequence of `t`, because replacing a character cannot shorten the string. Otherwise, scan `t` from left to right while retaining two prefix lengths. `exact` is the greatest number of leading characters of `s` that can be matched in the scanned prefix of `t` without a replacement. `changed` is the greatest prefix length that can be matched after using one replacement; `-1` denotes that no such state exists yet.

For each current character of `t`, save both old lengths before making transitions so that this one text position cannot be consumed twice. An existing `changed` state advances only when the next required character of `s` equals the current text character. Independently, any valid `exact` state can consume the current text character by replacing its next character of `s`, so it can create a `changed` prefix of length `previous_exact + 1`. If the exact next character already matches, `exact` advances normally as well. Keep the larger attainable `changed` length.

After scanning any prefix of `t`, these two values equal the longest achievable prefixes of `s` under their respective replacement counts. The transitions cover every possibility for the new text character: skip it, use it for an ordinary match, or use it for the sole replacement. Conversely, each transition preserves order and consumes the text position at most once. A greater matched prefix dominates a smaller one in the same state because its remaining requirement is a suffix of what the smaller state still needs. Therefore reaching length $n$ in either state is necessary and sufficient, and the scan may return `true` immediately.

## Complexity detail

The algorithm visits each of the $m$ characters of `t` once and performs constant work per character, so its time complexity is $O(m)$. It stores only four prefix counters and the target length, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Prefix and suffix match arrays:** Earliest prefix positions and latest suffix positions can test every replacement index in $O(n+m)$ time, but the arrays require $O(n)$ extra space.
- **Try every replacement:** Replacing each position with every letter and rerunning a subsequence scan is correct but costs $O(26nm)$ time.
- **Spend the replacement on the first mismatch in `t`:** This greedy choice is unsafe because skipping that text character may preserve the replacement for a later required character.
- **Already a subsequence:** The operation is allowed at most once, not exactly once, so the `exact` state may finish without any replacement.
- **`s` longer than `t`:** The answer is immediately `false`; no character change can create enough ordered positions.
- **One-character `s`:** When `t` is nonempty, its first available position can always be used by replacing the sole character if necessary.
- **Equal lengths:** A subsequence must then use every position of `t`, so at most one differing aligned character is permitted.
- **Repeated letters:** Prefix lengths, rather than character counts, preserve the required order even when many positions contain the same letter.
