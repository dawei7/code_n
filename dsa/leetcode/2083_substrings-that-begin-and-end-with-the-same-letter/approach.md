## General

**A substring is determined by its two endpoint positions**

For a substring to be valid, its first and last characters must match. The characters between them can be anything. Therefore, when the scan reaches a position that will serve as the substring's right endpoint, the only useful historical information is how many times the same character has appeared up to that point.

The solution processes `s` from left to right. `cnt` maps each character to the number of occurrences seen in the current prefix, and `ans` stores the total number of valid substrings counted so far.

For each current character `c`, it performs:

`cnt[c] += 1`

followed by

`ans += cnt[c]`.

The order is important. Incrementing first includes the current occurrence itself, which represents the one-character substring beginning and ending at the current position.

**Why the current frequency equals the number of new substrings**

Suppose the current character `c` is its $t$th occurrence in the string. After incrementing, `cnt[c] = t`.

There are exactly $t$ valid choices for the starting position of a substring that ends here:

- each of the previous $t-1$ occurrences of `c` can be the left endpoint;
- the current occurrence itself can be the left endpoint, producing a substring of length one.

Each starting occurrence determines one unique contiguous substring from that position through the current position. All those substrings begin and end with `c`, so they are valid. No other starting position works with this right endpoint because its character would differ from `c`.

Therefore, adding `cnt[c]` counts exactly all new valid substrings whose right endpoint is the current character.

For `s = "abcba"`, the running additions are:

- first `a`: its frequency becomes 1, adding the substring `"a"`;
- first `b`: its frequency becomes 1, adding `"b"`;
- `c`: its frequency becomes 1, adding `"c"`;
- second `b`: its frequency becomes 2, adding the one-character `"b"` and `"bcb"`;
- second `a`: its frequency becomes 2, adding the one-character `"a"` and `"abcba"`.

The total is $1+1+1+2+2=7$.

**Count occurrences by position, not distinct substring text**

The problem asks for substrings, which are defined by their positions in the original string. Two substrings with the same textual content but different positions are separate occurrences and must both be counted.

For example, in `"aaa"` there are three length-one substrings `"a"` at different positions, two length-two substrings `"aa"`, and one length-three substring `"aaa"`. The running frequencies are 1, 2, and 3, whose sum is 6. Using a set of substring strings would incorrectly collapse duplicates and return only three distinct texts.

The counter approach naturally respects positions because every right endpoint is processed separately and every earlier matching occurrence supplies a separate left endpoint.

**Connection to the closed-form frequency formula**

If a character occurs $m$ times in the entire string, its successive occurrences add

$$
1+2+\cdots+m=\frac{m(m+1)}{2}
$$

valid substrings.

This is also the number of ways to choose two different occurrences as endpoints, $\binom{m}{2}$, plus $m$ one-character substrings:

$$
\binom{m}{2}+m
=\frac{m(m-1)}{2}+m
=\frac{m(m+1)}{2}.
$$

The exact source computes the same total online rather than making a second pass over final frequencies. Each `ans += cnt[c]` contributes the next term in that character's triangular sum.

**Why every valid substring is counted exactly once**

Take any valid substring `s[left:right + 1]`. Its endpoints contain the same character, say `c`. When the scan reaches `right`, the occurrence at `left` is among the `cnt[c]` occurrences seen up to that point. It supplies one of the starting choices counted in the addition for `right`.

The substring was not counted earlier because its right endpoint had not yet been processed. It will not be counted later because additions in later iterations count only substrings ending at those later positions.

Conversely, every choice represented by `cnt[c]` starts at an occurrence of `c` and ends at the current occurrence of `c`, so every counted substring is valid. Thus the method has neither omissions nor duplicates.

**Why a `Counter` is sufficient**

`Counter()` returns zero for a character not yet present, so the first increment changes its count from zero to one without a membership check. The string contains only lowercase English letters, limiting the number of possible keys to 26.

An explicit 26-element array indexed by `ord(c) - ord('a')` would also work. The counter makes the connection between characters and frequencies direct while still using constant space under the fixed alphabet.

Python integers can grow beyond 32-bit bounds. This matters because a length-$10^5$ string of one repeated letter has

$$
\frac{100000\cdot100001}{2}=5{,}000{,}050{,}000
$$

valid substrings, which exceeds a signed 32-bit integer.

## Complexity detail

Let $n$ be the length of `s`.

The loop visits each character exactly once. A counter lookup, increment, and addition take expected constant time, so total time complexity is $O(n)$.

The counter has at most 26 entries because the input contains only lowercase English letters. Its size is therefore $O(26)=O(1)$ with respect to $n$. The remaining variables also use constant storage, giving $O(1)$ auxiliary space.

If the alphabet were not fixed, the same implementation would use $O(A)$ space for $A$ distinct characters. Under this problem's contract, $A\le26$.

The algorithm never constructs substring contents, so its work does not depend on the sum of substring lengths.

## Alternatives and edge cases

- **Enumerating all substrings:** There are $O(n^2)$ endpoint pairs, and materializing their text can cost even more. The prefix count groups all matching starts for one right endpoint into one addition.
- **Final frequency formula:** Count every character first, then sum $m(m+1)/2$ over frequencies. This is also $O(n)$ and correct; the exact source accumulates the same triangular numbers during the first pass.
- **Set of substring strings:** This answers how many distinct textual values exist, not how many positional substrings satisfy the endpoint rule. Duplicate occurrences must remain separate.
- **Checking only adjacent equal characters:** Valid endpoints can be arbitrarily far apart, and the middle characters are unrestricted.
- **Incrementing after adding:** If `ans += cnt[c]` occurred before `cnt[c] += 1`, every one-character substring would be omitted. Incrementing first includes the current position as both endpoints.
- **Single-character string:** The first frequency becomes one, so the method returns one.
- **All characters different:** Every frequency is one when encountered, and only the $n$ one-character substrings are counted.
- **All characters equal:** The additions are $1,2,\ldots,n$, producing $n(n+1)/2$, which counts every possible substring.
- **Repeated textual substrings:** Different start or end positions remain separate choices and are counted independently.
- **Large answer:** The maximum can exceed 32-bit range. Python handles it directly; fixed-width implementations should use a 64-bit integer.
- **Fixed lowercase alphabet:** This guarantee makes the counter's storage constant. A more general character domain would change only the space analysis, not the counting logic.
- **No input mutation:** The string is read once from left to right, and all state resides in `cnt` and `ans`.
