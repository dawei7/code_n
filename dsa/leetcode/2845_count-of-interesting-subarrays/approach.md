## General

**Reduce each element to whether it is special.** For the subarray definition, the original magnitude of `nums[i]` matters only through the predicate

`nums[i] % modulo == k`.

The source builds `arr` containing one for a qualifying index and zero otherwise. Then the number `cnt` in any original subarray is simply the sum of its corresponding binary values.

**Use prefix counts.** Let $P[r]$ be the number of qualifying indices in the prefix before boundary $r$, with $P[0]=0$. For a subarray `nums[l..r]`, its qualifying count is

$$
P[r+1]-P[l].
$$

The subarray is interesting when this difference modulo `modulo` equals `k`.

Rearranging the modular equation gives

$$
P[l]\bmod\texttt{modulo}
=
(P[r+1]-\texttt{k})\bmod\texttt{modulo}.
$$

Therefore, at each right boundary, the number of interesting subarrays ending there equals the number of earlier prefix boundaries with one specific remainder.

**Count earlier remainders in a Counter.** `cnt[0] = 1` records the empty prefix before the first element. This allows subarrays beginning at index zero to be counted.

Variable `s` is the running prefix count. For each binary `x`:

- Add `x` to `s`.
- Look up `cnt[(s - k) % modulo]` and add it to `ans`.
- Record the current remainder with `cnt[s % modulo] += 1`.

The lookup must happen before inserting the current prefix. Otherwise, the same boundary could pair with itself and represent an empty subarray. The definition requires nonempty subarrays.

**Why Python modulo handles negative differences.** When `s < k`, `s - k` is negative. Python's modulo operator returns the corresponding nonnegative residue, so the dictionary key still represents the correct congruence class.
Before processing an element, `cnt[r]` equals the number of prefix boundaries already seen whose qualifying-count remainder is $r$. After updating `s` for the current right endpoint, every earlier boundary with remainder `(s-k) % modulo` creates one and only one interesting subarray ending here.

Adding that frequency counts all such left endpoints. Recording the current boundary then establishes the invariant for the next iteration. Since every nonempty subarray has a unique right endpoint and left prefix boundary, all interesting subarrays are counted exactly once.

**The `k = 0` case works without special handling.** The method looks for equal current and earlier prefix remainders. Their difference is divisible by `modulo`, including a subarray with zero qualifying positions. The empty prefix count remains essential.

**Why prefix values themselves can grow without bound.** `s` is at most `n` because it counts binary ones. The Counter stores only `s % modulo`, since congruence is the only property needed for future differences.

**The explicit binary array is optional but present.** The exact source constructs `arr` before scanning, using $O(n)$ space. The predicate could be evaluated inline and avoid that array, but the manifest's $O(n)$ space already permits it.

**Counter missing keys.** Accessing an absent Counter key returns zero, so no separate membership test is needed. Incrementing later creates the key.

**A short trace.** With binary indicators `[1, 0, 0]`, modulo two, and `k = 1`, the initial remainder-zero count is one. After the first one, `s = 1` and the needed earlier remainder is zero, so one subarray is found. Each following zero leaves `s = 1` and again finds the same initial boundary, counting the two longer subarrays. Recording current remainders also makes later starts available without enumerating them.

**Why values failing the predicate still matter to endpoints.** A zero indicator does not change `s`, but it creates a new prefix boundary with the same remainder. Those repeated remainder occurrences correspond to different left endpoints and can produce additional distinct subarrays later. The Counter must record every boundary, not only positions where `s` changes.

## Complexity detail

Building `arr` visits $n$ numbers and takes $O(n)$ time. The prefix loop visits $n$ binary values. Each Counter access or update is expected $O(1)$, so total expected time is $O(n)$.

`arr` contains $n$ integers. The Counter stores at most $\min(n+1,\texttt{modulo})$ distinct remainders. Total auxiliary space is $O(n+\min(n,\texttt{modulo}))=O(n)$. A tighter decomposition makes clear that the explicit binary array is the dominant guaranteed allocation.

The answer can be as large as $n(n+1)/2$, so 64-bit arithmetic is normally required. Python integers handle it automatically.

Expected hash complexity is appropriate for integer keys.

## Alternatives and edge cases

- **Evaluate the predicate inline:** Replace `arr` with direct iteration over `nums` and update `s` immediately. This preserves $O(n)$ time and reduces space to $O(\min(n,\texttt{modulo}))$.
- **Fixed remainder array:** If `modulo` is small, a list of that length can replace the Counter. Since modulo can be $10^9$, allocating it unconditionally is unsafe.
- **Brute-force every subarray:** Maintaining counts for all $O(n^2)$ endpoint pairs is too slow at $10^5$ elements.
- **`k = 0`:** Equal prefix remainders are paired, correctly including subarrays with zero qualifying indices.
- **No qualifying elements:** Depending on `k`, many or no subarrays may be interesting; prefix algebra handles both.
- **Every element qualifies:** `s` increases at each step, and remainder frequencies count lengths congruent to `k`.
- **Subarray starting at zero:** The seeded empty-prefix remainder supplies its left boundary.
- **Nonempty requirement:** Querying before inserting the current prefix prevents counting a boundary paired with itself.
- **Large modulo:** Only remainders actually encountered are stored in the Counter.
- **Negative intermediate `s-k`:** Python modulo normalizes it to the correct nonnegative key.
- **Input preservation:** The source creates a binary representation and does not modify `nums`.
