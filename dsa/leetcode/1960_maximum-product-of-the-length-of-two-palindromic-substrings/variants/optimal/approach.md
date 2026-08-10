## General

**Represent every odd palindrome by a center and radius**

An odd-length palindrome has one center index. Let `hlen[i]` be the number of matching character pairs around center $i$. Its maximal palindrome spans

$$
[i-\texttt{hlen}[i],\,i+\texttt{hlen}[i]]
$$

and has length $2\cdot\texttt{hlen}[i]+1$.

The first loop computes all radii with the odd-palindrome form of Manacher's algorithm. `center` and `right` describe the palindrome currently reaching farthest right.

If $i<right$, mirror index `2 * center - i` lies inside that known palindrome. Symmetry guarantees an initial radius up to the smaller of the mirror radius and the remaining distance to `right`. The code uses that safe value instead of comparing those characters again.

The while loop then expands beyond the guaranteed radius while both endpoints stay in bounds and have equal characters. If this palindrome reaches farther right, `center` and `right` are updated.

**Record the strongest palindrome at each maximal endpoint**

For each center, the code knows one maximal palindrome. It writes its length into:

- `prefix[i + hlen[i]]`, indexed by its ending position;
- `suffix[i - hlen[i]]`, indexed by its starting position.

Several centers may share an endpoint, so `max` keeps the longest.

This initial marking is not enough. A smaller palindrome obtained by removing both endpoints of a larger palindrome has a different start and end and may be the best choice beside a split. The next passes recover these nested palindromes without enumerating them one by one.

**Propagate shrunken palindromes to exact endpoints**

The first propagation traverses `prefix` from right to left. The source expresses index $j=n-i-1$ as `~i`. It applies:

`prefix[j] = max(prefix[j], prefix[j + 1] - 2)`.

If an odd palindrome of length $L$ ends at $j+1$, removing its two outer characters creates a palindrome of length $L-2$ ending at $j$. Thus this pass makes `prefix[j]` the best odd palindrome ending exactly at $j$.

Symmetrically, the forward update

`suffix[i] = max(suffix[i], suffix[i - 1] - 2)`

shrinks a palindrome starting at $i-1$ into one starting at $i$. Afterward, `suffix[i]` is the best palindrome starting exactly at $i$.

Values can briefly propagate negative candidates such as $0-2$, but `max` with the zero-initialized entry prevents a negative length from being stored.

**Turn exact endpoints into best values on either side**

The next forward pass makes `prefix[i]` the longest odd palindrome ending at or before $i$ by taking the maximum with `prefix[i - 1]`.

The matching backward pass makes `suffix[i]` the longest odd palindrome starting at or after $i$. Again, `~i` is simply a compact negative-index way to visit $n-2,n-3,\ldots,0$.

Now consider a split before index $i$. Any left palindrome must end at or before $i-1$, and any right palindrome must start at or after $i$. Their best possible lengths are exactly `prefix[i - 1]` and `suffix[i]`. Multiplying them for every split from one through $n-1$ and taking the maximum produces the answer.

**Why every optimal pair is considered**

Any two nonintersecting substrings have some boundary between them. Choose $i$ immediately after the left palindrome's end or anywhere before the right palindrome's start. The cumulative arrays at that split are at least as long as those two palindromes, so the computed product is at least the pair's product.

Conversely, every product uses one palindrome ending entirely left of the split and one beginning entirely right, so the substrings do not intersect. The arrays contain only genuine odd palindromes produced from Manacher maxima and valid two-character shrinking. Every candidate product is achievable. Together these directions prove the maximum is exact.

## Complexity detail

Let $N$ be the string length.

Manacher expansion is $O(N)$ amortized: reused mirror radii avoid restarting comparisons, and the right boundary advances at most $N$ times. Marking endpoints, both shrink-propagation passes, both cumulative passes, and scanning splits are each linear. Total time is $O(N)$.

`hlen`, `prefix`, and `suffix` each contain $N$ integers, so auxiliary space is $O(N)$. The final product generator uses constant additional iteration state.

## Alternatives and edge cases

- **Expand around every center independently:** It is simple but can take $O(N^2)$ on a uniform string.
- **Rolling hashes plus binary search:** Hashes can find palindrome radii in $O(N\log N)$ expected time but add collision risk and are slower asymptotically.
- **Even palindromes:** The task permits only odd lengths, so one radius array suffices; no even-center Manacher array is needed.
- **Length-one palindrome:** Every individual character is a valid odd palindrome with radius zero, ensuring both sides of every split have at least one candidate.
- **Two-character string:** The only split pairs the two length-one palindromes, producing one.
- **Nested palindromes:** The $-2$ propagation is what exposes shorter nested choices at shifted endpoints.
- **Negative indexing:** `~i` equals `-i-1` in Python and is used only to traverse arrays backward; it is not a bitwise algorithmic trick.
- **Palindromes separated by a gap:** Cumulative prefix and suffix maxima allow unused characters between the two selected substrings.
- **Touching palindromes:** A split can place the right substring immediately after the left, which remains nonintersecting.
- **Uniform string:** Manacher remains linear, and the best product comes from partitioning into two odd lengths.
- **Input unchanged:** All information is stored in numeric arrays; the string is read only.
