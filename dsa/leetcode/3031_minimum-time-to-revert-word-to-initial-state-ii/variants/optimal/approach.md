## General

After $t$ seconds, the first $tk$ original characters have disappeared. If $tk < N$, the untouched suffix `word[tk:]` is forced to occupy the beginning of the current word. Appended characters control only the remaining positions. Thus, time $t$ is feasible exactly when that suffix equals `word[:N - tk]`.

Testing those equalities independently can be quadratic. Instead, build the Z-function of `word`, where `z[i]` is the length of the longest prefix of `word` that matches the substring beginning at index $i$. The standard Z-box `[left, right]` reuses matches already known inside the rightmost prefix-matching interval. Each character advances the right boundary only a constant number of times across the complete scan, so all Z-values are computed in linear time.

For every positive removal offset `k, 2 * k, 3 * k, ...` below $N$, the surviving suffix has length `N - removed`. It matches the required prefix precisely when `z[removed] >= N - removed`. Return the first such offset divided by `k`. If none succeeds, $\lceil N/k \rceil$ operations remove all original characters, after which arbitrary appended characters can reconstruct the target.

## Complexity detail

Constructing the Z-function takes $O(N)$ time. Checking all multiples of `k` takes at most $O(N)$ additional time, so the total is $O(N)$. The Z-array contains $N$ integers and uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Prefix function:** KMP preprocessing also lists every prefix that is a suffix in $O(N)$ time; the Z-function maps more directly from each removal offset to the needed match length.
- **Rolling hash:** Prefix hashes can test each candidate in constant expected time after linear preprocessing, but deterministic string matching avoids collision concerns.
- **Repeated slicing:** Directly comparing every reachable suffix and prefix is simple and suitable for the small-input companion problem, but it can require $O(N^2)$ character work here.
- **Full removal:** If no proper suffix works, $\lceil N/k \rceil$ seconds always suffice because no original character remains fixed.
- **Positive time:** Time zero is excluded, even when the first operation can immediately recreate the same word.
- **Arbitrary appended characters:** Only the surviving suffix is constrained; appended characters need not reproduce the removed block.
