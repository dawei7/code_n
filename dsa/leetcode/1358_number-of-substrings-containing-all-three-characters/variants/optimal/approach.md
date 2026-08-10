## General

Rather than enumerate every substring, count valid substrings by their ending index. For a fixed right endpoint `i`, the only information needed is the most recent position of `a`, `b`, and `c`. The earliest among those three positions determines exactly how far right a substring may start while still containing all three characters.

**Track the latest occurrence of each required character**

The dictionary begins as `{"a": -1, "b": -1, "c": -1}`. A value of negative one means that character has not appeared in the processed prefix.

During `for i, c in enumerate(s)`, `d[c] = i` updates the last-seen position of the current character. The input guarantee that every character is `a`, `b`, or `c` makes every dictionary assignment valid.

After this update, `d["a"]`, `d["b"]`, and `d["c"]` are the greatest indices no larger than `i` at which the corresponding characters occur.

**Find the latest possible valid starting boundary**

Let

$$
p=\min(\texttt{lastA},\texttt{lastB},\texttt{lastC}).
$$

The occurrence at position `p` is the leftmost among the three most recent required occurrences. Any substring ending at `i` and starting at an index from zero through `p` contains all three of those occurrences. There are `p + 1` such starting indices.

Any start greater than `p` excludes the required character whose most recent occurrence is at `p`. Because that occurrence is already the most recent one, no later copy of that character exists before or at `i`. Such a substring cannot contain all three.

Therefore, the number of valid substrings ending exactly at `i` is
`min(d["a"], d["b"], d["c"]) + 1`.

**Why the negative-one initialization removes a branch**

Before all three characters have appeared, at least one last position is negative one. The minimum is then negative one, and adding one contributes zero. The same formula works both before and after the prefix becomes complete, so the code needs no separate “have all characters appeared?” test.

For `s = "abcab"` at final index four, the most recent positions are three for `a`, four for `b`, and two for `c`. Their minimum is two. Starts zero, one, and two give three valid substrings ending at index four; a start of three would exclude `c`.

Tracing `"abcabc"` shows how the total grows. The first two endpoints contribute zero because one required character is missing. Endpoint two has latest positions zero, one, and two, so it contributes one. Endpoint three updates `a` to three; the minimum becomes one, so starts zero and one contribute two more. Endpoint four contributes three, and endpoint five contributes four. The sum of endpoint contributions is ten, matching the example.

Notice that the formula counts substrings ending now, whereas a conventional sliding window often counts all future endings for a chosen start. Both viewpoints partition the same set of valid substrings, but the last-position method needs no moving left pointer or frequency decrements.

**Why summing endpoint counts is exact**

Every substring has one unique ending index. At that endpoint, the formula counts its starting index exactly when the substring contains all three characters. It never counts the same substring under another endpoint and never omits a valid start. Adding the per-endpoint counts into `ans` therefore gives the total number of valid substrings.

Repeated occurrences cause no problem. Only the latest occurrence of each character matters for maximizing the valid starting boundary. Older copies lie farther left and cannot allow a start beyond the most recent copy.

## Complexity detail

Let $n$ be the string length.

The loop processes each character once. Updating one dictionary entry, reading three fixed entries, taking their minimum, and adding to `ans` are constant-time operations. Total time is $O(n)$.

The dictionary always contains exactly three keys and three indices. The answer and loop variables are scalar. Auxiliary space is $O(1)$.

The number of substrings can be quadratic in $n$, but Python integers hold the result without fixed-width overflow. The running time remains linear because the method counts groups of starting positions arithmetically rather than constructing substrings.

## Alternatives and edge cases

- **Sliding window with counts:** Expand a right pointer, then shrink the left pointer while all three characters are present. It also runs in $O(n)$ time and constant space.
- **Brute-force substrings:** Enumerating all start-end pairs and checking content takes at least quadratic time and may become cubic with repeated scans.
- **Prefix frequency tables:** They can test any substring quickly but still leave quadratically many substrings to test.
- **Character not yet seen:** Its last position remains negative one, making the contribution zero automatically.
- **Exactly `"abc"`:** Only the full string contains all three, and the final endpoint contributes one.
- **Long run of one character:** No contribution occurs until both other characters have appeared.
- **Repeated required characters:** Updating to the latest position can only move the minimum boundary right or leave it unchanged, correctly increasing or preserving the number of valid starts.
- **At least one occurrence:** The method does not require exactly one of each; extra copies remain inside valid substrings without changing validity.
- **Alphabet guarantee:** A character outside `a`, `b`, and `c` would create another dictionary key but is outside the contract; the three required entries still drive counting.
- **No substring construction:** Indices alone are enough, avoiding allocation proportional to substring lengths.
- **Quadratic answer with linear work:** One endpoint can contribute many starts at once, which is why the algorithm can count $\Theta(n^2)$ valid substrings without taking quadratic time.
