## General

**Define the suffix subproblem**

A substring is balanced when every distinct character present in it occurs the same number of times. Single-character substrings are always balanced, so a valid partition always exists.

Let `dfs(i)` be the minimum number of balanced substrings needed to partition suffix `s[i:]`. If `i >= n`, the suffix is empty and needs zero pieces.

For a nonempty suffix, choose the end `j` of its first piece. Whenever `s[i:j+1]` is balanced, using it costs one piece plus the best partition of what remains:

$$
1+\operatorname{dfs}(j+1).
$$

Taking the minimum over all balanced endpoints gives the optimal answer for `dfs(i)`. The cache stores one answer per starting index.

**Maintain balance while extending j**

Recounting every candidate substring from scratch would introduce an extra factor of $n$. The exact code extends `j` one character at a time and maintains two maps:

- `cnt[c]` is the current number of occurrences of character $c$ in `s[i:j+1]`;
- `freq[v]` is the number of distinct characters whose current occurrence count equals $v$.

When adding character `s[j]`, suppose its old count is $v>0$. It must leave frequency bucket $v$, so `freq[v]` is decremented and the key is removed if its bucket becomes empty. The character count becomes $v+1$, and the corresponding new bucket is incremented.

After this update, `freq` contains exactly the positive occurrence counts represented in the current substring. The substring is balanced exactly when `len(freq) == 1`: all present characters belong to the same count bucket.

Zero counts are intentionally absent. A character not present in the substring should not be required to match the frequencies of characters that are present.

**Why the recurrence is correct**

Consider an optimal partition of `s[i:]`. Its first substring ends at some index $j$ and must be balanced. The loop examines that exact endpoint and considers one plus `dfs(j+1)`. By the definition of `dfs`, the cached suffix cost is no greater than the remaining number of pieces in the optimal partition. Therefore, the recurrence can achieve the optimum.

Conversely, every transition taken by the recurrence uses a substring verified balanced by `len(freq) == 1` and appends an optimal valid partition of the suffix. Every candidate cost is therefore achievable. The minimum cannot be lower than the true optimum. Together, these directions prove equality.

The initial value `ans = n - i` is a valid upper bound because each remaining character can be its own balanced substring. The walrus expression computes `t = 1 + dfs(j + 1)` and updates only when it improves that bound.

**Example of the frequency-of-frequencies structure**

For substring `"aabb"`:

- after `"aab"`, counts are $a:2,b:1$, so `freq` has keys 2 and 1 and the substring is not balanced;
- after the final `b`, counts are $a:2,b:2$, the bucket for 1 disappears, and `freq` has only key 2, so the substring is balanced.

For `"abc"`, all three characters have count 1. `freq` has one key, 1, whose value is 3. The length of the map—not the number of characters in its only bucket—is what detects equality of all occurrence counts.

**Top-down evaluation order**

Every `dfs(i)` begins by examining the one-character substring `s[i:i+1]`, which is balanced, so it calls `dfs(i+1)`. This first path can recurse through the entire string. Memoization prevents later endpoints from recomputing suffix answers: by the time control returns to an earlier frame, all larger start indices have already been cached.

This evaluation detail preserves the $O(n^2)$ work bound, but it also creates a recursion-depth risk near the maximum length, which the complexity section states explicitly.

## Complexity detail

There are $n+1$ possible suffix indices. For a fixed `i`, the loop extends `j` from $i$ to $n-1$, performing expected constant-time dictionary updates per character. The total number of extensions is

$$
\sum_{i=0}^{n-1}(n-i)=O(n^2).
$$

Each state is computed once because of `@cache`, so expected time is $O(n^2)$.

The cache stores $O(n)$ scalar answers. The recursion stack can reach $O(n)$ depth. Each active frame on the initial deepest chain has only processed its first character before descending, so the simultaneously live local maps use $O(n)$ aggregate space on that chain. Later suffix calls are cached while an earlier frame builds a larger map. With the fixed 26-letter alphabet, each `cnt` and `freq` map also has only constant many keys. Overall auxiliary space is $O(n)$.

However, $n$ may be 1000, close to Python's standard recursion limit. The exact source does not raise that limit, so a legal long input can produce `RecursionError` depending on the runtime. An iterative prefix or suffix DP avoids this compatibility risk while keeping the same asymptotic bounds.

Expected dictionary $O(1)$ operations are assumed in the time analysis.

## Alternatives and edge cases

- **Bottom-up DP:** Compute the best partition count for prefixes or suffixes iteratively while extending balanced candidates. It keeps $O(n^2)$ time and $O(n)$ space without recursion risk.
- **Recount every substring:** Building a fresh frequency map for every `(i,j)` can cost $O(n^3)$. Incremental counts are the key optimization.
- **Check minimum and maximum count:** With a fixed 26-element count array, a substring is balanced when all positive counts have equal minimum and maximum. Scanning 26 values is still constant per endpoint.
- **Prefix frequency vectors:** They obtain a substring's 26 counts in constant-alphabet time but require $O(26n)$ storage; the DP remains quadratic.
- **Single character:** It is balanced, so every suffix always has at least the one-character transition.
- **All characters equal:** The whole string is balanced and the answer is one.
- **All characters distinct:** The whole string is also balanced because every present character occurs once.
- **Mixed frequencies:** A substring such as `"aab"` is rejected because `freq` contains keys 2 and 1.
- **Zero-frequency letters:** They must not participate in balance; only characters present in the substring are compared.
- **Removing empty buckets:** If a zero-valued `freq` key were left in the map, `len(freq)` could falsely report multiple frequencies.
- **Full string balanced:** The endpoint $j=n-1$ considers `1 + dfs(n) = 1` and reaches the minimum possible answer.
- **Recursion limit:** Near length 1000, iteration is safer than relying on judge-specific stack configuration.
