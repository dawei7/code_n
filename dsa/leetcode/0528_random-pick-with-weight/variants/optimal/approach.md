## General

The weights define how much probability each index should receive. A useful way to realize those probabilities is to give index `i` exactly `w[i]` equally likely integer tickets, then choose one ticket uniformly.

The constructor represents consecutive ticket ranges with prefix sums. It starts:

`self.s = [0]`

and for each weight `c` appends `self.s[-1] + c`. If the weights are `[1, 3, 2]`, the resulting array is `[0, 1, 4, 6]`.

The last value, six, is the total weight. The individual ticket intervals are:

- index zero owns integer tickets from `self.s[0] + 1` through `self.s[1]`, namely one;
- index one owns tickets two through four;
- index two owns tickets five through six.

In general, index `i` owns:

$$
(\texttt{self.s}[i],\texttt{self.s}[i+1]]
$$

among integer points. This interval contains exactly `w[i]` integers because its endpoint difference is `self.s[i + 1] - self.s[i]`.

All input weights are positive, so every prefix sum is strictly larger than the previous one. That strict ordering makes binary search possible and ensures every index owns a nonempty ticket range.

**Draw one uniform ticket.** Method `pickIndex` calls:

`random.randint(1, self.s[-1])`.

Python's `randint` includes both endpoints. Thus every integer ticket from one through the total weight has the same probability, exactly one divided by the total.

Index `i` owns `w[i]` of those tickets, so the probability that the random result lands in its interval is:

$$
\frac{w[i]}{\sum_j w[j]}.
$$

That is precisely the required distribution. The method needs only one random call per pick.

**Find the owning prefix boundary.** Given ticket `x`, the target index is determined by the first prefix sum greater than or equal to `x`. For the example prefixes `[0, 1, 4, 6]`, ticket four maps to boundary position two and therefore original index one; ticket five maps to boundary position three and original index two.

The binary search operates over prefix positions one through `len(self.s) - 1`. Position zero is excluded because its value zero cannot reach any ticket `x >= 1`.

At every step, `mid` divides the remaining interval:

- if `self.s[mid] >= x`, `mid` could be the first adequate boundary, so `right = mid` keeps it and discards later-only positions;
- otherwise the prefix is too small, so every position through `mid` is also too small and `left = mid + 1` discards them.

The invariant is that the first prefix position with value at least `x` remains inside `[left, right]`. Since the interval shrinks each iteration, eventually `left == right` at exactly that first adequate position.

The prefix array has an extra leading zero, so prefix position one ends index zero's ticket range. The method returns `left - 1` to convert boundary position back to the original weight index.

For `w = [1, 3]`, prefixes are `[0, 1, 4]`. Ticket one selects the first boundary and returns index zero. Tickets two, three, and four select the second boundary and return index one. Hence the probabilities are one quarter and three quarters.

**Boundary choices are exact.** Using the first prefix `>= x` matches inclusive integer ticket intervals. If ticket `x` equals a prefix value, it belongs to the index ending at that prefix, not the next index. This is why the comparison uses `>=` rather than `>`.

Starting random tickets at one also avoids ambiguity around prefix zero. An equivalent zero-based construction would draw from zero through total minus one and search for the first prefix strictly greater than the target, but the inequality must change consistently.

**Why every call is independent and correctly distributed.** The prefix sums never change after construction. Each `pickIndex` draws a fresh uniform ticket over the same complete range and performs a deterministic mapping from that ticket to an index. Previous results do not remove tickets or alter future probabilities, which is appropriate because the problem asks for repeated weighted sampling with replacement.

The output sequence need not contain frequencies exactly proportional to the weights over a small number of calls. Randomness guarantees the probability of each individual result; empirical frequencies approach those proportions only over many trials.

## Complexity detail

Let $n$ be the number of weights and $q$ the number of `pickIndex` calls. Constructor work is $O(n)$ because it computes one prefix sum per weight, and the prefix array uses $O(n)$ space.

Each pick makes one random call and binary-searches $n$ prefixes in $O(\log n)$ time with $O(1)$ temporary space. Across construction and $q$ picks, total time is $O(n+q\log n)$ and retained space is $O(n)$, matching the manifest.

The maximum total weight under the constraints can exceed narrow 16-bit storage, so implementations in fixed-width languages need an integer type large enough for the sum. Python integers expand automatically.

## Alternatives and edge cases

- **Expand one entry per ticket:** Uniformly choosing from an expanded array is conceptually direct but uses space proportional to the total weight rather than the number of indices.
- **Linear scan of prefix sums:** It maps tickets correctly but costs $O(n)$ per pick instead of $O(\log n)$.
- **Alias method:** It can provide $O(1)$ sampling after preprocessing, but its setup and probability bookkeeping are more complex.
- **One weight:** The only ticket range belongs to index zero, and binary search returns it for every call.
- **Equal weights:** Equal-size ticket intervals produce equal probabilities.
- **Very uneven weights:** A large interval naturally receives proportionally more integer tickets without special logic.
- **Ticket equal to a prefix:** The `>=` comparison assigns it to the interval ending at that prefix.
- **First ticket:** `x = 1` always maps to the first positive prefix.
- **Last ticket:** `x = self.s[-1]` maps to the final index.
- **Positive-weight guarantee:** It makes prefix sums strictly increasing and every probability nonzero.
- **Sampling with replacement:** No state changes during picks, so returning an index once does not reduce its future probability.
