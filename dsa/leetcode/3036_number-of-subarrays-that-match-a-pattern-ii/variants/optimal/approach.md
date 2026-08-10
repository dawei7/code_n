## General

**Transform numbers into the language of the pattern.** The pattern describes relationships between adjacent values, not the values themselves. The source first builds an array `s` of length $N-1$. For every adjacent pair:

- append 1 when the new value is larger;
- append 0 when the values are equal;
- append $-1$ when the new value is smaller.

A subarray `nums[i..i+M]` matches the length-$M$ pattern exactly when

`s[i..i+M-1]`

equals `pattern`. This is a one-to-one equivalence: each of the subarray's $M$ required comparisons becomes one symbol in the transformed array. The problem is now ordinary exact pattern matching.

**Build KMP prefix information.** Helper `partial(pattern)` constructs the prefix-function array `pi`. `pi[i]` is the length of the longest proper prefix of `pattern[0..i]` that is also a suffix of that same segment.

Variable `g` is the current candidate border length. When `pattern[g]` differs from `pattern[i]`, the code repeatedly falls back to `pi[g - 1]`. That fallback tries the next-longest border without rechecking symbols already known to match. If the current symbols agree, the Boolean comparison contributes one and extends the border:

`pi[i] = g = g + (s[g] == s[i])`.

Because Python treats a Boolean as 0 or 1, this leaves `g` unchanged on mismatch after all fallbacks or increments it on a match.

**Stream the transformed array through KMP.** Helper `match(s, pattern)` builds `pi` once, then scans `s` from left to right. Variable `g` is the number of pattern symbols currently matched by the suffix ending just before the next text symbol.

On mismatch, `g = pi[g - 1]` preserves the longest suffix that could still be the beginning of another match. On equality, `g` advances. These fallbacks are what prevent restarting from scratch at every candidate start.

When `g == len(pattern)`, a full occurrence ends at transformed index `i`. Its start is

$$
i+1-M,
$$

so the source appends `i + 1 - g` to `idx`. It then falls back to `pi[g - 1]` so overlapping occurrences can also be found.

The solution returns `len(match(s, pattern))`. Every occurrence in the transformed relation array corresponds to exactly one matching subarray of `nums`, so this length is the requested count.

**Why KMP is linear.** Although mismatch handling contains a while-loop, `g` cannot repeatedly move forward and backward without bound. It advances at most once per text position, and every fallback strictly decreases it. Across the entire scan, total fallback work is linear. The same amortized argument applies while building `pi`.

**A concrete transformation.** For `nums = [1,4,4,1,3,5,5,3]`, the adjacent relation array is

`[1,0,-1,1,1,0,-1]`.

Searching for `[1,0,-1]` finds starts 0 and 4. These correspond to original windows `nums[0..3]` and `nums[4..7]`, namely `[1,4,4,1]` and `[3,5,5,3]`.

**Why overlap handling matters.** If `s = [1,1,1]` and `pattern = [1,1]`, occurrences begin at 0 and 1. After finding the first, resetting `g` to zero would risk losing the fact that the final 1 is already a prefix of the next occurrence. Falling back through `pi` preserves it and counts both length-three increasing subarrays.

**Only the used helpers affect execution.** The module also defines `string_find`, which returns whether a pattern occurs, but `countMatchingSubarrays` never calls it. The runtime path is transformation, `match`, and `partial`.

## Complexity detail

Let $N$ be `len(nums)` and $M$ be `len(pattern)`. Creating `s` costs $O(N)$ time. Prefix-function construction costs $O(M)$, and matching costs $O(N+M)$ amortized. Total time is $O(N+M)$.

The exact space behavior differs from the local manifest. Array `s` stores $N-1$ relation values, `pi` stores $M$ integers, and `match` stores every match start in `idx` even though the caller needs only the count. There can be $O(N)$ overlapping matches. Peak auxiliary space is therefore $O(N+M)$, not $O(M)$.

A truly streaming version could generate relations without `s` and increment a counter instead of building `idx`, reaching $O(M)$ space. That is not what this protected source does.

## Alternatives and edge cases

- **Naive comparison at every start:** It takes $O((N-M)M)$ worst-case time and is too slow for $N$ up to one million.
- **Z-function:** Concatenating pattern, a separator, and the relation array also finds matches in linear time, but still normally stores a linear auxiliary array.
- **Rolling hash:** It can compare windows quickly but introduces collision risk unless equality is independently verified.
- **Streaming KMP count:** Relations can be fed directly into the KMP state and a scalar count incremented on matches. It would preserve linear time and use $O(M)$ space, unlike the exact source's materialized arrays.
- **Pattern length one:** Every adjacent relationship matching that one symbol is counted.
- **Overlapping matches:** The `pi[g - 1]` fallback after a full match preserves them.
- **Equal adjacent values:** They map to zero, distinct from both increasing and decreasing relationships.
- **Large values:** Only comparisons are performed; magnitudes up to $10^9$ do not affect matching.
- **Input preservation:** Neither `nums` nor `pattern` is mutated.
- **Manifest mismatch:** Its $O(M)$ space claim describes a streaming KMP design, while the protected source uses $O(N+M)$ storage.
