## General

The desired result is exactly the string after removing its maximal suffix consisting of the character `'0'`. Python's `rstrip("0")` performs that operation directly: it scans backward while characters belong to the specified removal set and stops at the first nonzero digit.

Only the suffix is considered, so zeros between nonzero digits remain untouched. The input is a positive integer without leading zeros; consequently, it cannot consist entirely of zeros, and the operation cannot produce an empty result. The returned prefix therefore contains precisely all digits through the original last nonzero digit.

## Complexity detail

Let $n$ be the length of `num`. In the worst case the trailing suffix contains $n-1$ zeros, so locating its boundary takes $O(n)$ time. The returned immutable string may contain $O(n)$ characters, giving $O(n)$ result space and $O(1)$ auxiliary state beyond that result. The benchmark uses `size` as $n$ and compares the single suffix scan with repeated one-character slicing.

## Alternatives and edge cases

- **Repeatedly slice one zero:** A loop using `num = num[:-1]` is correct, but immutable strings copy progressively shorter prefixes and can take $O(n^2)$ time.
- **Convert to an integer:** Numeric conversion removes trailing zeros only after additional arithmetic and may exceed fixed-width integer limits in other languages.
- **Search forward:** Tracking the last nonzero digit during a forward scan is also $O(n)$ and returns the prefix through that position.
- A number with no trailing zero is returned unchanged.
- Interior zeros must remain in the result.
- The string `"1000"` becomes `"1"`, never an empty string.
- Only the character `'0'` is removed; other digits terminate the suffix.
