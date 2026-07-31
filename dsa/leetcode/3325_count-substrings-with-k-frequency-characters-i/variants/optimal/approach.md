## General

Process each right endpoint from left to right while maintaining frequencies for a window `s[left..right]`. Also maintain `qualifying`, the number of letters whose current frequency is at least $k$. When a newly added character's frequency becomes exactly $k$, that letter has just entered the qualifying set.

While `qualifying` is positive, remove characters from the left. If the character being removed currently has frequency exactly $k$, its decrement makes it stop qualifying, so decrease `qualifying` before updating the count. Stop at the first `left` for which every frequency is below $k`.

At that moment, `s[left..right]` is invalid, but each substring ending at `right` and starting at an index smaller than `left` is valid: those starts were removed only while the window still contained a threshold-reaching character. Extending any start already known to be valid at the previous right endpoint also preserves validity. Thus exactly `left` substrings ending at `right` qualify, and adding `left` to the answer counts all endpoints without enumeration.

Both pointers move only forward. The frequency-threshold counter avoids scanning all 26 letters when deciding whether to shrink, although such a scan would still have constant alphabet cost.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The right pointer processes every character once, and the left pointer removes every character at most once, so total time is $O(n)$. The 26-entry frequency array and scalar window state use $O(1)$ auxiliary space because the lowercase English alphabet is fixed.

## Alternatives and edge cases

- **Enumerate every substring:** Extending a counter from every start is direct but takes $O(n^2)$ time even when no substring can qualify.
- **Binary search each start:** Validity is monotone in the end position, but repeatedly evaluating candidate substrings adds unnecessary logarithmic or counting work.
- **Scan all frequencies after every update:** This remains linear for a fixed alphabet but obscures the exact threshold-crossing events captured by `qualifying`.
- **k equals one:** Every substring qualifies, and the accumulated left values produce $n(n+1)/2$.
- **No qualifying substring:** The left pointer remains zero throughout, so the result is zero.
- **Several qualifying letters:** Shrinking continues until the last threshold-reaching letter drops below $k$; tracking only the most recently added letter would be incorrect.
- **Threshold boundary:** Decrease `qualifying` when removing from frequency exactly $k$, before the frequency becomes $k-1$.
