## General

**An attainable even number must end in `2`**

The input contains only digits `1` and `2`. A decimal integer is even exactly when its last digit is even, so every nonempty valid subsequence must end at an occurrence of `2`.

If no `2` occurs, no deletion pattern can create an even final digit and the answer is the empty string.

**Use the last `2` as the final digit**

Suppose the final retained digit is the `2` at index `p`. Every retained character must come from positions at most `p` because subsequence order cannot change.

Keeping all characters `s[0:p+1]` produces the longest possible subsequence ending at that occurrence. Deleting any character from this prefix would shorten the result without helping evenness.

Among all possible final `2` occurrences, choosing the last one permits the greatest prefix length. Every character after the last `2` is necessarily `1` and must be deleted because retaining it would make the number odd.

Thus the unique optimal form is the entire prefix ending at the last `2`.

This separates forced deletions from harmful ones. Every character after the last two is forced out by parity. Every character at or before it can remain without changing the final digit, and deleting any of them only reduces magnitude.

**Why maximum length determines maximum numeric value**

All digits are nonzero. Any $L$-digit positive decimal number is at least $10^{L-1}$, while any number with fewer than $L$ digits is smaller than $10^{L-1}$.

Therefore a longer attainable subsequence always represents a larger integer than every shorter one, regardless of its arrangement of ones and twos. The last-`2` prefix has maximum length, so no lexicographic comparison among shorter candidates is needed.

Within that maximum length, there is only one subsequence: retaining every position through the last `2`. It is consequently the largest numeric result.

**Express deletion of trailing ones with `rstrip`**

`s.rstrip("1")` removes the longest suffix consisting only of characters in the argument string—in this case, trailing `1` characters.

If `s` ends in `2`, there is no trailing one and `rstrip` returns the full string. If it ends in several ones, they are removed until the last `2` becomes the final character.

For `"221"`, removing the trailing one gives `"22"`. For `"12111"`, the result is `"12"`. For `"1112"`, the input already ends in two and remains unchanged.

**Handle the no-solution case automatically**

When `s` consists entirely of ones, the entire string is a trailing run of the removable character. `rstrip("1")` returns `""`, exactly the required sentinel.

The source needs no separate search or branch for a missing `2`.

`rstrip` removes a suffix, not every occurrence of its argument. For `"1211"` it returns `"12"` rather than `"2"` or `""`, preserving useful internal ones.

**Why internal ones must remain**

An internal `1` before the final `2` does not affect parity. Removing it shortens the decimal representation and therefore strictly decreases its value.

For example, from `"112"`, candidate `"12"` is even but smaller than `"112"`. The source correctly strips only the suffix after the last two, never internal ones.

**Why later trailing ones cannot be retained**

Keeping even one character after the chosen final `2` makes that later character the result's actual last digit. Since every such character after the last `2` is one, the number becomes odd.

This shows the source deletes every forced position and no optional beneficial position.

There cannot be two different maximum-length candidates ending at the last two: a subsequence of the full prefix has equal length only when it retains every position. No equal-length tie-break is needed.

## Complexity detail

Let $N=len(s)$. In the worst case, `rstrip` scans the entire string from right to left, so time is $O(N)$.

The returned string may contain $O(N)$ characters. Under output-inclusive accounting, space is $O(N)$. Python may return the original object when no trimming is needed as an implementation optimization, but the safe general bound remains linear for the produced result.

## Alternatives and edge cases

- **Search explicitly for the last `2`:** `s.rfind("2")` followed by a prefix slice expresses the same logic, but `rstrip` is shorter.
- **Keep only all twos:** Internal ones can remain without hurting parity and increase digit count, so deleting them is suboptimal.
- **Choose the first `2`:** A later `2` permits a longer and therefore larger result.
- **Delete arbitrary trailing digits:** Only trailing ones are forced; deleting a trailing two would lose the best final digit.
- **All ones:** No even subsequence exists, so return `""`.
- **Single `2`:** It is already the largest even result.
- **Single `1`:** Stripping returns the empty string.
- **String already ends in `2`:** Keep every character.
- **Multiple trailing ones:** All are removed in one operation.
- **Internal ones:** They remain because they increase the number's length.
- **No leading-zero concern:** The input alphabet excludes zero.
- **Input preservation:** Strings are immutable; trimming returns a string result without modifying `s`.
- **`rstrip` semantics:** It removes only the maximal trailing run of ones.
- **Maximum-length uniqueness:** Keeping the whole last-two prefix is the sole candidate of that length.
