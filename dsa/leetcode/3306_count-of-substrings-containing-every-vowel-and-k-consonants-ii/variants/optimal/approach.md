## General

**Transform exact consonant count into a difference of cumulative counts.** Define $F(t)$ as the number of substrings containing all five vowels and at least $t$ consonants. A substring with exactly $k$ consonants is included in $F(k)$ but excluded from $F(k+1)$. Any substring with more consonants appears in both and cancels. Therefore

$$
\text{answer}=F(k)-F(k+1).
$$

This formulation is ideal for a monotone sliding window and avoids storing information for all $O(n^2)$ substrings.

The nested source helper `f(k)` computes $F(k)$. `cnt` stores the number of each vowel in the active window. It removes a vowel key when its count reaches zero, making `len(cnt) == 5` an exact test that all five distinct vowels are present. Variable `x` counts consonants, and `l` marks the active left boundary.

**Expand once for each right endpoint.** For every character `c` in `word`, the method adds it to the window. If `c in "aeiou"`, it increments the corresponding frequency. Otherwise it increments the consonant count. At this moment, the window may or may not satisfy both `x >= k` and `len(cnt) == 5`.

**Shrink through every valid start.** While both conditions hold, the source removes the character at `l` and increments `l`. Vowel removal decrements its frequency and deletes the key if no copy remains. Consonant removal decrements `x`.

The loop stops at the first invalid active window. Just before its final removal, the previous start was valid. Any earlier start is also valid because extending a substring to the left can only add vowel occurrences and consonants. Any start at or after the new `l` is invalid because it removes even more characters from an already-invalid window. Thus exactly the `l` starts from zero through `l-1` form valid substrings ending at the current right boundary. `ans += l` counts all of them at once.

This orientation can initially feel reversed: after the loop, the stored active window is invalid, yet `l` tells how many valid substrings existed. The key is that `l` is a boundary between valid earlier starts and invalid later starts for this fixed ending.
For each right endpoint, the shrinking invariant identifies precisely all starts whose substring contains every vowel and at least $k$ consonants. Adding their count `l` gives the correct number for that endpoint. Every substring has a unique right endpoint, so summing across the scan counts every member of $F(k)$ once and only once.

The set relation $F(k+1)\subseteq F(k)$ then proves subtraction. A substring with $c$ consonants contributes one when $c\ge k$ and zero when $c<k$ to the first total. It contributes one to the second exactly when $c\ge k+1$. The difference of its indicators is one exactly when $c=k$.

**Why the larger constraint is safe.** Both pointers are monotone. The right side moves $n$ times. Although the left pointer can move many times during one outer iteration, it moves at most $n$ times total because it never retreats. One call is linear, and two calls remain linear. No per-position arrays are allocated, which keeps memory independent of the $2\cdot10^5$ input length.

**Handle zero naturally.** In `f(0)`, the consonant condition `x >= 0` is always true, so windows become shrinkable as soon as all vowels are present. `f(1)` counts the all-vowel substrings that also have a consonant. Their difference leaves all-vowel substrings with exactly zero consonants.

The source matches the editorial's relaxed-constraint approach even though the variable names are compact. The counter and `x` are the full state; no next-consonant preprocessing is needed.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$. Within one `f` call, each character enters the window once and leaves it at most once. That is $O(n)$ expected time. Running `f(k)` and `f(k+1)` takes $2O(n)=O(n)$ time.

At most five vowel keys exist in `cnt`. Variables `ans`, `l`, and `x` are scalars. Auxiliary space is therefore $O(1)$ relative to $n$. Hash-map operations are expected constant-time, and a five-slot or 26-slot array could provide the same logic without hashing.

## Alternatives and edge cases

- **Brute-force substrings:** Even if frequency updates are incremental, enumerating all start/end pairs costs $O(n^2)$ and is impossible for $n=2\cdot10^5$.
- **Next-consonant preprocessing:** Maintain a window with exactly $k$ consonants and use the next consonant position to count vowel-only right extensions. It is linear but uses $O(n)$ extra space and more state than cumulative subtraction.
- **Last-seen vowel positions:** Combining the minimum last-seen vowel index with consonant boundaries can also count valid starts in linear time, but it is easier to make off-by-one errors.
- **Missing vowel:** If even one vowel never occurs, `len(cnt)` never reaches five, so both helper results and the final answer are zero.
- **`k = 0`:** Subtracting $F(1)$ from $F(0)$ removes every substring containing at least one consonant.
- **Large `k`:** If no substring contains that many consonants along with all vowels, $F(k)$ is zero; the subtraction remains valid.
- **Repeated copy of one vowel:** A key remains present until its last copy leaves the window. Extra copies do not incorrectly increase the distinct-vowel count.
- **Character classification:** Every lowercase non-vowel is a consonant under the contract, so the `else` branch is complete.
- **Several valid starts for one ending:** `ans += l` counts them collectively, which is essential for linear time.
- **Quadratic-size result:** Up to $n(n+1)/2$ substrings may be counted. Python's integer is unbounded; fixed-width implementations should use 64-bit arithmetic.
- **Why `>=` rather than `==` inside `f`:** The cumulative set must be monotone under extension. Exact equality is recovered only after subtraction.
- **Counter key deletion:** Leaving a zero-count vowel key would make `len(cnt) == 5` falsely report presence, so `cnt.pop(d)` is essential.
- **Two helper passes:** Their left boundaries and counters must be independent. Each invocation creates fresh local state, as the source does.
