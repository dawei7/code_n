## General

Deleting only rightmost characters means every reachable nonempty result from a string is one of its nonempty prefixes. Therefore all three strings can become equal exactly when they share a nonempty prefix.

Among shared prefixes, the longest one minimizes deletions. If its length is $L$, the operation count is

$$
(|s_1|-L)+(|s_2|-L)+(|s_3|-L)
=
|s_1|+|s_2|+|s_3|-3L.
$$

The source scans the three strings together to find that maximum $L$.

**Total original length**

Variable `s` stores `len(s1) + len(s2) + len(s3)`. Once the common-prefix length is known, `s - 3 * L` computes the exact number of removed suffix characters.

Each deletion removes one character from exactly one string, so this arithmetic is both a lower bound and an achievable operation count.

**Scan only while all three have characters**

`n = min(len(s1), len(s2), len(s3))` is the greatest possible common-prefix length. The loop checks positions `0..n-1`.

At index $i$, condition

`s1[i] == s2[i] == s3[i]`

tests whether all three prefixes can extend through this character.

**First mismatch determines the answer**

Suppose the first mismatch occurs at index $i$.

- Characters at positions $0$ through $i-1$ match in all strings, so a common prefix of length $i$ exists.
- Any prefix of length $i+1$ includes the mismatching characters, so no longer equal result is possible.

Thus $L=i$. If $i>0$, the source returns `s - 3 * i`.

If $i=0$, the strings share no first character. Their only common prefix is empty, but completely emptying a string is forbidden. The source returns `-1`.

**No mismatch before the shortest string ends**

If the loop completes, all characters of the shortest string match the corresponding characters of the other two. That entire shortest string is the longest possible common result: it cannot be extended because one input has no next character.

The method returns `s - 3 * n`, deleting only the suffixes beyond that shared shortest length.

For `"abc"`, `"abb"`, and `"ab"`, the scan completes through the shortest length $2$. Total length is $8$, so the answer is $8-6=2$: delete one character from each length-three string.

**Why a shorter common prefix cannot help**

Every reduction of $L$ by one adds one deletion in each of the three strings, increasing cost by three. Since right deletions cannot change an earlier mismatching character, there is no tradeoff where extra deletion enables a different same-length result. The longest common nonempty prefix is unconditionally optimal.

## Complexity detail

Let $L=\min(|s_1|,|s_2|,|s_3|)$. At most $L$ positions are compared, with constant work per position. Time complexity is $O(L)$.

Only total length, shortest length, and loop index are stored. Python strings are read without copying or slicing, so auxiliary space is $O(1)$.

Early return at a mismatch may use less time, but $O(L)$ is the worst case.

## Alternatives and edge cases

- **Repeatedly delete from the longest string:** Simulation can eventually work but obscures the fact that the target must be a common prefix and may perform unnecessary string construction.
- **Generate all prefixes:** Comparing prefix sets uses extra time and space; the first mismatch identifies the longest one directly.
- **First characters differ:** Returning the empty string is illegal, so the correct answer is `-1`.
- **All strings already equal:** $L$ equals every length and the formula returns zero.
- **One string is a prefix of both others:** Keep it and delete the two remaining suffixes.
- **Shortest string length one:** If all first characters agree, that single character is a valid target; otherwise equality is impossible.
- **Mismatch after a long prefix:** Only suffix characters at and after the mismatch are deleted. Earlier matching characters remain.
- **No left deletions:** A common substring that is not a prefix is unreachable and must not be considered.
- **Operation count:** Deleting $q$ characters always costs exactly $q$ operations because each operation removes only one rightmost character.
- **Lowercase alphabet:** Character comparisons need no normalization; case or Unicode equivalence is outside the contract.
- **Deleting from only one string may be insufficient:** Equality requires all three final lengths and contents to match. The formula separately accounts for each suffix, even when two strings already have the same length.
- **Why operations commute:** Deleting a suffix character from one string does not affect the available prefixes of the others. Once the target prefix is fixed, deletions may occur in any order and always total the same count.
- **A mismatch cannot be repaired:** Rightmost deletion never changes characters before the new endpoint. If position $i$ differs while retained, deleting later characters cannot alter it; the common result must end before $i$.
- **Different total lengths:** Total `s` may be much larger than $3L$, but every extra character is necessarily outside the shared prefix and must be removed exactly once.
- **Impossible versus costly:** `-1` is used only when the shared prefix length is zero. Any positive common first character gives a valid result, even if nearly every other character must be deleted.
