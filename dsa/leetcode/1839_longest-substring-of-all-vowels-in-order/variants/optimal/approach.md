## General
**Treat each non-decreasing run as one candidate region**

Scan adjacent characters. A strict decrease such as `u` followed by `a` makes every substring crossing that boundary invalid, so reset the current run length to 1 and its distinct-group count to 1. Equal adjacent vowels extend the current group, while a strict increase extends the run and begins one new vowel group.

Because `word` contains only the five ordered vowels, a non-decreasing run can change character at most four times. Reaching five distinct groups means it started with `a` and encountered `e`, `i`, `o`, and `u` in order without skipping one.

**Measure a run only after all groups appear**

Track the current run length from its most recent decrease. Whenever its group count is five, the full current run is beautiful. Update the maximum on every later character as well, because additional `u` characters continue extending the same valid substring.

If a run skips a vowel, it cannot reach five groups: there are only five possible vowel values. If it decreases, resetting discards exactly the prefixes that no longer can participate in an ordered substring.

**Why the scan finds the longest substring**

Every beautiful substring lies entirely inside one maximal non-decreasing run. Within such a run, once all five groups have appeared, taking the substring from the run's beginning through the current position is at least as long as any beautiful suffix ending there and remains valid. The algorithm evaluates that maximal candidate at every endpoint, so the largest recorded length equals the longest beautiful substring.

## Complexity detail
The scan examines each of the $n$ characters once and performs constant work, giving $O(n)$ time. The run length, group count, and best length use $O(1)$ space.

## Alternatives and edge cases
- **Start a scan at every position:** Incrementally checking ordered vowel groups is correct but takes $O(n^2)$ time on a fully ordered word.
- **Split on every descending pair:** Processing the resulting non-decreasing runs separately is also linear, but the direct scan avoids constructing substrings.
- **Count vowels globally:** Global counts ignore contiguity and order, so they cannot identify a beautiful substring.
- **Exactly `"aeiou"`:** This is the shortest possible beautiful substring, of length 5.
- **Missing vowel:** A run with fewer than five distinct groups is not beautiful regardless of length.
- **Skipped vowel:** A transition such as `a` to `i` prevents that run from accumulating all five groups.
- **Repeated vowels:** Equal adjacent characters extend the run without increasing the group count.
- **Descending transition:** Reset at the later character; no valid ordered substring can cross the decrease.
- **Multiple valid runs:** Keep the maximum rather than returning the first.
- **Only one vowel value:** Return zero even for a very long word.
