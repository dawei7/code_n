## General

**Count by right endpoint instead of listing subarrays.** Every subarray has one unique ending index. If the algorithm knows how many alternating subarrays end at each position, adding those counts gives the total without generating any subarray explicitly.

The exact source maintains `s`, the length of the longest alternating suffix ending at the current element. For the first element, `s=1` because a one-element subarray has no adjacent pair that can violate the rule. It also initializes `ans=1` to count that first singleton.

**What makes an alternating suffix extend.** The loop examines adjacent values `a` and `b` through `pairwise(nums)`. If `a != b`, then every alternating subarray ending at `a` can be extended by `b`: the only new adjacency is the pair `(a,b)`, and it differs. The longest alternating suffix therefore grows by one:

`s = s + 1`.

If `a == b`, no alternating subarray containing both positions can cross this boundary. Any alternating suffix ending at `b` must start at `b` itself, so its longest possible length resets to one:

`s = 1`.

The binary-array constraint is not required for this local comparison; inequality is the whole alternating rule. With binary values, however, a run that keeps extending must alternate exactly between zero and one.

**Why `s` is also a count.** Suppose the longest alternating suffix ending at index $r$ has length $s$. Every suffix of that suffix is also alternating because removing elements from the left cannot create an equal adjacent pair. The possible ending-at-$r$ alternating subarrays have lengths:

$$
1,2,\ldots,s.
$$

There are exactly $s$ of them. No longer subarray ending at $r$ is alternating, by the definition of `s` as the longest valid suffix. Therefore, `ans += s` adds precisely the number of new alternating subarrays whose right endpoint is the current position.

This dual interpretation is the central simplification: `s` is both a maximum length and the number of valid suffix choices.

**A trace for `[0,1,1,1]`.** The first zero contributes one singleton, so `ans=1` and `s=1`.

- Pair `(0,1)` differs. The longest suffix length becomes two, representing `[1]` and `[0,1]`. Add two, making `ans=3`.
- Pair `(1,1)` is equal. Reset `s` to one and count only the new singleton. `ans` becomes four.
- The last pair is also equal. Reset and add one again, producing five.

Those five are exactly the four singleton subarrays and `[0,1]`.

For `[1,0,1,0]`, every adjacent pair differs. The values of `s` are 1, 2, 3, and 4, and their sum is 10. That equals the total number $n(n+1)/2$ of all subarrays, as expected when the entire array alternates.

**A loop invariant.** After processing through current index $r$:

- `s` is the length of the longest alternating subarray ending at $r$;
- `ans` is the number of all alternating subarrays contained in indices zero through $r$.

The invariant holds at $r=0$. At the next index, the adjacent comparison computes the new longest suffix exactly. Adding its length counts all and only valid subarrays with the new right endpoint, while older subarrays remain counted once. Thus the invariant is preserved.

At the final index, every alternating subarray lies within the processed prefix and has been counted under its unique right endpoint, proving the result.

**Why there is no sliding left pointer.** A conventional window could track the start of the current alternating run. Its length would be the same `s`. The source compresses that boundary into a length because only the number of valid suffixes is needed. On equality, resetting length to one is equivalent to moving the run start to the current index.

**The answer needs a wide integer.** A fully alternating array of length $n$ has $n(n+1)/2$ valid subarrays. For $n=10^5$, this is about five billion, larger than a signed 32-bit integer. Python integers grow automatically. A fixed-width implementation should use 64-bit storage for `ans`.

## Complexity detail

`pairwise(nums)` produces each of the $n-1$ adjacent pairs lazily. Every pair triggers constant work: one comparison, one length update, and one addition. Total time is $O(n)$.

Only `ans`, `s`, and the pairwise iterator's constant state are needed, so auxiliary space is $O(1)$. The required answer is a scalar. The source does not create a slice or a list of pairs.

Even though the answer can be quadratic in numeric magnitude, computing it does not require quadratic time. The per-endpoint aggregation compresses many subarrays into one addition.

## Alternatives and edge cases

- **Run-length formula:** Split the array at equal adjacent pairs. An alternating run of length $L$ contributes $L(L+1)/2$ subarrays. This is also $O(n)$ but postpones contributions until a run ends.
- **Explicit sliding-window start:** Track the earliest index of the current alternating suffix and add `right - left + 1`. It is equivalent to storing `s`.
- **Enumerate every subarray:** Checking all starts and ends is $O(n^2)$ and unnecessary.
- **Single element:** Initialization counts its singleton and no pair loop runs.
- **Equal adjacent values:** They break every alternating subarray crossing that boundary.
- **Different adjacent values:** They extend every currently alternating suffix by exactly one.
- **All values equal:** Every `s` is one, so only the $n$ singleton subarrays are counted.
- **Entire array alternating:** The accumulated sum is $1+2+\cdots+n=n(n+1)/2$.
- **Binary guarantee:** It bounds values but is not needed beyond the adjacent inequality test.
- **Subarray versus subsequence:** Only contiguous suffixes ending at each index are counted; skipped positions are never allowed.
- **Singleton validity:** With no adjacent pair, a one-element subarray is vacuously alternating.
- **Unique right endpoint:** This partitions all valid subarrays and prevents double counting.
- **Large result:** Python is safe; other languages should use a 64-bit integer.
- **Lazy pairwise iterator:** `itertools.pairwise` does not allocate all adjacent pairs.
- **No input mutation:** `nums` is traversed in original order and never changed.
