## General

**There are only ten possible good strings**

A good integer must contain exactly three copies of one decimal digit. Therefore, regardless of how long `num` is, every possible answer belongs to this fixed list:

`"999"`, `"888"`, `"777"`, ..., `"111"`, `"000"`.

The solution exploits that tiny answer space directly. It does not need to parse the entire input as an integer, construct every length-three window, or retain every match. It tests these ten candidates from largest to smallest and returns the first one present as a substring.

**Generate candidates in descending order**

The range `range(9, -1, -1)` begins at nine, stops before minus one, and moves by minus one. Its values are exactly nine through zero in descending order.

For a current digit `i`, `str(i)` converts it to its one-character decimal representation. Multiplying that string by three forms the corresponding good candidate. The assignment expression

`s := str(i) * 3`

both constructs the candidate and stores it in `s` for the immediate return.

The containment test `s in num` asks whether that exact three-character string occurs contiguously anywhere in `num`. Contiguity matters because the definition requires a substring, not merely three appearances at unrelated indices.

**Why the first match is the maximum**

Every candidate contains the same number of characters. Among equal-length decimal strings, the one with the greater repeated digit is the greater integer. For example, every occurrence of `"777"` is greater than `"666"`, and `"000"` is smaller than every other good string.

The loop examines candidates strictly in this numeric order. If it returns `s` at digit `i`, every larger repeated-digit candidate has already been tested and found absent. The returned string is present and hence valid, while no larger valid answer exists. That makes it the maximum good integer.

This descending-search argument means the method may stop immediately. Once `"777"` is found, the presence of `"333"` or any smaller candidate cannot change the answer.

**Why all valid answers are covered**

Take any good length-three substring. It has one unique digit, so its three positions all contain some decimal digit `d`. It must therefore equal `str(d) * 3`. The loop generates that exact candidate when `i = d`.

Thus, the ten tests cover every string satisfying the definition. There is no possible good integer outside the generated set, and containment prevents the method from accepting a generated candidate that is not actually present in `num`.

**Leading zeros remain part of the result**

The result is requested as a string, and the statement explicitly permits leading zeros. The candidate for digit zero is built as `"000"` and tested without converting it back to an integer. If it is the only good substring, it is returned unchanged.

An integer-based approach might turn `"000"` into `0` and then return `"0"`, which would violate the required three-character representation. Keeping all work in strings avoids that loss of formatting.

**A trace with two good values**

For `num = "6777133339"`, the loop first tests `"999"` and `"888"`; neither is contained. It then constructs `"777"`. That substring occurs beginning at index one, so the function returns it immediately.

Although `"333"` also occurs later, the loop never needs to reach digit three. Its candidate is numerically smaller than the match already found.

For `num = "2300019"`, candidates nine through one are absent. The last iteration constructs `"000"`, finds it, and returns the three-character string. For an input with no three equal consecutive digits, every test fails and control reaches the empty-string return.

**What Python's containment test is doing conceptually**

The expression `s in num` searches for a length-three contiguous pattern. Conceptually, it can compare `s` with each length-three window of `num` until one matches or the windows are exhausted. The implementation delegates that search to Python's optimized string machinery rather than spelling out the window loop.

Because the pattern length is always three and the outer loop runs exactly ten times, these repeated searches remain linear in the input length up to a constant factor. This exact source is the editorial's “one search per digit” strategy, even though the branch summary describes retaining a maximum while scanning the windows once. Both have the same asymptotic bounds, but the proof here follows the descending candidate tests that actually execute.

**Why an empty string is the right sentinel**

If all ten candidates are absent, then the coverage argument proves no valid good integer exists. Returning `""` exactly matches the required no-answer representation. It is also unambiguous: every genuine answer has length three, so the empty string cannot be mistaken for a valid candidate.

## Complexity detail

Let `n` be the length of `num`. Each containment operation searches for a pattern of fixed length three and takes `O(n)` time in the worst case. There are exactly ten candidates, so the total is `O(10n) = O(n)`.

The loop stores only the integer digit and one three-character candidate. The pattern length and number of candidates do not grow with `n`, so auxiliary space is `O(1)`. The implementation does not build an array of windows or modify `num`.

It may finish earlier when a large candidate occurs, but worst-case analysis includes testing all ten, such as when no good substring exists or only `"000"` exists.

## Alternatives and edge cases

- **Single pass over length-three windows:** Check `num[i] == num[i + 1] == num[i + 2]` and retain the largest matching character. This also takes `O(n)` time and `O(1)` space, but it is not the exact descending-candidate implementation.
- **Run-length counting:** Track the current digit and consecutive-run length; whenever a run reaches three, update the best digit. This is useful if the required repetition length varies.
- **Convert windows to integers:** Numeric conversion is unnecessary and mishandles the required representation of `"000"` unless special care is added.
- **Sort all matching windows:** Collecting and sorting matches uses extra space and time even though only ten different answers are possible.
- **Exactly three input digits:** The sole length-three window is found if all characters match; otherwise, the result is empty.
- **Run longer than three:** A run such as `"7777"` contains overlapping `"777"` substrings, and the containment test correctly recognizes the candidate once.
- **Several occurrences of one candidate:** Presence is all that matters; repeated matches do not change the maximum.
- **Several different good candidates:** Descending iteration returns the largest digit's candidate regardless of where it occurs.
- **Only zeros form a match:** `"000"` is returned as a three-character string, preserving its leading zeros.
- **No good substring:** All ten containment checks fail and the method returns `""`.
- **Digits are characters:** Character preservation avoids arithmetic overflow even though `num` may represent a large integer.
- **Substring rather than subsequence:** `s in num` requires adjacent characters, so separated copies of a digit are never accepted.
- **Loop bounds:** Stopping before minus one is what includes zero while excluding invalid negative candidates.
- **Early return:** It is valid only because candidates are checked from nine downward; ascending order would return the minimum instead.
- **Input preservation:** String searches are read-only and create only constant-size candidate strings.
