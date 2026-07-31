## General

**Rewrite the good-pair equality.** A pair is good precisely when

$$
j-i=\texttt{nums[j]}-\texttt{nums[i]}
\quad\Longleftrightarrow\quad
\texttt{nums[i]}-i=\texttt{nums[j]}-j.
$$

Thus indices belong to the same good-pair group when their
`nums[index] - index` keys match.

**Count bad earlier partners online.** At index $j$, there are $j$ earlier
indices in total. If the current key has appeared $c$ times, exactly those
$c$ indices form good pairs with $j$, so this position contributes $j-c$ new
bad pairs. Add that amount, then increment the key frequency.

Every pair is considered exactly when its later index is processed. The key
equivalence identifies all and only good pairs, making the complementary count
exact.

## Complexity detail

One expected-constant-time hash lookup and update is performed per element, so
time is $O(n)$ expected. Up to $n$ distinct keys require $O(n)$ space.

## Alternatives and edge cases

- **Count all pairs then subtract good groups:** After building frequencies,
  subtract $\binom c2$ for every key from $\binom n2$; this is equivalent.
- **Check every pair:** Directly applying the definition takes $O(n^2)$ time.
- **Single element:** With no index pair, the answer is zero.
- **Large count:** Use a 64-bit integer outside Python.
- **Negative keys:** `nums[i] - i` may be negative and must remain valid.
