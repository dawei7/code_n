## General

**Rewrite the interior-sum condition**

Let $P[i]$ be the sum of `capacity[0..i-1]`, so the sum strictly between endpoints `left` and `right` is $P[\texttt{right}] - P[\texttt{left}+1]$. Because $P[\texttt{left}+1] = P[\texttt{left}] + \texttt{capacity[left]}$, requiring that interior sum to equal the left boundary is equivalent to

$$
P[\texttt{right}]
= P[\texttt{left}] + 2\,\texttt{capacity[left]}.
$$

The other stability condition requires `capacity[left] = capacity[right]`. Thus a left endpoint can be represented by the pair

$$
\bigl(\texttt{capacity[left]},\ P[\texttt{left}] + 2\,\texttt{capacity[left]}\bigr),
$$

and a right endpoint asks how many earlier pairs equal

$$
\bigl(\texttt{capacity[right]},\ P[\texttt{right}]\bigr).
$$

**Enforce the minimum length while scanning**

When processing a right endpoint, add `left = right - 2` to a frequency map before querying it. The map then contains exactly the possible left endpoints satisfying `left <= right - 2`, which is the length-at-least-three rule. Every matching key represents one stable subarray ending at `right`; adding its frequency counts duplicates, overlaps, and nested ranges individually.

## Complexity detail

Let $n$ be the length of `capacity`. Building prefix sums and scanning the endpoints each take $O(n)$ time. Hash-map operations take expected $O(1)$ time, so the total expected time is $O(n)$. The prefix array and frequency map use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate endpoint pairs:** Prefix sums can test each subarray in $O(1)$ time, but examining all valid pairs still takes $O(n^2)$ time.
- **Store indices by boundary value only:** Equal endpoints are necessary but insufficient; the transformed prefix-sum component of the key is also required.
- **Length two:** Equal adjacent values do not count because a stable subarray must contain at least one interior element.
- **Negative values:** The algebra and hash keys remain valid when boundaries or interior sums are negative.
- **Zero values:** An all-zero subarray of any length at least three is stable, so repeated identical keys must retain their full frequency.
- **Overlapping ranges:** Each matching endpoint pair is a distinct subarray and must be counted even if its elements overlap another match.
- **Large totals:** Prefix sums and the answer can exceed 32-bit signed range, so fixed-width implementations need 64-bit integers.
