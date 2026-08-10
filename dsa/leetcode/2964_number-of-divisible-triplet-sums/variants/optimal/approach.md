## General

**Use remainders and preserve index order**

The task counts index triples $i<j<k$ whose values have a sum divisible by `d`. Divisibility depends only on remainders modulo `d`:

$$
(\texttt{nums}[i]+\texttt{nums}[j]+\texttt{nums}[k]) \bmod d = 0.
$$

For fixed middle and right indices $j$ and $k$, the needed remainder of `nums[i]` is determined. If

`r = (nums[j] + nums[k]) % d`,

then the earlier value must have remainder `(-r) % d`. The implementation writes this nonnegative complement as

`x = (d - r) % d`.

The final modulo is important when `r == 0`: the needed remainder is zero, not `d`.

**Let the dictionary represent only eligible left indices**

The outer loop chooses `j` from left to right. Before processing a particular `j`, dictionary `cnt` contains remainder frequencies only for indices `i < j`. The inner loop tries every `k > j`. For each pair $(j,k)$, `cnt[x]` tells exactly how many eligible earlier indices have the complementary remainder, so adding it counts all triples with that fixed middle/right pair.

Only after all `k` values for the current `j` have been processed does the code execute `cnt[nums[j] % d] += 1`. That timing is essential. It makes the current `j` available as a future left index but prevents it from being used as `i` in its own iteration. The three indices are therefore automatically distinct and strictly ordered without any explicit comparisons inside the lookup.

For example, let `nums = [3, 3, 4, 7]` and `d = 5`. When `j = 1`, `cnt` contains the remainder of index zero, which is three. Pairing `nums[1] = 3` with `nums[2] = 4` gives pair remainder two and needs left remainder three, so one triple is counted. Pairing with seven gives pair remainder zero and needs remainder zero, which is absent. Afterward, the second three is inserted for use by later middle positions.

**Why remainder counts are enough**

If two earlier numbers have the same remainder modulo `d`, then for any fixed `nums[j] + nums[k]` they either both make the total divisible or both fail. Their actual magnitudes do not matter to divisibility. Nevertheless, their multiplicity matters because different indices form different triplets. The dictionary stores a frequency rather than a set so that all eligible occurrences contribute.

For every pair $(j,k)$, there is exactly one complementary remainder class. Every earlier index in that class creates a valid triple, and no earlier index outside it can create one. Thus `ans += cnt[x]` is both exhaustive and exclusive for that pair.

**Why every valid triple is counted exactly once**

Take any valid triple $(i,j,k)$ with $i<j<k$. When the outer loop reaches its middle index $j$, index $i$ has already been inserted into `cnt` and index $j$ has not. The inner loop eventually reaches its exact $k$. Since the total is divisible by `d`, `nums[i] % d` equals the computed complement `x`, so that occurrence contributes one to the lookup count.

The triple cannot be counted under another outer iteration because its middle index is uniquely $j$, and it cannot be counted for another inner iteration because its right index is uniquely $k$. Conversely, every occurrence counted by a lookup has an earlier index with the exact complementary remainder, so its sum is divisible and its indices satisfy the required order.

**Why this is quadratic rather than cubic**

There are still $\Theta(N^2)$ possible ordered choices for $(j,k)$, and the implementation enumerates all of them. The improvement is that it does not scan all possible $i$ for each pair. The hash map aggregates every earlier $i$ by remainder and answers “how many work?” in expected constant time. This removes one entire factor of $N$.

The dictionary is a `defaultdict(int)`, so looking up a missing remainder returns zero. Such a lookup may create a zero-valued key, but this has no effect on the count.

## Complexity detail

Let $N$ be the length of `nums`. The inner loop runs $N-j-1$ times for each `j`. Summing these lengths gives $N(N-1)/2$, so there are $O(N^2)$ pair iterations. Each uses expected $O(1)$ dictionary work, giving expected $O(N^2)$ total time.

At most `d` distinct normalized remainders exist, and at most $N$ values are inserted. The dictionary therefore uses $O(\min(N,d))$ meaningful frequency space, commonly stated as $O(N)$ under the input-size bound. Zero-valued keys introduced by missing lookups are also drawn from the same `d` remainder classes. The answer and loop variables use constant space.

## Alternatives and edge cases

- **Three nested loops:** Testing every $(i,j,k)$ directly takes $O(N^3)$ time and repeats the same modular relationships.
- **Two-sum map rebuilt for every index:** Several pair-counting arrangements are possible, but rebuilding a map per fixed index still costs quadratic time with more setup. The streaming remainder map maintains index order naturally.
- **Use a set of remainders:** A set loses multiplicity and undercounts when several earlier indices share the needed remainder.
- **Complement without final modulo:** `d - r` equals `d` when `r=0`, but normalized remainders range from zero to `d-1`. The outer `% d` fixes this case.
- **Repeated values:** They represent different indices and must contribute separately; dictionary frequencies preserve them.
- **Fewer than three elements:** No inner configuration can form a triple, so the answer remains zero.
- **`d = 1`:** Every value has remainder zero, so every index triple is divisible; the algorithm accumulates exactly $\binom{N}{3}$.
- **Large answer:** The number of triples can be $\Theta(N^3)$ even though computation is $O(N^2)$; Python integers represent the result without overflow.
- **Input preservation:** The solution reads values in their original order and never modifies the list.
