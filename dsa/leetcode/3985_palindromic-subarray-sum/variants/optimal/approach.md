## General

Every array value is positive. Around any fixed odd or even center, palindromic ranges are nested: a shorter one lies inside every longer one with that center. Extending a palindrome therefore strictly increases its sum. It is enough to find the longest palindrome around each center and compare those $O(n)$ sums; shorter palindromes at the same center can never win.

Build prefix sums so the sum of `nums[l..r]` is `prefix[r + 1] - prefix[l]`. Then run Manacher's algorithm twice. In the odd pass, `odd[c] = d` means the maximum palindrome centered at `c` spans `[c - d + 1, c + d - 1]`. In the even pass, `even[c] = d` means the maximum even palindrome centered between `c - 1` and `c` spans `[c - d, c + d - 1]`. Each completed radius immediately identifies two prefix-sum indices and hence one candidate answer.

For either parity, retain the left and right endpoints of the palindrome reaching farthest to the right. When the next center lies inside this interval, reflect it across the interval's center and copy the mirror radius, capped at the current right boundary. Everything strictly inside the boundary has already been compared successfully by symmetry. Direct comparisons resume only beyond that boundary. If the expanded palindrome extends farther right, it becomes the new retained interval.

The radius assigned to each center is exact: the mirrored portion is known palindromic, and the subsequent loop expands until an array edge or the first unequal pair. Conversely, every successful comparison adds the same value at symmetric positions, so the reported interval is a palindrome. Manacher's two passes enumerate the longest palindrome for every possible odd and even center. Positivity proves that one of those intervals has at least the sum of every shorter palindromic subarray, so the greatest prefix-sum difference returned is the required answer.

## Complexity detail

Although a single center can expand far, every comparison that crosses the current right boundary advances that boundary. Mirror reuse handles the remaining interior work in constant time per center. The odd and even passes therefore take $O(n)$ total time. Building prefix sums also takes $O(n)$ time. The prefix array and two radius arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Expand around every center:** This is straightforward and exact, but an all-equal array causes $O(n^2)$ successful comparisons.
- **Dynamic programming over intervals:** Recording whether every `nums[l..r]` is palindromic also costs $O(n^2)$ time and $O(n^2)$ space.
- **Rolling hash plus binary search:** Forward and reverse hashes can locate each center's maximum radius in $O(n\log n)$ time, but collision handling and extra arithmetic are unnecessary here.
- **Odd and even centers:** Two separate radius conventions are required; considering only element-centered palindromes misses ranges such as `[10,10]`.
- **One element:** Its odd radius is one, so the algorithm naturally returns that value.
- **Strictly changing values:** Only singleton palindromes exist, and comparing all odd centers returns the largest array value.
- **Large sum:** Up to $10^5$ values of $10^9$ may belong to one palindrome, so the result can reach $10^{14}$.
- **Positive values:** The longest-palindrome-per-center reduction depends on every added pair having positive sum; it would not be valid for a contract permitting negative values.
