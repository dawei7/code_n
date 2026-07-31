## General

**Turn character isolation into occurrence boundaries.** For each lowercase letter, record its first and last positions in `s`. If a self-contained interval starts at position `left`, then the character at `left` cannot occur earlier: otherwise that same character would occur both inside and outside the interval. Consequently, a valid left boundary must be the first occurrence of its character. There are at most $26$ such candidates.

**Grow a candidate until it is closed.** Scan `right` from a candidate `left` toward the end of the string. Whenever a character is encountered, its last occurrence must also belong to any self-contained interval ending at or after `right`. Maintain `required_right` as the maximum last occurrence among all characters seen since `left`.

If a scanned character has its first occurrence before `left`, the candidate can never become valid: that character is already split across the outside prefix and the interval, and extending the right boundary cannot repair this. Stop scanning that start.

Otherwise, every position with `right >= required_right` closes all characters seen so far. The interval `[left, right]` is then self-contained because none of those characters occurs before `left` or after `right`. Record its length when it is a proper substring, meaning either `left > 0` or `right < n - 1`. Continue scanning after a closed boundary because adjoining closed character groups may combine into a longer valid interval.

Every valid substring is considered: its left boundary is one of the recorded first occurrences, the scan cannot stop before reaching its right boundary, and that boundary is recognized once all required last occurrences have been included. Taking the maximum recorded length therefore produces the answer, while the absence of any proper closed interval leaves `-1`.

## Complexity detail

Let $n$ be the length of `s` defined in the function contract. The occurrence arrays are built in $O(n)$ time. At most $26$ candidate left boundaries each scan at most $n$ positions, so the total is $O(26n) = O(n)$ because the lowercase alphabet has fixed size. The two arrays contain $26$ entries each, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Shrink candidate endings:** Prefix counts can test whether a character crosses an interval boundary while recursively reducing an initial ending. This follows the hints and can run in $O(26^2 n)$ time, but the forward closure scan is simpler.
- **Enumerate all substrings:** Maintain inside and outside character counts while extending every left boundary. This can validate each interval in constant time with a shared-character counter, but still requires $O(n^2)$ time.
- **Minimal partition only:** Stopping as soon as `right` reaches `required_right` finds the smallest closed block for a start, but can miss a longer answer formed by joining adjacent closed blocks. The scan must keep evaluating later closed boundaries.
- **The whole string is forbidden:** A closed interval equal to `s` does not qualify. Strings such as `"aa"` therefore return `-1` even though the whole string contains all occurrences of its character.
- **Invalid left boundary:** Any position that is not the first occurrence of its character can be skipped immediately, because that character already occurs outside the proposed interval.
- **Distinct characters:** If every character is unique, any proper substring is self-contained, so the answer is $n-1$.
