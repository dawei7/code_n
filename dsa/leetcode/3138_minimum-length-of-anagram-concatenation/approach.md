## General

**A candidate length must divide the whole string**

If `s` is a concatenation of anagrams of some length-$k$ string `t`, then `s` consists of an integer number

$$
q=\frac nk
$$

of blocks, each with length $k$. Therefore, $k$ must divide $n$. The outer loop tests lengths in increasing order and calls `check(i)` only when `n % i == 0`. The first successful length is automatically the minimum requested answer.

Length $n$ always works: there is one block, and `t` may be `s` itself. Thus the function is guaranteed to return even though there is no explicit fallback after the loop.

**Anagrams are characterized by letter frequencies**

Two strings are anagrams exactly when every letter appears the same number of times in both. Order inside a block does not matter.

The code first builds `cnt = Counter(s)`, the frequency of each character in the complete string. For a candidate block length $k$, there are $q=n/k$ blocks. If every block is an anagram of the same `t`, each block must contain exactly one $q$th share of every global letter count:

$$
q\cdot \operatorname{count}_{block}(c)=\operatorname{count}_{s}(c)
$$

for every character $c$.

Helper `check(k)` slices each aligned block `s[i:i+k]` and builds its counter `cnt1`. It then tests

`cnt1[c] * (n // k) == v`

for every global pair `(c, v)`. If any equality fails, that block cannot have the common frequency vector, so the candidate length is rejected immediately.

There cannot be an extra character in `cnt1` absent from `cnt` because the block is a substring of `s`. Therefore, iterating only over global keys is sufficient.

**Why comparison against global totals works**

If all blocks are anagrams, each has the same frequency $a_c$ for letter $c$, and the global count is $q a_c$. Every code equality passes.

Conversely, suppose every block passes. For each global letter $c$, every block's count equals `cnt[c] / q` because the tested product is equal to `cnt[c]`. Thus every block has the same count for every character and all blocks are pairwise anagrams. Any one block can serve as `t`.

This test also rejects impossible divisibility automatically. If a global count $v$ is not divisible by $q$, no integer `cnt1[c]` can satisfy `cnt1[c] * q == v`, so the first inspected block fails.

**Example**

For `s = "abba"` and candidate $k=1$, $q=4$. Global counts are two `a` characters and two `b` characters. A one-character block containing `a` has local count 1, and $1\cdot4\ne2$, so length 1 fails.

For $k=2$, $q=2$. The blocks are `"ab"` and `"ba"`. Each has one `a` and one `b`; multiplying each local count by 2 produces the global count 2. Length 2 passes and is returned.

For `"cdef"`, every proper divisor candidate fails because its blocks have different letter vectors. Candidate 4 has one block and necessarily passes.

**Why increasing order is enough**

The goal is only the minimum length, not all possible lengths. The outer loop begins at 1, so when a divisor passes, every smaller integer has already been considered. Nondivisors cannot be valid block lengths, and smaller divisors have failed their complete frequency checks. Returning immediately is therefore safe.

The solution does not need to reconstruct `t`. Once a length passes, the first block itself is an anagram representative and proves existence.

## Complexity detail

Let $\tau(n)$ be the number of positive divisors of $n$.

For one tested divisor $k$, slicing and counting all $n/k$ blocks processes a total of $n$ characters. The inner loop checks at most 26 global lowercase-letter keys for every block, costing $O(26n/k)$, which is bounded by $O(n)$. Thus one successful full check is $O(n)$, and all divisor checks cost $O(n\tau(n))$. The outer loop's divisibility tests add $O(n)$ time.

Since $\tau(n)=O(\sqrt n)$ by the elementary divisor-pair bound, the manifest's coarse worst-case $O(n\sqrt n)$ time follows. The sharper expression is $O(n\tau(n)+n)$, and practical execution often stops before testing all divisors.

The counters contain at most 26 keys because the alphabet is lowercase English letters, so counter storage is $O(1)$ with respect to $n$. However, the exact Python expression `s[i:i+k]` creates a temporary string of length $k$. At candidate $k=n$, that temporary is length $n$. Therefore, peak auxiliary space for the exact source is $O(n)$, not the manifest's $O(1)$. An index-based counter that avoids slicing could realize constant auxiliary space for a fixed alphabet.

The global counter is built once in $O(n)$ time. Temporary block counters are released between iterations.

## Alternatives and edge cases

- **Compare each block to the first block:** Build the first block's frequency vector and compare all later blocks. This is direct and can avoid global multiplication, with the same per-candidate time.
- **Enumerate divisors first:** Generate divisors in $O(\sqrt n)$ and sort them, avoiding the outer $O(n)$ divisibility scan. The block checks still dominate for many candidates.
- **Prefix frequency arrays:** Precompute 26 prefix counts so each block vector is obtained in $O(26)$ time without slicing. This uses $O(26n)$ space but can reduce repeated character scans.
- **Index-based fixed arrays:** Count each block directly from character indices into a 26-element array. It retains $O(n\tau(n))$ time while avoiding the $O(k)$ slice allocation.
- **Sort each block:** Sorted anagrams compare equal, but sorting every block adds a $\log k$ factor and allocates more data.
- **Length one:** It works only when all characters are identical, because every one-character block must be an anagram of every other.
- **Length n:** It always works because the complete string is one block.
- **Global count not divisible by block count:** The multiplication equality rejects the candidate without requiring an explicit divisibility precheck per character.
- **Repeated arrangements:** Blocks may have completely different orders; only their frequency vectors matter.
- **Early mismatch:** `check` returns immediately on the first differing letter, which improves average time but not the worst-case bound.
- **Fixed alphabet:** The constant-space counter claim for the data structure depends on lowercase English letters. The slice allocation remains input-sized regardless.
- **First passing divisor:** Returning immediately is correct because lengths are visited numerically in ascending order.
