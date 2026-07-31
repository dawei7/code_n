## General

First determine which half-open intervals can disappear completely. Let `removable[i][j]` mean that `s[i:j]` can be reduced to the empty string. Every empty interval is removable. For a nonempty interval to vanish, its first character `s[i]` must eventually be paired with some `s[k]`. At that moment, the characters strictly between them must already be gone, and everything after `k` inside the interval must also be independently removable. Therefore

$$
\text{removable}[i][j]
=
\bigvee_{i<k<j}
\left(
\operatorname{adjacent}(s_i,s_k)
\land \text{removable}[i+1][k]
\land \text{removable}[k+1][j]
\right).
$$

Only indices $k$ that leave even-length subintervals need consideration. Increasing interval length ensures both smaller states are known. Alphabet adjacency means a code-point difference of $1$, or $25$ for `a` and `z`.

Next let `best[i]` be the lexicographically smallest string reachable from suffix `s[i:]`. If the whole suffix is removable, `best[i]` is empty. Otherwise, suppose position $j$ is the first character that survives. Then `s[i:j]` must be removable, `s[j]` is kept, and the remaining suffix can independently become `best[j + 1]`. Examine every such $j$ and choose the smallest candidate `s[j] + best[j + 1]`.

This construction also includes performing zero operations: choosing $j=i$ is always legal because the empty prefix `s[i:i]` is removable. Conversely, every reachable result has a first surviving position whose preceding prefix vanished, so one of the examined candidates represents it. Induction over suffixes proves `best[0]` is the global lexicographic minimum.

## Complexity detail

Let $n=\lvert s \rvert$. There are $O(n^2)$ intervals, and each interval may try $O(n)$ pairing positions, for $O(n^3)$ time. Constructing and comparing the suffix candidates also costs at most $O(n^3)$ characters in the straightforward string representation. The removability table occupies $O(n^2)$ space; the stored suffix answers contribute at most another $O(n^2)$ characters.

## Alternatives and edge cases

- **Explore every reachable string:** Memoizing strings avoids duplicate states but still permits exponentially many distinct states.
- **Always remove the leftmost pair:** That solves the deterministic variant but is wrong here; `abc` should remove `bc` and retain `a`.
- **Always perform every possible removal:** Stopping is optional, and a longer string can be lexicographically smaller, as `zdce` is smaller than reachable `ze`.
- **Minimize only the final length:** Lexicographic order depends first on differing characters, not solely on length.
- **Ignore circular adjacency:** The pairs `az` and `za` must be treated like ordinary consecutive letters.
- **Fully removable suffix:** The empty string is lexicographically smaller than every nonempty candidate.
- **Equal adjacent letters:** Their code-point difference is zero, so they cannot be removed as a pair.
