## General

We must change exactly one character, make the result non-palindromic, and choose the lexicographically smallest possible result. These goals suggest two greedy priorities:

1. if we can make an early character smaller, do it at the earliest possible position;
2. if no useful decrease is possible, make the smallest possible increase as far right as possible.

The exact Optimal solution examines only the first half of the palindrome because every first-half character has a matching second-half partner.

**Why length one is impossible**

Every one-character string is a palindrome, regardless of which lowercase letter it contains. Changing its only character still leaves a one-character string.

Therefore, `n == 1` returns the empty string, as the contract requires when no valid replacement exists.

**Why changing a non-`a` character to `a` is best**

`a` is the smallest lowercase letter. At a position containing any other character, replacing it with `a` creates the smallest possible character at that position.

Lexicographic comparison is decided by the first differing position. Consequently, changing an earlier non-`a` character to `a` always beats changing a later position, even if the later replacement is also a decrease.

The loop begins at zero and advances while:

`i < n // 2 and s[i] == "a"`.

It stops at the first non-`a` character in the left half. If it finds one, `s[i] = "a"` performs the greatest lexicographic improvement at the earliest possible location.

**Why that change breaks the palindrome**

The input is a palindrome, so `s[i]` originally equals its mirror `s[n - 1 - i]`. The loop restricts `i` to the first half, so the mirror is a different position.

Changing only `s[i]` to `a` while its original non-`a` mirror remains unchanged makes that pair unequal. The result is therefore not a palindrome.

The middle character of an odd-length palindrome is deliberately excluded by `i < n // 2`. Changing only the middle character would preserve symmetry and fail to break the palindrome.

**Why only the left half needs examination**

For every non-middle position in the right half, there is an equal mirror in the left half. Changing the left occurrence affects an earlier lexicographic position and is therefore better than changing the matching right occurrence to the same new character.

Once the first half contains no non-`a` character, the right half contains no such character either because the string is palindromic. The only possible non-`a` character could be the unpaired middle character, but changing it cannot break symmetry.

**Fallback when the first half is all `a`**

If `i == n // 2`, no first-half character can be decreased to `a`. To make the palindrome unequal, some `a` must instead be increased.

The smallest possible greater letter is `b`. Because an increase makes the string lexicographically larger, it should occur at the latest possible position. The source sets:

`s[-1] = "b"`.

The last position is mirrored by the first. The first character is `a` in this fallback case, so changing only the last to `b` breaks the palindrome.

This also handles strings such as `"aaa"` and `"aba"`. In `"aba"`, the only non-`a` character is the middle `b`, which cannot be usefully changed; changing the final `a` to `b` gives `"abb"`.

**Following the main example**

For `"abccba"`, index zero contains `a`, so the loop advances. Index one contains `b`, the first non-`a` in the left half. Replacing it produces `"aaccba"`.

The mirrored second-last character remains `b`, so the result is not palindromic. Any valid change after index one would leave the prefix `"ab"`, which is lexicographically larger than the new prefix `"aa"`.

**Why the result is globally smallest**

If a first-half non-`a` exists, the algorithm changes the earliest one to the smallest possible letter. No other valid result can differ earlier with a smaller character, and any result differing later keeps a larger character at this position.

If none exists, no lexicographic decrease can break the palindrome. Any valid answer must increase some non-middle `a`. Changing the rightmost position causes the latest possible first difference, and changing it to `b` uses the smallest increase.

These cases exhaust all palindromes longer than one, proving optimality.

## Complexity detail

Let $n$ be the string length. Converting the immutable string to a list takes $O(n)$ time and space.

The loop examines at most $\lfloor n/2\rfloor$ positions. One assignment is constant-time, and `"".join(s)` processes all $n$ characters. Total time is $O(n)$.

The character list and returned string use $O(n)$ representation space, matching the manifest. Apart from them, only scalar variables are used.

Even if the loop stops immediately, conversion and joining still make worst-case time linear.

## Alternatives and edge cases

- **Try every replacement:** Generating all alternatives and comparing strings is correct but can take quadratic time.
- **Change a right-half non-`a` to `a`:** It breaks the palindrome but is lexicographically worse than changing its earlier left mirror.
- **Change the middle character:** In an odd-length palindrome, this preserves the palindrome and is invalid.
- **Length one:** No replacement can make it non-palindromic, so the answer is empty.
- **All `a` characters:** Change the final one to `b`.
- **Only the middle is non-`a`:** Ignore it and use the final-position fallback.
- **First character is non-`a`:** Changing it to `a` is immediately optimal.
- **Even length:** Every position has a distinct mirror, and the same first-half rule applies.
- **Exactly one replacement:** The fallback changes `a` to `b` rather than leaving the input unchanged.
- **Immutable input:** The list conversion enables one character assignment and explains the linear space bound.
