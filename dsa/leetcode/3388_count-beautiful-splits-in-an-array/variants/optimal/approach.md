## General

Let the first cut be $i$ and the second cut be $j$. The three subarrays are `nums[0:i]`, `nums[i:j]`, and `nums[j:n]`. Their prefix conditions depend only on two longest-common-prefix (LCP) values:

- The first subarray prefixes the second when $i \le j-i$ and the suffixes starting at 0 and $i$ agree for at least $i$ positions.
- The second subarray prefixes the third when $j-i \le n-j$ and the suffixes starting at $i$ and $j$ agree for at least $j-i$ positions.

**Match the global prefix.** Compute the Z-array of `nums`. `prefix_matches[i]` is the LCP length of the full array and the suffix starting at $i$, so it answers the first condition for every second cut paired with $i$.

**Match arbitrary suffixes with rolling rows.** Define $L(i,j)$ as the LCP length of the suffixes beginning at $i$ and $j$. Its recurrence is

$$
L(i,j) =
\begin{cases}
1 + L(i+1,j+1), & \text{if } \texttt{nums[i]}=\texttt{nums[j]},\\
0, & \text{otherwise}.
\end{cases}
$$

Process $i$ from right to left. The row for $i+1$ is sufficient to construct the entire row for $i$, so only two length-$n$ arrays are needed. As each $(i,j)$ entry is formed, apply both length guards and both prefix tests, joining them with logical OR so a split satisfying both is counted once.

The Z-value is exact for every first-versus-second comparison. The LCP recurrence is exact because equal leading elements contribute one plus the common continuation, while unequal leaders contribute zero. Therefore each pair of legal cuts is counted precisely when one of the problem's two prefix relations holds.

## Complexity detail

Let $n$ be the length of `nums`. The Z-array takes $O(n)$ time. The rolling LCP computation visits every ordered pair with $1 \le i < j < n$ once, taking $O(n^2)$ time. The Z-array and two LCP rows use $O(n)$ auxiliary space.

The benchmark defines `size` as $n$ and uses 24-, 60-, and 117-element repeated arrays. Repetition forces every explicit comparison to examine its full permitted length. The reference remains quadratic, while a correct direct comparator checks both candidate prefixes element by element for every cut pair and takes $O(n^3)$ time.

## Alternatives and edge cases

- **Store the full LCP table:** It supports the same constant-time queries but uses $O(n^2)$ memory; rolling rows retain exactly the dependencies needed here.
- **Double rolling hash:** Hashes reduce comparison time but introduce collision risk and extra modular arithmetic, whereas the LCP recurrence is deterministic.
- **Compare slices for every split:** This is simple but copies or compares up to $O(n)$ elements for each of $O(n^2)$ cut pairs, producing cubic work.
- **Count both conditions separately:** Adding their counts double-counts splits where both prefix relations hold; evaluate their union per pair instead.
- **Length guards:** Matching initial elements is insufficient when the proposed prefix is longer than the subarray it should prefix.
- **Fewer than three elements:** No two cuts can create three non-empty subarrays, so the answer is zero.
- **All elements equal:** Many splits satisfy one or both conditions, making this a useful check of length guards and union counting.
