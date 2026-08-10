## General

**Turn two range sums into one zero-sum condition**

For each position, define the difference

$$
d_k=\texttt{nums1}[k]-\texttt{nums2}[k].
$$

The two arrays have equal sums on a range $[i,j]$ exactly when

$$
\sum_{k=i}^{j} d_k=0.
$$

This transformation combines the two range calculations into one running difference. Because the arrays are binary, each per-position difference is -1, 0, or 1, but the method works for general integers as well.

**Use equal prefix differences**

Let `s` after index `j` be the sum of differences from index zero through `j`. If the same prefix value previously occurred after index `p`, subtracting the two equal prefixes gives

$$
\sum_{k=p+1}^{j}d_k=0.
$$

Therefore `nums1[p+1:j+1]` and `nums2[p+1:j+1]` have equal sums. Its length is `j - p`.

Every valid equal-sum range can be described this way: the prefix difference immediately before its start equals the prefix difference at its end.

**Represent the prefix before index zero**

The dictionary starts as `{0: -1}`. Index -1 is a conceptual position before the arrays, where both prefix sums are zero and their difference is zero.

This sentinel lets a valid range starting at index zero use the same formula. If the running difference becomes zero at index `i`, the computed length is `i - (-1) = i + 1`, exactly the size of prefix `[0,i]`.

Without the sentinel, ranges beginning at zero would need a separate condition and are easy to miss.

**Keep only the earliest occurrence**

When a running difference `s` is seen for the first time, the source records `d[s] = i`. On later occurrences, it does not overwrite that index. For a fixed right endpoint `i`, pairing with the earliest equal prefix creates the greatest possible length.

Suppose the same prefix difference appeared at positions two and five and appears again at nine. Position two yields length seven, while position five yields length four. The later occurrence can never help form a wider range with this or any future endpoint, so retaining only the earliest is sufficient.

This is why the `else` branch stores a value only when `s` is new.

**Update the best range online**

The loop processes paired elements with `zip(nums1, nums2)` and `enumerate`. It updates

`s += a - b`

to obtain the current prefix difference.

If `s` already exists in the dictionary, `i - d[s]` is the length of an equal-sum range. `ans = max(ans, ...)` preserves the widest length found anywhere so far. If `s` is new, the current index becomes its earliest occurrence.

The arrays have equal guaranteed lengths, so `zip` processes every position rather than silently truncating meaningful input.

**Trace the first example**

For `nums1 = [1,1,0,1]` and `nums2 = [0,1,1,0]`, the element differences are `[1,0,-1,1]`.

The running prefix differences are one at index zero, one at index one, zero at index two, and one at index three.

The first one is stored at index zero. Its repeat at index one produces length one. Prefix zero at index two matches the sentinel -1 and produces length three, covering indices zero through two. At index three, prefix one matches its earliest occurrence zero and produces length three, covering indices one through three. The maximum remains three.

**Why the algorithm is correct**

Whenever the source updates `ans`, the two matching prefix differences subtract to zero, so the corresponding range truly has equal sums.

Conversely, take any valid range $[i,j]$. Its difference sum is zero, so the prefix difference at $j$ equals the prefix difference at $i-1$. When the loop reaches $j$, the dictionary contains an occurrence of that value no later than $i-1$. Pairing with an even earlier occurrence can only create a range at least as wide. Thus the algorithm considers a candidate no shorter than every valid range and cannot miss the optimum.

Since `ans` starts at zero, it correctly remains zero when no repeated prefix difference ever forms a nonempty equal-sum range.

## Complexity detail

Let $N$ be the common array length. The loop processes each aligned pair once. Dictionary lookup and insertion take expected $O(1)$ time, so total expected time is $O(N)$.

At most $N+1$ distinct prefix differences, including the sentinel, are stored. The dictionary therefore uses $O(N)$ space, while scalar variables use $O(1)$.

## Alternatives and edge cases

- **Check every range directly:** $O(N^2)$ ranges, even with prefix sums, are too slow for $N=10^5$.
- **Store all positions for each prefix value:** Correct but unnecessary; only the earliest produces the widest range for future endpoints.
- **Overwrite the earliest index:** This can lose the optimal width and is therefore incorrect.
- **Range starting at zero:** The sentinel `0: -1` handles it automatically.
- **Equal elements at one index:** A zero difference immediately repeats the prior prefix and yields a valid length-one range.
- **Identical arrays:** The running difference is always zero, so the full length $N$ is returned.
- **No valid pair:** `ans` remains zero.
- **Several widest ranges:** Only their common maximum length is requested.
- **Negative running difference:** Dictionary keys may be negative and work normally.
- **Binary constraint:** It bounds each update to -1, 0, or 1 but is not essential to the prefix-equality proof.
- **Equal-length guarantee:** It makes `zip` safe for all positions.
- **Input preservation:** The method reads aligned values and does not modify either array.
