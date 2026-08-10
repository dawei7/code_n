## General

**Oddness depends only on the last digit.** A decimal integer is odd exactly when its units digit is one of `1, 3, 5, 7, 9`. For any substring of `num`, only that substring's final character determines parity. The algorithm therefore searches for a suitable ending position rather than evaluating large numeric substrings.

**For a fixed ending, start at index zero.** Suppose an odd digit occurs at index `i`. Any substring ending there is odd. Among those substrings, `num[:i + 1]` has the greatest length because it starts at the beginning. The original number has no leading zeros, so this prefix represents an $(i+1)$-digit positive integer. Every later-starting substring has fewer digits and is therefore numerically smaller, regardless of its first digit.

Even if leading zeros were present, adding them would not increase numeric value, but the stated no-leading-zero guarantee makes the length comparison direct and eliminates representational ambiguity for the chosen prefix.

**Choose the rightmost odd ending.** Prefixes beginning at zero grow as their ending index moves right. A prefix ending at a later odd digit has more digits than a prefix ending at an earlier odd digit and therefore has a larger numeric value. Consequently, the optimal substring is the prefix ending at the rightmost odd digit.

**Scan backward to find it immediately.** The loop starts at `len(num) - 1` and moves toward zero. `int(num[i]) & 1` inspects the low binary bit of the one-digit integer; it equals one precisely for an odd digit. The first successful test encountered from the right is the rightmost odd digit, so the method returns `num[: i + 1]` immediately.

The bitwise test and the more familiar `int(num[i]) % 2 == 1` are equivalent for nonnegative digits. Conversion is safe and constant time because each string contains exactly one decimal character at that position.

**Why no other substring can be larger.** Let the returned ending be `i`. A substring ending after `i` has an even final digit because `i` was the rightmost odd position, so it cannot qualify. A qualifying substring ending at or before `i` has length at most `i + 1`, and equality is possible only by starting at zero and ending at `i`—the returned prefix. Because decimal strings without leading zeros compare by length before digit values, every shorter candidate is smaller.

**Trace `"52"`.** The scan first sees `2`, whose low bit is zero. It then sees `5`, whose low bit is one, and returns prefix `"5"`. Substring `"52"` is even and substring `"2"` is even, so five is the only possible answer.

For `"35427"`, the final digit is already odd, so the first test succeeds and the entire input is returned. Keeping all digits maximizes value.

**Return empty when no odd digit exists.** If every digit is even, every nonempty substring ends in an even digit and thus represents an even number. The loop exhausts all positions and returns `''`. There is no need to enumerate substrings or parse the potentially $10^5$-digit number.

**Input remains textual.** The method never converts the full number into an integer, so it is unaffected by machine integer limits. It only converts individual digits and returns a string slice.

## Complexity detail

Let $n$ be the number of digits. In the worst case, the backward loop examines all $n$ positions, so search time is $O(n)$. Constructing the returned prefix copies up to $n$ characters in Python, also $O(n)$ time. Total time remains $O(n)$.

The scan itself uses $O(1)$ auxiliary space. Python string slicing creates the returned string, which can occupy $O(n)$ output storage. The manifest's $O(n)$ space is therefore accurate when output allocation is counted; excluding the required result, auxiliary space is constant.

The source stops at the first odd digit found from the right, so favorable inputs ending in an odd digit require constant search work, although returning the full slice still copies linear output in Python.

## Alternatives and edge cases

- **Forward scan remembering the last odd index:** This also takes $O(n)$ time and returns the same prefix, but the reverse scan can return immediately.
- **Enumerate all substrings:** There are $O(n^2)$ candidates and parsing them is unnecessary because parity and length determine the answer structure.
- **Convert the full string to an integer:** The input may have $10^5$ digits and exceed practical numeric limits. Full conversion provides no useful information beyond the final digit.
- **Entire number odd:** The last digit succeeds and the whole string is returned.
- **All digits even:** No odd substring exists because every possible ending is even, so the empty string is correct.
- **Odd digit only at index zero:** The result is the first character, as in `"52"`.
- **Several odd digits:** Only the rightmost matters; its prefix strictly contains more digits than every earlier odd prefix.
- **No leading zeros:** This guarantees a longer chosen prefix is numerically larger in the usual decimal representation.
- **Output allocation:** The algorithmic working state is constant, but Python materializes `num[:i + 1]` as a new string.
