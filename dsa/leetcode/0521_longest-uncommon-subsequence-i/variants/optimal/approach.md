## General

The word “subsequence” can make this problem look as though it requires generating many strings, but with exactly two input strings the whole-string candidates settle the answer.

A string is always a subsequence of itself: delete zero characters. Therefore `a` is a subsequence of `a`, and `b` is a subsequence of `b`. The only remaining question is whether one entire input string is also a subsequence of the other.

There are two exhaustive cases.

**Case one: the strings are equal.** If `a == b`, they have exactly the same characters in the same order. Every subsequence obtainable from `a` is also obtainable from `b` by making the same deletions. The reverse is equally true.

An uncommon subsequence must belong to exactly one string, so equality makes every possible candidate common to both. There is no uncommon subsequence of any length, and the required result is `-1`.

This conclusion includes the whole strings themselves. Although `a` is a subsequence of `a`, the equal string `b` also contains it as a subsequence, so it is not uncommon.

**Case two: the strings are different.** The solution returns:

`max(len(a), len(b))`.

To see why this is valid, first suppose the lengths differ. Let the longer string be `longer` and the shorter be `shorter`. The entire `longer` string is a subsequence of itself. It cannot be a subsequence of `shorter` because a subsequence cannot have more characters than its source: deletion can preserve or reduce length, never increase it. Therefore `longer` itself is an uncommon subsequence.

Its length is also the largest answer possible. No subsequence of either input can exceed the length of the input it came from, and `longer` already has the maximum input length. Thus this candidate supplies both a valid lower bound and the universal upper bound.

Now suppose the strings have equal length but different contents. The entire `a` is a subsequence of itself. Could it also be a subsequence of `b`? A subsequence of `b` with the same length as `b` cannot delete any character. It must therefore equal `b` exactly. Since `a != b`, `a` cannot be such a subsequence. So `a` is uncommon; by the same reasoning, `b` is uncommon as well.

Each has the common full length, and no subsequence can be longer than its source. Returning either length is optimal, which is exactly what `max` returns.

**Why character-by-character subsequence testing is unnecessary.** Usually, deciding whether one string is a subsequence of another needs two pointers. Here, only the entire longer-length candidate matters. A longer string fails the shorter target immediately by length. Equal-length strings can be subsequences of one another only when they are identical. The single equality comparison already distinguishes that exceptional situation.

For `a = "aba"` and `b = "cdc"`, the strings have equal length but differ. The full string `"aba"` cannot be obtained from `"cdc"` without changing characters, and it is length three, the maximum possible. The answer is three.

For `a = "xyz"` and `b = "wxyz"`, the second string has length four. It is a subsequence of itself and is too long to be a subsequence of the length-three first string, so four is the answer. It does not matter that `"xyz"` is a subsequence of `"wxyz"`; the longer whole string is already uncommon.

For `a = "aaa"` and `b = "aaa"`, equality means every deletion pattern produces the same subsequence on both sides. Returning `-1` is therefore necessary.

The one-line conditional expression encodes exactly these cases:

`-1 if a == b else max(len(a), len(b))`.

Python evaluates the equality test first. If it succeeds, the no-solution sentinel is returned. Otherwise, the proof above guarantees that the maximum input length is attainable by an uncommon whole-string subsequence.

**Why there is no hidden third case.** Two strings are either equal or unequal. Within the unequal branch, their lengths are either different or equal, and both subcases have been covered. This exhaustive split is what permits such a short implementation without omitting a difficult subsequence configuration.

The result concerns a length only, so the method does not need to return which full string is the witness. When equal-length unequal strings both qualify, either one proves the same numeric answer.

## Complexity detail

Let $A=\lvert a\rvert$ and $B=\lvert b\rvert$. Computing lengths is constant time in Python because strings store their lengths. The equality comparison can inspect characters until it finds a mismatch and takes $O(\min(A,B))$ time in the worst relevant equal-length case; when the strings are identical it takes $O(A)$.

A safe combined bound is $O(A+B)$, matching the manifest. The method creates no subsequences and uses only the comparison result and integer lengths, so auxiliary space is $O(1)$. It returns an integer rather than a copied string.

No algorithm can avoid inspecting potentially all characters when equal-length strings share a long prefix: the final character can decide whether the answer is `-1` or the full length.

## Alternatives and edge cases

- **Generate all subsequences:** Each length-$n$ string has up to $2^n$ deletion choices, which is exponential and unnecessary because a whole input string is always the optimal witness when the inputs differ.
- **Two-pointer subsequence check:** It would correctly test whether one input is a subsequence of the other, but length and equality already imply the needed result for whole-string candidates.
- **Longest common subsequence DP:** Computing an LCS solves a much harder question and costs quadratic time and space without changing this answer.
- **Equal strings:** Every subsequence occurs in both, so the required sentinel is `-1`.
- **Different lengths:** The longer entire string is automatically uncommon because it cannot fit as a subsequence of the shorter one.
- **Equal lengths but different characters:** Neither full string can be a subsequence of the other; a same-length subsequence would have to use every character unchanged.
- **One-character equal strings:** They have no uncommon subsequence and return `-1`.
- **One-character unequal strings:** Either whole character is uncommon, so the answer is one.
- **Repeated characters:** Repetition does not affect the equality-and-length proof.
- **One string is a subsequence of the other:** If lengths differ, the longer whole string still supplies the optimum even when the shorter is common to both.
